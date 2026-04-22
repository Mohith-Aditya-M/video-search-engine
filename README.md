# 🎥 Intelligent Video Search Engine  
### Natural Language Querying Over Video Archives

An AI-powered system that enables searching inside videos using natural language queries.  
It converts video frames into embeddings, stores them in a vector database, and retrieves relevant moments using semantic similarity.

---

# 🚀 Setup & Installation

## 1. Clone repository
git clone https://github.com/Mohith-Aditya-M/video-search-engine.git  
cd video-search-engine  

## 2. Create virtual environment
python -m venv venv  
source venv/bin/activate   # Mac/Linux  
venv\Scripts\activate      # Windows  

## 3. Install dependencies
pip install -r requirements.txt  

## 4. Install FFmpeg (required)
Install FFmpeg and add it to system PATH

## 5. Run project

### Step 1: Index videos
python src/index.py --input data/videos/

### Step 2: Run search engine
python src/search.py

### Step 3: Start UI
streamlit run app.py  

---

# 🧠 Architecture Overview

Video Input  
→ Frame Extraction (FFmpeg / OpenCV)  
→ Frame Sampling (uniform / scene-based)  
→ Feature Extraction (CLIP model)  
→ Embedding Storage (FAISS vector database)  
→ Query Embedding (text → vector)  
→ Similarity Search  
→ Top-K Retrieval  
→ Re-ranking (temporal smoothing)  
→ Final timestamp output  

---

# 🏗️ Design Decisions

## Vector Store: FAISS
- Fast similarity search
- Lightweight and scalable
- Better performance for local systems

## Embedding Model: CLIP
- Strong text-image alignment
- Works in zero-shot setting
- Best fit for natural language video search

## Frame Sampling Strategy
- Uniform sampling (1 FPS default)
- Scene detection tested but expensive
- Final hybrid approach used

## Re-ranking Strategy
- Temporal grouping for continuity
- Reduces noisy frame-level results

---

# 📊 Benchmark Results

Hardware: Intel i5, 16GB RAM (CPU only)

## Indexing Performance
- 18–25 frames/sec extraction
- 8–12 frames/sec embedding
- 2–3 min per 10 min video

## Query Latency
- Vector search: 30–80 ms
- End-to-end: < 500 ms

## Memory Usage
- 300–600 MB per hour of video embeddings

---

# ⚠️ Known Limitations

- Weak on fast motion scenes
- Struggles with small text in frames
- No real-time ingestion
- No multilingual query support
- CPU-only slows embedding generation

---

# 🔍 What I Explored Beyond

- Scene detection indexing (PySceneDetect)
- Caption-based retrieval (BLIP experiments)
- FAISS optimization (Flat vs IVF)
- Temporal scoring improvements
- Query expansion techniques

Findings:
- Hybrid embeddings improve accuracy
- Scene-based segmentation improves precision but increases cost

---

# 📌 Future Improvements

- Real-time video ingestion
- Multilingual query support
- GPU acceleration for embeddings
- Transformer-based temporal reasoning
- Scalable cloud vector database integration

---

video:
- 

https://github.com/user-attachments/assets/c237d3fd-ef09-4ab5-9845-5dd77e449b98





