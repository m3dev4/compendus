from transformers import AutoTokenizer
from model import summarizer
from fastapi import HTTPException, status
from dotenv import load_dotenv
import os

load_dotenv()

GET_TOKEN = os.getenv("TOKEN_HUGGINFFACE")

tokenizer = AutoTokenizer.from_pretrained("csebuetnlp/mT5_multilingual_XLSum", token=GET_TOKEN)

MAX_INPUT_TOKEN = tokenizer.model_max_length


def summarize(text: str):
    tokens = tokenizer.encode(text)
    print(f"Le nombre token: {len(tokenizer.encode(text))}")
    if len(tokens) <= MAX_INPUT_TOKEN:

        result = summarizer(text, max_length=42, min_length=40, do_sample=False)

        return result[0]["summary_text"]

    else:
        if len(tokens) > MAX_INPUT_TOKEN:
            raise HTTPException(status_code=413, detail="Le texte est trop long")
