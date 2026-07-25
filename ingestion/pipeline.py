"""
Document ingestion pipeline.
"""

from pathlib import Path

from ingestion.loader import PDFLoader
from ingestion.splitter import DocumentSplitter
from retrieval.qdrant_store import QdrantStore
from utils.logger import setup_logger

logger = setup_logger(__name__)


class IngestionPipeline:
    """
    Complete document ingestion pipeline.
    """

    def __init__(self) -> None:
        self.loader = PDFLoader()
        self.splitter = DocumentSplitter()
        self.store = QdrantStore()

    def ingest(self, pdf_path: str | Path) -> None:
        """
        Ingest a PDF into Qdrant.
        """

        logger.info("Starting ingestion pipeline.")

        documents = self.loader.load(pdf_path)

        chunks = self.splitter.split(documents)

        self.store.add_documents(chunks)

        logger.info("Pipeline completed.")

        return { 
            "filename": str(pdf_path),
            "documents": len(documents),
            "chunks": len(chunks)
        }