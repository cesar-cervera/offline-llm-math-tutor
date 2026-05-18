import json
import os
import re
import inference
from inference import run_model
from prompts import base_prompt, structured_rag_prompt

print("USING INFERENCE FILE:", inference.__file__)

ROOT = os.path.dirname(os.path.dirname(__file__))

PHI_MODEL = os.path.join(ROOT, "models", "Phi-3-mini-4k-instruct-q4.gguf")
TINY_MODEL = os.path.join(ROOT, "models", "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf")


def load_dataset(path):
    with open(path, "r") as f:
        return json.load(f)


def extract_final_answer(reference_solution):
    match = re.search(r"####\s*(-?\d+(?:\.\d+)?)", reference_solution)
    if match:
        return match.group(1).strip()

    lines = [line.strip() for line in reference_solution.strip().split("\n") if line.strip()]
    if not lines:
        return None

    last_line = lines[-1]
    numbers = re.findall(r"-?\d+(?:\.\d+)?", last_line)
    if numbers:
        return numbers[-1]

    return None


def extract_model_answer(text):
    match = re.search(r"FINAL ANSWER:\s*(-?\d+(?:\.\d+)?)", text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None


def run_experiment(dataset_path, model_path, mode="base", limit=5, debug=False):
    data = load_dataset(dataset_path)
    total_score = 0

    print(f"\nRunning {mode} mode on {os.path.basename(model_path)}")

    for i, example in enumerate(data[:limit]):
        problem = example["problem"]
        reference = example["reference_solution"]

        if mode == "base":
            prompt = base_prompt(problem)
        else:
            prompt = structured_rag_prompt(problem, reference)

        output = run_model(model_path, prompt)
        gold = extract_final_answer(reference)
        pred = extract_model_answer(output)

        if debug and i == 0:
            print("\nDEBUG EXAMPLE")
            print("GOLD:", gold)
            print("PRED:", pred)
            print("RAW OUTPUT:\n", output[:800])
            print("----")

        score = int(gold == pred) if gold is not None and pred is not None else 0
        total_score += score

    accuracy = total_score / limit
    print(f"Accuracy: {accuracy:.2f}")
    return accuracy


if __name__ == "__main__":
    dataset_easy = os.path.join(ROOT, "code", "data", "mathdial_bridge_hard.json")

    print("===== Hard DATASET PILOT =====")

    phi_base = run_experiment(dataset_easy, PHI_MODEL, mode="base", limit=5, debug=True)
    phi_rag = run_experiment(dataset_easy, PHI_MODEL, mode="rag", limit=5)

    tiny_base = run_experiment(dataset_easy, TINY_MODEL, mode="base", limit=5)
    tiny_rag = run_experiment(dataset_easy, TINY_MODEL, mode="rag", limit=5)

    print("\n===== PILOT SUMMARY =====")
    print(f"Phi-3 Base: {phi_base:.2f}")
    print(f"Phi-3 RAG: {phi_rag:.2f}")
    print(f"TinyLlama Base: {tiny_base:.2f}")
    print(f"TinyLlama RAG: {tiny_rag:.2f}")