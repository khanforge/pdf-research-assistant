from agentic_rag.graph import graph

state = {
    "question": "What skills does Parvej have?",
    "rewritten_query": "",
    "documents": [],
    "context": "",
    "answer": "",
    "reflection": False,
    "retry_count": 0,
}

result = graph.invoke(state)

print("\nOriginal Question:")
print(result["question"])

print("\nRewritten Query:")
print(result["rewritten_query"])

print("\nRetrieved Documents:")
print(f"Total: {len(result['documents'])}")

for i, doc in enumerate(result["documents"], start=1):
    print(f"\nDocument {i}")
    print(f"Source: {doc.metadata.get('source')}")
    print(f"Page: {doc.metadata.get('page')}")
    print(doc.page_content[:200])