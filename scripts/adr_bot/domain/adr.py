from dataclasses import dataclass, field
from typing import Dict, List, Optional
from datetime import datetime

REQUIRED_SECTIONS = {
    "title",
    "context",
    "decision",
    "options",
    "consequences",
    "status"
}


@dataclass
class ADR:
    issue_id: int
    discussion_id: int
    created_by: str
    state: str
    sections: Dict[str, str] = field(default_factory=dict)
    history: List[Dict] = field(default_factory=list)
    supersedes: Optional[str] = None
    approved_by: Optional[str] = None

    def missing_sections(self) -> List[str]:
        return [
            section for section in REQUIRED_SECTIONS
            if not self.sections.get(section)
        ]

    def add_history(self, user: str, action: str) -> None:
        self.history.append({
            "timestamp": datetime.utcnow().isoformat(),
            "user": user,
            "action": action
        })
