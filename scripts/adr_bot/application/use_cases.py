from domain.state import ADR, ADRStatus
from infrastructure.json_repository import ADRJsonRepository
from infrastructure.github_api import GitHubAPI, GitHubAPIError

class ADRUseCases:
    def __init__(self, repository: ADRJsonRepository, github_client: GitHubAPI):
        self.repository = repository
        self.github = github_client

    def fill(self, issue_id: int, section: str, content: str) -> str:
        adr = self.repository.load(issue_id)
        if adr.status != ADRStatus.DRAFT:
            return f"Impossible de remplir ADR: statut actuel {adr.status}"
        if section not in adr.sections:
            return f"Section inconnue: {section}"
        adr.sections[section] = content
        self.repository.save(adr)
        return f"Section '{section}' mise à jour."

    def append(self, issue_id: int, section: str, content: str) -> str:
        adr = self.repository.load(issue_id)
        if adr.status != ADRStatus.DRAFT:
            return f"Impossible de modifier ADR: statut actuel {adr.status}"
        if section not in adr.sections:
            return f"Section inconnue: {section}"
        adr.sections[section] += "\n" + content
        self.repository.save(adr)
        return f"Section '{section}' enrichie."

    def propose(self, issue_id: int) -> str:
        adr = self.repository.load(issue_id)
        if not all(adr.sections.values()):
            return "Toutes les sections doivent être remplies avant de proposer l'ADR."
        if adr.status != ADRStatus.DRAFT:
            return f"ADR ne peut être proposé: statut {adr.status}"
        adr.status = ADRStatus.PROPOSED
        self.repository.save(adr)
        return "ADR proposé."

    def approve(self, issue_id: int) -> str:
        adr = self.repository.load(issue_id)
        if adr.status != ADRStatus.PROPOSED:
            return f"ADR ne peut être approuvé: statut {adr.status}"
        adr.status = ADRStatus.APPROVED
        self.repository.save(adr)
        return "ADR approuvé et prêt à committer."

    def supersede(self, old_issue_id: int, new_issue_id: int) -> str:
        old_adr = self.repository.load(old_issue_id)
        new_adr = self.repository.load(new_issue_id)
        if old_adr.status != ADRStatus.APPROVED:
            return "Impossible de superseder une ADR non approuvée."
        new_adr.supersedes = old_issue_id
        self.repository.save(new_adr)
        old_adr.status = ADRStatus.SUPERSEDED
        self.repository.save(old_adr)
        return f"ADR {new_issue_id} remplace {old_issue_id}."

    def refuse(self, issue_id: int) -> str:
        adr = self.repository.load(issue_id)
        if adr.status != ADRStatus.PROPOSED:
            return "Seules les ADR proposées peuvent être refusées."
        adr.status = ADRStatus.REFUSED
        self.repository.save(adr)
        return "ADR refusée."
