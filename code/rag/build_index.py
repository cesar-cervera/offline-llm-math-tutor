import json
import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "mathdial_bridge.json")
INDEX_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "index", "faiss_index.bin")
PROBLEMS_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "index", "problems.json")

def build_index():
    print("Loading dataset...")
    with open(DATA_PATH, "r") as f:
        data = json.load(f)

    problems = [ex["problem"] for ex in data]
    solutions = [ex["reference_solution"] for ex in data]

    print("Building embeddings...")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(problems, show_progress_bar=True)
    embeddings = np.array(embeddings).astype("float32")

    print("Building FAISS index...")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)
    faiss.write_index(index, INDEX_PATH)

    with open(PROBLEMS_PATH, "w") as f:
        json.dump({"problems": problems, "solutions": solutions}, f)

    print(f"Index built with {len(problems)} examples.")

if __name__ == "__main__":
    build_index()