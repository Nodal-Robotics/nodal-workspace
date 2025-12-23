import os
import sys
from interfaces.detect_adr import handle_detect_adr
from interfaces.process_command import handle_process_command

def main():
    event_path = os.getenv("GITHUB_EVENT_PATH")
    if not event_path:
        print("GITHUB_EVENT_PATH non défini")
        sys.exit(1)

    import json
    with open(event_path, "r", encoding="utf-8") as f:
        event = json.load(f)

    event_type = os.getenv("GITHUB_EVENT_NAME")
    if event_type == "issues" and event["action"] == "opened":
        handle_detect_adr(event["issue"])
    elif event_type == "discussion_comment" and event["action"] == "created":
        handle_process_command(event)
    else:
        print(f"Event {event_type} ignoré")

if __name__ == "__main__":
    main()
