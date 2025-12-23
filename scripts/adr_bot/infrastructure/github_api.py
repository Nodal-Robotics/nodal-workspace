import os
from typing import Optional, Dict, List
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

class GitHubAPIError(Exception):
    pass

class GitHubAPI:
    """
    Client officiel GraphQL GitHub pour Discussions.
    """

    def __init__(self):
        token = os.getenv("GITHUB_TOKEN")
        repo_full = os.getenv("GITHUB_REPOSITORY")

        if not token:
            raise GitHubAPIError("GITHUB_TOKEN is not set")
        if not repo_full or "/" not in repo_full:
            raise GitHubAPIError("GITHUB_REPOSITORY is not set or invalid")

        self.owner, self.repo = repo_full.split("/", 1)
        transport = RequestsHTTPTransport(
            url="https://api.github.com/graphql",
            headers={"Authorization": f"Bearer {token}"},
            verify=True
        )
        self.client = Client(transport=transport, fetch_schema_from_transport=True)
        self.repo_id = self._get_repository_node_id()

    def _get_repository_node_id(self) -> str:
        query = gql("""
        query($owner: String!, $repo: String!) {
          repository(owner: $owner, name: $repo) { id }
        }
        """)
        result = self.client.execute(query, variable_values={
            "owner": self.owner,
            "repo": self.repo
        })
        return result["repository"]["id"]

    def get_discussion_categories(self) -> List[Dict]:
        query = gql("""
        query($owner: String!, $repo: String!) {
          repository(owner: $owner, name: $repo) {
            discussionCategories(first: 100) {
              nodes { id name }
            }
          }
        }
        """)
        result = self.client.execute(query, variable_values={
            "owner": self.owner,
            "repo": self.repo
        })
        return result["repository"]["discussionCategories"]["nodes"]

    def list_discussions(self, category_id: Optional[str] = None) -> List[Dict]:
        if category_id:
            query = gql("""
            query($owner: String!, $repo: String!, $categoryId: ID!) {
              repository(owner: $owner, name: $repo) {
                discussions(first: 100, categoryId: $categoryId) {
                  nodes { id number title }
                }
              }
            }
            """)
            variables = {"owner": self.owner, "repo": self.repo, "categoryId": category_id}
        else:
            query = gql("""
            query($owner: String!, $repo: String!) {
              repository(owner: $owner, name: $repo) {
                discussions(first: 100) { nodes { id number title } }
              }
            }
            """)
            variables = {"owner": self.owner, "repo": self.repo}

        result = self.client.execute(query, variable_values=variables)
        return result["repository"]["discussions"]["nodes"]

    def create_discussion(self, category_id: str, title: str, body: str) -> Dict:
        mutation = gql("""
        mutation($repoId: ID!, $categoryId: ID!, $title: String!, $body: String!) {
          createDiscussion(input: {repositoryId: $repoId, categoryId: $categoryId, title: $title, body: $body}) {
            discussion { id number }
          }
        }
        """)
        result = self.client.execute(mutation, variable_values={
            "repoId": self.repo_id,
            "categoryId": category_id,
            "title": title,
            "body": body
        })
        return result["createDiscussion"]["discussion"]

    def add_discussion_comment(self, discussion_id: str, body: str) -> None:
        mutation = gql("""
        mutation($discussionId: ID!, $body: String!) {
          addDiscussionComment(input: {discussionId: $discussionId, body: $body}) {
            comment { id }
          }
        }
        """)
        self.client.execute(mutation, variable_values={"discussionId": discussion_id, "body": body})
