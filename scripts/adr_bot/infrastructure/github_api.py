import os
import requests
from typing import Dict, Any, Optional

class GitHubAPIError(Exception):
    pass

class GitHubAPI:
    BASE_URL = "https://api.github.com"

    def __init__(self):
        token = os.getenv("GITHUB_TOKEN")
        if not token:
            raise GitHubAPIError("GITHUB_TOKEN is not set")

        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
        })

        repo_full = os.getenv("GITHUB_REPOSITORY")
        if not repo_full or "/" not in repo_full:
            raise GitHubAPIError("Invalid GITHUB_REPOSITORY")
        self.owner, self.repo = repo_full.split("/", 1)

    def _request(self, method: str, url: str, **kwargs) -> Any:
        response = self.session.request(method, url, **kwargs)
        if response.status_code >= 400:
            raise GitHubAPIError(
                f"GitHub API {method} {url} failed "
                f"{response.status_code} {response.text}"
            )
        return response.json()

    def get_discussion_categories(self) -> Any:
        url = f"{self.BASE_URL}/repos/{self.owner}/{self.repo}/discussion-categories"
        return self._request("GET", url)

    def list_discussions(self) -> Any:
        url = f"{self.BASE_URL}/repos/{self.owner}/{self.repo}/discussions"
        return self._request("GET", url)

    def get_or_create_discussion(
        self,
        issue_id: int,
        issue_title: str,
        category_name: str = "Architecture Decisions",
    ) -> Dict[str, Any]:
        # 1) find category id
        categories = self.get_discussion_categories()
        cat = next((c for c in categories if c["name"] == category_name), None)
        if not cat:
            raise GitHubAPIError(
                f"Discussion category '{category_name}' not found"
            )
        category_id = cat["id"]

        # 2) find an existing discussion
        discussions = self.list_discussions()
        for d in discussions:
            if f"Issue #{issue_id}" in d["title"]:
                return d

        # 3) create discussion
        url = f"{self.BASE_URL}/repos/{self.owner}/{self.repo}/discussions"
        payload = {
            "title": f"ADR – Issue #{issue_id} – {issue_title}",
            "body": (
                f"Cette discussion est liée à l’issue #{issue_id}.\n\n"
                "Elle est utilisée pour documenter et valider une ADR."
            ),
            "category_id": category_id,
        }
        return self._request("POST", url, json=payload)

    def post_discussion_message(
        self,
        discussion_number: int,
        message: str,
    ) -> None:
        """
        Note: Discussion API uses discussion_number, not internal id.
        """
        url = (
            f"{self.BASE_URL}/repos/{self.owner}/{self.repo}"
            f"/discussions/{discussion_number}/comments"
        )
        self._request("POST", url, json={"body": message})
