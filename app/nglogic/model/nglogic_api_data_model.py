import logging
from pathlib import Path
from typing import Dict, List

import settings

DATA_PATH = settings.BASE_DIR / "app" / "nglogic" / "model" / "input.txt"
logger = logging.getLogger(__name__)


class NglogicApiDataModel:
    def __init__(self):
        self.MIN_VALUE: int = 0
        self.MAX_VALUE: int = 0
        self.data: Dict[int, int] = {}
        self.keys: List[int] = []

    def initialize(self, path: Path = DATA_PATH):
        logger.debug(f"Initializing data model form source: {path}")

        with open(path, "r") as datafile:
            data = {}
            max_value = 0

            for idx, row in enumerate(datafile):
                max_value = int(row)
                data[max_value] = idx

            self.MAX_VALUE = max_value
            self.data = data
            self.keys = list(data.keys())

        return self

    @property
    def max_value(self) -> int:
        return self.MAX_VALUE

    def get_nearest_key(self, value: int) -> int:
        """
        calculates the nearest index of self.data dict,
        if the value is not that exist in self.data.
        It assumes that the self.data.keys() not going to be in that order
        in which dict was populated
        (starting form Python 2.7 in most cases, they are although in that order,
        but... :))
        """
        return min(self.keys, key=lambda k: abs(k - value))


nglogic_api_data = NglogicApiDataModel()
