from services.vectorstore import get_qdrant_client
from config import settings
from pprint import pprint

client = get_qdrant_client()

points, _ = client.scroll(
    collection_name=settings.qdrant_collection,
    limit=5,
    with_payload=True,
)

for point in points:
    print(point.payload['metadata']["source"])