# scripts/adr_bot/parser.py
from fsm import can_transition, next_status
from state_io import load_state, save_state

def execute_command(command, payload=None):
    state = load_state()
    current_status = state["status"]

    # Vérification de transition
    if can_transition(current_status, command):
        new_status = next_status(current_status, command)
        state["status"] = new_status

        # Gestion du contenu
        if command in ("fill", "append") and payload:
            state["content"].setdefault(command, []).append(payload)
        save_state(state)
        return {"status": "success", "new_status": str(new_status)}
    else:
        # Commandes valides mais sans changement d’état (show)
        if command == "show":
            return {"status": "show", "content": state["content"]}
        return {"status": "error", "message": f"Commande '{command}' impossible depuis l'état {current_status}"}
