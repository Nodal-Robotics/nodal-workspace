from domain.state import ADRState


class ADRFSM:

    @staticmethod
    def can_modify(state: ADRState) -> bool:
        return state in {ADRState.INIT, ADRState.DRAFT}

    @staticmethod
    def can_propose(state: ADRState) -> bool:
        return state == ADRState.READY

    @staticmethod
    def can_approve(state: ADRState) -> bool:
        return state == ADRState.PROPOSED

    @staticmethod
    def is_terminal(state: ADRState) -> bool:
        return state in {
            ADRState.APPROVED,
            ADRState.SUPERSEDED,
            ADRState.REJECTED
        }
