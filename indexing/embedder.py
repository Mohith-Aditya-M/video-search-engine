import os
import numpy as np
from models.clip_model import encode_image

def generate_embeddings(frame_folder):
    embeddings = []
    paths = []

    for file in os.listdir(frame_folder):
        path = os.path.join(frame_folder, file)

        try:
            emb = encode_image(path)
            embeddings.append(emb[0])
            paths.append(path)
        except:
            continue

    return np.array(embeddings), paths