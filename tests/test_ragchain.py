from agentic_rag.rag_chain import RAGChain

rag = RAGChain()

qs = "What skills does Parvej have?,Which company did Parvej work for?,Tell me about the Tutor Listing Platform., Which cloud technologies are mentioned?"

for q in qs.split(","):
    response = rag.answer(
        q
    )
    print(response["answer"])
