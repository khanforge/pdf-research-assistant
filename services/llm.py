"""
LLM service.

Provides a singleton Gemini model instance.
"""

from functools import lru_cache

from langchain_google_genai import ChatGoogleGenerativeAI

from config import settings


@lru_cache
def get_llm(model_index=0) -> ChatGoogleGenerativeAI:
    """
    Return a configured Gemini chat model.

    Returns:
        ChatGoogleGenerativeAI
    """

    MODEL_MAP = {
        0:settings.llm_model,
        1:settings.llm_model1
    }

    return MODEL_MAP[model_index], ChatGoogleGenerativeAI(
        model=MODEL_MAP[model_index],
        google_api_key=settings.google_api_key,
        temperature=0.2,
    )