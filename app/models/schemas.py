from pydantic import BaseModel, Field

class SentimentRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=1000, description="The text to be analyzed")

class SentimentResponse(BaseModel):
    text: str
    sentiment: str = Field(..., description="Classification: Positive, Negative or Neutral")
    polarity: float = Field(..., description="Score from -1.0 (negative) to 1.0 (positive)")
