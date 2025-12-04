from fastapi import APIRouter
from schemas import SummaryResponse
from service_sum import get_summary

router = APIRouter()

@router.get("/summary", response_model=SummaryResponse)
def summary():
    return get_summary()