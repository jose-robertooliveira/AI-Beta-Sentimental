import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    """Test the welcome message at the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]

def test_analyze_sentiment_success():
    """Test a successful sentiment analysis request."""
    payload = {"text": "This is an amazing project!"}
    response = client.post("/api/analyze", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["text"] == payload["text"]
    assert data["sentiment"] == "Positive"
    assert data["polarity"] > 0

def test_analyze_sentiment_negative():
    """Test a negative sentiment analysis request."""
    payload = {"text": "I hate it when the code does not work."}
    response = client.post("/api/analyze", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["sentiment"] == "Negative"
    assert data["polarity"] < 0

def test_analyze_sentiment_invalid_input():
    """Test the API validation with empty text."""
    payload = {"text": ""} # Pydantic should catch this as min_length=1
    response = client.post("/api/analyze", json=payload)

    assert response.status_code == 422 # Unprocessable Entity
    assert "detail" in response.json()

def test_analyze_sentiment_missing_field():
    """Test the API validation with missing fields."""
    payload = {}
    response = client.post("/api/analyze", json=payload)

    assert response.status_code == 422
