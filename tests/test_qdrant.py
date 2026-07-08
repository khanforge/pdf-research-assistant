from services.vectorstore import get_qdrant_client

client = get_qdrant_client()

print(client.get_collections())