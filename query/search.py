from models.clip_model import encode_text
from indexing.faiss_index import load_index

def search(query, top_k=5):
    index, paths = load_index()

    q = encode_text(query)
    D, I = index.search(q, top_k)

    results = []
    for idx in I[0]:
        results.append(paths[idx])

    return results