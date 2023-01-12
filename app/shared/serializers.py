def to_camel(string: str) -> str:
    """BaseModel alias_generator setup to convert camel case to snake case attributes."""
    words = string.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])
