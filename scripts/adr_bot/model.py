# scripts/adr_bot/model.py
from enum import Enum, auto

class AdrStatus(Enum):
    DRAFT = auto()
    PROPOSED = auto()
    ACCEPTED = auto()
    REJECTED = auto()
    SUPERSEDED = auto()

    def __str__(self):
        return self.name
