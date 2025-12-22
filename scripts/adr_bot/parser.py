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

"""
ADR command parser.

Responsabilité unique :
- Parser le contenu texte des commentaires GitHub
- Extraire les commandes /adr
- Supporter /adr fill <section> avec contenu multi-ligne

Aucune logique métier ADR ici.
Aucune FSM ici.
"""

from typing import List, Dict


class AdrParseError(Exception):
    """Erreur de syntaxe ADR explicite et contrôlée."""
    pass


def parse_adr_commands(comment_body: str) -> List[Dict]:
    """
    Parse les commandes /adr présentes dans un commentaire GitHub.

    Commandes supportées :
      - /adr fill <section>
        (contenu multi-ligne jusqu'à la prochaine commande ou EOF)
      - /adr show
      - /adr status
      - /adr approve
      - /adr reject
      - toute autre commande mono-ligne /adr <action>

    :param comment_body: Texte brut du commentaire GitHub
    :return: Liste de commandes structurées
    """

    if not comment_body or not comment_body.strip():
        return []

    lines = comment_body.splitlines()
    commands: List[Dict] = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # On ne s'intéresse qu'aux lignes commençant par /adr
        if not line.startswith("/adr"):
            i += 1
            continue

        tokens = line.split()

        if len(tokens) < 2:
            raise AdrParseError("Invalid /adr command")

        action = tokens[1]

        # ─────────────────────────────────────────────
        # /adr fill <section>
        # ─────────────────────────────────────────────
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

            commands.append({
                "type": "fill",
                "section": section,
                "content": content
            })

        # ─────────────────────────────────────────────
        # Commandes mono-ligne
        # ─────────────────────────────────────────────
        else:
            commands.append({
                "type": action
            })

        i += 1

    return commands
