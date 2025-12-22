# scripts/adr_bot/fsm.py
from model import AdrStatus

# Définition claire et complète de la FSM
TRANSITIONS = {
    AdrStatus.DRAFT: {
        "fill": AdrStatus.DRAFT,
        "append": AdrStatus.DRAFT,
        "show": AdrStatus.DRAFT,
        "propose": AdrStatus.PROPOSED,
    },
    AdrStatus.PROPOSED: {
        "show": AdrStatus.PROPOSED,
        "approve": AdrStatus.ACCEPTED,
        "reject": AdrStatus.REJECTED,
        "supersede": AdrStatus.SUPERSEDED,
    },
    AdrStatus.ACCEPTED: {},
    AdrStatus.REJECTED: {},
    AdrStatus.SUPERSEDED: {},
}

def can_transition(current_status, command):
    """Vérifie si la transition est possible"""
    return command in TRANSITIONS.get(current_status, {})

def next_status(current_status, command):
    """Retourne le nouvel état si la transition est valide"""
    if can_transition(current_status, command):
        return TRANSITIONS[current_status][command]
    raise ValueError(f"Transition impossible: {current_status} → {command}")
