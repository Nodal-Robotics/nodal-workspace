import re
from domain.commands import ADRCommand

ADR_CMD_REGEX = re.compile(
    r"^/adr\s+(\w+)(?:\s+(\w+))?\n?(.*)$",
    re.DOTALL
)


def parse_command(body: str, author: str) -> ADRCommand | None:
    match = ADR_CMD_REGEX.match(body.strip())
    if not match:
        return None

    return ADRCommand(
        name=match.group(1),
        section=match.group(2),
        content=match.group(3),
        author=author
    )
