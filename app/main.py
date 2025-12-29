from fastapi import FastAPI, HTTPException
from app.model import answer_question
from app.utils import clean_text, validate_inputs, format_response

app = FastAPI()

@app.post("/ask")
def ask(question: str, context:str):
    try:
        question = clean_text(question)
        context = clean_text(context)

        validate_inputs(question, context)

        result = answer_question(question, context)
        return format_response(result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))