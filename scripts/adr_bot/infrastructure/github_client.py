from pathlib import Path
import subprocess


class GitClient:

    def generate_adr_file(self, adr):
        path = Path(f"docs/governance/adr/ADR-{adr.issue_id}.md")
        path.parent.mkdir(parents=True, exist_ok=True)

        content = f"""# ADR-{adr.issue_id}

        ## Status
        {adr.state}

        ## Context
        {adr.sections['context']}

        ## Decision
        {adr.sections['decision']}

        ## Options Considered
        {adr.sections['options']}

        ## Consequences
        {adr.sections['consequences']}
        """
        path.write_text(content)
        return path

    def commit_adr(self, adr):
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run([
            "git", "commit",
            "-m",
            f"docs(adr): approve ADR-{adr.issue_id}"
        ], check=True)
        subprocess.run(["git", "push"], check=True)
