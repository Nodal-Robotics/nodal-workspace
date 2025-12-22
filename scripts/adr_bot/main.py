import json
import sys

from constants import STATE_FILE, ADR_TEMPLATE_FILE, ADR_DIR
from model import AdrStatus
from fsm import apply_fsm
from state_io import load_state, save_state, create_empty_state
from commands import apply_approve, apply_supersede
from render import format_section_content, inject_sections
from errors import bot_error, bot_success
from utils import is_maintainer
from parser import parse_comment


def main(input_file):
    with open(input_file) as f:
        payload = json.load(f)

    comments = payload["comments"]
    meta = payload["meta"]

    try:
        state = load_state(STATE_FILE)
    except FileNotFoundError:
        state = create_empty_state(meta)

    current_status = AdrStatus(state["state"]["status"])

    last_terminal = None
    last_ctx = {}

    for c in comments:
        parsed = parse_comment(c["body"])
        if not parsed:
            continue

        cmd = parsed["action"]
        section = parsed.get("section")
        content = parsed.get("content")

        next_status = apply_fsm(current_status, cmd)

        if cmd == "fill":
            state["sections"][section]["content"] = content.strip()

        elif cmd == "append":
            cur = state["sections"][section]["content"]
            state["sections"][section]["content"] = (
                cur + "\n\n" + content.strip() if cur else content.strip()
            )

        elif cmd == "approve":
            if not is_maintainer(c["author_role"]):
                bot_error("Permission denied")
            last_terminal = "approve"
            last_ctx = {"author": c["author"], "time": c["created_at"]}

        elif cmd == "supersede":
            if not is_maintainer(c["author_role"]):
                bot_error("Permission denied")
            last_terminal = "supersede"
            last_ctx = {
                "author": c["author"],
                "time": c["created_at"],
                "supersedes": parsed["target"]
            }

        elif cmd == "show":
            last_terminal = "show"
            last_ctx = {"section": section}

        current_status = next_status

    # Action finale
    if last_terminal == "show":
        bot_success(
            "ADR content",
            content=format_section_content(state, last_ctx["section"])
        )

    elif last_terminal == "approve":
        apply_approve(state, **last_ctx)
        save_state(state, STATE_FILE)
        bot_success("ADR approved")

    elif last_terminal == "supersede":
        apply_supersede(state, **last_ctx)
        save_state(state, STATE_FILE)
        bot_success("ADR superseded")

    save_state(state, STATE_FILE)

if __name__ == "__main__":
    main(sys.argv[1])