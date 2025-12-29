def clean_text(text: str) -> str:
    return text.strip()

def validate_inputs(question: str, context:str):
    if not question or not context:
        raise ValueError("Question and context must not be empty")
    
    if len(context) > 5000:
        raise ValueError("Context too long")
    
def format_response(answer_data: dict) -> dict:
    return {
        "answer": answer_data["answer"]
    }