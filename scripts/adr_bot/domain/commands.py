from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ADRCommand:
    name: str
    section: Optional[str]
    content: Optional[str]
    author: str
