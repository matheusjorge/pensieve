from datetime import datetime, date
from enum import Enum
import os
from types import MappingProxyType
from typing import Dict, List, Optional

from .env import NOTES_PATH

class SearchMethod(str, Enum):
    date="date"

class Seacher:
    methods_map: MappingProxyType[Enum, str] = MappingProxyType({
        SearchMethod.date: "search_by_date"
    })

    @classmethod
    def search(cls, method: SearchMethod, **kwargs) -> Dict[date, List[str]]:
        return getattr(cls, cls.methods_map[method])(**kwargs)

    @staticmethod
    def search_by_date(min_date: Optional[datetime] = None, max_date: Optional[datetime] = None):
        subdirs = [d for d in os.walk(NOTES_PATH) if len(d[2]) != 0]
        files = dict()
        for d in subdirs:
            for f in d[2]:
                filename = f"{d[0]}/{f}"
                create_date = date.fromtimestamp(os.stat(filename).st_birthtime)
                if create_date in files:
                    files[create_date].append(filename.replace(str(NOTES_PATH), "")[1:])
                else:
                    files[create_date] = [filename.replace(str(NOTES_PATH), "")[1:]]
        return files
