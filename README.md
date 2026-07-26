# 📄 Agentic PDF Research Assistant

An intelligent **Agentic RAG (Retrieval-Augmented Generation)** application that enables users to chat with PDF documents using Google's Gemini models, LangGraph workflows, and Qdrant vector search.

The assistant goes beyond traditional RAG by incorporating **query rewriting, reflection, conversation memory, and iterative retrieval**, resulting in more accurate and context-aware responses.

---

## 🌐 Live Demo

https://chat-ragbot.streamlit.app/

## 🚀 Features

- 📑 PDF document ingestion
- ✂️ Intelligent document chunking
- 🔎 Semantic retrieval using Qdrant
- 🤖 Google Gemini powered responses
- 🧠 Conversation memory with automatic summarization
- 🔄 Query rewriting for improved retrieval
- 🎯 Reflection node for retrieval quality improvement
- ⚡ LangGraph-based agentic workflow
- 💬 Streamlit chat interface
- 🐳 Docker & Docker Compose support
- ☁️ Deployable to Streamlit Community Cloud

---

# 🏗️ Architecture

```text
        ┌────────────────────┐
        │     User Query     │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────────┐
        │   Rewrite Query Node   │
        └─────────┬──────────────┘
                  │
                  ▼
        ┌────────────────────────┐
        │    Retrieve Chunks     │
        │       (Qdrant)         │
        └─────────┬──────────────┘
                  │
                  ▼
        ┌────────────────────────┐
        │   Generate Response    │
        │      (Gemini)          │
        └─────────┬──────────────┘
                  │
                  ▼
        ┌────────────────────────┐
        │    Reflection Node     │
        └───────┬─────────┬──────┘
                │         │
    Needs Retry │         │ Good Answer
                │         │
                ▼         ▼
    Rewrite Query     Update Memory
        ▲                 │
        │                 ▼
        └──────────► Conversation
                    Summary Update
                            │
                            ▼
                    Return Response
```

---

# 📁 Project Structure

```
pdf-research-assistant/
│
├── agentic_rag/
│   ├── assistant.py
│   ├── graph.py
│   ├── nodes.py
│   ├── prompts.py
│   └── state.py
│
├── ingestion/
│   ├── loader.py
│   ├── pipeline.py
│   └── splitter.py
│
├── retrieval/
│   ├── qdrant_store.py
│   └── retriever.py
│
├── services/
│   ├── embeddings.py
│   ├── llm.py
│   └── qdrant.py
│
├── utils/
│   └── logger.py
│
├── tests/
│
├── app.py
├── config.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# 🧠 Agent Workflow

The application is built using **LangGraph**, where every user query flows through multiple intelligent nodes.

## 1. Query Rewrite

The user's question is rewritten to improve semantic retrieval.

Example

> "What did he do?"

becomes

> "What did Alan Turing contribute to computer science?"

---

## 2. Document Retrieval

The rewritten query is embedded and relevant chunks are retrieved from Qdrant.

---

## 3. Answer Generation

Gemini receives

- Current question
- Conversation summary
- Recent chat history
- Retrieved documents

to generate an accurate answer.

---

## 4. Reflection

The LLM evaluates whether the retrieved documents were sufficient.

If not,

- query is rewritten again
- retrieval is retried

This creates an iterative retrieval loop.

---

## 5. Conversation Memory

The assistant stores

- recent conversation
- summarized long-term memory

allowing multi-turn conversations without exceeding context limits.

---

# ⚙️ Tech Stack
* **LLM:** Google Gemini
* **Framework:** LangGraph
* **Orchestration:** LangChain
* **Vector Database:** Qdrant
* **Embeddings:** `BAAI/bge-small-en-v1.5`
* **UI:** Streamlit
* **PDF Parsing:** PyMuPDF
* **Container:** Docker
* **Cloud:** Streamlit Community Cloud, Qdrant Cloud

---

# 📥 Installation

Clone the repository

```bash
git clone https://github.com/khanforge/pdf-research-assistant.git

cd pdf-research-assistant
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

macOS/Linux

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```bash
cp .env.example .env
```

---

# 📚 Ingest Documents

```python
from ingestion.pipeline import IngestionPipeline

pipeline = IngestionPipeline()

pipeline.ingest("research.pdf")
```

The pipeline performs

- Load PDF
- Split into chunks
- Generate embeddings
- Store vectors inside Qdrant

---

# 💬 Run the Application

```bash
streamlit run app.py
```

Open

```
http://localhost:8501
```

---

# 🐳 Docker

Build

```bash
docker build -t rag-assistant .
```

Run

```bash
docker run \
-p 8501:8501 \
--env-file .env \
rag-assistant
```

---

# 🐳 Docker Compose

```bash
docker compose up --build
```

---

# ☁️ Deployment

The application can be deployed using

- Streamlit Community Cloud
- Qdrant Cloud
- Google Gemini API

Deployment architecture

```text
GitHub
   │
   ▼
Streamlit Cloud
   │
   ├── Gemini API
   │
   └── Qdrant Cloud
```

---

# 📈 Future Improvements

- Hybrid Search (Dense + BM25)
- Cross-Encoder Reranking
- Multi-PDF collections
- Metadata filtering
- OCR support
- Citation highlighting
- Streaming responses
- Authentication
- Feedback collection
- Local LLM support (Ollama/vLLM)
- Multi-agent research workflows

---

# 🧪 Testing

Run

```bash
python -m tests.test_ingestion
python -m tests.test_graph
```

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Parvej Khan**

Software Development Engineer | AI Engineer

GitHub: https://github.com/khanforge

LinkedIn: https://linkedin.com/in/khan-parvej-pk

---

## ⭐ If you found this project useful, consider giving it a star!