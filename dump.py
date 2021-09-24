import os
import datetime

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
                "branch": "annotations",
                "repo": "https://github.com/gtsueng/biorxiv.git"
            },
            "url": "https://api.biorxiv.org/covid19/help",
            "license": "https://www.biorxiv.org/about-biorxiv"
        }
    }
    # override in subclass accordingly
    SRC_ROOT_FOLDER = os.path.join(DATA_ARCHIVE_ROOT, SRC_NAME)
    
    SCHEDULE = "15 7 * * *"  # daily at 7:15PT

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_release()

    def set_release(self):
        self.release = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M')
