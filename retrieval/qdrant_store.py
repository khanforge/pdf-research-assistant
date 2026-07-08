from typing import Iterable


class QdrantStore:
    def __init__(self, url: str):
        self.url = url

    def upsert(self, embeddings: Iterable[list[float]]) -> None:
        pass

    def search(self, query_embedding: list[float], limit: int = 5) -> list[dict[str, float]]:
        return []
