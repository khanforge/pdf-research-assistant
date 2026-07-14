"""
Shared state for LangGraph.
"""

from typing import TypedDict

from langchain_core.documents import Document


class GraphState(TypedDict):
    """
    Shared state passed between nodes.
    """

    question: str

    rewritten_query: str

    documents: list[Document]

    context: str

    answer: str

    reflection: bool

    retry_count: int