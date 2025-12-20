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

def load_state(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)

def save_state(state: dict, path: str):
    with open(path, "w") as f:
        json.dump(state, f, indent=2)
