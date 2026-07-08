"""
Application configuration.

Loads settings from environment variables using Pydantic.
"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    """Centralized application settings."""

    "BASE PATH"

    BASE_PATH:Path = Path.cwd()

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # ------------------------
    # Google Gemini
    # ------------------------
    google_api_key: str = Field(default="")

    # ------------------------
    # LLM
    # ------------------------
    llm_provider: str = "google"
    llm_model: str = "gemini-2.5-flash"

    # ------------------------
    # Embeddings
    # ------------------------
    embedding_model: str = "BAAI/bge-small-en-v1.5"

    # ------------------------
    # Qdrant
    # ------------------------
    qdrant_host: str = "localhost"
    qdrant_port: int = 6333
    qdrant_collection: str = "research_documents"

    # ------------------------
    # Chunking
    # ------------------------
    chunk_size: int = 800
    chunk_overlap: int = 150


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance."""
    return Settings()


settings = get_settings()