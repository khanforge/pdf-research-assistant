from typing import Any


class LangGraph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node: Any) -> None:
        self.nodes.append(node)

    def run(self, input_text: str) -> str:
        return input_text
