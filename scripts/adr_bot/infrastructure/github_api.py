import os
import requests
from typing import Dict, Optional


class GitHubAPIError(Exception):
    pass


class GitHubAPI:
    BASE_URL = "https://api.github.com"

    def __init__(self) -> None:
        token = os.getenv("GITHUB_TOKEN")
        if not token:
            raise GitHubAPIError("GITHUB_TOKEN is not set")

        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        })

        self.owner, self.repo = self._get_repo_context()

    # ---------- Public API ----------

    def get_or_create_discussion(
        self,
        issue_id: int,
        issue_title: str,
        category_name: str = "Architecture Decisions",
    ) -> Dict:
        category_id = self._get_discussion_category_id(category_name)

        existing = self._find_discussion(issue_id)
        if existing:
            return existing

        return self._create_discussion(
            category_id=category_id,
            issue_id=issue_id,
            issue_title=issue_title,
        )

    def post_discussion_message(self, discussion_id: int, message: str) -> None:
        url = f"{self.BASE_URL}/repos/{self.owner}/{self.repo}/discussions/{discussion_id}/comments"

        response = self.session.post(url, json={"body": message})
        if response.status_code != 201:
            raise GitHubAPIError(
                f"Failed to post discussion message: "
                f"{response.status_code} {response.text}"
            )

    # ---------- Internal helpers ----------

    def _get_repo_context(self) -> tuple[str, str]:
        repo = os.getenv("GITHUB_REPOSITORY")
        if not repo or "/" not in repo:
            raise GitHubAPIError("GITHUB_REPOSITORY is not set or invalid")

        owner, name = repo.split("/", 1)
        return owner, name

    def _get_discussion_category_id(self, category_name: str) -> int:
        url = f"{self.BASE_URL}/repos/{self.owner}/{self.repo}/discussion-categories"

        response = self.session.get(url)
        if response.status_code != 200:
            raise GitHubAPIError(
                f"Failed to list discussion categories: "
                f"{response.status_code} {response.text}"
            )

        for category in response.json():
            if category["name"] == category_name:
                return category["id"]

        raise GitHubAPIError(
            f"Discussion category '{category_name}' not found"
        )

    def _find_discussion(self, issue_id: int) -> Optional[Dict]:
        """
        Recherche une discussion existante liée à l’issue.
        Règle : le titre contient 'Issue #<id>'.
        """
        url = f"{self.BASE_URL}/repos/{self.owner}/{self.repo}/discussions"

        page = 1
        while True:
            response = self.session.get(
                url,
                params={"per_page": 100, "page": page},
            )

            if response.status_code != 200:
                raise GitHubAPIError(
                    f"Failed to list discussions: "
                    f"{response.status_code} {response.text}"
                )

            discussions = response.json()
            if not discussions:
                return None

            for discussion in discussions:
                if f"Issue #{issue_id}" in discussion["title"]:
                    return discussion

            page += 1

    def _create_discussion(
        self,
        category_id: int,
        issue_id: int,
        issue_title: str,
    ) -> Dict:
        url = f"{self.BASE_URL}/repos/{self.owner}/{self.repo}/discussions"

        payload = {
            "title": f"ADR – Issue #{issue_id} – {issue_title}",
            "body": (
                f"Cette discussion est liée à l’issue #{issue_id}.\n\n"
                "Elle est utilisée pour documenter et valider une "
                "Architecture Decision Record (ADR)."
            ),
            "category_id": category_id,
        }

        response = self.session.post(url, json=payload)
        if response.status_code != 201:
            raise GitHubAPIError(
                f"Failed to create discussion: "
                f"{response.status_code} {response.text}"
            )

        return response.json()
