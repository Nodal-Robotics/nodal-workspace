import json
from pathlib import Path
from domain.state import ADR

class ADRJsonRepository:
    def __init__(self, base_path: str = "docs/governance/adr"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)

    def save(self, adr: ADR) -> None:
        path = self.base_path / f"adr_{adr.issue_id}.json"
        with path.open("w", encoding="utf-8") as f:
            json.dump({
                "issue_id": adr.issue_id,
                "title": adr.title,
                "sections": adr.sections,
                "status": adr.status.value,
                "discussion_id": adr.discussion_id,
                "supersedes": adr.supersedes,
            }, f, indent=2)

    def load(self, issue_id: int) -> ADR:
        path = self.base_path / f"adr_{issue_id}.json"
        if not path.exists():
            raise FileNotFoundError(f"ADR {issue_id} not found")
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        from domain.state import ADR, ADRStatus
        return ADR(
            issue_id=data["issue_id"],
            title=data["title"],
            sections=data["sections"],
            status=ADRStatus(data["status"]),
            discussion_id=data.get("discussion_id"),
            supersedes=data.get("supersedes")
        )
