def is_maintainer(role: str) -> bool:
    return role in {"OWNER", "MEMBER"}
