import json
from model import AdrStatus
from constants import REQUIRED_SECTIONS


def create_empty_state(meta):
    return {
        "meta": meta,
        "state": {
            "status": AdrStatus.DRAFT.value,
            "approved_by": None,
            "approved_at": None,
            "rejected_by": None,
            "rejected_at": None,
            "superseded_by": None,
            "superseded_at": None,
            "supersedes": None,
        },
        "sections": {
            s: {"content": ""} for s in REQUIRED_SECTIONS
        }
    }


def load_state(path):
    with open(path) as f:
        return json.load(f)


def save_state(state, path):
    with open(path, "w") as f:
        json.dump(state, f, indent=2)
