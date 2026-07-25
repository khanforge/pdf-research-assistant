from agentic_rag.assistant import ResearchAssistant

assistant = ResearchAssistant()

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    result = assistant.ask(question)

    print("\nAssistant:\n")
    print(result["answer"])