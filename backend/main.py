from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI(title="AI Event Shock Propagation Model")

# Load ML model once
model = SentenceTransformer("all-MiniLM-L6-v2")

# Reference shock events
REFERENCE_EVENTS = [
    "global recession",
    "bank collapse",
    "war outbreak",
    "oil supply disruption",
    "interest rate hike"
]
REFERENCE_EMBEDDINGS = model.encode(REFERENCE_EVENTS)

class EventRequest(BaseModel):
    event_text: str

@app.get("/")
def home():
    return {"message": "AI Event Shock Propagation Backend is running"}

SECTORS = {
    "Banking": {"Stock Market": 0.8, "Consumer": 0.6},
    "Stock Market": {"Manufacturing": 0.7, "Consumer": 0.5},
    "Energy": {"Manufacturing": 0.9},
    "Manufacturing": {"Consumer": 0.6},
    "Consumer": {}
}

@app.post("/simulate")
def simulate_event(event: EventRequest):
    event_embedding = model.encode([event.event_text])
    similarities = cosine_similarity(event_embedding, REFERENCE_EMBEDDINGS)
    base_shock = float(np.max(similarities))

    decay = 0.85
    days = 7

    daily_impact = []

    current_impacts = {
        "Banking": base_shock
    }

    for day in range(1, days + 1):
        day_result = {}

        for sector, value in current_impacts.items():
            day_result[sector] = round(value, 3)

        daily_impact.append({
            "day": day,
            "impact": day_result
        })

        next_impacts = {}

        for sector, value in current_impacts.items():
            for target, weight in SECTORS.get(sector, {}).items():
                propagated = value * weight * decay
                next_impacts[target] = next_impacts.get(target, 0) + propagated

        current_impacts = next_impacts

    return {
        "event": event.event_text,
        "initial_shock": round(base_shock, 3),
        "timeline": daily_impact
    }
