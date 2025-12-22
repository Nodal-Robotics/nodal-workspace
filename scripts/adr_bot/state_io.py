# scripts/adr_bot/state_io.py
import json
from model import AdrStatus

STATE_FILE = "adr_state.json"

def load_state():
    try:
        with open(STATE_FILE, "r") as f:
            data = json.load(f)
            data["status"] = AdrStatus[data["status"]]
            return data
    except FileNotFoundError:
        # état par défaut
        return {"status": AdrStatus.DRAFT, "content": {}}

def save_state(state):
    # Conversion Enum → str
    data = state.copy()
    data["status"] = str(state["status"])
    with open(STATE_FILE, "w") as f:
        json.dump(data, f, indent=2)
