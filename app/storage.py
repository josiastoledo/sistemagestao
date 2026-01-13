from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, Generic, List, TypeVar


T = TypeVar("T")


@dataclass
class Repository(Generic[T]):
    _data: Dict[int, T] = field(default_factory=dict)
    _next_id: int = 1

    def create(self, item: T) -> int:
        item_id = self._next_id
        self._data[item_id] = item
        self._next_id += 1
        return item_id

    def list_all(self) -> List[T]:
        return list(self._data.values())

    def get(self, item_id: int) -> T:
        return self._data[item_id]


@dataclass
class Store:
    repos: Dict[str, Repository] = field(default_factory=lambda: defaultdict(Repository))

    def repo(self, name: str) -> Repository:
        return self.repos[name]
