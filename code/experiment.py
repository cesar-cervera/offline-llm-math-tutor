import json
import os
import sys
from tqdm import tqdm
from inference import load_model, run_model
from prompts import base_prompt, rag_prompt
from rag.retrieve import retrieve
from evaluate import score_response

MODELS = {
    "Qwen3B": "Qwen/Qwen2.5-3B-Instruct",
    "Gemma4B": "google/gemma-2-4b-it"
}

ROOT = os.path.dirname(os.path.dirname(__file__))
DATA = {
    "easy": os.path.join(ROOT, "code", "data", "mathdial_bridge.json"),
    "hard": os.path.join(ROOT, "code", "data", "mathdial_bridge_hard.json")
}
RESULTS_PATH = os.path.join(ROOT, "code", "results", "results.json")


def load_dataset(path):
    with open(path, "r") as f:
        return json.load(f)


def run_experiment(model, tokenizer, model_name, dataset, split, mode):
    answer_correct = 0
    explanation_correct = 0
    both_correct = 0
    answer_only = 0
    total = len(dataset)

    print(f"\nRunning {model_name} | {split} | {mode}")

    for example in tqdm(dataset):
        problem = example["problem"]
        reference = example["reference_solution"]

        if mode == "base":
            prompt = base_prompt(problem)
        else:
            retrieved = retrieve(problem, k=3)
            prompt = rag_prompt(problem, retrieved)

        output = run_model(model, tokenizer, prompt)
        scores = score_response(reference, output)

        if scores["answer_correct"]:
            answer_correct += 1
        if scores["explanation_correct"]:
            explanation_correct += 1
        if scores["answer_correct"] and scores["explanation_correct"]:
            both_correct += 1
        if scores["answer_correct"] and not scores["explanation_correct"]:
            answer_only += 1

    results = {
        "answer_accuracy": answer_correct / total,
        "explanation_accuracy": explanation_correct / total,
        "both_correct": both_correct / total,
        "answer_only": answer_only / total,
        "total": total
    }

    print(f"Answer Accuracy: {results['answer_accuracy']:.4f}")
    print(f"Explanation Accuracy: {results['explanation_accuracy']:.4f}")
    print(f"Both Correct: {results['both_correct']:.4f}")
    print(f"Answer Only (misleading): {results['answer_only']:.4f}")

    return results


def main():
    all_results = {}
    os.makedirs(os.path.dirname(RESULTS_PATH), exist_ok=True)

    for model_name, model_id in MODELS.items():
        print(f"\n{'='*50}")
        print(f"Loading {model_name}")
        print(f"{'='*50}")

        model, tokenizer = load_model(model_id)
        all_results[model_name] = {}

        for split, path in DATA.items():
            dataset = load_dataset(path)
            all_results[model_name][split] = {}

            for mode in ["base", "rag"]:
                results = run_experiment(
                    model, tokenizer, model_name,
                    dataset, split, mode
                )
                all_results[model_name][split][mode] = results

        with open(RESULTS_PATH, "w") as f:
            json.dump(all_results, f, indent=2)
        print(f"\nResults saved to {RESULTS_PATH}")

    print("\n===== FINAL RESULTS =====")
    for model_name, splits in all_results.items():
        for split, modes in splits.items():
            for mode, results in modes.items():
                print(f"\n{model_name} | {split} | {mode}")
                print(f"  Answer Accuracy: {results['answer_accuracy']:.4f}")
                print(f"  Explanation Accuracy: {results['explanation_accuracy']:.4f}")
                print(f"  Both Correct: {results['both_correct']:.4f}")
                print(f"  Answer Only (misleading): {results['answer_only']:.4f}")


if __name__ == "__main__":
    main()