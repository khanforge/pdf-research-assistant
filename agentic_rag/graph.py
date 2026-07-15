from .nodes import (
    rewrite_query_node,
    retrieve_documents_node,
)
from langgraph.graph import StateGraph, START, END
from .state import GraphState

builder = StateGraph(GraphState)

builder.add_node(
    "rewrite_query",
    rewrite_query_node,
)

builder.add_node(
    "retrieve_documents",
    retrieve_documents_node,
)

builder.add_edge(
    START,
    "rewrite_query",
)

builder.add_edge(
    "rewrite_query",
    "retrieve_documents",
)

builder.add_edge(
    "retrieve_documents",
    END,
)

graph = builder.compile()