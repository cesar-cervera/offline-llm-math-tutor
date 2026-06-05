def base_prompt(problem):
    return f"""You are a math tutor. Solve the following problem step by step.

Show your work clearly with numbered steps.
You must end your response with exactly one line in this format:
FINAL ANSWER: <number>

Problem:
{problem}
"""


def rag_prompt(problem, retrieved_examples):
    examples_text = ""
    for i, ex in enumerate(retrieved_examples):
        examples_text += f"""
Example {i+1}:
Problem: {ex['problem']}
Solution: {ex['solution']}
"""

    return f"""You are a math tutor. Use the following solved examples to help you solve the new problem.

{examples_text}

Now solve this new problem step by step using the examples above as guidance.
Show your work clearly with numbered steps.
You must end your response with exactly one line in this format:
FINAL ANSWER: <number>

Problem:
{problem}
"""


def explanation_score_prompt(problem, reference_solution, model_explanation):
    return f"""You are evaluating a math tutor's explanation.

Problem:
{problem}

Reference Solution:
{reference_solution}

Model Explanation:
{model_explanation}

Check if the key numbers and steps from the reference solution appear in the model explanation.
Respond with only a JSON object in this format:
{{"explanation_correct": true/false, "reason": "brief reason"}}
"""