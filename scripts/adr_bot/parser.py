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
        if action == "fill":
            if len(tokens) != 3:
                raise AdrParseError(
                    "Invalid /adr fill syntax. Expected: /adr fill <section>"
                )

            section = tokens[2]
            content_lines = []

            i += 1
            while i < len(lines):
                current_line = lines[i]

                # Nouvelle commande → fin du contenu
                if current_line.strip().startswith("/adr"):
                    i -= 1
                    break

                content_lines.append(current_line)
                i += 1

            content = "\n".join(content_lines).strip()

            if not content:
                raise AdrParseError(
                    f"/adr fill syntax error: empty content for section '{section}'"
                )

            # commands.append({
            # })

            return {
                "type": "fill",
                "section": section,
                "content": content
            }

    return None
