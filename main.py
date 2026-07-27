from fastapi import FastAPI
from schema import SummarizeRequest, SummarizeResponse
from service import summarize

app = FastAPI()


@app.post("/summarize", response_model=SummarizeResponse)
def summarize_text(request: SummarizeRequest):
    summary = summarize(request.text)
    print(len(summary))
    return {"summary": summary}


# {"summury": "Je suis Mamour"}
