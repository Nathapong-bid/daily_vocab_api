import requests
from schemas import ValidateResponse

N8N_WEBHOOK = "http://localhost:5678/webhook/worddee-ai"

def send_to_n8n(sentence: str, word: str) -> ValidateResponse:
    payload = {
        "word": word,
        "sentence": sentence
    }

    try:
        res = requests.post(N8N_WEBHOOK, json=payload)
        data = res.json()

        return ValidateResponse(
            score=data.get("score", 0),
            level=data.get("level", "Unknown"),
            suggestion=data.get("suggestion", ""),
            corrected_sentence=data.get("corrected_sentence", "")
        )
    except:
        return ValidateResponse(
            score=0,
            level="Error",
            suggestion="Cannot connect to n8n",
            corrected_sentence=sentence
        )