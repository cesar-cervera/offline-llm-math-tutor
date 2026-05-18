def base_prompt(problem):
    return f"""
You are a math tutor. Solve the following problem step by step.

You must end your response with exactly one line in this format:
FINAL ANSWER: <number>

Problem:
{problem}
"""


def structured_rag_prompt(problem, reference_solution):
    return f"""
You are a math tutor. You must base your explanation ONLY on the provided reference solution.
Do not change the logic.

You must end your response with exactly one line in this format:
FINAL ANSWER: <number>

Problem:
{problem}

Reference Solution:
{reference_solution}

Now explain the solution clearly and step by step.
"""