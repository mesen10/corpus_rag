#!/usr/bin/env python3
"""
ingest.py - Sentence-Aware Document Ingestion for Qdrant
"""

import os
from glob import glob
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaEmbeddings

BOOKS_DIR = "./books"
QDRANT_STORAGE_DIR = "./qdrant_storage"
COLLECTION_NAME = "gutenberg_books"
EMBEDDING_MODEL = "nomic-embed-text"
VECTOR_SIZE = 768

# Smaller chunk size with larger proportional overlap to preserve exact policy figures
CHUNK_SIZE = 400
CHUNK_OVERLAP = 120

SUPPORTED_EXTENSIONS = (".txt", ".pdf", ".md", ".markdown", ".json")


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
                    loader = PyPDFLoader(filepath)
                else:
                    loader = TextLoader(filepath, encoding="utf-8")

                loaded_docs = loader.load()
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

    client = QdrantClient(path=QDRANT_STORAGE_DIR)

    if client.collection_exists(COLLECTION_NAME):
        client.delete_collection(COLLECTION_NAME)
        print(f"[Ingest] Re-created clean collection: '{COLLECTION_NAME}'")

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE),
    )

    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)

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