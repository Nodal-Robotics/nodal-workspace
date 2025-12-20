from enum import Enum

class AdrStatus(str, Enum):
    DRAFT = "DRAFT"
    UNDER_DISCUSSION = "UNDER_DISCUSSION"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    ARCHIVED = "ARCHIVED"


VALID_SECTIONS = {
    "context": "Context",
    "decision": "Decision",
    "alternatives": "Alternatives",
    "consequences": "Consequences",
    "safetyimpact": "SafetyImpact",
    "implementation": "Implementation",
}

REQUIRED_SECTIONS = {
    "Context",
    "Decision",
    "Consequences",
}

def is_maintainer(user_role: str) -> bool:
    """
    Business rule:
    A maintainer is a user with ADMIN or MAINTAIN role on the repository.
    """
    return user_role in {"ADMIN", "MAINTAIN"}