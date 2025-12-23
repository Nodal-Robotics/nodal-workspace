import json
from pathlib import Path
from domain.state import ADR, ADRStatus

class ADRArtifactRepository:
    """
    Stockage des ADR via GitHub Actions artifacts.
    """

    def __init__(self, base_path: str = "/tmp/adr_artifacts"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)

    def _path(self, issue_id: int) -> Path:
        return self.base_path / f"adr_{issue_id}.json"

    def save(self, adr: ADR) -> None:
        path = self._path(adr.issue_id)
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
        path = self._path(issue_id)
        if not path.exists():
            # Crée un ADR vide si absent
            adr = ADR(
                issue_id=issue_id,
                title=f"ADR {issue_id}",
                sections={"context": "", "decision": "", "options": "", "consequences": ""},
                status=ADRStatus.DRAFT,
                discussion_id=None
            )
            self.save(adr)
            return adr

        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return ADR(
            issue_id=data["issue_id"],
            title=data["title"],
            sections=data["sections"],
            status=ADRStatus(data["status"]),
            discussion_id=data.get("discussion_id"),
            supersedes=data.get("supersedes")
        )
