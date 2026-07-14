from agentic_rag.graph import graph

state = {
    "question": "Backend stack?",
    "rewritten_query": "",
    "documents": [],
    "context": "",
    "answer": "",
    "reflection": False,
    "retry_count": 0,
}

result = graph.invoke(state)

print("\nOriginal:")
print(result["question"])

print("\nRewritten:")
print(result["rewritten_query"])