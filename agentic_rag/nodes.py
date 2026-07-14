from langchain_core.messages import HumanMessage, SystemMessage

from .prompts import QUERY_REWRITE_PROMPT
from services.llm import get_llm
from .state import GraphState

llm = get_llm()


def rewrite_query_node(state: GraphState) -> GraphState:
    """
    Rewrite the user's question for better retrieval.
    """

    print("Running Query Rewrite Node...")

    messages = [
        SystemMessage(
            content=QUERY_REWRITE_PROMPT.format(
                question=state["question"]
            )
        ),
        HumanMessage(
            content=state["question"]
        ),
    ]

    response = llm.invoke(messages)

    state["rewritten_query"] = response.content.strip()

    return state