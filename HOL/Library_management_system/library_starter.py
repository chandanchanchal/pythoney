from __future__ import annotations
from typing import Dict, List, Optional
from dataclasses import dataclass, field

@dataclass
class Item:
    # TODO: item_id: str, title: str, available: bool = True
    # TODO: __str__ friendly text
    pass

@dataclass
class Book(Item):
    # TODO: author: str, year: int, isbn: str
    pass

@dataclass
class Member:
    # TODO: member_id: str, name: str
    pass

@dataclass
class Loan:
    # TODO: item_id: str, member_id: str
    pass

class Library:
    def __init__(self) -> None:
        # TODO: items: Dict[str, Item]; members: Dict[str, Member]; loans: Dict[str, Loan]
        pass

    def add_item(self, item: Item) -> None:
        pass

    def add_member(self, member: Member) -> None:
        pass

    def search(self, query: str) -> Dict[str, Item]:
        pass

    def checkout(self, item_id: str, member_id: str) -> bool:
        pass

    def checkin(self, item_id: str) -> bool:
        pass

def demo():
    pass

if __name__ == "__main__":
    demo()
