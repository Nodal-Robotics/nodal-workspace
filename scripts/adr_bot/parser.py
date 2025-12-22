import re
from errors import bot_error


ADR_COMMAND_RE = re.compile(
    r"""^
    /adr
    \s+
    (?P<action>fill|append|show|approve|reject|supersede)
    (?:\s+(?P<args>.+))?
    $
    """,
    re.IGNORECASE | re.VERBOSE
)


SECTION_RE = re.compile(r"^(?P<section>[a-zA-Z0-9_-]+)\s*:\s*(?P<content>.+)$", re.DOTALL)


def parse_comment(body: str):
    """
    Parse a single GitHub comment body.
    Returns a dict or None if no ADR command is found.

    Output schema (depending on command):
    {
        action: str,
        section: Optional[str],
        content: Optional[str],
        target: Optional[str]   # for supersede
    }
    """

    lines = [l.strip() for l in body.splitlines() if l.strip()]

    for line in lines:
        match = ADR_COMMAND_RE.match(line)
        if not match:
            continue

        action = match.group("action").lower()
        args = match.group("args")

        # === Commands without arguments ===
        if action in {"approve", "reject"}:
            if args:
                bot_error(f"/adr {action} does not accept arguments")
            return {
                "action": action,
                "section": None,
                "content": None,
            }

        # === /adr show [section] ===
        if action == "show":
            return {
                "action": "show",
                "section": args.strip() if args else None,
                "content": None,
            }

        # === /adr supersede ADR-XXX ===
        if action == "supersede":
            if not args:
                bot_error("/adr supersede requires a target ADR id")
            return {
                "action": "supersede",
                "section": None,
                "content": None,
                "target": args.strip(),
            }

        # === fill / append ===
        if action in {"fill", "append"}:
            if not args:
                bot_error(f"/adr {action} requires section: content")

            sec_match = SECTION_RE.match(args)
            if not sec_match:
                bot_error(
                    f"/adr {action} syntax error",
                    expected="section: content"
                )

            return {
                "action": action,
                "section": sec_match.group("section"),
                "content": sec_match.group("content").strip(),
            }

    return None
