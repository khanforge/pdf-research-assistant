from services.embeddings import get_embeddings

embdeddings = get_embeddings()

vector = embdeddings.embed_query("What is Retrieval-Augmented Generation?")
print(len(vector))
print(vector)
