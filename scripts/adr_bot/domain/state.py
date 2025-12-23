from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, Optional

class ADRStatus(str, Enum):
    DRAFT = "draft"
    PROPOSED = "proposed"
    APPROVED = "approved"
    SUPERSEDED = "superseded"
    REFUSED = "refused"

@dataclass
class ADR:
    issue_id: int
    title: str
    sections: Dict[str, str] = field(default_factory=lambda: {
        "context": "",
        "decision": "",
        "options": "",
        "consequences": "",
    })
    status: ADRStatus = ADRStatus.DRAFT
    discussion_id: Optional[str] = None
    supersedes: Optional[int] = None
