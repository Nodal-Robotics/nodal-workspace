import json
import os
import sys
from typing import Any, Dict


class ConfigurationError(Exception):
    pass


class UsageError(Exception):
    pass


def load_github_event() -> Dict[str, Any]:
    event_path = os.getenv("GITHUB_EVENT_PATH")
    if not event_path:
        raise ConfigurationError("GITHUB_EVENT_PATH is not set")

    try:
        with open(event_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError as exc:
        raise ConfigurationError(
            f"GitHub event file not found: {event_path}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise ConfigurationError(
            f"Invalid JSON in GitHub event file: {event_path}"
        ) from exc


def parse_args(argv: list[str]) -> str:
    if len(argv) != 2:
        raise UsageError(
            "Usage: python main.py <detect-adr|process-command>"
        )

    command = argv[1]
    if command not in {"detect-adr", "process-command"}:
        raise UsageError(
            f"Unknown command '{command}'. "
            "Expected 'detect-adr' or 'process-command'."
        )

    return command


def main() -> None:
    try:
        command = parse_args(sys.argv)
        event = load_github_event()

        if command == "detect-adr":
            from interfaces.detect_adr import handle_detect_adr
            handle_detect_adr(event)

        elif command == "process-command":
            from interfaces.process_command import handle_process_command
            handle_process_command(event)

    except UsageError as exc:
        print(f"[USAGE ERROR] {exc}", file=sys.stderr)
        sys.exit(2)

    except ConfigurationError as exc:
        print(f"[CONFIG ERROR] {exc}", file=sys.stderr)
        sys.exit(3)

    except Exception as exc:
        # En CI, toute exception non prévue doit faire échouer le job
        print(f"[UNEXPECTED ERROR] {exc}", file=sys.stderr)
        raise


if __name__ == "__main__":
    main()
