# Shock Propagation Model

An AI-powered event shock simulation system that models how major real-world events propagate across interconnected economic sectors over time.

## Overview

Shock Propagation Model is a research-oriented AI simulation platform designed to analyze how global events such as financial crises, wars, oil supply disruptions, and economic recessions impact interconnected industries.

The system uses Natural Language Processing (NLP) and graph-based propagation modeling to simulate cascading economic effects across sectors.

The project consists of:
- An iOS frontend built using SwiftUI
- A Python backend built using FastAPI
- AI-powered semantic event analysis using Sentence Transformers

---

# Features

- AI-based event understanding using NLP embeddings
- Semantic similarity analysis using Sentence Transformers
- Sector-wise shock propagation simulation
- Weighted economic dependency graph
- Temporal decay modeling
- FastAPI backend API
- SwiftUI-based iOS application
- Real-time event simulation workflow

---

# Architecture

```text
User Input (iOS App)
        ↓
SwiftUI Frontend
        ↓
FastAPI Backend
        ↓
Sentence Transformer Embeddings
        ↓
Cosine Similarity Engine
        ↓
Shock Propagation Model
        ↓
Sector Impact Timeline
Tech Stack
Component	Technology
Frontend	SwiftUI
Backend	FastAPI
Language	Python, Swift
AI/NLP	Sentence Transformers
ML Libraries	NumPy, Scikit-learn
API Framework	FastAPI
Mobile Platform	iOS
AI & Simulation Concepts Used
NLP Semantic Analysis
The project uses Sentence Transformers to convert events into vector embeddings and compare them against predefined macroeconomic shock events.
Example:
Global recession
Banking crisis
War outbreak
Oil supply disruption
Semantic similarity is calculated using cosine similarity.
Shock Propagation Engine
Economic sectors are represented as interconnected nodes in a weighted graph.
Example propagation flow:
Banking → Stock Market → Manufacturing → Consumer
Each connection contains a propagation weight representing how strongly one sector affects another.
Temporal Decay Modeling
The simulation includes a decay mechanism that gradually reduces the impact intensity over time.
This helps model realistic economic shock weakening across multiple days.
API Endpoints
Health Check
GET /
Response:
{
  "message": "AI Event Shock Propagation Backend is running"
}
Run Simulation
POST /simulate
Example Request:
{
  "event_text": "major oil crisis in Asia"
}
Example Response:
{
  "event": "major oil crisis in Asia",
  "initial_shock": 0.82,
  "timeline": [
    {
      "day": 1,
      "impact": {
        "Banking": 0.82
      }
    }
  ]
}
Project Structure
Shock Propagation Model/
│
├── README.md
├── .gitignore
│
├── EventShockPropagation/     # SwiftUI iOS App
│
├── backend/                   # FastAPI Backend
│   ├── main.py
│   └── requirements.txt
Installation & Setup
Backend Setup
1. Navigate to backend folder
cd backend
2. Install dependencies
pip install fastapi uvicorn sentence-transformers numpy scikit-learn
3. Run FastAPI server
uvicorn main:app --reload
Backend will run on:
http://127.0.0.1:8000
Frontend Setup
Open the Xcode project
Run the application on iOS Simulator or physical device
Ensure the FastAPI backend server is running
Future Improvements
Dynamic economic graph generation
Real-time financial data integration
Interactive propagation visualizations
Heatmaps and analytics dashboard
Multi-event simulation support
Database integration
Cloud deployment
Use Cases
Economic impact analysis
AI-based simulation research
Educational demonstrations
Financial shock modeling
Crisis propagation analysis
Academic AI projects
Author
Ronit Mia
BTech Computer Science Engineering
License
This project is intended for educational and research purposes.
