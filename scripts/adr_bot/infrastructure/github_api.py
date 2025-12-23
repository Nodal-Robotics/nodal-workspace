from github import Github, GithubException
import os


class GitHubAPIError(Exception):
    pass


class GitHubAPI:
    def __init__(self) -> None:
        token = os.getenv("GITHUB_TOKEN")
        if not token:
            raise GitHubAPIError("GITHUB_TOKEN is not set")

        # Création du client PyGithub
        self.client = Github(token)
        try:
            self.repo = self.client.get_repo(os.getenv("GITHUB_REPOSITORY"))
        except GithubException as exc:
            raise GitHubAPIError(f"Unable to access repo: {exc}")

    def get_or_create_discussion(self, issue_id: int, issue_title: str, category_name: str = "Architecture Decisions"):
        try:
            # Chercher discussion existante
            discussions = self.repo.get_discussions()
            for discussion in discussions:
                if f"Issue #{issue_id}" in discussion.title:
                    return discussion

            # Création sinon
            categories = self.repo.get_discussion_categories()
            category = next((c for c in categories if c.name == category_name), None)
            if not category:
                raise GitHubAPIError(f"Discussion category '{category_name}' not found")

            discussion = self.repo.create_discussion(
                title=f"ADR – Issue #{issue_id} – {issue_title}",
                body=(
                    f"Cette discussion est liée à l’issue #{issue_id}.\n\n"
                    "Elle est utilisée pour documenter et valider une "
                    "Architecture Decision Record (ADR)."
                ),
                category=category
            )
            return discussion

        except GithubException as exc:
            raise GitHubAPIError(f"GitHub error during discussion get/create: {exc}")

    def post_discussion_message(self, discussion_id: int, message: str) -> None:
        try:
            discussion = self.repo.get_discussion(discussion_id)
            discussion.create_comment(message)
        except GithubException as exc:
            raise GitHubAPIError(f"Failed to post discussion message: {exc}")
