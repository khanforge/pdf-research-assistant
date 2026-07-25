from agentic_rag.graph import graph
from agentic_rag.state import GraphState

class ResearchAssistant:
    """
    High-level interface over the LangGraph workflow.
    """

    def __init__(self):
        self.chat_history = []
        self.conversation_summary = ""

    def ask(self, question: str):
        state: GraphState = {
            "question": question,
            "rewritten_query": "",
            "previous_queries": [],
            "documents": [],
            "answer": "",
            "reflection": False,
            "retry_count": 0,
            "chat_history": self.chat_history,
            "conversation_summary": self.conversation_summary,
        }

        result = graph.invoke(state)

        self.chat_history = result["chat_history"]
        self.conversation_summary = result["conversation_summary"]

        return {
            "answer": result["answer"],
            "rewritten_query": result["rewritten_query"],
            "documents": result["documents"],
            "reflection": result["reflection"],
            "retry_count": result["retry_count"],
        }