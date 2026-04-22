import faiss
import pickle

def build_index(embeddings, paths):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    faiss.write_index(index, "data/index.faiss")

    with open("data/meta.pkl", "wb") as f:
        pickle.dump(paths, f)

def load_index():
    index = faiss.read_index("data/index.faiss")

    with open("data/meta.pkl", "rb") as f:
        paths = pickle.load(f)

    return index, paths