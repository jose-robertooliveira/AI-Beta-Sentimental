from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI(
    title="AI Sentiment Analyzer",
    description="A professional AI-powered API for sentiment analysis of customer feedback",
    version="1.0.0"
)

# Include the routes from the api module
app.include_router(api_router, prefix="/api", tags=["Sentiment Analysis"])

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Sentiment Analyzer API. Visit /docs for documentation."}
