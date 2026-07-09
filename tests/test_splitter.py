from ingestion.loader import PDFLoader
from ingestion.splitter import DocumentSplitter

loader = PDFLoader()
splitter = DocumentSplitter()

documents = loader.load("data/uploads/parvej_khan.pdf")

chunks = splitter.split(documents)

print(f"Pages: {len(documents)}")
print(f"Chunks: {len(chunks)}")

print("-" * 50)

print(chunks[0].metadata)

print("-" * 50)

print(chunks[0].page_content)

count = 1
for chunk in chunks:
    print(" "*5, f"chunk {count}")
    print("-" * 50)
    print(chunk)
    print("-" * 50)
    count += 1
