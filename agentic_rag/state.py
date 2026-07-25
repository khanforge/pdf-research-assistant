from typing import TypedDict
from langchain_core.documents import Document
from langchain_core.messages import BaseMessage


class GraphState(TypedDict):
    # Current user query
    question: str

    # Query rewriting
    rewritten_query: str
    previous_queries: list[str]

    # Retrieval
    documents: list[Document]

    # Final answer
    answer: str

    # Reflection
    reflection: bool
    retry_count: int

    # Conversation memory
    chat_history: list[BaseMessage]
    conversation_summary: str