from agentic_rag.graph import graph

state = {
    "question": "What skills does Panda Singh have?",
    "previous_queries": [],
    "rewritten_query": "",
    "documents": [],
    "answer": "",
    "reflection": False,
    "retry_count": 0,
}

result = graph.invoke(state)

print("\nAnswer:\n")
print(result["answer"])