from typing import Iterable

from .qdrant_store import QdrantStore


class Retriever:
    def __init__(self, store: QdrantStore):
        self.store = store

    def retrieve(self, embeddings: Iterable[list[float]]) -> list[dict[str, float]]:
        return []
