"""
LLM service.

Provides a singleton Gemini model instance.
"""

from functools import lru_cache

from langchain_google_genai import ChatGoogleGenerativeAI

from config import settings


@lru_cache
def get_llm() -> ChatGoogleGenerativeAI:
    """
    Return a configured Gemini chat model.

    Returns:
        ChatGoogleGenerativeAI
    """

    return ChatGoogleGenerativeAI(
        model=settings.llm_model,
        google_api_key=settings.google_api_key,
        temperature=0.2,
    )