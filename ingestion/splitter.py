"""
Document splitter.

Responsible for splitting documents into smaller chunks
while preserving metadata.
"""

from typing import List

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import settings
from utils.logger import setup_logger

logger = setup_logger(__name__)


class DocumentSplitter:
    """
    Splits LangChain Documents into smaller chunks.
    """

    def __init__(self) -> None:
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                "",
            ],
        )

    def split(self, documents: List[Document]) -> List[Document]:
        """
        Split documents into chunks.

        Args:
            documents: List of loaded documents.

        Returns:
            List of chunked documents.
        """

        logger.info("Splitting %d document(s)...", len(documents))

        chunks = self.text_splitter.split_documents(documents)

        logger.info("Generated %d chunks.", len(chunks))

        return chunks