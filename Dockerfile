# Stage 1: base
FROM python:3.11-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# system deps for matplotlib (minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libfreetype6-dev \
    libpng-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . /app

# Use gunicorn in production; default command runs gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "run:app"]