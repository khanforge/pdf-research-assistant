"""
Retriever module.

Handles semantic search over indexed documents.
"""

from langchain_core.documents import Document

from retrieval.qdrant_store import QdrantStore
from utils.logger import setup_logger

logger = setup_logger(__name__)


class Retriever:
    """
    Semantic document retriever.
    """

    def __init__(self, k: int = 4):
        self.store = QdrantStore()
        self.k = k

    def retrieve(self, query: str) -> list[Document]:
        """
        Retrieve the most relevant chunks.

        Args:
            query: User question.

        Returns:
            List of relevant documents.
        """

        logger.info("Searching for: %s", query)

        documents = self.store.vector_store.similarity_search(
            query=query,
            k=self.k,
        )

        logger.info("Retrieved %d chunks.", len(documents))

        return documents