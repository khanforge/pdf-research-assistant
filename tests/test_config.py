from config import settings

print("Provider:", settings.llm_provider)
print("Model:", settings.llm_model)
print("Embedding:", settings.embedding_model)
print("Collection:", settings.qdrant_collection)
print("Chunk Size:", settings.chunk_size)

