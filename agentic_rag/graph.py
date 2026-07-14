"""
Simple LangGraph.
"""

from langgraph.graph import START, END, StateGraph

from .nodes import hello_node
from .state import GraphState


builder = StateGraph(GraphState)

builder.add_node("hello", hello_node)

builder.add_edge(START, "hello")

builder.add_edge("hello", END)

graph = builder.compile()