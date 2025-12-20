import json
from datetime import datetime
from adr_commands import AdrStatus, VALID_SECTIONS

def now_iso():
    return datetime.utcnow().isoformat() + "Z"

def create_empty_state(meta: dict) -> dict:
    return {
        "meta": meta,
        "state": {
            "status": AdrStatus.UNDER_DISCUSSION.value,
            "approved_by": None,
            "approved_at": None,
            "rejected_by": None,
            "rejected_at": None,
        },
        "sections": {
            section: {
                "content": "",
                "last_updated_by": None,
                "last_updated_at": None,
            }
            for section in VALID_SECTIONS.values()
        },
        "history": [],
    }

    def adr_filename_from_state(state: dict) -> str:
        """
        Génère un nom de fichier ADR unique basé sur le timestamp d'approbation.
        """
        approved_at = state["state"].get("approved_at")
        if approved_at:
            # Exemple: "2025-12-20T18:32:45Z"
            dt = datetime.fromisoformat(approved_at.replace("Z", "+00:00"))
        else:
            dt = datetime.utcnow()

        ts_str = dt.strftime("%Y%m%d-%H%M%S")
        return f"ADR-{ts_str}.md"


def load_state(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)

def save_state(state: dict, path: str):
    with open(path, "w") as f:
        json.dump(state, f, indent=2)
