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

    if settings.qdrant_url:
        return QdrantClient(
            url=settings.qdrant_url,
            api_key = settings.qdrant_api_key
        )

    return QdrantClient(
        host=settings.qdrant_host,
        port=settings.qdrant_port,
    )