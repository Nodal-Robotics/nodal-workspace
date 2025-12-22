import json
import sys
import os

from constants import STATE_FILE
from model import AdrStatus
from fsm import apply_fsm
from state_io import load_state, save_state, create_empty_state
from commands import apply_approve, apply_supersede
from render import format_section_content
from errors import bot_error, bot_success
from utils import is_maintainer
from parser import parse_adr_commands, AdrParseError


def main(input_file: str) -> None:
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
        try:
            commands = parse_adr_commands(c["body"])
        except AdrParseError as e:
            bot_error(str(e))
            return

        if not commands:
            continue

        for parsed in commands:
            cmd = parsed["type"]

            try:
                next_status = apply_fsm(current_status, cmd)
            except ValueError as e:
                bot_error(str(e))
                return

            section = parsed.get("section")
            content = parsed.get("content")

            if cmd == "fill":
                state["sections"][section]["content"] = content.strip()
                bot_success(f"Section '{section}' updated successfully.")

            elif cmd == "append":
                cur = state["sections"][section]["content"]
                state["sections"][section]["content"] = (
                    cur + "\n\n" + content.strip() if cur else content.strip()
                )
                bot_success(f"Section '{section}' appended successfully.")

            elif cmd == "approve":
                if not is_maintainer(c["author_role"]):
                    bot_error("Permission denied")
                    return

                last_terminal = "approve"
                last_ctx = {
                    "author": c["author"],
                    "time": c["created_at"]
                }

            elif cmd == "supersede":
                if not is_maintainer(c["author_role"]):
                    bot_error("Permission denied")
                    return

                last_terminal = "supersede"
                last_ctx = {
                    "author": c["author"],
                    "time": c["created_at"],
                    "supersedes": parsed.get("target")
                }

            elif cmd == "show":
                last_terminal = "show"
                last_ctx = {"section": section}

            current_status = next_status
            state["state"]["status"] = current_status.value

    if last_terminal == "show":
        bot_success(
            "ADR content",
            content=format_section_content(state, last_ctx.get("section"))
        )

    elif last_terminal == "approve":
        if not os.path.exists(STATE_FILE):
            bot_error("No ADR state found. Run /adr fill before /adr approve.")
            return

        apply_approve(state, **last_ctx)
        save_state(state, STATE_FILE)
        bot_success("ADR approved")

    elif last_terminal == "supersede":
        apply_supersede(state, **last_ctx)
        save_state(state, STATE_FILE)
        bot_success("ADR superseded")

    else:
        save_state(state, STATE_FILE)


if __name__ == "__main__":
    main(sys.argv[1])
