import json
import time
import os

import requests
from dateutil import parser
from datetime import date
import pathlib

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

DEFAULT_TIMEOUT = 5 # seconds

class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)

## Set time outs, backoff, retries
httprequests = requests.Session()
retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    method_whitelist=["HEAD", "GET", "OPTIONS"]
)
adapter = TimeoutHTTPAdapter(timeout=2.5,max_retries=retry_strategy)
httprequests.mount("https://", adapter)
httprequests.mount("http://", adapter)    
    
script_path = pathlib.Path(__file__).parent.absolute()
with open(os.path.join(script_path,'append_misc_meta.py'),'w+') as appendfile:
    r = httprequests.get('https://raw.githubusercontent.com/gtsueng/outbreak_misc_meta/main/append_misc_meta.py')
    appendfile.write(r.text)
    appendfile.close()

from append_misc_meta import *

try:
    from biothings import config
    logging = config.logger
except ImportError:
    import logging


def parse_item(rec):
    publication={
        "@context": {
            "schema":"http://schema.org/",
            "outbreak":"https://discovery.biothings.io/view/outbreak/",
        },
        "@type":'Publication',
        "keywords":[],
        "author":[],
        "funding":[],
        "isBasedOn":[]
    }
    publication["_id"] = rec['rel_doi'].split('/', 1)[-1]
    publication["doi"] = rec.get("rel_doi", None)
    publication["url"] = rec.get("rel_link", None)

    website = {"@type":"schema:WebSite", "curationDate": date.today().strftime("%Y-%m-%d")}
    name = rec.get("rel_site", "")
    website['name'] = name
    website['url'] = rec.get("rel_link", "")

    publication["curatedBy"] = website
    publication["publicationType"] = ["Preprint"]
    publication["name"] = rec.get("rel_title", None)
    publication["journalName"] = rec.get("rel_site", None)
    publication["journalNameAbbreviation"] = rec.get("rel_site", None)
    publication["abstract"] = rec.get("rel_abs", None)
    publication["identifier"] = rec['rel_doi'].split('/', 1)[-1]

    dp = rec.get("rel_date", None)
    if dp:
        d = parser.parse(dp)
        dp = d.strftime("%Y-%m-%d")
        publication["datePublished"] = dp

    authors = rec.get("rel_authors")

    if authors and len(authors):
        for auth in authors:
            author = {"@type":"outbreak:Person"}

            full_name = auth.get("author_name", None)
            if full_name is not None:
                author["name"] = full_name
                author["givenName"] = full_name.split(' ', 1)[0]
                try:
                    author["familyName"] = full_name.split(' ',1)[1]
                except:
                    logging.info("No familyName for: '%s'" % rec['rel_doi'])
                    pass


            institutions = auth.get("author_inst", None)
            if institutions is not None:
                organization = {"@type":"outbreak:Organization"}
                author["affiliation"] =[]
                organization["name"] = auth["author_inst"]
                if organization["name"] is not None:
                    author["affiliation"].append(organization)
            for key in author:
                if author[key] is None: del author[key]
            publication["author"].append(author)

    #cleanup doc of empty vals
    for key in list(publication):
        if not publication.get(key):del publication[key]

    return publication

def fetch_data():
    data_url       = "https://api.biorxiv.org/covid19/{cursor}/json"
    cursor         = 0
    collected_dois = set([None])

    data_request = httprequests.get(data_url.format(cursor=cursor))

    try:
        data_json  = data_request.json()
        total      = data_json['messages'][0]['total']
        collection = data_json['collection']
    except:
        logging.warning("Biorxiv API down")
        raise StopIteration

    while len(collection) > 0:
        logging.info(f"getting {cursor}")
        for result in collection:
            if result.get('rel_doi') not in collected_dois:
                yield result
        collected_dois |= set(r.get('rel_doi') for r in collection)

        cursor += 30
        data_request = httprequests.get(data_url.format(cursor=cursor))
        data_json    = data_request.json()
        collection   = data_json['collection']
        new_total    = data_json['messages'][0].get('total') or new_total

    collected_dois.remove(None)
    logging.info(f"initial total {total}, latest total {new_total}, actually collected {len(collected_dois)}")

def load_annotations():
    path_dict = fetch_path_dict()
    for rec in fetch_data():
        publication_rec = parse_item(rec)
        publication = add_anns(path_dict,publication_rec)
        yield publication

if __name__ == '__main__':
    import sys
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)
    logging = root
    (i for i in load_annotations())
