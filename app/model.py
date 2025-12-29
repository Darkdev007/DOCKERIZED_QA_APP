import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

model_checkpoint = "Darkdev007/bert-finetuned-squad"

model = AutoModelForQuestionAnswering.from_pretrained(model_checkpoint)
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model.eval()

def answer_question(question:str, context:str) -> dict:
    inputs = tokenizer(
        question,
        context,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    with torch.no_grad():
        outputs=model(**inputs)

    start= torch.argmax(outputs.start_logits)
    end= torch.argmax(outputs.end_logits) + 1

    answer = tokenizer.decode(inputs["input_ids"][0][start:end])
    return {"answer" : answer}