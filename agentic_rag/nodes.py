"""
LangGraph nodes.
"""

from .state import GraphState


def hello_node(state: GraphState) -> GraphState:
    """
    First LangGraph node.
    """

    print("Executing Hello Node...")

    state["message"] += " -> Hello from LangGraph"

    return state