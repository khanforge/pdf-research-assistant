from pathlib import Path
from typing import Iterable

from .loader import load_documents
from .splitter import split_text
from .embedder import embed_documents


def build_ingestion_pipeline(directory: Path, chunk_size: int, overlap: int) -> dict[str, list]:
    paths = load_documents(directory)
    texts = [path.read_text(encoding="utf-8") for path in paths]
    chunks = [split_text(text, chunk_size, overlap) for text in texts]
    embeddings = [embed for document in chunks for embed in embed_documents(document)]
    return {"paths": paths, "chunks": chunks, "embeddings": embeddings}
