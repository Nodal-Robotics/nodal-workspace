from enum import Enum


class ADRState(str, Enum):
    INIT = "INIT"
    DRAFT = "DRAFT"
    READY = "READY"
    PROPOSED = "PROPOSED"
    APPROVED = "APPROVED"
    SUPERSEDED = "SUPERSEDED"
    REJECTED = "REJECTED"
