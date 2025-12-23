from domain.adr import ADR
from domain.state import ADRState
from domain.fsm import ADRFSM


class ADRService:

    def fill_section(self, adr: ADR, section: str, content: str, author: str) -> None:
        if not ADRFSM.can_modify(ADRState(adr.state)):
            raise ValueError("ADR is frozen and cannot be modified")

        adr.sections[section] = content.strip()
        adr.state = ADRState.DRAFT.value
        adr.add_history(author, f"fill {section}")

    def append_section(self, adr: ADR, section: str, content: str, author: str) -> None:
        if not ADRFSM.can_modify(ADRState(adr.state)):
            raise ValueError("ADR is frozen and cannot be modified")

        existing = adr.sections.get(section, "")
        adr.sections[section] = f"{existing}\n{content}".strip()
        adr.state = ADRState.DRAFT.value
        adr.add_history(author, f"append {section}")

    def propose(self, adr: ADR, author: str) -> None:
        missing = adr.missing_sections()
        if missing:
            raise ValueError(f"Missing sections: {', '.join(missing)}")

        adr.state = ADRState.PROPOSED.value
        adr.add_history(author, "propose")

    def approve(self, adr: ADR, approver: str) -> None:
        if not ADRFSM.can_approve(ADRState(adr.state)):
            raise ValueError("ADR is not in PROPOSED state")

        adr.state = ADRState.APPROVED.value
        adr.approved_by = approver
        adr.add_history(approver, "approve")
