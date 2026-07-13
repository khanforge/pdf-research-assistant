"""
Qdrant Vector Store Manager.
"""

from langchain_qdrant import QdrantVectorStore
from qdrant_client.http.models import Distance, VectorParams

from config import settings
from services.embeddings import get_embeddings
from services.vectorstore import get_qdrant_client
from utils.logger import setup_logger
from langchain_core.documents import Document


logger = setup_logger(__name__)


class QdrantStore:
    """
    Handles creation and interaction with the Qdrant vector store.
    """

    def __init__(self) -> None:
        self.client = get_qdrant_client()
        self.embeddings = get_embeddings()

        self.collection_name = settings.qdrant_collection

        self._create_collection()

        self.vector_store = QdrantVectorStore(
            client=self.client,
            collection_name=self.collection_name,
            embedding=self.embeddings,
        )

    def _create_collection(self) -> None:
        """
        Create collection if it does not exist.
        """

        collections = self.client.get_collections().collections

        existing = [c.name for c in collections]

        if self.collection_name in existing:
            logger.info("Collection already exists.")
            return

        logger.info("Creating collection...")

        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE,
            ),
        )

        logger.info("Collection created successfully.")

def add_documents(self, documents: list[Document]) -> None:
    """
    Store documents in Qdrant.
    """

    logger.info("Indexing %d chunks...", len(documents))

    self.vector_store.add_documents(documents)

    logger.info("Indexing completed.")