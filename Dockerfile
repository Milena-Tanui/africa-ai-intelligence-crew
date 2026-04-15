FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml pyproject.toml
COPY src src
COPY knowledge knowledge

# Install UV and dependencies
RUN pip install --no-cache-dir uv && \
    uv pip install --system -e .

# Create .env file from environment variables at runtime
COPY .env .env.example

# Run the crew
CMD ["python", "-m", "ai_news_across_africa.main"]
