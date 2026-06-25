"""Pipeline for Automate Product Listing Optimization For E Commer."""
from fastapi import FastAPI
from src.agents.product_analyzer import product_analyzer
from src.agents.content_optimizer import content_optimizer
from src.agents.pricing_agent import pricing_agent
from src.agents.review_manager import review_manager

app = FastAPI(title="Automate Product Listing Optimization For E Commer")

@app.post("/run")
def run_pipeline(input_data: dict):
    """Run the full agent pipeline."""
    result = input_data
    result = product_analyzer(result)  # Analyze product listings, pricing, reviews, competitive positioning
    result = content_optimizer(result)  # Generate SEO-optimized titles, descriptions, tags
    result = pricing_agent(result)  # Monitor competitor pricing, recommend dynamic pricing adjustments
    result = review_manager(result)  # Aggregate reviews, generate response templates, flag urgent issues
    return {"status": "complete", "result": result}

@app.get("/health")
def health():
    return {"status": "ok"}
