from ingestion.loader import PDFLoader

loader = PDFLoader()

docs = loader.load("data/uploads/parvej_khan.pdf")

print(f"Pages Loaded: {len(docs)}")

print("-" * 40)

print(docs[0].metadata)

print("-" * 40)

print(docs[0].page_content[:500])
print(docs)