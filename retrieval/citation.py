from typing import TypedDict


class Citation(TypedDict):
    source: str
    text: str


def format_citation(source: str, text: str) -> Citation:
    return {"source": source, "text": text}
