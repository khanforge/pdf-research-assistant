from typing import Any


class LangNode:
    def __init__(self, name: str):
        self.name = name

    def execute(self, context: dict[str, Any]) -> dict[str, Any]:
        return context
