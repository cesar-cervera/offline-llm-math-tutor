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


def retrieve(query, k=3, exclude=None):
    embedding = model.encode([query])
    embedding = np.array(embedding).astype("float32")
    search_k = max(k * 5, 20)
    distances, indices = index.search(embedding, search_k)

    results = []
    seen = set()
    for idx in indices[0]:
        if exclude is not None and problems[idx].strip() == exclude.strip():
            continue
        key = problems[idx].strip()
        if key in seen:
            continue
        seen.add(key)
        results.append({"problem": problems[idx], "solution": solutions[idx]})
        if len(results) == k:
            break
    return results