import re
from adr_commands import VALID_SECTIONS

ADR_CMD_RE = re.compile(
    r"^/adr\s+(\w+)(?:\s+(\w+))?\s*$",
    re.IGNORECASE
)

def parse_comment(body: str):
    """
    Retourne:
      {
        action: str,
        section: str | None,
        content: str | None
      }
    ou None si ce n'est pas une commande ADR
    """

    lines = body.strip().splitlines()
    if not lines:
        return None

    match = ADR_CMD_RE.match(lines[0])
    if not match:
        return None

    action = match.group(1).lower()
    raw_section = match.group(2)

    section = None
    if raw_section:
        key = raw_section.lower()
        if key not in VALID_SECTIONS:
            raise ValueError(f"Unknown ADR section: {raw_section}")
        section = VALID_SECTIONS[key]

    content = "\n".join(lines[1:]).strip() if len(lines) > 1 else None

    return {
        "action": action,
        "section": section,
        "content": content,
    }
