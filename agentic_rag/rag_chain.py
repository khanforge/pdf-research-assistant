"""
RAG Chain.
"""

from langchain_core.documents import Document
from langchain_core.messages import HumanMessage, SystemMessage

from .prompts import RAG_SYSTEM_PROMPT
from retrieval.retriever import Retriever
from services.llm import get_llm
from utils.logger import setup_logger

logger = setup_logger(__name__)

class RAGChain:
    """
    Basic Retrieval-Augmented Generation chain.
    """

    def __init__(self):
        self.retriever = Retriever()
        self.llm = get_llm()

    def _build_context(
        self,
        documents: list[Document],
    ) -> str:
        """
        Build context from retrieved documents.
        """

        context = []

        for doc in documents:

            source = doc.metadata.get("source", "Unknown")

            page = doc.metadata.get("page", "N/A")

            context.append(
                f"""
    Source: {source}
    Page: {page}

    {doc.page_content}
    """
            )

        return "\n\n".join(context)
    
    def answer(
        self,
        question: str,
    ):
        """
        Answer a user question.
        """

        logger.info("Running RAG chain.")

        documents = self.retriever.retrieve(question)

        context = self._build_context(documents)

        messages = [

            SystemMessage(
                content=RAG_SYSTEM_PROMPT.format(
                    context=context
                )
            ),

            HumanMessage(
                content=question
            ),
        ]

        try:
            response = self.llm.invoke(messages)
        except Exception:
            self.llm = get_llm(1)
            response = self.llm.invoke(messages)

        return {
            "answer": response.content,
            "documents": documents,
        }