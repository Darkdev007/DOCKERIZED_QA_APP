from fastapi import FastAPI, Request, Query, HTTPException
from app.model import answer_question
from app.utils import clean_text, validate_inputs, format_response

app = FastAPI()

@app.post("/ask")
async def ask(
    request: Request = None,
    question: str = Query(None, description="The question to ask"),
    context: str = Query(None, description="The context to use")
):
    try:
        # Try to get JSON body if available
        if request:
            try:
                body = await request.json()
                question = body.get("question") or question
                context = body.get("context") or context
            except:
                # Not JSON body, ignore
                pass

        # Validate inputs
        if not question or not context:
            raise ValueError("Both 'question' and 'context' must be provided.")

        # Clean and process
        question = clean_text(question)
        context = clean_text(context)

        validate_inputs(question, context)
        result = answer_question(question, context)
        return format_response(result)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
