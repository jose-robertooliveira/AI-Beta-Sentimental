# Use the same Python version as the host machine
FROM python:3.14-slim

# Prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install uv for fast dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy pyproject.toml and uv.lock
COPY pyproject.toml uv.lock ./

# Install dependencies only (without trying to build the project as a package)
RUN uv pip install --system -r pyproject.toml

# Copy the application code
COPY app ./app

# Expose the FastAPI port
EXPOSE 8000

# Start the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
