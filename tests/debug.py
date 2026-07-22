from langchain_core.messages import HumanMessage
from services.llm import get_llm

_, llm = get_llm(1)

response = llm.invoke([
    HumanMessage(content="Reply with YES")
])

print(response)