from abc import ABC, abstractmethod
from textblob import TextBlob
from app.models.schemas import SentimentResponse
from loguru import logger

class BaseAnalyzer(ABC):
    """
    Base interface for sentiment analyzers.
    Allows switching the AI implementation (e.g., from TextBlob to OpenAI)
    without altering the rest of the application.
    """
    @abstractmethod
    def analyze(self, text: str) -> SentimentResponse:
        pass

class TextBlobAnalyzer(BaseAnalyzer):
    """
    Sentiment analysis implementation using the TextBlob library.
    Ideal for prototypes and basic sentiment analysis.
    """
    def analyze(self, text: str) -> SentimentResponse:
        logger.info(f"Analyzing text: {text[:50]}...")

        # TextBlob analyzes polarity: -1.0 (negative) to 1.0 (positive)
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        # Classification based on thresholds
        if polarity > 0.1:
            sentiment = "Positive"
        elif polarity < -0.1:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        logger.debug(f"Analysis result: {sentiment} (polarity: {polarity})")
        return SentimentResponse(
            text=text,
            sentiment=sentiment,
            polarity=polarity
        )

def get_analyzer() -> BaseAnalyzer:
    """
    Factory function to return the analyzer instance.
    If we decide to change the AI in the future, we only update this function.
    """
    return TextBlobAnalyzer()
