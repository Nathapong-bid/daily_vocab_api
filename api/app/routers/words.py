from fastapi import APIRouter
import random

router = APIRouter()

WORDS = ["play", "hard", "get", "edit", "add", "scam"]

@router.get("/word")
async def get_random_word():
    return {
        "word": random.choice(WORDS)
    }