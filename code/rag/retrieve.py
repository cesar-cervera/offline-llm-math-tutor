import json
import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "index", "faiss_index.bin")
PROBLEMS_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "index", "problems.json")

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index(INDEX_PATH)

with open(PROBLEMS_PATH, "r") as f:
    data = json.load(f)
    problems = data["problems"]
    solutions = data["solutions"]


def retrieve(query, k=3):
    embedding = model.encode([query])
    embedding = np.array(embedding).astype("float32")
    distances, indices = index.search(embedding, k)
    
    results = []
    for idx in indices[0]:
        results.append({
            "problem": problems[idx],
            "solution": solutions[idx]
        })
    return results