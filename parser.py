import json

import requests
from dateutil import parser

from biothings import config
logging = config.logger

def load_annotations():
    r = requests.get('https://connect.biorxiv.org/relate/collection_json.php?grp=181')
    if r.status_code == 200:
        data = json.loads(r.text)
    for rec in data['rels']:
        publication={
            "@context": {
                "schema":"http://schema.org/",
                "outbreak":"https://discovery.biothings.io/view/outbreak/",
            },
            "@type":'Publication',
            "keywords":[],
            "author":[],
            "funding":[],
            "publicationType":[],
            "isBasedOn":[]
        }
        publication["_id"] = rec['rel_doi'].split('/', 1)[-1]
        publication["doi"] = rec.get("rel_doi", None)
        publication["url"] = rec.get("rel_link", None)

        website = {"@type":"schema:WebSite"}
        name = rec.get("rel_site", "")
        website['name'] = name
        website['url'] = rec.get("rel_link", "")

        publication["curatedBy"] = website

        publication["name"] = rec.get("rel_title", None)
        publication["journalName"] = rec.get("rel_title", None)
        publication["journalNameAbbreviation"] = rec.get("rel_title", None)
        publication["abstract"] = rec.get("rel_abs", None)
        publication["identifier"] = rec['rel_doi'].split('/', 1)[-1]

        dp = rec.get("rel_date", None)
        if dp:
            d = parser.parse(dp)
            dp = d.strftime("%Y-%m-%d")
            publication["datePublished"] = dp

        authors = rec.get("rel_authors", [])
        if len(authors):
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

        yield publication
