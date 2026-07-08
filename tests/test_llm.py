from services.llm import get_llm

llm = get_llm()
response = llm.invoke("Say hello in three Line ")

print(response.content)