# AI Sentiment Analyzer
A professional-grade AI Sentiment Analysis API built with Python, FastAPI, and TextBlob.

## 🚀 Overview
This project demonstrates the application of AI Engineering best practices to build a scalable and maintainable sentiment analysis system. It analyzes customer feedback and classifies it into Positive, Negative, or Neutral sentiments.

## 🛠️ Tech Stack
- **Language:** Python 3.12+
- **AI Engine:** TextBlob (NLP)
- **Framework:** FastAPI
- **Data Validation:** Pydantic
- **Environment Management:** `uv`
- **Observability:** Loguru
- **Containerization:** Docker & Docker Compose
- **Testing:** Pytest

## 🏗️ Architecture
The project follows a layered architecture to ensure separation of concerns:
- **`app/api`**: Handles HTTP requests, input validation, and responses.
- **`app/core`**: Contains the AI business logic and the analyzer interface.
- **`app/models`**: Defines the data contracts (Schemas) for the entire application.
- **`tests/`**: Comprehensive unit and integration tests.

### AI Design Pattern
We implemented the **Strategy Pattern** via the `BaseAnalyzer` abstract class. This allows the AI engine to be swapped (e.g., from TextBlob to a LLM like GPT-4) by simply creating a new implementation of the analyzer without changing any other part of the system.

## 🚦 Getting Started

### Local Development
1. Install `uv`: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Clone the repo and enter the directory.
3. Install dependencies: `uv sync`
4. Run the server: `uv run uvicorn app.main:app --reload`
5. Access the interactive docs at: `http://127.0.0.1:8000/docs`

### Deployment with Docker
1. Ensure Docker and Docker Compose are installed.
2. Run: `docker-compose up --build`
3. The API will be available at `http://localhost:8000`

## 🧪 Testing
Run the test suite using:
```bash
PYTHONPATH=. uv run pytest
```

## 📜 API Endpoints
### `POST /api/analyze`
**Request Body:**
```json
{
  "text": "The product quality is amazing!"
}
```
**Response Body:**
```json
{
  "text": "The product quality is amazing!",
  "sentiment": "Positive",
  "polarity": 0.6
}
```
