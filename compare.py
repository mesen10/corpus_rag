#!/usr/bin/env python3
"""
compare_v1.py - High-Precision Retrieval Evaluation Pipeline
"""

import json
import re
import os

from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

LLM_MODEL = "llama3.2"
EMBEDDING_MODEL = "nomic-embed-text"
QDRANT_STORAGE_DIR = "./qdrant_storage"
COLLECTION_NAME = "gutenberg_books"

TEST_DATASET = [
    {"id": 1,
     "question": "What is the basic annual leave entitlement (excluding bank holidays) for an employee with less than 5 years of service?",
     "expected": "23 days per annum."},
    {"id": 2,
     "question": "After how many years of continuous service does the basic annual leave entitlement increase to 28 days?",
     "expected": "5 years of service."},
    {"id": 3, "question": "How many statutory and public bank holidays are normally observed per year?",
     "expected": "8 public and bank holidays per year."},
    {"id": 4,
     "question": "How many days of untaken annual leave can employees carry over into the next leave year with prior written consent?",
     "expected": "Up to a maximum of 5 days."},
    {"id": 5,
     "question": "What threshold duration in calendar days distinguishes short-term sickness absence from long-term sickness absence?",
     "expected": "Short-term is up to 27 days; long-term is 28 calendar days or more."},
    {"id": 6,
     "question": "Within how many calendar days of sickness can an employee self-certify before a doctor's fit note is required?",
     "expected": "Seven calendar days or less."},
    {"id": 7,
     "question": "What is the deadline and method for an employee to report their absence on the first day of sickness?",
     "expected": "Notify line manager by telephone before start time and no later than 1 hour after starting time."},
    {"id": 8, "question": "When does sickness starting mid-shift count as a full day of sickness absence?",
     "expected": "When the employee leaves work before completing 50% of their working day."},
    {"id": 9,
     "question": "How many weeks of total maternity leave is an employee entitled to take, and how is it split?",
     "expected": "52 weeks total (26 weeks Ordinary Maternity Leave and 26 weeks Additional Maternity Leave)."},
    {"id": 10, "question": "What is the mandatory compulsory period of maternity leave following childbirth?",
     "expected": "A two-week compulsory maternity leave period immediately following the birth."},
    {"id": 11,
     "question": "How many 'Keeping in Touch' (KIT) days can an employee attend with full pay during maternity leave?",
     "expected": "Up to 10 KIT days."},
    {"id": 12,
     "question": "How many days of paid Maternity/Adoption Support Leave are granted to a partner or nominated carer?",
     "expected": "5 days of paid leave."},
    {"id": 13,
     "question": "How much written notice in advance must an employee give to request a period of unpaid Parental Leave?",
     "expected": "At least 21 days' notice in writing."},
    {"id": 14,
     "question": "What is the maximum number of weeks of unpaid Parental Leave an employee can take per year per child?",
     "expected": "Up to 4 weeks per year per child."},
    {"id": 15,
     "question": "How many elected members sit on Chichester City Council, and how many wards do they represent?",
     "expected": "18 elected members representing 5 wards."},
    {"id": 16, "question": "How many times a year does the Full Council meet?", "expected": "5 times a year."},
    {"id": 17,
     "question": "At what spinal column point (SCP) threshold are employees restricted from engaging in political activities?",
     "expected": "Spinal column point (SCP) 46 or above."},
    {"id": 18,
     "question": "Within how many days must an employee lodge an appeal against a formal sickness warning or dismissal?",
     "expected": "Within 5 days of receiving written confirmation."},
    {"id": 19, "question": "What is the maximum length of a councillor's term of office before re-election?",
     "expected": "A maximum of 4 years."},
    {"id": 20, "question": "Under what circumstance is alcohol allowed on Council premises during working hours?",
     "expected": "When specifically approved by the Town Clerk."}
]


def get_optimized_retriever():
    if not os.path.exists(QDRANT_STORAGE_DIR):
        raise FileNotFoundError(f"Qdrant directory '{QDRANT_STORAGE_DIR}' not found.")

    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    client = QdrantClient(path=QDRANT_STORAGE_DIR)

    vector_store = QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
        embedding=embeddings,
    )

    # Increased fetch window and tuned lambda for higher density match
    return vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 6,
            "fetch_k": 15,
            "lambda_mult": 0.65
        }
    )


def format_docs(docs):
    formatted = []
    for idx, doc in enumerate(docs, 1):
        formatted.append(f"--- CONTEXT CHUNK {idx} ---\n{doc.page_content.strip()}")
    return "\n\n".join(formatted)


def build_rag_chain(retriever, llm):
    # Enhanced extraction instructions tailored for llama3.2
    prompt_template = ChatPromptTemplate.from_template(
        "SYSTEM: You are a strict factual extraction agent. Your job is to answer the QUESTION "
        "using ONLY the facts contained in the PROVIDED CONTEXT.\n\n"
        "RULES:\n"
        "1. Direct numerical facts, dates, time limits, and specific conditions must be extracted exactly as stated.\n"
        "2. Do not assume or extrapolate beyond the provided text.\n"
        "3. Keep your response brief, precise, and limited to 1-2 sentences.\n\n"
        "PROVIDED CONTEXT:\n{context}\n\n"
        "QUESTION: {question}\n\n"
        "EXACT ANSWER:"
    )

    return (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt_template
            | llm
            | StrOutputParser()
    )


def evaluate_answers(judge_llm, question: str, expected: str, norag_ans: str, rag_ans: str) -> tuple[int, int, str]:
    eval_prompt = ChatPromptTemplate.from_template(
        "You are an objective evaluator grading model responses against a Ground Truth Expected Answer.\n\n"
        "Question: {question}\n"
        "Expected Answer: {expected}\n\n"
        "Model 1 (No-RAG) Answer: {norag_ans}\n"
        "Model 2 (RAG) Answer: {rag_ans}\n\n"
        "Grade each answer from 0 to 5 points based on factual accuracy against the Expected Answer:\n"
        "- 5: Factually complete and accurate (contains exact key numbers/metrics).\n"
        "- 3-4: Mostly correct, missing minor details.\n"
        "- 1-2: Partially correct.\n"
        "- 0: Incorrect, incomplete, or hallucination.\n\n"
        "Return ONLY a JSON object matching this schema:\n"
        '{{"norag_score": <int 0-5>, "rag_score": <int 0-5>, "reasoning": "<1-sentence explanation>"}}'
    )

    chain = eval_prompt | judge_llm | StrOutputParser()
    response_text = chain.invoke({
        "question": question,
        "expected": expected,
        "norag_ans": norag_ans,
        "rag_ans": rag_ans
    })

    try:
        json_match = re.search(r"\{.*\}", response_text, re.DOTALL)
        if json_match:
            data = json.loads(json_match.group())
            return int(data.get("norag_score", 0)), int(data.get("rag_score", 0)), data.get("reasoning", "")
    except Exception:
        pass

    return 0, 0, "Evaluation parsing failed."


def run_evaluation():
    print("=" * 80)
    print(" Querying High-Precision Qdrant RAG Pipeline")
    print(f" Database Path : {QDRANT_STORAGE_DIR}")
    print(f" Search Strategy: MMR (k=6, fetch_k=15, lambda=0.65)")
    print("=" * 80 + "\n")

    llm = ChatOllama(model=LLM_MODEL, temperature=0.0)
    retriever = get_optimized_retriever()
    rag_chain = build_rag_chain(retriever, llm)

    norag_total_pts = 0
    rag_total_pts = 0
    max_possible_pts = len(TEST_DATASET) * 5

    for item in TEST_DATASET:
        qid = item["id"]
        q_text = item["question"]
        expected = item["expected"]

        norag_ans = llm.invoke(f"Answer concisely in 1-2 sentences:\nQuestion: {q_text}\nAnswer:").content.strip()
        rag_ans = rag_chain.invoke(q_text).strip()

        norag_pts, rag_pts, reasoning = evaluate_answers(llm, q_text, expected, norag_ans, rag_ans)

        norag_total_pts += norag_pts
        rag_total_pts += rag_pts

        print(f"Question [{qid}/{len(TEST_DATASET)}]: {q_text}")
        print(f"  • Expected Answer : {expected}")
        print(f"  • No-RAG Answer   : {norag_ans} ({norag_pts}/5 pts)")
        print(f"  • RAG Answer      : {rag_ans} ({rag_pts}/5 pts)")
        print(f"  • Judge Reason    : {reasoning}")
        print("-" * 80)

    print("\n" + "=" * 80)
    print(" OPTIMIZED RAG SCOREBOARD")
    print("=" * 80)
    print(f" Model Tested         : {LLM_MODEL}")
    print(f" Total Questions      : {len(TEST_DATASET)}")
    print(f" Max Score Possible   : {max_possible_pts} pts")
    print(
        f" No-RAG Total Score   : {norag_total_pts} / {max_possible_pts} pts ({(norag_total_pts / max_possible_pts) * 100:.1f}%)")
    print(
        f" RAG Total Score      : {rag_total_pts} / {max_possible_pts} pts ({(rag_total_pts / max_possible_pts) * 100:.1f}%)")
    print(f" Net Gain             : +{rag_total_pts - norag_total_pts} points")
    print("=" * 80)


if __name__ == "__main__":
    run_evaluation()