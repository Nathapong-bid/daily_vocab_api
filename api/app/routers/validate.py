from fastapi import APIRouter
from pydantic import BaseModel
import httpx

router = APIRouter()

class SentenceRequest(BaseModel):
    sentence: str
    word: str

@router.post("/validate-sentence")
async def validate_sentence(data: SentenceRequest):
    # ส่งเข้า n8n ที่ set ไว้
    N8N_URL = "https://your-n8n-webhook-url"

    async with httpx.AsyncClient() as client:
        response = await client.post(N8N_URL, json=data.dict())

    return response.json()
