import sys
sys.path.insert(0, "code")

from inference import load_model, run_model
from prompts import base_prompt
from rag.retrieve import retrieve
from rag.retrieve import retrieve
import json

with open("code/data/mathdial_bridge.json") as f:
    data = json.load(f)

problem = data[0]["problem"]
print("PROBLEM:", problem[:100])

print("\nLoading model...")
model, tokenizer = load_model("TinyLlama/TinyLlama-1.1B-Chat-v1.0")

print("\nRunning base...")
output = run_model(model, tokenizer, base_prompt(problem))
print("OUTPUT:", output[:300])