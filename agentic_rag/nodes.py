from langchain_core.messages import HumanMessage, SystemMessage

from .prompts import QUERY_REWRITE_PROMPT
from services.llm import get_llm
from .state import GraphState
from retrieval.retriever import Retriever

llm = get_llm()
retriever = Retriever()

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

def retrieve_documents_node(state: GraphState) -> GraphState:
    """
    Retrieve relevant documents using the rewritten query.
    """

    print("Running Retrieval Node...")

    query = state["rewritten_query"]

    documents = retriever.retrieve(query)

    state["documents"] = documents

    return state