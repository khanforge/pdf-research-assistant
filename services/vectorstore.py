"""
Qdrant client service.
"""

from functools import lru_cache

from qdrant_client import QdrantClient

from config import settings


@lru_cache
def get_qdrant_client() -> QdrantClient:
    """
    Return a configured Qdrant client.
    """

    return QdrantClient(
        host=settings.qdrant_host,
        port=settings.qdrant_port,
    )