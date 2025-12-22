def format_section_content(state, section=None):
    if section:
        return state["sections"][section]["content"]

    out = []
    for name, data in state["sections"].items():
        out.append(f"## {name.capitalize()}\n\n{data['content']}")
    return "\n\n".join(out)


def inject_sections(template, state):
    body = template
    for name, data in state["sections"].items():
        body = body.replace(
            f"{{{{{name}}}}}",
            data["content"]
        )
    return body