from transformers import pipeline

summarizer = pipeline("summarization", model="csebuetnlp/mT5_multilingual_XLSum")


