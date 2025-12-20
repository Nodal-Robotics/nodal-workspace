import json
import sys
from datetime import datetime
from adr_commands import REQUIRED_SECTIONS, is_maintainer, AdrStatus
from adr_parser import parse_comment
from adr_state import create_empty_state, load_state, save_state
from adr_template import inject_sections

STATE_FILE = "adr_state.json"

def adr_filename_from_state(state: dict) -> str:
    """
    Génère un nom de fichier ADR unique basé sur le timestamp d'approbation.
    Format: ADR-YYYYMMDD-HHMMSS.md
    """
    approved_at = state["state"].get("approved_at")
    if approved_at:
        dt = datetime.fromisoformat(approved_at.replace("Z", "+00:00"))
    else:
        dt = datetime.utcnow()
    ts_str = dt.strftime("%Y%m%d-%H%M%S")
    return f"ADR-{ts_str}.md"

def main(input_file: str):
    # Lecture des commentaires JSON générés par le GitHub Action
    with open(input_file, "r") as f:
        payload = json.load(f)

    comments = payload["comments"]
    meta = payload["meta"]

    # Chargement de l'état existant ou création d'un nouveau
    try:
        state = load_state(STATE_FILE)
    except FileNotFoundError:
        state = create_empty_state(meta)

    for c in comments:
        parsed = parse_comment(c["body"])
        if not parsed:
            continue

        action = parsed["action"]
        section = parsed["section"]
        content = parsed["content"]

        # Vérification des droits mainteneur pour approve/reject
        if action in {"approve", "reject"}:
            if not is_maintainer(c["author_role"]):
                continue  # ignore la commande

        # Gestion des commandes
        if action == "fill":
            if not section or not content or not content.strip():
                raise ValueError("/adr fill requires section and non-empty content")
            state["sections"][section]["content"] = content
            state["sections"][section]["last_updated_by"] = c["author"]
            state["sections"][section]["last_updated_at"] = c["created_at"]

        elif action == "append":
            if not section or not content or not content.strip():
                raise ValueError("/adr append requires section and non-empty content")
            cur = state["sections"][section]["content"]
            state["sections"][section]["content"] = (cur + "\n\n" + content) if cur else content
            state["sections"][section]["last_updated_by"] = c["author"]
            state["sections"][section]["last_updated_at"] = c["created_at"]

        elif action == "approve":
            # Vérifie que l'ADR n'est pas vide
            non_empty = [s for s, v in state["sections"].items() if v["content"].strip()]
            print(f"empty value: {non_empty} test")
            if not non_empty:
                print(f"value: {non_empty} test")
                raise RuntimeError("Cannot approve ADR: all sections are empty")

            # Vérifie que les sections obligatoires sont présentes
            missing = [s for s in REQUIRED_SECTIONS if not state["sections"][s]["content"].strip()]
            if missing:
                raise RuntimeError(f"Cannot approve ADR: missing required sections: {missing}")

            state["state"]["status"] = AdrStatus.APPROVED.value
            state["state"]["approved_by"] = c["author"]
            state["state"]["approved_at"] = c["created_at"]

        elif action == "reject":
            state["state"]["status"] = AdrStatus.REJECTED.value
            state["state"]["rejected_by"] = c["author"]
            state["state"]["rejected_at"] = c["created_at"]
    save_state(state, STATE_FILE)

    # Si l'ADR est approuvé, générer le fichier final
    if state["state"]["status"] == AdrStatus.APPROVED.value:
        with open("adr_template.md", "r") as f:
            template = f.read()

        body = inject_sections(template, state)
        filename = adr_filename_from_state(state)

        # Écriture du fichier ADR
        with open(f"docs/adr/{filename}", "w") as f:
            f.write(body)

        print(f"ADR_FILE=docs/adr/{filename}")
