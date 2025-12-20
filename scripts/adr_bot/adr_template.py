def generate_adr(template: str, state: dict) -> str:
    output = template

    for section, data in state["sections"].items():
        marker = f"## {section}"
        parts = output.split(marker)

        if len(parts) != 2:
            continue

        before, rest = parts
        _, after = rest.split("\n", 1)

        output = (
            before
            + marker
            + "\n\n"
            + data["content"].strip()
            + "\n\n"
            + after.split("---", 1)[1]
        )

    return output.strip()

def inject_sections(template: str, state: dict) -> str:
    output = template

    for section, data in state["sections"].items():
        marker = f"## {section}"
        if marker not in output:
            continue

        before, after = output.split(marker, 1)
        after = after.split("---", 1)[1]

        output = (
            before
            + marker
            + "\n\n"
            + data["content"].strip()
            + "\n\n---"
            + after
        )

    return output.strip()
