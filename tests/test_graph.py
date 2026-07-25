from agentic_rag.graph import graph
from langchain_core.messages import HumanMessage, AIMessage

state = {
    "question": "What technologies were used there?",
    "rewritten_query": "",
    "previous_queries": [],
    "documents": [],
    "answer": "",
    "reflection": False,
    "retry_count": 0,

    "conversation_summary": "",

    "chat_history": [
        HumanMessage(content="Tell me about Parvej."),
        AIMessage(content="Parvej is a Software Engineer at CollegeDekho."),
        HumanMessage(content="What projects did he work on?"),
        AIMessage(content="He worked on backend services and CMS."),
        HumanMessage(content="Tell me more."),
        AIMessage(content="He used Django and Python."),
    ],
}

result = graph.invoke(state)

print("\nSUMMARY\n")
print(result["chat_history"])

print("="*80)
print(result["conversation_summary"])

print("\nAnswer:\n")
print(result["answer"])