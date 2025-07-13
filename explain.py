import subprocess

def build_prompt(code: str) -> str:
    return f"""
            You are a Leetcode expert, particularly in python. Given the following LeetCode solution, explain what the code is doing step-by-step, please make sure to describe
            what data structure/algorithm is being used and why. Then, estimate the time and space complexity, and make sure to describe why. You are describing your explanation
            who is a beginner in programming, so make sure to explain fundamental concepts and avoid using jargon or complex terms.
            Here is the code:
            ```python
            {code}
            ```
            Provide your answer in this format:
            1. What the answer is solving
            2. Step-by-step explanation
            3. Time complexity
            4. Space complexity

            Do not do it in paragraph form, you should be able to break it down in sections. Also, ignore any comments in the code, make you're own explanation and explain how you got
            to such conclusion.
            """

def explain_solution(code: str) -> str:
    prompt = build_prompt(code)
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode().strip()
