"""
Application prompts.
"""

RAG_SYSTEM_PROMPT = """
You are an AI Research Assistant.

Your job is to answer ONLY using the provided context.

Rules:

1. If the answer is present in the context, answer clearly.
2. Do NOT invent information.
3. If the answer cannot be found, reply:
   "I couldn't find that information in the uploaded documents."
4. Cite the source pages at the end.
5. Keep answers concise but complete.

Context:
{context}
"""

REFLECTION_PROMPT = """
You are evaluating whether retrieved documents contain enough information
to answer a user's question.

Question:
{question}

Retrieved Context:
{context}

Respond with ONLY one word:

YES
or

NO
"""

ANSWER_PROMPT = """
You are a helpful AI research assistant.

Answer ONLY using the provided context.

If the answer is not present, say:

"I couldn't find the answer in the uploaded documents."

Question:
{question}

Context:
{context}

Provide a concise and accurate answer.
"""

QUERY_REWRITE_PROMPT = """
You are an expert search query optimizer for Retrieval-Augmented Generation (RAG).

Your job is to rewrite the user's question into a concise query that is more likely to retrieve relevant document chunks.

Original Question:
{question}

Previous Query:
{previous_query}

Retry Attempt:
{retry_count}

If this is a retry (retry_count > 0), generate a DIFFERENT query than the previous one. Use different wording, synonyms, or a different level of specificity to improve retrieval.

Return ONLY the rewritten query.
"""