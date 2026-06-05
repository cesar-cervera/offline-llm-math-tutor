import re


def extract_final_answer(text):
    match = re.search(r"####\s*(-?\d+(?:\.\d+)?)", text)
    if match:
        return match.group(1).strip()
    lines = [l.strip() for l in text.strip().split("\n") if l.strip()]
    if lines:
        numbers = re.findall(r"-?\d+(?:\.\d+)?", lines[-1])
        if numbers:
            return numbers[-1]
    return None


def extract_model_answer(text):
    match = re.search(r"FINAL ANSWER:\s*(-?\d+(?:\.\d+)?)", text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None


def score_explanation(reference_solution, model_explanation):
    ref_numbers = set(re.findall(r"-?\d+(?:\.\d+)?", reference_solution))
    exp_numbers = set(re.findall(r"-?\d+(?:\.\d+)?", model_explanation))

    if not ref_numbers:
        return False

    overlap = ref_numbers.intersection(exp_numbers)
    coverage = len(overlap) / len(ref_numbers)

    return coverage >= 0.5


def score_response(reference_solution, model_output):
    gold = extract_final_answer(reference_solution)
    pred = extract_model_answer(model_output)

    answer_correct = (
        gold is not None and
        pred is not None and
        gold == pred
    )

    explanation_correct = score_explanation(reference_solution, model_output)

    return {
        "answer_correct": answer_correct,
        "explanation_correct": explanation_correct,
        "gold": gold,
        "pred": pred
    }