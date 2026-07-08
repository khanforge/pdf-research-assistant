from typing import TypedDict


class PromptSchema(TypedDict):
    instruction: str
    input: str


DEFAULT_PROMPT: PromptSchema = {
    "instruction": "Use the provided document context to answer the user query.",
    "input": "{query}",
}
