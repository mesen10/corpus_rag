# 📄 Open-Source Document RAG (Retrieval-Augmented Generation)

A lightweight, production-ready RAG application that lets you get answers from public handbooks and policy PDFs locally. This project avoids heavy API dependencies and massive LLMs by using **Qdrant Lite** (in-memory vector storage) and **Ollama** for both local embeddings and compact local LLMs.

---

## 🎯 Why Use Small Models for a RAG Demo?

When showcasing a RAG pipeline on GitHub, using small/basic models (like 2B–3B parameter models) is a deliberate architectural choice, not a compromise:

1. **Proving RAG Efficacy (No Parametric Memory Leakage):** Massive models often have memorized popular public text. Using smaller models plus unfamiliar policy documents makes it easier to prove the answer comes from retrieval, not the model's memory.
2. **Deterministic Adherence:** Smaller models are less prone to injecting outside assumptions and strictly follow prompt instructions to answer *only* from the provided context.
3. **Zero GPU/API Cost:** 2B–3B models run fast on standard laptop CPUs without requiring expensive Cloud APIs or dedicated GPUs, making the GitHub repository easily cloneable and runnable for anyone.

---

## 📚 Included Document

I tried to use ebooks from project Gutenberg, but they are often too well-known and memorized by LLMs. Instead, I downloaded random handbook PDF that is less likely to be in the model's training data.

I wish I could use
* The Odyssey by Homer
* Alice's Adventures in Wonderland by Lewis Carroll
* Romeo and Juliet by William Shakespeare
* Crime and Punishment by Fyodor Dostoevsky

My approach:
1. filetype:pdf "employee handbook" "carryover" "probationary period" city policy
Chichester City Council Staff Handbook
2. filetype:pdf "purchasing policy" "dollar threshold" "micro-purchase" authority
County of Humboldt Purchasing Policy
3. filetype:pdf "faculty handbook" "sabbatical leave" "office hours"
Sacred Heart University Faculty Handbook
---

## 🚀 Recommended Local Models

| Model | Size | Strengths for RAG & Documents | Ollama Command |
| :--- | :--- | :--- | :--- |
| **Llama 3.2 (3B)** | ~2.0 GB | **Best Overall:** Excellent context recall, high precision with extracted text excerpts. | `ollama run llama3.2:3b` |
| **Phi-3.5 Mini (3.8B)** | ~2.2 GB | **Fast & Balanced:** Low resource footprint with clean context adherence. | `ollama run phi3.5` |
| **Gemma 2 (2B)** | ~1.6 GB | **Ultra-Lightweight:** Runs on low-spec CPUs and older laptops effortlessly. | `ollama run gemma2:2b` |

---

➡️ See [sample-results.md](sample-results.md) for example outputs.
LLM as a judge!

## 💻 Pulling & Running Models with Ollama

### Terminal Commands

```bash
# Pull and test Llama 3.2 (3B)
# Local embedding model
ollama pull nomic-embed-text

# Local generator model
ollama pull llama3.2:3b
```

## Project Structure
```
├── books/                  # Downloaded source PDFs and extracted text files
├── download_books.py       # Automated public-document downloader script
├── ingest_v1.py         # Chunking & Ollama embeddings -> Qdrant
├── ingest_v2.py         # Chunking & Ollama embeddings -> Qdrant
├── query_rag.py            # RAG answer path (retrieval + local LLM)
├── query_no_rag.py         # Baseline answer path (local LLM only)
├── compare_v1.py              # Runs benchmark; calls query_rag.py + query_no_rag.py
├── compare_v2.py              # Runs benchmark; calls query_rag.py + query_no_rag.py
└── README.md
```

## Quickstart Guide
~~* Step 1: Download the source document~~
~~`python download_books.py`~~

* Step 1: Manually download the source documents and put them under the `books/` folder.
```

* Step 2: Ingest Documents into Qdrant
```
python ingest.py
``` 

* Step 3: Query the RAG Pipeline
```
python query_rag.py
```

* Step 4: Query without RAG baseline
```
python query_no_rag.py
```

* Step 5: Compare RAG vs No-RAG
```
python compare.py
```
