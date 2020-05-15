import os

import biothings, config
biothings.config_for_app(config)
from config import DATA_ARCHIVE_ROOT

import biothings.hub.dataload.dumper


class BiorxivDumper(biothings.hub.dataload.dumper.DummyDumper):

    SRC_NAME = "biorxiv"
    __metadata__ = {
        "src_meta": {
            "author":{
                "name": "Marco Cano",
                "url": "https://github.com/marcodarko"
            },
            "code":{
                "branch": "master",
                "repo": "https://github.com/marcodarko/biorxiv.git"
            },
            "url": "https://www.ncbi.nlm.nih.gov/research/coronavirus/ ",
            "license": "https://www.ncbi.nlm.nih.gov/home/about/policies/"
        }
    }
    # override in subclass accordingly
    SRC_ROOT_FOLDER = os.path.join(DATA_ARCHIVE_ROOT, SRC_NAME)
