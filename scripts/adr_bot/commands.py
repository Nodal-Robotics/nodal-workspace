from constants import REQUIRED_SECTIONS, ADR_DIR
from model import AdrStatus
from errors import bot_error


def validate_required_sections(state):
    missing = [
        s for s in REQUIRED_SECTIONS
        if not state["sections"][s]["content"].strip()
    ]
    if missing:
        bot_error(
            "Missing required ADR sections",
            missing=missing
        )


def apply_supersede(state, superseded_adr_id, author, time):
    state["state"]["status"] = AdrStatus.SUPERSEDED.value
    state["state"]["superseded_by"] = superseded_adr_id
    state["state"]["superseded_at"] = time


def apply_approve(state, author, time):
    validate_required_sections(state)
    state["state"]["status"] = AdrStatus.APPROVED.value
    state["state"]["approved_by"] = author
    state["state"]["approved_at"] = time
