from infrastructure.github_api import GitHubAPI
from infrastructure.json_repository import ADRJsonRepository
from application.use_cases import ADRUseCases

def parse_command(message: str) -> tuple[str, str]:
    """
    Retourne (commande, contenu). Multi-lignes supportées.
    """
    lines = message.strip().split("\n")
    first = lines[0].strip()
    if first.startswith("/adr "):
        cmd = first[5:].split()[0]
        content = "\n".join(lines[1:]).strip()
        return cmd, content
    return "", ""

def handle_process_command(event: dict):
    github = GitHubAPI()
    repo = ADRJsonRepository()
    use_cases = ADRUseCases(repo, github)

    comment = event["comment"]["body"]
    cmd, content = parse_command(comment)
    issue_id = event["issue"]["number"]

    if cmd == "fill":
        section, _, text = content.partition("\n")
        msg = use_cases.fill(issue_id, section.strip(), text.strip())
    elif cmd == "append":
        section, _, text = content.partition("\n")
        msg = use_cases.append(issue_id, section.strip(), text.strip())
    elif cmd == "propose":
        msg = use_cases.propose(issue_id)
    elif cmd == "approve":
        msg = use_cases.approve(issue_id)
    elif cmd == "supersede":
        old_id_str, new_id_str = content.strip().split()
        msg = use_cases.supersede(int(old_id_str), int(new_id_str))
    elif cmd == "refuse":
        msg = use_cases.refuse(issue_id)
    else:
        msg = "Commande inconnue."

    adr = repo.load(issue_id)
    github.add_discussion_comment(adr.discussion_id, msg)
