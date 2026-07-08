"""
Embedding service.

Provides a singleton HuggingFace embedding model.
"""

from functools import lru_cache

from langchain_huggingface import HuggingFaceEmbeddings

from config import settings


@lru_cache
def get_embeddings() -> HuggingFaceEmbeddings:
    """
    Return configured embedding model.
    """

    return HuggingFaceEmbeddings(
        model_name=settings.embedding_model,
        model_kwargs={
            "device": "cpu",
        },
        encode_kwargs={
            "normalize_embeddings": True,
        },
    )