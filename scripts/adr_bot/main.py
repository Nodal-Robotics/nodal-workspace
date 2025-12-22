# scripts/adr_bot/main.py
import sys
from parser import execute_command
from state_io import load_state, save_state
import json

def main(input_file):
    # Lecture du JSON d'entrée
    with open(input_file, "r") as f:
        data = json.load(f)

    # Extraction des commandes de la discussion
    commands = [c["body"].strip() for c in data.get("comments", [])]

    output = {}
    for cmd in commands:
        parts = cmd.split(maxsplit=1)
        action = parts[0].replace("/adr", "").strip()
        payload = parts[1] if len(parts) > 1 else None

        try:
            result = execute_command(action, payload)
            output.update(result)
        except Exception as e:
            output = {"status": "error", "message": str(e)}
            break

    # Si ADR accepté, générer le fichier final
    state = load_state()
    if state["status"] == state["status"].__class__.ACCEPTED:
        adr_filename = f"adr_{state.get('content', {}).get('id', 'unknown')}.md"
        with open(adr_filename, "w") as f:
            f.write("# ADR Generated\n\n")
            f.write(json.dumps(state["content"], indent=2))
        output["adr_file"] = adr_filename

    # Sauvegarde de l'état
    save_state(state)

    # Sortie bot
    with open("bot_output.json", "w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    main(sys.argv[1])
