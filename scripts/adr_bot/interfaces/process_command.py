from typing import Dict, Any

from interfaces.handlers import parse_command
from infrastructure.json_repository import ADRJsonRepository
from infrastructure.github_api import GitHubAPI, GitHubAPIError
from application.use_cases import ADRUseCases
from domain.state import ADRState


def handle_process_command(event: Dict[str, Any]) -> None:
    # Sécurité : ce handler ne doit répondre qu’aux commentaires de discussion
    if "discussion" not in event or "comment" not in event:
        return

    discussion = event["discussion"]
    comment = event["comment"]

    discussion_id = discussion["id"]
    body = comment.get("body", "")
    author = comment["user"]["login"]

    # On ne traite que les commandes ADR
    command = parse_command(body, author)
    if not command:
        return

    repository = ADRJsonRepository(".adr/state")
    github = GitHubAPI()
    use_cases = ADRUseCases(repository, github_client=github)

    # Trouver l’ADR associée à cette discussion
    adr = _load_adr_by_discussion(repository, discussion_id)

    if not adr:
        github.post_discussion_message(
            discussion_id,
            "❌ Aucune ADR associée à cette discussion."
        )
        return

    try:
        match command.name:
            case "fill":
                _ensure_section(command.section)
                use_cases.handle_fill(
                    adr,
                    command.section,
                    command.content or "",
                    author,
                )
                github.post_discussion_message(
                    discussion_id,
                    f"✅ Section `{command.section}` remplie par @{author}."
                )

            case "append":
                _ensure_section(command.section)
                use_cases.handle_append(
                    adr,
                    command.section,
                    command.content or "",
                    author,
                )
                github.post_discussion_message(
                    discussion_id,
                    f"✅ Contenu ajouté à `{command.section}` par @{author}."
                )

            case "show":
                github.post_discussion_message(
                    discussion_id,
                    _render_adr_summary(adr)
                )

            case "propose":
                use_cases.handle_propose(adr, author)
                github.post_discussion_message(
                    discussion_id,
                    f"📌 ADR proposée par @{author}. Elle est maintenant figée."
                )

            case "approve":
                use_cases.handle_approve(adr, author)
                github.post_discussion_message(
                    discussion_id,
                    f"✔ ADR approuvée par @{author} et commitée."
                )

            case _:
                github.post_discussion_message(
                    discussion_id,
                    f"❌ Commande `/adr {command.name}` inconnue."
                )

    except ValueError as exc:
        # Erreur métier contrôlée → feedback utilisateur
        github.post_discussion_message(
            discussion_id,
            f"❌ Impossible d’exécuter la commande : {exc}"
        )

    except GitHubAPIError:
        # Erreur infra → on remonte (job failed)
        raise


def _ensure_section(section: str | None) -> None:
    if not section:
        raise ValueError("Section manquante (ex: /adr fill context)")


def _load_adr_by_discussion(
    repository: ADRJsonRepository,
    discussion_id: int,
):
    """
    Recherche linéaire volontaire.
    Volume faible, lisibilité > optimisation (YAGNI).
    """
    base = repository.base_path
    if not base.exists():
        return None

    for file in base.glob("adr-*.json"):
        adr = repository.load(int(file.stem.split("-")[1]))
        if adr.discussion_id == discussion_id:
            return adr

    return None


def _render_adr_summary(adr) -> str:
    return (
        f"### ADR – Issue #{adr.issue_id}\n\n"
        f"**État** : `{adr.state}`\n\n"
        f"**Contexte**\n{adr.sections.get('context', '_Non défini_')}\n\n"
        f"**Décision**\n{adr.sections.get('decision', '_Non définie_')}\n\n"
        f"**Options**\n{adr.sections.get('options', '_Non définies_')}\n\n"
        f"**Conséquences**\n{adr.sections.get('consequences', '_Non définies_')}"
    )
