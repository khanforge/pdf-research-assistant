from .nodes import (
    rewrite_query_node,
    retrieve_documents_node,
    reflection_node,
    reflection_router,
    retry_node,
    generate_answer_node
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

builder.add_node(
    "reflection",
    reflection_node,
)

builder.add_node(
    "retry_node",
    retry_node
)

builder.add_node(
    "generate_answer_node",
    generate_answer_node
)

builder.add_edge(
    "retrieve_documents",
    "reflection",
)

builder.add_edge(
    START,
    "rewrite_query",
)

builder.add_edge(
    "rewrite_query",
    "retrieve_documents",
)

builder.add_conditional_edges(
    "reflection",
    reflection_router,
)

builder.add_edge(
    "retry_node",
    "rewrite_query"
)


graph = builder.compile()