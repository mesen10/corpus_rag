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