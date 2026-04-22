import os
from utils.frame_extractor import extract_frames
from indexing.embedder import generate_embeddings
from indexing.faiss_index import build_index

video_folder = "data/videos"
frame_folder = "data/frames"

os.makedirs(frame_folder, exist_ok=True)

# Extract frames
for video in os.listdir(video_folder):
    path = os.path.join(video_folder, video)
    print(f"Processing: {video}")
    extract_frames(path, frame_folder)

# Generate embeddings
embeddings, paths = generate_embeddings(frame_folder)

print("Total embeddings:", embeddings.shape)

# Build index
build_index(embeddings, paths)

print("Indexing Done")