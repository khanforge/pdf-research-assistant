from langchain_core.messages import HumanMessage, SystemMessage

from .prompts import QUERY_REWRITE_PROMPT, REFLECTION_PROMPT
from services.llm import get_llm
from .state import GraphState
from retrieval.retriever import Retriever
from logging import getLogger
import traceback
from langgraph.graph import END

model_name, llm = get_llm()
retriever = Retriever()
logger = getLogger(__name__)


def rewrite_query_node(state: GraphState) -> GraphState:
    """
    Rewrite the user's question for better retrieval.
    """

    logger.info("Running Query Rewrite Node...")

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

    try:
        response = llm.invoke(messages)
    except Exception:
        fallback_model_name, fallback_llm = get_llm(1)
        logger.info(f"retrying with {fallback_model_name}")
        response = fallback_llm.invoke(messages)

    try:
        state["rewritten_query"] = response.content.strip()
    except Exception as e:
        if isinstance(response.content, list):
            try:
                state["rewritten_query"] = response.content[0]["text"]
            except Exception as e:
                logger.error(f"some exception happened {traceback.format_exc}\n\n response = {response.content}")
    return state

def retrieve_documents_node(state: GraphState) -> GraphState:
    """
    Retrieve relevant documents using the rewritten query.
    """

    logger.info("Running Retrieval Node...")

    query = state["rewritten_query"]

    documents = retriever.retrieve(query)

    state["documents"] = documents

    return state

def reflection_node(state: GraphState) -> GraphState:
    """
    Decide whether the retrieved documents
    are sufficient to answer the question.
    """

    logger.info("Running Reflection Node...")

    context = "\n\n".join(
        doc.page_content
        for doc in state["documents"]
    )

    messages = [
        HumanMessage(
            content=REFLECTION_PROMPT.format(
                question=state["question"],
                context=context,
            )
        )
    ]

    try:
        response = llm.invoke(messages)
    except Exception as e:
        fallback_model_name, fallback_llm = get_llm(1)
        logger.info(f"trying with model: {fallback_model_name}")
        response = fallback_llm.invoke(messages)

    try:
        decision = response.content.strip()
    except Exception as e:
        if isinstance(response.content, list):
            try:
                decision = response.content[0]["text"]
            except Exception as e:
                logger.error(f"some exception happened {traceback.format_exc}\n\n response = {response.content}")

    state["reflection"] = decision == "YES"

    return state

MAX_RETRIES = 2
def reflection_router(state: GraphState):
    """
    Decide the next node after reflection.
    """

    # Enough context -> finish
    if state["reflection"]:
        return END

    # Maximum retries reached -> finish
    if state["retry_count"] >= MAX_RETRIES:
        return END

    # Retry retrieval
    return "retry_node"

def retry_node(state: GraphState) -> GraphState:
    logger.info("Retrying retrieval...")

    state["retry_count"] += 1

    return state