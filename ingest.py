#!/usr/bin/env python3
"""
ingest.py - Sentence-Aware Document Ingestion for Qdrant
"""

import os
from glob import glob
from ollama import Client as OllamaClient, ResponseError as OllamaResponseError
from pypdf import PdfReader
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaEmbeddings

BOOKS_DIR = "./books"
QDRANT_STORAGE_DIR = "./qdrant_storage"
COLLECTION_NAME = "gutenberg_books"
EMBEDDING_MODEL = "nomic-embed-text"

# Smaller chunk size with larger proportional overlap to preserve exact policy figures
CHUNK_SIZE = 400
CHUNK_OVERLAP = 120

SUPPORTED_EXTENSIONS = (".txt", ".pdf", ".md", ".markdown", ".json")


def ensure_ollama_model_available(model_name: str):
    client = OllamaClient()

    try:
        model_list = client.list()
    except OllamaResponseError as e:
        raise RuntimeError(
            f"Unable to query Ollama models ({e.status_code}). Is Ollama running?"
        ) from e

    installed = set()
    for m in getattr(model_list, "models", []):
        if isinstance(m, dict):
            model = m.get("model") or m.get("name")
        else:
            model = getattr(m, "model", None) or getattr(m, "name", None)
        if not model:
            continue
        installed.add(model)
        installed.add(model.split(":", 1)[0])

    if model_name in installed or model_name.split(":", 1)[0] in installed:
        return

    print(f"[Ingest] Ollama model '{model_name}' is missing. Pulling now...")
    try:
        client.pull(model_name, stream=False)
    except OllamaResponseError as e:
        raise RuntimeError(
            f"Failed to pull Ollama model '{model_name}' ({e.status_code}): {e.error}"
        ) from e

    print(f"[Ingest] Pulled Ollama model: {model_name}")


def load_documents():
    documents = []
    if not os.path.exists(BOOKS_DIR):
        os.makedirs(BOOKS_DIR)
        print(f"[Ingest] Created missing directory: {BOOKS_DIR}.")
        return documents

    for filepath in glob(os.path.join(BOOKS_DIR, "**"), recursive=True):
        if filepath.endswith(SUPPORTED_EXTENSIONS):
            try:
                if filepath.endswith(".pdf"):
                    reader = PdfReader(filepath)
                    loaded_docs = []
                    for page_index, page in enumerate(reader.pages, start=1):
                        page_text = page.extract_text() or ""
                        loaded_docs.append(
                            Document(
                                page_content=page_text,
                                metadata={"source": filepath, "page": page_index},
                            )
                        )
                else:
                    with open(filepath, "r", encoding="utf-8") as f:
                        loaded_docs = [
                            Document(
                                page_content=f.read(),
                                metadata={"source": filepath},
                            )
                        ]
                documents.extend(loaded_docs)
                print(f"[Ingest] Loaded: {filepath} ({len(loaded_docs)} pages/docs)")
            except Exception as e:
                print(f"[Ingest] Error loading {filepath}: {e}")

    return documents


def run_ingestion():
    print("=" * 80)
    print(" Starting High-Precision Qdrant Ingestion Pipeline")
    print("=" * 80)

    docs = load_documents()
    if not docs:
        print("[Ingest] No documents found to ingest. Exiting.")
        return

    # Preserves sentence boundaries across chunk cuts
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", "; ", ", ", " "],
        add_start_index=True
    )
    chunks = text_splitter.split_documents(docs)
    print(f"\n[Ingest] Split {len(docs)} document(s) into {len(chunks)} chunks.")

    ensure_ollama_model_available(EMBEDDING_MODEL)
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    vector_size = len(embeddings.embed_query("dimension_probe"))

    client = QdrantClient(path=QDRANT_STORAGE_DIR)

    if client.collection_exists(COLLECTION_NAME):
        client.delete_collection(COLLECTION_NAME)
        print(f"[Ingest] Re-created clean collection: '{COLLECTION_NAME}'")

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
    )

    vector_store = QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
        embedding=embeddings,
    )
    vector_store.add_documents(documents=chunks)

    print(f"\n[Ingest] Indexed {len(chunks)} chunks into Qdrant at '{QDRANT_STORAGE_DIR}'.")
    print("=" * 80)


if __name__ == "__main__":
    run_ingestion()