from application.services import ADRService


class ADRUseCases:

    def __init__(self, repository, github_client):
        self.repository = repository
        self.github_client = github_client
        self.service = ADRService()

    def handle_fill(self, adr, section, content, author):
        self.service.fill_section(adr, section, content, author)
        self.repository.save(adr)

    def handle_append(self, adr, section, content, author):
        self.service.append_section(adr, section, content, author)
        self.repository.save(adr)

    def handle_propose(self, adr, author):
        self.service.propose(adr, author)
        self.repository.save(adr)
        return self.github_client.generate_adr_file(adr)

    def handle_approve(self, adr, approver):
        self.service.approve(adr, approver)
        self.github_client.commit_adr(adr)
        self.repository.save(adr)
