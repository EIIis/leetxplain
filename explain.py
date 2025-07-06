import subprocess

def build_prompt(code: str) -> str:
    return f"""You are a helpful software engineer. Given the following LeetCode-style solution, explain what the code is doing step-by-step.

Then, estimate the time and space complexity.

Here is the code:
```python
{code}
```
Provide your answer in this format:
1. What the algorithm solves
2. Step-by-step explanation
3. Time complexity
4. Space complexity
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
