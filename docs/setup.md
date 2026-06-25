# Setup Guide — Automate Product Listing Optimization For E Commer

## Prerequisites

- Python 3.11+
- Docker (optional)
- Git

## Installation

```bash
git clone https://github.com/phanindraintelligenzit-afk/automate-product-listing-optimization-for-e-commer.git
cd automate-product-listing-optimization-for-e-commer
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Run Tests

```bash
pytest tests/ -v
```

## Run Locally

```bash
uvicorn src.pipeline:app --reload
```

## Deploy with Docker

```bash
docker build -t automate-product-listing-optimization-for-e-commer .
docker run -p 8000:8000 automate-product-listing-optimization-for-e-commer
```
