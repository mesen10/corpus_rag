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
| **Ornith-1.5 (9B)** | ~5.4 GB | **High Quality:** Larger model, still CPU-runnable, strong on nuanced policy language. | `ollama pull ornith-1.5:9b` |
| **Granite 4.2 (3B)** | ~2.1 GB | **Enterprise-Tuned:** IBM Granite line, tuned for grounded document QA and low hallucination. | `ollama pull granite4.2:3b` |

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
├── ingest.py               # Chunking & Ollama embeddings -> Qdrant
├── compare.py              # Runs benchmark; calls RAG and no RAG
└── README.md
```

## Quickstart Guide
~~* Step 1: Download the source document~~
~~`python download_books.py`~~

* Step 1: Manually download the source documents and put them under the `books/` folder.
* Step 2: Ingest Documents into Qdrant
```
python ingest.py
```

* Step 3: Compare RAG vs No-RAG
```
python compare.py
```

## Sample Results Llama 3.2 (3B)

```
================================================================================
 Querying High-Precision Qdrant RAG Pipeline
 Database Path : ./qdrant_storage
 Search Strategy: MMR (k=6, fetch_k=15, lambda=0.65)
================================================================================

Question [1/20]: How many elected members make up Chichester City Council, and how many times per year does the Full Council meet?
  • Expected Answer : 18 elected members; 5 times per year.
  • No-RAG Answer   : Chichester City Council has 31 elected members. The Full Council typically meets 4 times per year. (0/5 pts)
  • RAG Answer      : Chichester City Council comprises 18 elected members. The Full Council meets 5 times a year. (5/5 pts)
  • Judge Reason    : Model 1 is incorrect as it provides an incorrect number of elected members and the frequency of Full Council meetings. Model 2 is correct but Model 1 is incorrect, so it gets a score of 5 for RAG.
--------------------------------------------------------------------------------
Question [2/20]: What is the basic annual leave entitlement (excluding bank holidays) for an employee with less than 5 years of service, and what does it increase to after 5 years of service?
  • Expected Answer : 23 days per annum (increases to 28 days after 5 years of service).
  • No-RAG Answer   : The basic annual leave entitlement for an employee with less than 5 years of service is 20 days, excluding bank holidays. After 5 years of service, the entitlement increases to 25 days, excluding bank holidays. (2/5 pts)
  • RAG Answer      : The basic annual leave entitlement for an employee with less than 5 years of service is 23 days per annum. After 5 years of service, it increases to 28 days per annum. (5/5 pts)
  • Judge Reason    : Model 1 is partially correct but includes incorrect numbers, while Model 2 is fully accurate with the correct key numbers.
--------------------------------------------------------------------------------
Question [3/20]: How many maximum days of unused annual leave are employees permitted to carry forward into the next leave year with prior written consent?
  • Expected Answer : Up to 5 days leave (or equivalent of a normal working week for part-time employees).
  • No-RAG Answer   : I don't have the specific information on the maximum days of unused annual leave that can be carried forward into the next leave year with prior written consent. (0/5 pts)
  • RAG Answer      : Employees are permitted to carry forward up to a maximum of 5 days of unused annual leave into the next leave year with prior written consent. (5/5 pts)
  • Judge Reason    : Model 2 provided the exact key number, while Model 1 was incomplete and Model 1 did not provide any answer.
--------------------------------------------------------------------------------
Question [4/20]: By what time on the first day of sickness absence must an employee normally notify their manager of non-attendance?
  • Expected Answer : By telephone before they are due to start work and no later than one hour after they are due to begin work.
  • No-RAG Answer   : The exact time frame may vary depending on the company's policies, but typically, an employee must notify their manager of non-attendance as soon as possible, ideally within 30 minutes to 1 hour of missing work. (2/5 pts)
  • RAG Answer      : An employee must notify their manager of non-attendance by telephone before they are due to start work and, in any event, no later than one hour after they are due to begin work. (5/5 pts)
  • Judge Reason    : Model 1 is partially correct but lacks the exact time frame, while Model 2 is mostly correct but includes unnecessary words.
--------------------------------------------------------------------------------
Question [5/20]: How many continuous calendar days of sickness absence require medical evidence in the form of a doctor's fit note rather than a self-certification form?
  • Expected Answer : Absences lasting more than 7 calendar days (8 calendar days or more).
  • No-RAG Answer   : In the UK, for sickness absence of 4 days or more, a doctor's fit note is required, rather than a self-certification form. (2/5 pts)
  • RAG Answer      : According to Context Chunk 1, all sickness absences that last longer than 7 calendar days require medical evidence in the form of a doctor's fit note, rather than a self-certification form. (5/5 pts)
  • Judge Reason    : Model 1 is partially correct but lacks the exact threshold of 7 calendar days, while Model 2 is mostly correct but includes unnecessary context.
--------------------------------------------------------------------------------
Question [6/20]: What constitutes the distinction between short-term and long-term sickness absence under the Council's definitions?
  • Expected Answer : Short-term: a few hours up to 27 calendar days; Long-term: 28 calendar days or more.
  • No-RAG Answer   : Under the Council's definitions, the distinction between short-term and long-term sickness absence is typically based on the duration of the absence, with short-term absences lasting up to 13 weeks and long-term absences lasting more than 13 weeks. (0/5 pts)
  • RAG Answer      : Under the Council's definitions, short-term sickness absence means any period of sickness lasting from a few hours up to 27 calendar days, while long-term sickness absence means any period of sickness lasting 28 calendar days or more. (5/5 pts)
  • Judge Reason    : Model 1 is incorrect as it provides an incorrect duration for short-term sickness absence. Model 2 is correct as it accurately states the duration for both short-term and long-term sickness absence.
--------------------------------------------------------------------------------
Question [7/20]: How many statutory weeks of total maternity leave is an employee entitled to take, and how is it split?
  • Expected Answer : 52 weeks in total (26 weeks Ordinary Maternity Leave + 26 weeks Additional Maternity Leave).
  • No-RAG Answer   : In the UK, an employee is entitled to 52 weeks of statutory maternity leave, which is split into 39 weeks of ordinary maternity leave and 13 weeks of additional maternity leave. The 39 weeks of ordinary maternity leave are paid at the employee's normal rate of pay, while the 13 weeks of additional maternity leave are paid at 90% of the employee's normal rate of pay. (4/5 pts)
  • RAG Answer      : An employee is entitled to 50 weeks of statutory leave and 37 weeks of statutory pay within the first year after the child is born. The leave can be taken in one-week blocks, with both parents off together or separately. (0/5 pts)
  • Judge Reason    : Model 1 is mostly correct, missing the exact split of ordinary and additional maternity leave, but includes the total number of weeks. Model 2 is incorrect, as it mentions 50 weeks of statutory leave and 37 weeks of statutory pay, which is not the case.
--------------------------------------------------------------------------------
Question [8/20]: How many Keeping in Touch (KIT) days is an employee permitted to work during their maternity or adoption leave?
  • Expected Answer : Up to 10 KIT days with full pay.
  • No-RAG Answer   : I cannot verify the number of Keeping in Touch (KIT) days an employee is permitted to work during their maternity or adoption leave. (0/5 pts)
  • RAG Answer      : An employee is permitted to work up to 10 'Keeping in Touch' (KIT) days during their maternity or adoption leave. (5/5 pts)
  • Judge Reason    : Model 1 is incorrect as it does not provide any information, while Model 2 is correct as it states the exact number of KIT days with full pay.
--------------------------------------------------------------------------------
Question [9/20]: How many days of paid leave are granted under Maternity/Adoption Support Leave to the partner or nominated carer?
  • Expected Answer : 5 days of pay at the time of birth or adoption placement.
  • No-RAG Answer   : I don't have the specific information on the number of days of paid leave granted under Maternity/Adoption Support Leave to the partner or nominated carer. (0/5 pts)
  • RAG Answer      : 5 days of pay are granted to the partner or nominated carer of the mother/primary adopter at or around the time of the birth/adoption placement. (4/5 pts)
  • Judge Reason    : Model 1 is incorrect as it states it doesn't have the information, while Model 2 is mostly correct but misses the phrase 'at or around the time of the' in the expected answer.
--------------------------------------------------------------------------------
Question [10/20]: Within what timeframe must paternity leave be taken following the birth or adoption of a child?
  • Expected Answer : Within 52 weeks of the birth or adoption placement.
  • No-RAG Answer   : In the UK, the Paternity Leave and Pay (Amendment) Regulations 2019 state that paternity leave must be taken within 56 days following the birth or adoption of a child. (1/5 pts)
  • RAG Answer      : Paternity leave must be taken within 52 weeks of the birth or adoption of a child. (5/5 pts)
  • Judge Reason    : Model 1 is partially correct but misses the exact timeframe, while Model 2 is fully accurate with the correct timeframe of 52 weeks.
--------------------------------------------------------------------------------
Question [11/20]: How much continuous service with the Council must an employee have to qualify for parental leave?
  • Expected Answer : At least one year's continuous service.
  • No-RAG Answer   : I don't have specific information on parental leave policies for the Council. However, in general, the amount of continuous service required to qualify for parental leave varies by country, state, or organization, and is typically specified in the relevant employment laws or company policies. (0/5 pts)
  • RAG Answer      : An employee must have at least one year's continuous service with the Council by the time they want to take the leave to qualify for parental leave. (5/5 pts)
  • Judge Reason    : Model 1 is incorrect because it lacks specificity and references general information, while Model 2 is correct as it provides the exact required continuous service time.
--------------------------------------------------------------------------------
Question [12/20]: How far in advance must an employee advise their manager in writing if they wish to take a period of parental leave?
  • Expected Answer : At least 21 days in advance.
  • No-RAG Answer   : In the UK, an employee must give their employer at least 21 days' written notice of their intention to take parental leave, as per the Employment Rights Act 1996. (5/5 pts)
  • RAG Answer      : An employee must advise their manager in writing at least 21 days before they wish to take a period of parental leave. (5/5 pts)
  • Judge Reason    : Both models provide the exact key number (21 days) and the correct context (written notice of parental leave), making them factually complete and accurate.
--------------------------------------------------------------------------------
Question [13/20]: What is the total allowance of statutory unpaid parental leave per child for eligible employees up to the child's 18th birthday?
  • Expected Answer : Up to 18 weeks' unpaid leave per child.
  • No-RAG Answer   : In the UK, eligible employees are entitled to 18 weeks of statutory unpaid parental leave per child, up to the child's 18th birthday. (5/5 pts)
  • RAG Answer      : Up to 2 weeks of parental bereavement leave is available for employees whose child dies under the age of 18. (0/5 pts)
  • Judge Reason    : Model 1's answer is factually complete and accurate, while Model 2's answer is missing the key information about statutory unpaid parental leave.
--------------------------------------------------------------------------------
Question [14/20]: Under what circumstance will sickness absence that begins partway through the working day be recorded as half a day's absence?
  • Expected Answer : When the employee leaves after completing 50% or more of their working day.
  • No-RAG Answer   : Sickness absence that begins partway through the working day will be recorded as half a day's absence if the employee is unable to continue working due to illness and is sent home by their employer. (2/5 pts)
  • RAG Answer      : Sickness absence that begins partway through the day will be recorded as half a day's absence if the employee leaves before completing 50% of their working day. (5/5 pts)
  • Judge Reason    : Model 1 is partially correct but lacks the specific percentage threshold, while Model 2 is mostly correct but includes the employee leaving before completing 50% of their working day, which is not specified in the expected answer.
--------------------------------------------------------------------------------
Question [15/20]: What is the minimum advance written notice required if an employee wishes to change the start date of their maternity leave?
  • Expected Answer : At least 28 days' notice in writing.
  • No-RAG Answer   : The minimum advance written notice required if an employee wishes to change the start date of their maternity leave varies by state, but typically ranges from 30 to 60 days. (2/5 pts)
  • RAG Answer      : At least 28 days' notice in writing is required to change the start date of maternity leave. (5/5 pts)
  • Judge Reason    : Model 1 is partially correct but lacks specificity, while Model 2 is fully accurate with the exact key number.
--------------------------------------------------------------------------------
Question [16/20]: Who holds the ultimate responsibility for reviewing and amending the employee code of conduct and staff handbook policies?
  • Expected Answer : The Personnel Sub-Committee.
  • No-RAG Answer   : The ultimate responsibility for reviewing and amending the employee code of conduct and staff handbook policies typically lies with the organization's leadership, such as the CEO or HR Director. (2/5 pts)
  • RAG Answer      : The Personnel Sub-Committee holds the ultimate responsibility for reviewing and amending the employee code of conduct and staff handbook policies. (5/5 pts)
  • Judge Reason    : Model 1 is partially correct but lacks specificity, while Model 2 is fully accurate and directly references the expected answer.
--------------------------------------------------------------------------------
Question [17/20]: How many minimum working days' notice must an employee be given when invited in writing to a formal sickness absence management meeting?
  • Expected Answer : A minimum of 5 working days' notice.
  • No-RAG Answer   : An employee must be given at least 7 days' written notice before attending a formal sickness absence management meeting. (0/5 pts)
  • RAG Answer      : The employee must be given a minimum of 5 working days' notice when invited in writing to a formal sickness absence management meeting. (5/5 pts)
  • Judge Reason    : Model 1 is incorrect as it provides 7 days' notice, whereas the expected answer is 5 days' notice. Model 2 is correct as it matches the expected answer.
--------------------------------------------------------------------------------
Question [18/20]: Within how many calendar days must an employee lodge a written appeal after receiving confirmation of a formal sickness absence sanction or dismissal?
  • Expected Answer : Within 5 days of receiving written confirmation.
  • No-RAG Answer   : In the UK, an employee must lodge a written appeal within 3 calendar days after receiving confirmation of a formal sickness absence sanction or dismissal. (2/5 pts)
  • RAG Answer      : An employee must lodge a written appeal within five working days after receiving written confirmation of the sanction imposed on them by the Council. (1/5 pts)
  • Judge Reason    : Model 1 is partially correct, but the expected timeframe is 5 days, not 3. Model 2 is incorrect, as it mentions working days instead of calendar days.
--------------------------------------------------------------------------------
Question [19/20]: Which spinal column point (SCP) threshold restricts employees from standing for political posts or engaging in public political activities?
  • Expected Answer : Spinal column point (SCP) 46 or above (or posts determined as 'politically sensitive').
  • No-RAG Answer   : The SCP threshold that restricts employees from standing for political posts or engaging in public political activities is SCP 2. (0/5 pts)
  • RAG Answer      : There is no mention of a spinal column point (SCP) threshold in the provided context. The context only discusses restrictions on employees standing for political posts or engaging in public political activities, but does not mention a specific spinal column point. (0/5 pts)
  • Judge Reason    : Both models provided incorrect or missing information, with Model 1 providing a non-existent SCP threshold and Model 2 failing to identify the correct SCP threshold.
--------------------------------------------------------------------------------
Question [20/20]: How long does a formal warning issued regarding poor attendance remain in place?
  • Expected Answer : A minimum of six months.
  • No-RAG Answer   : The length of time a formal warning remains in place varies depending on the organization's policies, but it is typically 3-6 months. After this period, the warning is usually reviewed and may be replaced with a final written warning or disciplinary action. (3/5 pts)
  • RAG Answer      : A formal warning issued regarding poor attendance remains in place for a minimum of six months. (5/5 pts)
  • Judge Reason    : Model 1 is partially correct, but lacks the exact minimum duration of six months. Model 2 is fully accurate, including the exact key number/metric.
--------------------------------------------------------------------------------

================================================================================
 OPTIMIZED RAG SCOREBOARD
================================================================================
 Model Tested         : llama3.2
 Total Questions      : 20
 Max Score Possible   : 100 pts
 No-RAG Total Score   : 32 / 100 pts (32.0%)
 RAG Total Score      : 80 / 100 pts (80.0%)
 Net Gain             : +48 points
================================================================================
```

## Sample Results Ornith-1.5 (9B)

```
================================================================================
 Querying High-Precision Qdrant RAG Pipeline
 Database Path : ./qdrant_storage
 Search Strategy: MMR (k=6, fetch_k=15, lambda=0.65)
================================================================================

Question [1/20]: How many elected members make up Chichester City Council, and how many times per year does the Full Council meet?
  • Expected Answer : 18 elected members; 5 times per year.
  • No-RAG Answer   : Chichester City Council is made up of 54 elected councillors, and the Full Council meets approximately 10 times per year (roughly twice a month). (0/5 pts)
  • RAG Answer      : Chichester City Council comprises 18 elected members, and the Full Council meets five times per year. (5/5 pts)
  • Judge Reason    : Model 1 gives both numbers wrong (54 councillors and ~10 meetings instead of 18 and 5), while Model 2 matches the expected answer exactly.
--------------------------------------------------------------------------------
Question [2/20]: What is the basic annual leave entitlement (excluding bank holidays) for an employee with less than 5 years of service, and what does it increase to after 5 years of service?
  • Expected Answer : 23 days per annum (increases to 28 days after 5 years of service).
  • No-RAG Answer   : Under the UK Civil Service scheme, an employee with less than 5 years of service is entitled to **25 days** of annual leave, which increases to **27.5 days** after 5 years of service. (0/5 pts)
  • RAG Answer      : The basic annual leave entitlement is 23 days per annum, and it increases to 28 days after 5 years of service. (5/5 pts)
  • Judge Reason    : Model 1 gives incorrect figures (25 days / 27.5 days) that contradict the expected answer, while Model 2 matches the expected answer exactly (23 days increasing to 28 days).
--------------------------------------------------------------------------------
Question [3/20]: How many maximum days of unused annual leave are employees permitted to carry forward into the next leave year with prior written consent?
  • Expected Answer : Up to 5 days leave (or equivalent of a normal working week for part-time employees).
  • No-RAG Answer   : I don't have access to the specific policy document you're referencing, so I can't confirm the exact number of days. Could you share the relevant handbook or policy text so I can give you an accurate answer? (0/5 pts)
  • RAG Answer      : Employees are permitted to carry forward up to a maximum of **5 days** of unused annual leave (or the equivalent of a normal working week if they work part-time), with prior written consent from their line manager. (5/5 pts)
  • Judge Reason    : Model 1 refuses to answer and provides no information, while Model 2 correctly states the exact 5-day maximum plus the part-time equivalent and prior written consent, matching the expected answer.
--------------------------------------------------------------------------------
Question [4/20]: By what time on the first day of sickness absence must an employee normally notify their manager of non-attendance?
  • Expected Answer : By telephone before they are due to start work and no later than one hour after they are due to begin work.
  • No-RAG Answer   : Employees are normally expected to notify their manager by **9:00 AM** on the first day of sickness absence. (0/5 pts)
  • RAG Answer      : Normally, the employee should notify their manager of non-attendance by telephone before they are due to start work, and in any event no later than one hour after they are due to begin work. (5/5 pts)
  • Judge Reason    : Model 1 hallucinates a specific time (9:00 AM) that contradicts the expected answer, while Model 2 accurately captures all key elements (by telephone, before start, and no later than one hour after).
--------------------------------------------------------------------------------
Question [5/20]: How many continuous calendar days of sickness absence require medical evidence in the form of a doctor's fit note rather than a self-certification form?
  • Expected Answer : Absences lasting more than 7 calendar days (8 calendar days or more).
  • No-RAG Answer   : In the UK, employees are self-certified for the first **7 days** of sickness absence, after which a doctor's fit note (medical evidence) is required. (5/5 pts)
  • RAG Answer      : Sickness absences lasting **longer than seven calendar days** require medical evidence in the form of a doctor's fit note, whereas the first seven calendar days can be self-certified. (5/5 pts)
  • Judge Reason    : Both answers correctly state that the first 7 days are self-certified and a doctor's fit note is required after that, which is equivalent to the expected answer of more than 7 calendar days (8 or more).
--------------------------------------------------------------------------------
Question [6/20]: What constitutes the distinction between short-term and long-term sickness absence under the Council's definitions?
  • Expected Answer : Short-term: a few hours up to 27 calendar days; Long-term: 28 calendar days or more.
  • No-RAG Answer   : The distinction is typically based on duration: short-term sickness absence generally refers to absence lasting up to four weeks, while long-term sickness absence refers to absence exceeding four weeks. (Note: exact thresholds can vary by specific Council policy, so it's worth confirming the precise definition in your organisation's handbook.) (0/5 pts)
  • RAG Answer      : Short-term sickness absence is defined as any period of sickness lasting from a few hours up to 27 calendar days, whereas long-term sickness absence is any period of sickness lasting 28 calendar days or more. (5/5 pts)
  • Judge Reason    : Model 1 incorrectly states a four-week threshold (28 days) rather than the correct 27/28-day split, while Model 2 exactly matches the expected answer with the precise 27/28 calendar day figures.
--------------------------------------------------------------------------------
Question [7/20]: How many statutory weeks of total maternity leave is an employee entitled to take, and how is it split?
  • Expected Answer : 52 weeks in total (26 weeks Ordinary Maternity Leave + 26 weeks Additional Maternity Leave).
  • No-RAG Answer   : An employee is entitled to **52 weeks** of statutory maternity leave, split into **26 weeks of paid leave** (Statutory Maternity Pay or Maternity Allowance) and **26 weeks of unpaid leave**. (5/5 pts)
  • RAG Answer      : Based on the provided context, the only maternity leave figures stated are **26 weeks of Additional Maternity Leave (AML)** and a **compulsory two-week period of maternity leave immediately following the birth**. The context does not explicitly state a total statutory maternity leave entitlement or how it is split between ordinary and additional leave. (1/5 pts)
  • Judge Reason    : Model 1 correctly states the 52-week total split into 26+26 weeks (matching the expected answer), while Model 2 fails to provide the total entitlement or the ordinary/additional split, only mentioning 26 weeks AML.
--------------------------------------------------------------------------------
Question [8/20]: How many Keeping in Touch (KIT) days is an employee permitted to work during their maternity or adoption leave?
  • Expected Answer : Up to 10 KIT days with full pay.
  • No-RAG Answer   : An employee is permitted to work up to **10 Keeping in Touch (KIT) days** during their maternity or adoption leave without losing their leave entitlement. (5/5 pts)
  • RAG Answer      : An employee is permitted to attend work with full pay for up to 10 'Keeping in Touch' (KIT) days during their maternity or adoption leave without losing their entitlements to leave and pay. (5/5 pts)
  • Judge Reason    : Both answers correctly state the key metric of 10 KIT days during maternity/adoption leave; Model 2 is marginally more complete by explicitly mentioning 'full pay,' but both are factually accurate and complete enough for full marks.
--------------------------------------------------------------------------------
Question [9/20]: How many days of paid leave are granted under Maternity/Adoption Support Leave to the partner or nominated carer?
  • Expected Answer : 5 days of pay at the time of birth or adoption placement.
  • No-RAG Answer   : Under the Paid Parental Leave scheme, a partner or nominated carer is granted **10 days** of paid Maternity/Adoption Support Leave. (0/5 pts)
  • RAG Answer      : 5 days of pay are granted at the time of the birth/placement. (5/5 pts)
  • Judge Reason    : Model 1 incorrectly states 10 days instead of the correct 5 days, while Model 2 accurately matches the expected answer of 5 days of pay at birth/adoption placement.
--------------------------------------------------------------------------------
Question [10/20]: Within what timeframe must paternity leave be taken following the birth or adoption of a child?
  • Expected Answer : Within 52 weeks of the birth or adoption placement.
  • No-RAG Answer   : Paternity leave must generally be taken within 56 days of the child's birth (in the UK), though this timeframe varies by country and employer policy. (1/5 pts)
  • RAG Answer      : Paternity leave must be taken within 52 weeks of the birth (or adoption placement). (5/5 pts)
  • Judge Reason    : Model 2 correctly states the 52-week timeframe matching the expected answer, while Model 1 incorrectly cites 56 days instead of 52 weeks, making it factually inaccurate against the expected answer.
--------------------------------------------------------------------------------
Question [11/20]: How much continuous service with the Council must an employee have to qualify for parental leave?
  • Expected Answer : At least one year's continuous service.
  • No-RAG Answer   : I don't have specific information about which Council you're referring to or their exact parental leave policy. The continuous service requirement would be outlined in that particular Council's employee handbook or leave policy, so I'd recommend checking their official HR resources or contacting their human resources department directly. (0/5 pts)
  • RAG Answer      : An employee must have at least one year's continuous service with the Council by the time they want to take the leave. (5/5 pts)
  • Judge Reason    : Model 1 declines to answer and provides no factual information, while Model 2 correctly states the exact requirement of at least one year's continuous service.
--------------------------------------------------------------------------------
Question [12/20]: How far in advance must an employee advise their manager in writing if they wish to take a period of parental leave?
  • Expected Answer : At least 21 days in advance.
  • No-RAG Answer   : Under UK law, an employee must give at least 28 weeks' notice in writing to their manager if they wish to take parental leave. (0/5 pts)
  • RAG Answer      : An employee must advise their manager in writing at least 21 days before they wish to take the parental leave. (5/5 pts)
  • Judge Reason    : Model 1 incorrectly states 28 weeks' notice (wrong metric), while Model 2 correctly matches the expected 21 days in advance.
--------------------------------------------------------------------------------
Question [13/20]: What is the total allowance of statutory unpaid parental leave per child for eligible employees up to the child's 18th birthday?
  • Expected Answer : Up to 18 weeks' unpaid leave per child.
  • No-RAG Answer   : Eligible employees are entitled to **18 weeks** of statutory unpaid parental leave for each child under 18. (5/5 pts)
  • RAG Answer      : Based on the provided context, eligible employees are entitled to a total of **18 weeks of ordinary parental leave** per child, up to the child's 18th birthday. (5/5 pts)
  • Judge Reason    : Both answers correctly state the key metric of 18 weeks of parental leave per child, matching the expected answer; Model 2 uses 'ordinary parental leave' instead of 'unpaid parental leave,' a minor terminology difference that does not affect the core accuracy.
--------------------------------------------------------------------------------
Question [14/20]: Under what circumstance will sickness absence that begins partway through the working day be recorded as half a day's absence?
  • Expected Answer : When the employee leaves after completing 50% or more of their working day.
  • No-RAG Answer   : Sickness absence is recorded in units of half a day, so any absence that begins partway through the working day (rather than at the start) is recorded as half a day's absence. (1/5 pts)
  • RAG Answer      : Sickness absence that begins after the employee has completed 50% of their working day will be recorded as half a day's absence. (5/5 pts)
  • Judge Reason    : Model 1 fails to mention the 50% threshold and incorrectly states that ANY absence beginning partway is recorded as half a day, while Model 2 correctly identifies the 50% completion rule matching the expected answer.
--------------------------------------------------------------------------------
Question [15/20]: What is the minimum advance written notice required if an employee wishes to change the start date of their maternity leave?
  • Expected Answer : At least 28 days' notice in writing.
  • No-RAG Answer   : Under UK statutory maternity leave rules, an employee must give at least **28 days' written notice** to change the start date of their maternity leave. (5/5 pts)
  • RAG Answer      : At least 28 days' notice in writing is required to change the start date of maternity leave. (5/5 pts)
  • Judge Reason    : Both answers correctly state the required 28 days' written notice, matching the expected answer exactly.
--------------------------------------------------------------------------------
Question [16/20]: Who holds the ultimate responsibility for reviewing and amending the employee code of conduct and staff handbook policies?
  • Expected Answer : The Personnel Sub-Committee.
  • No-RAG Answer   : The ultimate responsibility typically rests with the employer or the organization's top leadership (such as the CEO or executive team), who may delegate day-to-day updates to a designated committee or HR department. (0/5 pts)
  • RAG Answer      : The Personnel Sub-Committee holds the responsibility for reviewing and amending the employee code of conduct and policies contained in the employee handbook. (5/5 pts)
  • Judge Reason    : Model 1 gives a generic answer that fails to identify the specific Personnel Sub-Committee, while Model 2 correctly matches the expected answer exactly.
--------------------------------------------------------------------------------
Question [17/20]: How many minimum working days' notice must an employee be given when invited in writing to a formal sickness absence management meeting?
  • Expected Answer : A minimum of 5 working days' notice.
  • No-RAG Answer   : An employee must be given at least **5 working days' notice** when invited in writing to a formal sickness absence management meeting, in line with ACAS guidance. (5/5 pts)
  • RAG Answer      : An employee must be given a minimum of **five working days' notice** when invited in writing to a formal sickness absence management meeting. (5/5 pts)
  • Judge Reason    : Both answers correctly state the minimum of 5 working days' notice, matching the expected answer exactly.
--------------------------------------------------------------------------------
Question [18/20]: Within how many calendar days must an employee lodge a written appeal after receiving confirmation of a formal sickness absence sanction or dismissal?
  • Expected Answer : Within 5 days of receiving written confirmation.
  • No-RAG Answer   : An employee must lodge a written appeal within **5 working days** of receiving confirmation of the sanction or dismissal. (Note: this reflects a common UK public-sector/NHS policy timeframe—verify against your specific organisation's policy, as some may specify calendar days or a different period.) (1/5 pts)
  • RAG Answer      : Based on the provided context, an employee must lodge their appeal within **five days** of receiving written confirmation of the sanction imposed on them (Context Chunk 1). Note that for appeals against a formal warning or dismissal, the requirement is **five working days** (Context Chunk 6). (5/5 pts)
  • Judge Reason    : Model 1 incorrectly states '5 working days' instead of the expected '5 calendar days,' while Model 2 correctly answers 'five days' matching the expected answer.
--------------------------------------------------------------------------------
Question [19/20]: Which spinal column point (SCP) threshold restricts employees from standing for political posts or engaging in public political activities?
  • Expected Answer : Spinal column point (SCP) 46 or above (or posts determined as 'politically sensitive').
  • No-RAG Answer   : This question appears to be based on a false premise—there is no such thing as a "spinal column point (SCP) threshold" that restricts employees from political activities. The terms "spinal column" (an anatomical structure) and political activity restrictions are unrelated, so no such threshold exists. (0/5 pts)
  • RAG Answer      : SCP 46. (5/5 pts)
  • Judge Reason    : Model 1 incorrectly rejects the premise and scores 0, while Model 2 correctly provides the exact threshold (SCP 46), matching the expected answer and earning 5.
--------------------------------------------------------------------------------
Question [20/20]: How long does a formal warning issued regarding poor attendance remain in place?
  • Expected Answer : A minimum of six months.
  • No-RAG Answer   : A formal warning typically remains in place for **6 to 12 months**, though the exact duration depends on your organization's specific attendance policy. I'd recommend checking your employee handbook or HR guidelines for the precise timeframe. (1/5 pts)
  • RAG Answer      : A formal warning regarding poor attendance remains in place for a minimum of six months. (5/5 pts)
  • Judge Reason    : Model 2 exactly matches the expected answer of a minimum of six months, while Model 1 gives an inaccurate range of 6-12 months and fails to state the correct minimum.
--------------------------------------------------------------------------------

================================================================================
 OPTIMIZED RAG SCOREBOARD
================================================================================
 Model Tested         : ornith-1.5:9b
 Total Questions      : 20
 Max Score Possible   : 100 pts
 No-RAG Total Score   : 34 / 100 pts (34.0%)
 RAG Total Score      : 96 / 100 pts (96.0%)
 Net Gain             : +62 points
================================================================================

```
