import json
from pathlib import Path
from domain.adr import ADR


class ADRJsonRepository:

    def __init__(self, base_path: str):
        self.base_path = Path(base_path)

    def _path(self, issue_id: int) -> Path:
        return self.base_path / f"adr-{issue_id}.json"

    def load(self, issue_id: int) -> ADR:
        with self._path(issue_id).open() as f:
            data = json.load(f)
        return ADR(**data)

    def save(self, adr: ADR) -> None:
        self.base_path.mkdir(parents=True, exist_ok=True)
        with self._path(adr.issue_id).open("w") as f:
            json.dump(adr.__dict__, f, indent=2)
