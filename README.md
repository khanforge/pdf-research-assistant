# Agentic RAG

A starter retrieval-augmented generation application with PDF ingestion and agentic workflows.

## Setup

1. Copy `.env.example` to `.env`
2. Install dependencies: `pip install -r requirements.txt`
3. Run locally: `streamlit run app.py`

## Project structure

- `app.py` — Streamlit entry point
- `config.py` — Central configuration
- `agent/` — Agent orchestration logic
- `ingestion/` — Document loader, splitter, embedder, and pipeline
- `retrieval/` — Vector store and retriever logic
- `utils/` — Shared helpers and logging
- `data/uploads/` — Uploaded documents
