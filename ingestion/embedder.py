from __future__ import annotations
from typing import Iterable


def embed_documents(documents: Iterable[str]) -> list[list[float]]:
    return [[float(ord(char)) for char in doc[:32]] for doc in documents]
