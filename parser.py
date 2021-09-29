import json
import time
import os

import requests
from dateutil import parser
from datetime import date


try:
    from biothings import config
    logging = config.logger
except ImportError:
    import logging

def find_gen_path():
    tmp_dir = os.getcwd()
    while 'topic_classifier' not in os.listdir(tmp_dir):
        tmp_dir = os.path.dirname(tmp_dir)
    return(tmp_dir)

def fetch_path_dict():
    general_path = find_gen_path()
    topic_folder = os.path.join(general_path,'topic_classifier')
    topic_results = os.path.join(topic_folder,'results')
    alt_path = os.path.join(general_path,'covid_altmetrics')
    alt_results = os.path.join(alt_path,'results')
    preprint_path = os.path.join(general_path,'outbreak_preprint_matcher')
    preprint_results = os.path.join(preprint_path,'results')
    preprint_dumps = os.path.join(preprint_results,'update dumps')
    loe_ann_path = os.path.join(general_path,'covid19_LST_annotations')
    loe_results = os.path.join(loe_ann_path,'results')
    path_dict = {
        'topics_file':os.path.join(topic_results,'topicCats.json'),
        'altmetrics_file':os.path.join(alt_results,'altmetric_annotations.json'),
        'litcovid_updates':os.path.join(preprint_dumps,'litcovid_update_file.json'),
        'preprint_updates':os.path.join(preprint_dumps,'preprint_update_file.json'),
        'loe_annotations':os.path.join(loe_results,'loe_annotations.json')
        }
    return(path_dict)


def fetch_annotation(path_dict,source,outbreak_id):
    with open(path_dict[source],'r') as infile:
        ann_dict = json.load(infile)
    ann_info = [x for x in ann_dict if x["_id"]==outbreak_id]
    try:
        return(ann_info[0])
    except:
        return(ann_info)

    
def add_anns(path_dict,doc):
    ## add corrections
    if doc['@type']=='Publication':
        if 'pmid' in doc['_id']:
            ## doc is from litcovid
            corrections = fetch_annotation(path_dict,'litcovid_updates',doc['_id'])
            loe_info = fetch_annotation(path_dict,'loe_annotations',doc['_id'])
        else:
            corrections = fetch_annotation(path_dict,'preprint_updates',doc['_id'])
            loe_info = None
        if corrections != None and len(corrections)>0 and corrections!="[]":
            if 'correction' in doc.keys():  ## check if correction field already used
                try:
                    doc['correction'].append(corrections["correction"][0])
                except:
                    correct_object = doc['correction']
                    doc['correction']=[correct_object,corrections["correction"][0]]
            else:
                doc['correction']=corrections["correction"][0]
        if loe_info != None and len(loe_info)>0 and loe_info!="[]":
            doc['evaluations'] = loe_info['evaluations']
            if 'citedBy' in doc.keys():
                doc['citedBy'].append(loe_info['citedBy'])
            else:
                doc['citedBy'] = []
                doc['citedBy'].append(loe_info['citedBy'])
    ## add topic_cats
    topic_cats = fetch_annotation(path_dict,'topics_file',doc['_id'])
    if topic_cats != None and len(topic_cats)>0 and topic_cats!="[]":
        doc['topicCategory']=topic_cats['topicCategory'].replace("'","").strip("[").strip("]").split(",")
    ## add altmetrics
    altinfo = fetch_annotation(path_dict,'altmetrics_file',doc['_id'])
    if altinfo != None and len(altinfo)>0:
        if 'evaluations' in doc.keys():
            try:
                doc['evaluations'].append(altinfo['evaluations'][0])
            except:
                eval_object = doc['evaluations']
                doc['evaluations']=[eval_object,altinfo['evaluations'][0]]
        else:
            doc['evaluations'] = altinfo['evaluations']       
    return(doc)


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

    data_request = requests.get(data_url.format(cursor=cursor))

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
        data_request = requests.get(data_url.format(cursor=cursor))
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
