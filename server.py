from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import run_query

app = FastAPI()

class QuestionInput(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(input: QuestionInput):
    try:
        response = run_query(input.question)

        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
