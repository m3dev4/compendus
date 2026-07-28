from transformers import AutoTokenizer
from model import summarizer
from fastapi import HTTPException, status
from dotenv import load_dotenv
import os

load_dotenv()

GET_TOKEN = os.getenv("TOKEN_HUGGINFFACE")

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn", token=GET_TOKEN)

MAX_INPUT_TOKEN = tokenizer.model_max_length


def summarize(text: str):
    tokens = tokenizer.encode(text)
    if len(tokens) <= MAX_INPUT_TOKEN:

        result = summarizer(text, max_length=140, min_length=20, do_sample=False)

        return result[0]["summary_text"]

    else:
        if len(tokens) > MAX_INPUT_TOKEN:
            raise HTTPException(status_code=413, detail="Le texte est trop long")
