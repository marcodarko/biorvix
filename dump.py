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
            "url": "https://connect.biorxiv.org/relate/content/181",
            "license": "https://www.biorxiv.org/about-biorxiv"
        }
    }
    # override in subclass accordingly
    SRC_ROOT_FOLDER = os.path.join(DATA_ARCHIVE_ROOT, SRC_NAME)
    
    SCHEDULE = "15 7 * * *"  # daily at 14:15UTC/7:15PT
