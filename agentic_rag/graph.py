
from .nodes import (
    memory_node,
    rewrite_query_node,
    retrieve_documents_node,
    reflection_node,
    generate_answer_node,
    retry_node,
    reflection_router,
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

builder.add_node(
    "memory",
    memory_node,
)

builder.add_edge(
    START,
    "memory",
)

builder.add_edge(
    "memory",
    "rewrite_query",
)

builder.add_edge(
    "rewrite_query",
    "retrieve_documents",
)

builder.add_edge(
    "retrieve_documents",
    "reflection",
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