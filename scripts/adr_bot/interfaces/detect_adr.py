from infrastructure.github_api import GitHubAPI
from infrastructure.json_repository import ADRArtifactRepository
from application.use_cases import ADRUseCases
from domain.state import ADR

ADR_KEYWORDS = ["architecture", "architectural", "design decision", "adr",
                "technical decision", "system design", "refactor", "redesign", "architectural choice"]

def is_adr_issue(title: str, body: str) -> bool:
    text = f"{title} {body}".lower()
    return any(k in text for k in ADR_KEYWORDS)

def handle_detect_adr(issue: dict):
    github = GitHubAPI()
    repo = ADRArtifactRepository()
    use_cases = ADRUseCases(repo, github)

    issue_id = issue["number"]
    title = issue["title"]

    if not is_adr_issue(title, issue.get("body", "")):
        return "Pas une ADR"

    categories = github.get_discussion_categories()
    cat = next((c for c in categories if c["name"] == "Architecture Decisions"), None)
    if not cat:
        return "Catégorie 'Architecture Decisions' introuvable."

    discussions = github.list_discussions(category_id=cat["id"])
    existing = next((d for d in discussions if f"Issue #{issue_id}" in d["title"]), None)
    if existing:
        discussion_id = existing["id"]
    else:
        discussion = github.create_discussion(cat["id"], f"ADR – Issue #{issue_id} – {title}", "Discussion ADR")
        discussion_id = discussion["id"]

    adr = ADR(issue_id=issue_id, title=title, discussion_id=discussion_id)
    repo.save(adr)
    github.add_discussion_comment(discussion_id, "ADR créée et prête à être remplie.")
    return "ADR initialisée."
