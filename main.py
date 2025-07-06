from fastapi import FastAPI, Form
from explain import explain_solution

app = FastAPI()

@app.post("/explain")
async def explain(code: str = Form(...)):
    explanation = explain_solution(code)
    return {"explanation": explanation}
