```
================================================================================
 Querying High-Precision Qdrant RAG Pipeline
 Database Path : ./qdrant_storage
 Search Strategy: MMR (k=6, fetch_k=15, lambda=0.65)
================================================================================

Question [1/20]: What is the basic annual leave entitlement (excluding bank holidays) for an employee with less than 5 years of service?
  • Expected Answer : 23 days per annum.
  • No-RAG Answer   : In the UK, the basic annual leave entitlement (excluding bank holidays) for an employee with less than 5 years of service is 20 days per year. (3/5 pts)
  • RAG Answer      : The basic annual leave entitlement for an employee with less than 5 years of service is 23 days per annum. (5/5 pts)
  • Judge Reason    : Model 1 is partially correct but misses the exact number of days, while Model 2 is mostly correct but includes unnecessary words.
--------------------------------------------------------------------------------
Question [2/20]: After how many years of continuous service does the basic annual leave entitlement increase to 28 days?
  • Expected Answer : 5 years of service.
  • No-RAG Answer   : I don't have specific information on the exact number of years for a basic annual leave entitlement increase to 28 days. However, in many countries, the accrual rate for annual leave varies, and it's typically tied to the employee's length of service, but the exact timeframe can differ. (0/5 pts)
  • RAG Answer      : The basic annual leave entitlement increases to 28 days after 5 years of continuous service. (5/5 pts)
  • Judge Reason    : Model 1 is incorrect as it lacks specific information, while Model 2 provides the exact timeframe of 5 years.
--------------------------------------------------------------------------------
Question [3/20]: How many statutory and public bank holidays are normally observed per year?
  • Expected Answer : 8 public and bank holidays per year.
  • No-RAG Answer   : In the UK, there are 8 statutory bank holidays per year, plus 4 additional public holidays, making a total of 12 bank holidays. (2/5 pts)
  • RAG Answer      : There are normally 8 public and bank holidays per year. (5/5 pts)
  • Judge Reason    : Model 1 is partially correct but includes additional public holidays, while Model 2 is fully accurate but does not provide additional details.
--------------------------------------------------------------------------------
Question [4/20]: How many days of untaken annual leave can employees carry over into the next leave year with prior written consent?
  • Expected Answer : Up to a maximum of 5 days.
  • No-RAG Answer   : In the United States, the Fair Labor Standards Act (FLSA) allows employees to carry over up to 1,200 hours (or 30 days) of accrued but unused annual leave into the next leave year with prior written consent from their employer. (0/5 pts)
  • RAG Answer      : Employees can carry over up to 5 days of untaken annual leave into the next leave year with prior written consent. (5/5 pts)
  • Judge Reason    : Model 1 is incorrect as it references the FLSA and a specific number of hours, whereas the expected answer only mentions days. Model 2 is correct as it states the correct number of days (up to 5) and aligns with the expected answer.
--------------------------------------------------------------------------------
Question [5/20]: What threshold duration in calendar days distinguishes short-term sickness absence from long-term sickness absence?
  • Expected Answer : Short-term is up to 27 days; long-term is 28 calendar days or more.
  • No-RAG Answer   : The threshold duration for distinguishing short-term sickness absence from long-term sickness absence is typically 7 calendar days. (0/5 pts)
  • RAG Answer      : The threshold duration in calendar days that distinguishes short-term sickness absence from long-term sickness absence is 27 calendar days. (4/5 pts)
  • Judge Reason    : Model 1 is incorrect as it does not mention the 28-day threshold, while Model 2 is mostly correct but misses the 'or more' part.
--------------------------------------------------------------------------------
Question [6/20]: Within how many calendar days of sickness can an employee self-certify before a doctor's fit note is required?
  • Expected Answer : Seven calendar days or less.
  • No-RAG Answer   : In the UK, an employee can self-certify sickness for up to 7 days. After 7 days, a doctor's fit note is required. (4/5 pts)
  • RAG Answer      : An employee can self-certify for sickness up to 7 calendar days. After 7 calendar days, a doctor's fit note is required. (5/5 pts)
  • Judge Reason    : Model 1 is mostly correct but lacks the 'or less' clause, while Model 2 is fully accurate and includes the exact key numbers/metrics.
--------------------------------------------------------------------------------
Question [7/20]: What is the deadline and method for an employee to report their absence on the first day of sickness?
  • Expected Answer : Notify line manager by telephone before start time and no later than 1 hour after starting time.
  • No-RAG Answer   : The deadline for an employee to report their absence on the first day of sickness is typically within 3-5 days of the absence, and the method may be through a company's absence reporting system, email, or in-person with a supervisor. (2/5 pts)
  • RAG Answer      : The employee must inform their manager as soon as reasonably practicable that they will not be working because of illness or injury, and normally, this should be done by telephone before they are due to start work. (4/5 pts)
  • Judge Reason    : Model 1 is partially correct but lacks specific details, while Model 2 is mostly correct but uses the phrase 'as soon as reasonably practicable' which is not present in the expected answer.
--------------------------------------------------------------------------------
Question [8/20]: When does sickness starting mid-shift count as a full day of sickness absence?
  • Expected Answer : When the employee leaves work before completing 50% of their working day.
  • No-RAG Answer   : In the UK, sickness absence is typically counted as a full day if the employee is absent for more than 4 hours of their shift. (2/5 pts)
  • RAG Answer      : If the employee leaves before completing 50% of their working day, sickness absence starting mid-shift will count as one full day's sickness absence. (5/5 pts)
  • Judge Reason    : Model 1 is partially correct but lacks the specific percentage (50%) mentioned in the Expected Answer. Model 2 is fully accurate as it includes the exact key detail.
--------------------------------------------------------------------------------
Question [9/20]: How many weeks of total maternity leave is an employee entitled to take, and how is it split?
  • Expected Answer : 52 weeks total (26 weeks Ordinary Maternity Leave and 26 weeks Additional Maternity Leave).
  • No-RAG Answer   : In the United States, the Family and Medical Leave Act (FMLA) provides eligible employees with up to 12 weeks of unpaid leave for certain family and medical reasons, including childbirth. The leave is typically taken in a single block of 12 weeks, with some states offering additional paid family leave. (1/5 pts)
  • RAG Answer      : An employee is entitled to 26 weeks of maternity leave, with a compulsory 2-week period immediately following the birth of the baby, and an additional 24 weeks of flexible leave. (2/5 pts)
  • Judge Reason    : Model 1 is partially incorrect as it does not mention the total 52 weeks of maternity leave, and Model 2 is partially incorrect as it does not mention the 2-week compulsory period immediately following the birth of the baby.
--------------------------------------------------------------------------------
Question [10/20]: What is the mandatory compulsory period of maternity leave following childbirth?
  • Expected Answer : A two-week compulsory maternity leave period immediately following the birth.
  • No-RAG Answer   : In the United States, the mandatory compulsory period of maternity leave varies by state, but the federal Family and Medical Leave Act (FMLA) requires up to 12 weeks of unpaid leave for eligible employees. (0/5 pts)
  • RAG Answer      : The mandatory compulsory period of maternity leave immediately following childbirth is two weeks. (5/5 pts)
  • Judge Reason    : Model 1 is incorrect as it provides a federal leave requirement, whereas the expected answer specifies a state-specific two-week compulsory maternity leave. Model 2 is correct as it states the exact two-week period.
--------------------------------------------------------------------------------
Question [11/20]: How many 'Keeping in Touch' (KIT) days can an employee attend with full pay during maternity leave?
  • Expected Answer : Up to 10 KIT days.
  • No-RAG Answer   : I cannot provide information on the number of 'Keeping in Touch' (KIT) days an employee can attend with full pay during maternity leave. (0/5 pts)
  • RAG Answer      : An employee can attend work with full pay for up to 10 'Keeping in Touch' (KIT) days during maternity leave. (5/5 pts)
  • Judge Reason    : Model 1 is incorrect as it does not provide any information, while Model 2 is correct as it states the exact number of KIT days an employee can attend with full pay during maternity leave.
--------------------------------------------------------------------------------
Question [12/20]: How many days of paid Maternity/Adoption Support Leave are granted to a partner or nominated carer?
  • Expected Answer : 5 days of paid leave.
  • No-RAG Answer   : I don't have the specific information on the number of days of paid Maternity/Adoption Support Leave granted to a partner or nominated carer. (0/5 pts)
  • RAG Answer      : 5 days of pay are granted to a partner or nominated carer of the mother/primary adopter at or around the time of the birth/adoption placement. (5/5 pts)
  • Judge Reason    : Model 1 is incorrect as it states it doesn't have the specific information, while Model 2 provides the exact number of days of paid leave.
--------------------------------------------------------------------------------
Question [13/20]: How much written notice in advance must an employee give to request a period of unpaid Parental Leave?
  • Expected Answer : At least 21 days' notice in writing.
  • No-RAG Answer   : In the UK, an employee must give at least 12 weeks' written notice to request a period of unpaid Parental Leave. (0/5 pts)
  • RAG Answer      : An employee must give at least 21 days' written notice to request a period of parental leave. (5/5 pts)
  • Judge Reason    : Model 1 is incorrect as it states 12 weeks instead of 21 days. Model 2 is correct as it states 21 days.
--------------------------------------------------------------------------------
Question [14/20]: What is the maximum number of weeks of unpaid Parental Leave an employee can take per year per child?
  • Expected Answer : Up to 4 weeks per year per child.
  • No-RAG Answer   : In the United States, the Family and Medical Leave Act (FMLA) allows eligible employees to take up to 12 weeks of unpaid leave per year for a qualifying family or medical reason, including the birth or adoption of a child. (0/5 pts)
  • RAG Answer      : An employee can take up to 18 weeks of unpaid parental leave per child. (0/5 pts)
  • Judge Reason    : Both models provided incorrect information, Model 1 mentioned 12 weeks and Model 2 mentioned 18 weeks, whereas the expected answer is 4 weeks per year per child.
--------------------------------------------------------------------------------
Question [15/20]: How many elected members sit on Chichester City Council, and how many wards do they represent?
  • Expected Answer : 18 elected members representing 5 wards.
  • No-RAG Answer   : I don't have the most current information on the specific details of Chichester City Council. However, I can tell you that Chichester City Council is a unitary authority council in West Sussex, England, and it typically has 33 elected members. (0/5 pts)
  • RAG Answer      : Chichester City Council comprises 18 elected members, representing the five wards of Chichester: North, East, South, West, and Central. (5/5 pts)
  • Judge Reason    : Model 1 is incorrect as it provides outdated information, while Model 2 is accurate and provides the exact number of elected members and wards.
--------------------------------------------------------------------------------
Question [16/20]: How many times a year does the Full Council meet?
  • Expected Answer : 5 times a year.
  • No-RAG Answer   : I don't have the specific information on the Full Council meeting frequency. However, it's common for councils to meet at least quarterly or bi-annually. (0/5 pts)
  • RAG Answer      : The Full Council meets five times a year. (5/5 pts)
  • Judge Reason    : Model 1 is incorrect as it provides no specific information, while Model 2 is accurate but lacks context.
--------------------------------------------------------------------------------
Question [17/20]: At what spinal column point (SCP) threshold are employees restricted from engaging in political activities?
  • Expected Answer : Spinal column point (SCP) 46 or above.
  • No-RAG Answer   : I couldn't find specific information on a "Spinal Column Point" (SCP) threshold. However, I can tell you that the Fair Labor Standards Act (FLSA) prohibits federal employees from engaging in political activities during work hours, and this is typically enforced by the Office of Special Counsel. (0/5 pts)
  • RAG Answer      : There is no mention of a spinal column point (SCP) threshold in the provided context. The context only discusses restrictions on political activities for employees of the Council, but does not mention a specific spinal column point. (0/5 pts)
  • Judge Reason    : Both models failed to provide the exact SCP threshold, and instead provided general information about political activities for federal employees.
--------------------------------------------------------------------------------
Question [18/20]: Within how many days must an employee lodge an appeal against a formal sickness warning or dismissal?
  • Expected Answer : Within 5 days of receiving written confirmation.
  • No-RAG Answer   : In the UK, an employee must lodge an appeal against a formal sickness warning or dismissal within 3 days. (2/5 pts)
  • RAG Answer      : An employee must lodge an appeal against a formal sickness warning or dismissal within 5 working days. (5/5 pts)
  • Judge Reason    : Model 1 is partially correct but lacks the 'working' specification, while Model 2 is fully accurate with the exact key numbers/metrics.
--------------------------------------------------------------------------------
Question [19/20]: What is the maximum length of a councillor's term of office before re-election?
  • Expected Answer : A maximum of 4 years.
  • No-RAG Answer   : I don't have specific information on the maximum length of a councillor's term of office before re-election. This can vary depending on the jurisdiction and local laws. (0/5 pts)
  • RAG Answer      : A Councillor can only serve for a maximum of 4 years before submitting themselves to the electoral process. (5/5 pts)
  • Judge Reason    : Model 2's answer is accurate, while Model 1's is incomplete and lacks specificity.
--------------------------------------------------------------------------------
Question [20/20]: Under what circumstance is alcohol allowed on Council premises during working hours?
  • Expected Answer : When specifically approved by the Town Clerk.
  • No-RAG Answer   : I don't have specific information on the circumstances under which alcohol is allowed on Council premises during working hours. However, it's likely that alcohol is permitted for official events, meetings, or functions that are specifically approved by the Council. (2/5 pts)
  • RAG Answer      : Alcohol is permitted on Council premises during working hours if specifically approved by the Town Clerk for serving at a civic function. (5/5 pts)
  • Judge Reason    : Model 1 is partially correct but lacks specificity, while Model 2 is mostly correct but does not provide the full expected answer, which includes the Town Clerk's approval for serving at a civic function.
--------------------------------------------------------------------------------

================================================================================
 OPTIMIZED RAG SCOREBOARD
================================================================================
 Model Tested         : llama3.2
 Total Questions      : 20
 Max Score Possible   : 100 pts
 No-RAG Total Score   : 18 / 100 pts (18.0%)
 RAG Total Score      : 85 / 100 pts (85.0%)
 Net Gain             : +67 points
================================================================================
```