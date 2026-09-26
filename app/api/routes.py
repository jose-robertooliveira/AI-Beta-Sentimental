from fastapi import APIRouter, HTTPException
from app.models.schemas import SentimentRequest, SentimentResponse
from app.core.analyzer import get_analyzer
from loguru import logger

router = APIRouter()
analyzer = get_analyzer()

@router.post("/analyze", response_model=SentimentResponse)
async def analyze_sentiment(request: SentimentRequest):
    """
    Analyzes the sentiment of the provided text.
    Returns the sentiment label (Positive, Negative, Neutral) and the polarity score.
    """
    logger.info(f"Received analysis request for text: {request.text[:50]}...")
    try:
        result = analyzer.analyze(request.text)
        return result
    except Exception as e:
        logger.exception("An unexpected error occurred during sentiment analysis")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
