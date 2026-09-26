import pytest
from app.core.analyzer import get_analyzer

def test_positive_sentiment():
    analyzer = get_analyzer()
    result = analyzer.analyze("I love this AI Engineering course, it is wonderful!")
    assert result.sentiment == "Positive"
    assert result.polarity > 0

def test_negative_sentiment():
    analyzer = get_analyzer()
    result = analyzer.analyze("This system is horrible and doesn't work at all.")
    assert result.sentiment == "Negative"
    assert result.polarity < 0

def test_neutral_sentiment():
    analyzer = get_analyzer()
    result = analyzer.analyze("The sky is blue today.")
    assert result.sentiment == "Neutral"
    assert -0.1 <= result.polarity <= 0.1
