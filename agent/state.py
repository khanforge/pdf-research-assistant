from dataclasses import dataclass


@dataclass
class AgentState:
    history: list[str]
    context: dict[str, str]


def create_initial_state() -> AgentState:
    return AgentState(history=[], context={})
