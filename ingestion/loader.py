"""
PDF Loader Module.

Responsible for loading PDF files into LangChain Document objects.
"""

from pathlib import Path
from typing import List

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.documents import Document

from utils.logger import setup_logger
from config import settings

logger = setup_logger(__name__)


class PDFLoader:
    """
    Loads PDF documents while preserving metadata.
    """

    def load(self, pdf_path: str | Path) -> List[Document]:
        """
        Load a PDF file.

        Args:
            pdf_path: Path to the PDF file.

        Returns:
            List of LangChain Document objects.
        """

        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            pdf_path = settings.BASE_PATH/pdf_path
        
        print(f"base path = {settings.BASE_PATH}")
        print(settings.BASE_PATH/pdf_path)

        if not pdf_path.exists():
            raise FileNotFoundError(f"{pdf_path} does not exist.")

        logger.info(f"Loading PDF: {pdf_path.name}")

        loader = PyMuPDFLoader(str(pdf_path))

        documents = loader.load()

        logger.info(
            "Loaded %d pages from %s",
            len(documents),
            pdf_path.name,
        )

        return documents