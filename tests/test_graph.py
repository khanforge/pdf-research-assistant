from agentic_rag.graph import graph

result = graph.invoke(
    {
        "message": "Start"
    }
)

print(result)