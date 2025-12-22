from model import AdrStatus

ADR_TRANSITIONS = {
    AdrStatus.DRAFT: {
        "approve": AdrStatus.APPROVED,
        "reject": AdrStatus.REJECTED,
    },
    AdrStatus.APPROVED: {
        "supersede": AdrStatus.SUPERSEDED,
    },
    AdrStatus.REJECTED: {},
    AdrStatus.SUPERSEDED: {},
}

COMMANDS_BY_STATE = {
    AdrStatus.DRAFT: {"fill", "append", "show", "approve", "reject"},
    AdrStatus.APPROVED: {"show", "supersede"},
    AdrStatus.REJECTED: {"show"},
    AdrStatus.SUPERSEDED: {"show"},
}


def apply_fsm(current_state: AdrStatus, command: str) -> AdrStatus:
    if command not in COMMANDS_BY_STATE[current_state]:
        raise ValueError(
            f"Command '{command}' not allowed in state {current_state.value}"
        )

    return ADR_TRANSITIONS.get(current_state, {}).get(command, current_state)
