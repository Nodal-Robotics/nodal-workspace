from typing import Dict, Any

from domain.adr import ADR
from domain.adr_state import ADRState
from infrastructure.json_repository import ADRJsonRepository
from infrastructure.github_api import GitHubAPI


ADR_KEYWORDS = [
    "architecture",
    "architectural",
    "design decision",
    "adr",
    "technical decision",
    "system design",
    "refactor",
    "redesign",
    "architectural choice",
]


def _is_adr_issue(title: str, body: str) -> bool:
    text = f"{title}\n{body}".lower()
    return any(keyword in text for keyword in ADR_KEYWORDS)


def handle_detect_adr(event: Dict[str, Any]) -> None:
    # Sécurité : ce handler ne doit répondre qu’aux issues
    if "issue" not in event:
        return

    issue = event["issue"]
    issue_id = issue["number"]
    title = issue.get("title", "")
    body = issue.get("body", "") or ""
    author = issue["user"]["login"]

    if not _is_adr_issue(title, body):
        return  # ce n’est pas une ADR

    repository = ADRJsonRepository(".adr/state")

    # Idempotence : si l’ADR existe déjà, on ne refait rien
    try:
        repository.load(issue_id)
        return
    except FileNotFoundError:
        pass

    github = GitHubAPI()

    discussion = github.get_or_create_discussion(
        issue_id=issue_id,
        issue_title=title
    )

    adr = ADR(
        issue_id=issue_id,
        discussion_id=discussion["id"],
        created_by=author,
        state=ADRState.INIT.value,
        sections={
            "title": title,
            "context": "",
            "decision": "",
            "options": "",
            "consequences": "",
            "status": "draft",
        },
    )

    adr.add_history(author, "initialize ADR")

    repository.save(adr)

    github.post_discussion_message(
        discussion_id=discussion["id"],
        message=(
            "ADR détectée à partir de l’issue.\n\n"
            "État initialisé (`INIT`).\n\n"
            "Utilisez les commandes `/adr fill`, `/adr append`, `/adr show` "
            "pour compléter l’ADR."
        ),
    )
