from model import AdrStatus

# FSM déclarative :
# état courant -> commandes autorisées -> état suivant
FSM_TRANSITIONS = {
    AdrStatus.DRAFT: {
        "fill": AdrStatus.DRAFT,
        "append": AdrStatus.DRAFT,
        "approve": AdrStatus.ACCEPTED,
        "reject": AdrStatus.REJECTED,
        "supersede": AdrStatus.SUPERSEDED,
    },

    AdrStatus.ACCEPTED: {
        "supersede": AdrStatus.SUPERSEDED,
    },

    AdrStatus.REJECTED: {
        "supersede": AdrStatus.SUPERSEDED,
    },

    AdrStatus.SUPERSEDED: {
        # état terminal
    },
}


def apply_fsm(current_state: AdrStatus, command: str) -> AdrStatus:
    """
    Applique une transition FSM.

    Les commandes READ-ONLY (show, status) ne doivent JAMAIS arriver ici.
    """

    if command not in FSM_TRANSITIONS.get(current_state, {}):
        raise ValueError(
            f"Command '{command}' not allowed in state {current_state.value}"
        )

    return FSM_TRANSITIONS[current_state][command]
