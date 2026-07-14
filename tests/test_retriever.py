from retrieval.retriever import Retriever


retriever = Retriever()

documents = retriever.retrieve(
    "where did parvej work"
)

print(f"Retrieved {len(documents)} chunks\n")

for i, doc in enumerate(documents, start=1):
    print("=" * 80)
    print(f"Chunk {i}")
    print(f"Source : {doc.metadata['source']}")
    print(f"Page   : {doc.metadata['page']}")
    print("-" * 80)
    print(doc.page_content[:400])


