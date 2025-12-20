#!/usr/bin/env python3
"""
Generate ADR document from GitHub Discussion
"""
import argparse
import re
import yaml
from datetime import datetime
from pathlib import Path
from github import Github

ADR_DIR = Path("docs/governance/adr")
ADR_TEMPLATE = """---
title: "ADR-{adr_number:04d} – {title}"
nav_order: {nav_order}
parent: Architecture Decision Records
status: {status}
decision_date: {date}
related_requirements: {requirements}
related_issues: {issues}
sil_impact: {sil_impact}
participants: {participants}
---

# ADR-{adr_number:04d}: {title}

**Status**: {status}  
**Date**: {date}  
**Decision Makers**: {decision_makers}

---

## Context

{context}

---

## Decision

{decision}

---

## Alternatives Considered

{alternatives}

---

## Consequences

### Positive

{positive_consequences}

### Negative

{negative_consequences}

---

## Risks and Mitigations

{risks}

---

## Safety & Compliance Impact

**SIL Level Impact**: {sil_impact}

{safety_impact}

---

## Implementation Notes

{implementation_notes}

---

## Verification & Validation

{verification}

---

## References

- **Issue**: #{issue_number}
- **Discussion**: #{discussion_number}
{additional_references}

---

## Revision History

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| {date} | 1.0 | Initial ADR | {author} |
"""

def get_next_adr_number():
    """Get the next available ADR number"""
    if not ADR_DIR.exists():
        return 1
    
    existing = [
        int(re.search(r'adr-(\d+)', f.stem).group(1))
        for f in ADR_DIR.glob("adr-*.md")
        if re.search(r'adr-(\d+)', f.stem)
    ]
    
    return max(existing, default=0) + 1

def extract_section(text, section_name):
    """Extract content from a markdown section with various patterns"""
    
    # Patterns pour détecter les sections
    patterns = [
        # Pattern avec ##
        rf"##\s+{section_name}\s*\n(.*?)(?=\n##|\Z)",
        # Pattern avec backticks
        rf"`##\s+{section_name}`\s*\n(.*?)(?=\n`##|---|\Z)",
        # Pattern inline
        rf"\*\*{section_name}\*\*:?\s*\n(.*?)(?=\n\*\*|---|\Z)",
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if match:
            content = match.group(1).strip()
            if content and content != "Not documented":
                return content
    
    return "Not documented"

def parse_discussion_content(discussion):
    """Parse discussion body and comments to extract ADR content"""
    
    # Combiner le body principal et tous les commentaires
    full_content = discussion.body or ""
    
    for comment in discussion.comments():
        # Ajouter un séparateur pour distinguer les commentaires
        full_content += f"\n\n--- Comment by {comment.user.login} ---\n\n{comment.body}"
    
    print(f"📝 Parsing {len(discussion.comments())} comments...")
    
    # Extraire les sections principales
    context = extract_section(full_content, "Context")
    decision = extract_section(full_content, "Decision")
    alternatives = extract_section(full_content, "Alternatives?")
    consequences = extract_section(full_content, "Consequences")
    
    # Si pas trouvé avec "Consequences", essayer "Consequences?"
    if consequences == "Not documented":
        consequences = extract_section(full_content, "Consequences?")
    
    # Parser les conséquences positives/négatives
    pos_patterns = [
        r"###?\s*Positive\s*:?\s*\n(.*?)(?=###|---|\Z)",
        r"\*\*Positive\*\*:?\s*\n(.*?)(?=\*\*|---|\Z)",
        r"Positive:\s*\n(.*?)(?=Negative|---|\Z)"
    ]
    
    neg_patterns = [
        r"###?\s*Negative\s*:?\s*\n(.*?)(?=###|---|\Z)",
        r"\*\*Negative\*\*:?\s*\n(.*?)(?=\*\*|---|\Z)",
        r"Negative:\s*\n(.*?)(?=###|---|\Z)"
    ]
    
    positive = "- To be documented"
    negative = "- To be documented"
    
    for pattern in pos_patterns:
        match = re.search(pattern, consequences, re.DOTALL | re.IGNORECASE)
        if match:
            positive = match.group(1).strip()
            break
    
    for pattern in neg_patterns:
        match = re.search(pattern, consequences, re.DOTALL | re.IGNORECASE)
        if match:
            negative = match.group(1).strip()
            break
    
    # Extraire d'autres sections optionnelles
    risks = extract_section(full_content, "Risks")
    safety_impact_raw = extract_section(full_content, "Safety Impact")
    implementation = extract_section(full_content, "Implementation")
    verification = extract_section(full_content, "Verification")
    
    # Extraire le SIL level de plusieurs façons
    sil_patterns = [
        r"SIL\s*Level:?\s*(SIL\s*\d|None|N/A)",
        r"SIL:?\s*(\d)",
        r"SIL\s*(\d)",
    ]
    
    sil_impact = "None"
    for pattern in sil_patterns:
        match = re.search(pattern, full_content, re.IGNORECASE)
        if match:
            sil_text = match.group(1)
            if "none" in sil_text.lower() or "n/a" in sil_text.lower():
                sil_impact = "None"
            else:
                sil_match = re.search(r'\d', sil_text)
                if sil_match:
                    sil_impact = f"SIL {sil_match.group()}"
            break
    
    # Extraire les requirements mentionnés (SR-XXX, REQ-XXX, HAZ-XXX, etc.)
    requirement_patterns = [
        r'\b(SR-\d+)\b',
        r'\b(REQ-\d+)\b',
        r'\b(HAZ-\d+)\b',
    ]
    
    requirements = set()
    for pattern in requirement_patterns:
        requirements.update(re.findall(pattern, full_content, re.IGNORECASE))
    
    requirements = list(requirements)
    
    # Extraire les participants (commentateurs + auteur)
    participants = list(set([
        comment.user.login 
        for comment in discussion.comments()
    ] + [discussion.user.login]))
    
    print(f"✓ Context: {len(context)} chars")
    print(f"✓ Decision: {len(decision)} chars")
    print(f"✓ Alternatives: {len(alternatives)} chars")
    print(f"✓ Positive consequences: {len(positive)} chars")
    print(f"✓ Negative consequences: {len(negative)} chars")
    print(f"✓ SIL Impact: {sil_impact}")
    print(f"✓ Requirements: {requirements}")
    print(f"✓ Participants: {participants}")
    
    return {
        "context": context,
        "decision": decision,
        "alternatives": alternatives,
        "positive_consequences": positive,
        "negative_consequences": negative,
        "risks": risks if risks != "Not documented" else "No significant risks identified.",
        "safety_impact": safety_impact_raw if safety_impact_raw != "Not documented" else "No specific safety impact identified.",
        "implementation_notes": implementation if implementation != "Not documented" else "To be determined during implementation.",
        "verification": verification if verification != "Not documented" else "Standard verification procedures apply.",
        "sil_impact": sil_impact,
        "requirements": requirements,
        "participants": participants,
    }

def extract_issue_number_from_discussion(discussion):
    """Extract related issue number from discussion body"""
    match = re.search(r'\*\*Related Issue\*\*:\s*#(\d+)', discussion.body or "")
    return int(match.group(1)) if match else None

def generate_adr_document(discussion_number, github_token, repo_name):
    """Generate ADR document from discussion"""
    
    # Connexion à GitHub
    g = Github(github_token)
    repo = g.get_repo(repo_name)
    
    # Récupérer la discussion via GraphQL
    # Note: PyGithub ne supporte pas nativement les discussions
    # On doit utiliser l'API REST ou GraphQL directement
    
    # Pour simplifier, on va utiliser l'API REST via requests
    import requests
    
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # GraphQL query pour récupérer la discussion
    query = """
    query($owner: String!, $name: String!, $number: Int!) {
      repository(owner: $owner, name: $name) {
        discussion(number: $number) {
          id
          title
          body
          createdAt
          closedAt
          author {
            login
          }
          comments(first: 100) {
            nodes {
              body
              author {
                login
              }
            }
          }
        }
      }
    }
    """
    
    owner, name = repo_name.split('/')
    variables = {
        "owner": owner,
        "name": name,
        "number": discussion_number
    }
    
    response = requests.post(
        "https://api.github.com/graphql",
        json={"query": query, "variables": variables},
        headers={"Authorization": f"Bearer {github_token}"}
    )
    
    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.status_code}")
    
    data = response.json()
    discussion_data = data["data"]["repository"]["discussion"]
    
    # Créer un objet discussion-like pour compatibilité
    class Discussion:
        def __init__(self, data):
            self.title = data["title"]
            self.body = data["body"]
            self.user = type('User', (), {'login': data["author"]["login"]})()
            self._comments = data["comments"]["nodes"]
        
        def comments(self):
            class Comment:
                def __init__(self, data):
                    self.body = data["body"]
                    self.user = type('User', (), {'login': data["author"]["login"]})()
            
            return [Comment(c) for c in self._comments]
    
    discussion = Discussion(discussion_data)
    
    # Extraire le numéro d'issue
    issue_number = extract_issue_number_from_discussion(discussion)
    
    if not issue_number:
        print("⚠️  Warning: No related issue found in discussion")
        issue_number = "N/A"
    
    # Générer le numéro ADR
    adr_number = get_next_adr_number()
    
    # Parser le contenu
    content = parse_discussion_content(discussion)
    
    # Nettoyer le titre (enlever le préfixe "ADR Discussion:")
    title = re.sub(r'^ADR Discussion:\s*', '', discussion.title, flags=re.IGNORECASE)
    
    # Calculer le nav_order (dernier + 1)
    existing_orders = []
    for adr_file in ADR_DIR.glob("*.md"):
        with adr_file.open() as f:
            front = f.read().split('---', 2)
            if len(front) >= 2:
                fm = yaml.safe_load(front[1])
                if 'nav_order' in fm:
                    existing_orders.append(fm['nav_order'])
    
    nav_order = max(existing_orders, default=0) + 1
    
    # Générer le document
    adr_content = ADR_TEMPLATE.format(
        adr_number=adr_number,
        title=title,
        nav_order=nav_order,
        status="Accepted",
        date=datetime.now().strftime("%Y-%m-%d"),
        requirements=str(content['requirements']) if content['requirements'] else "[]",
        issues=f"[{issue_number}]" if issue_number != "N/A" else "[]",
        sil_impact=content['sil_impact'],
        participants=str(content['participants']),
        decision_makers=", ".join(content['participants']),
        context=content['context'],
        decision=content['decision'],
        alternatives=content['alternatives'],
        positive_consequences=content['positive_consequences'],
        negative_consequences=content['negative_consequences'],
        risks=content['risks'],
        safety_impact=content['safety_impact'],
        implementation_notes=content['implementation_notes'],
        verification=content['verification'],
        issue_number=issue_number,
        discussion_number=discussion_number,
        additional_references="",
        author=discussion.user.login
    )
    
    # Écrire le fichier
    adr_filename = f"adr-{adr_number:04d}.md"
    adr_path = ADR_DIR / adr_filename
    
    ADR_DIR.mkdir(parents=True, exist_ok=True)
    adr_path.write_text(adr_content, encoding='utf-8')
    
    print(f"✅ ADR-{adr_number:04d} generated: {adr_path}")
    
    # Écrire les métadonnées pour le workflow
    Path("/tmp/adr_number.txt").write_text(f"{adr_number:04d}")
    Path("/tmp/issue_number.txt").write_text(str(issue_number))
    Path("/tmp/adr_file.txt").write_text(str(adr_path))
    
    return adr_path

def main():
    parser = argparse.ArgumentParser(description="Generate ADR from GitHub Discussion")
    parser.add_argument("--discussion-number", type=int, required=True)
    parser.add_argument("--github-token", required=True)
    parser.add_argument("--repo", required=True, help="Repository in format owner/repo")
    
    args = parser.parse_args()
    
    try:
        generate_adr_document(
            args.discussion_number,
            args.github_token,
            args.repo
        )
    except Exception as e:
        print(f"❌ Error generating ADR: {e}")
        import traceback
        traceback.print_exc()
        exit(1)

if __name__ == "__main__":
    main()