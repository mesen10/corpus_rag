```
================================================================================
 Querying High-Precision Qdrant RAG Pipeline
 Database Path : ./qdrant_storage
 Search Strategy: MMR (k=6, fetch_k=15, lambda=0.65)
================================================================================

Question [1/20]: What is the basic annual leave entitlement (excluding bank holidays) for an employee with less than 5 years of service?
  • Expected Answer : 23 days per annum.
  • No-RAG Answer   : In the UK, the basic annual leave entitlement (excluding bank holidays) for an employee with less than 5 years of service is 20 days per year. (3/5 pts)
  • RAG Answer      : The basic annual leave entitlement, excluding bank holidays, is 23 days per annum for employees with less than 5 years of service. (5/5 pts)
  • Judge Reason    : Model 1 is partially correct but lacks the exact number of days (23) and Model 2 provides a fully accurate answer.
--------------------------------------------------------------------------------
Question [2/20]: After how many years of continuous service does the basic annual leave entitlement increase to 28 days?
  • Expected Answer : 5 years of service.
  • No-RAG Answer   : I don't have specific information on when the basic annual leave entitlement increases to 28 days. Annual leave entitlements can vary depending on the country, employer, or collective agreement. (0/5 pts)
  • RAG Answer      : The basic annual leave entitlement increases to 28 days after 5 years' service. (4/5 pts)
  • Judge Reason    : Model 1 is incorrect as it lacks specific information, while Model 2 provides the correct answer with a minor detail missing.
--------------------------------------------------------------------------------
Question [3/20]: How many statutory and public bank holidays are normally observed per year?
  • Expected Answer : 8 public and bank holidays per year.
  • No-RAG Answer   : In the UK, there are 8 statutory bank holidays per year. Additionally, some countries observe more public holidays, but these 8 are typically considered standard across most of Europe. (4/5 pts)
  • RAG Answer      : There are normally 8 public and bank holidays per year. Part-time employees will receive an entitlement that is pro-rated according to their hours of work. (3/5 pts)
  • Judge Reason    : Model 1 is mostly correct but lacks specificity about the holidays being observed in all of Europe. Model 2 provides additional context about part-time employees' entitlements but does not confirm the number of public and bank holidays.
--------------------------------------------------------------------------------
Question [4/20]: How many days of untaken annual leave can employees carry over into the next leave year with prior written consent?
  • Expected Answer : Up to a maximum of 5 days.
  • No-RAG Answer   : In most countries, including Australia and New Zealand, employees are allowed to carry over up to 5 days (or equivalent) of unused annual leave into the next leave year with prior written consent from their employer. (4/5 pts)
  • RAG Answer      : Employees can carry over up to 5 days of untaken annual leave into the next leave year, or the equivalent of a normal working week if they work part-time. (3/5 pts)
  • Judge Reason    : Model 1 is mostly correct but lacks the phrase 'or equivalent' in Model 2's RAG answer.
--------------------------------------------------------------------------------
Question [5/20]: What threshold duration in calendar days distinguishes short-term sickness absence from long-term sickness absence?
  • Expected Answer : Short-term is up to 27 days; long-term is 28 calendar days or more.
  • No-RAG Answer   : The World Health Organization (WHO) defines a threshold of 7 to 14 calendar days as distinguishing between short-term and long-term sickness absence. This duration helps differentiate between acute illnesses that are typically resolved within a shorter period, and chronic conditions that require longer periods of recovery or treatment. (2/5 pts)
  • RAG Answer      : The threshold duration that distinguishes short-term sickness absence from long-term sickness absence is 27 calendar days. Long-term sickness absence means any period of sickness lasting 28 calendar days or more. (4/5 pts)
  • Judge Reason    : Model 1 is partially correct but lacks the exact key numbers/metrics. Model 2 accurately states the threshold duration of 27 calendar days for short-term sickness absence and correctly defines long-term sickness absence as 28 calendar days or more.
--------------------------------------------------------------------------------
Question [6/20]: Within how many calendar days of sickness can an employee self-certify before a doctor's fit note is required?
  • Expected Answer : Seven calendar days or less.
  • No-RAG Answer   : In the UK, an employee must self-certify for sickness absence for up to 7 consecutive calendar days. After this period, a doctor's fit note is typically required. (4/5 pts)
  • RAG Answer      : An employee can self-certify for the first 7 calendar days of sickness. After that, a doctor's fit note (Med3) is required. (3/5 pts)
  • Judge Reason    : Model 1 is mostly correct but lacks specificity on consecutive days. Model 2 accurately states the time frame and includes the required note.
--------------------------------------------------------------------------------
Question [7/20]: What is the deadline and method for an employee to report their absence on the first day of sickness?
  • Expected Answer : Notify line manager by telephone before start time and no later than 1 hour after starting time.
  • No-RAG Answer   : The exact deadline may vary depending on the company's policies, but typically, employees are required to notify HR or management within a few hours or by the end of the workday of their absence. The method can be via phone, email, or online portal, often with a standard template provided by the employer. (2/5 pts)
  • RAG Answer      : The employee must inform their manager as soon as reasonably practicable by telephone before they are due to start work. (4/5 pts)
  • Judge Reason    : Model 1 is partially correct but lacks specific details about the deadline and method. Model 2 is mostly correct but uses the phrase 'as soon as reasonably practicable', which is not present in the expected answer.
--------------------------------------------------------------------------------
Question [8/20]: When does sickness starting mid-shift count as a full day of sickness absence?
  • Expected Answer : When the employee leaves work before completing 50% of their working day.
  • No-RAG Answer   : In the UK, sickness absence is typically counted from the start of the shift, not necessarily at the end. If an employee starts feeling unwell during their shift and reports it to their employer before the end of that shift, they are usually considered to have worked a full day. (2/5 pts)
  • RAG Answer      : If an employee leaves before completing 50% of their working day, sickness absence that begins part way through the day will count as one full day's sickness absence. (4/5 pts)
  • Judge Reason    : Model 1 is partially correct but misses the exact percentage (50%) and does not consider reporting to employer before end of shift. Model 2 is mostly correct, accurately stating that sickness absence begins part way through the day if employee leaves before completing 50% of their working day.
--------------------------------------------------------------------------------
Question [9/20]: How many weeks of total maternity leave is an employee entitled to take, and how is it split?
  • Expected Answer : 52 weeks total (26 weeks Ordinary Maternity Leave and 26 weeks Additional Maternity Leave).
  • No-RAG Answer   : In the United States, employees are typically entitled to up to 12 weeks of unpaid family and medical leave under the Family and Medical Leave Act (FMLA). The leave can be taken in a single block or split into two separate blocks of 12 weeks each. (2/5 pts)
  • RAG Answer      : An employee is entitled to 26 weeks additional maternity leave, with a compulsory two-week period immediately following the birth. The remaining 24 weeks can be taken in one-week blocks. (4/5 pts)
  • Judge Reason    : Model 1 is partially correct but lacks the total weeks and split details. Model 2 provides a more accurate breakdown of the leave but misses the total weeks.
--------------------------------------------------------------------------------
Question [10/20]: What is the mandatory compulsory period of maternity leave following childbirth?
  • Expected Answer : A two-week compulsory maternity leave period immediately following the birth.
  • No-RAG Answer   : In many countries, including the United States, Canada, and some European nations, there is no federal law requiring a specific number of weeks or months of paid maternity leave. However, some countries like Sweden, Norway, and Iceland have implemented mandatory parental leave policies that include both mothers and fathers. (2/5 pts)
  • RAG Answer      : The mandatory compulsory period of maternity leave immediately following childbirth is two weeks. (4/5 pts)
  • Judge Reason    : Model 1 is partially correct as it mentions a two-week period but does not specify 'compulsory', while Model 2 is mostly correct with the addition of 'mandatory' and 'compulsory'.
--------------------------------------------------------------------------------
Question [11/20]: How many 'Keeping in Touch' (KIT) days can an employee attend with full pay during maternity leave?
  • Expected Answer : Up to 10 KIT days.
  • No-RAG Answer   : I cannot provide information on the number of "Keeping in Touch" (KIT) days that an employee can attend with full pay during maternity leave. (0/5 pts)
  • RAG Answer      : An employee is entitled to up to 10 "Keeping in Touch" (KIT) days with full pay during maternity leave. This provision allows for attendance without losing maternity leave and pay entitlements. (5/5 pts)
  • Judge Reason    : Model 1 is incorrect as it does not provide any information, while Model 2 provides the exact expected answer.
--------------------------------------------------------------------------------
Question [12/20]: How many days of paid Maternity/Adoption Support Leave are granted to a partner or nominated carer?
  • Expected Answer : 5 days of paid leave.
  • No-RAG Answer   : I don't have the specific information on the number of days of paid Maternity/Adoption Support Leave granted to a partner or nominated carer. This can vary depending on the country, state, or organization's policies. (0/5 pts)
  • RAG Answer      : 5 days' pay is granted to the partner or nominated carer at the time of the birth/placement. (4/5 pts)
  • Judge Reason    : Model 2 is mostly correct but lacks the specific detail that the leave is 'at the time of the birth/placement', whereas the expected answer includes this crucial information.
--------------------------------------------------------------------------------
Question [13/20]: How much written notice in advance must an employee give to request a period of unpaid Parental Leave?
  • Expected Answer : At least 21 days' notice in writing.
  • No-RAG Answer   : In the UK, an employee can request a period of unpaid Parental Leave with at least 20 weeks' written notice. In some cases, less notice may be required if the employee is on maternity leave or has already given notice for maternity leave. (2/5 pts)
  • RAG Answer      : An employee must advise their manager in writing at least 21 days before wishing to take parental leave. (4/5 pts)
  • Judge Reason    : Model 1 is partially correct but lacks the exact number of days (21) and includes irrelevant information about maternity leave. Model 2 is mostly correct with the required notice period but does not provide additional context.
--------------------------------------------------------------------------------
Question [14/20]: What is the maximum number of weeks of unpaid Parental Leave an employee can take per year per child?
  • Expected Answer : Up to 4 weeks per year per child.
  • No-RAG Answer   : In the United States, under the Family and Medical Leave Act (FMLA), eligible employees are entitled to up to 12 weeks of unpaid leave per year for each qualifying family member. (2/5 pts)
  • RAG Answer      : An employee can take up to 18 weeks' unpaid leave for each child. (4/5 pts)
  • Judge Reason    : Model 1 is partially correct but lacks the specific detail that FMLA leave is unpaid. Model 2 provides an incorrect number of weeks (18) compared to the expected answer (up to 4 weeks).
--------------------------------------------------------------------------------
Question [15/20]: How many elected members sit on Chichester City Council, and how many wards do they represent?
  • Expected Answer : 18 elected members representing 5 wards.
  • No-RAG Answer   : I don't have the most current information. However, as of my knowledge cutoff in 2023, Chichester City Council has 24 elected members representing 17 wards. (2/5 pts)
  • RAG Answer      : There are 18 elected members on Chichester City Council, representing the five wards of North, East, South, West, and Central. (4/5 pts)
  • Judge Reason    : Model 1 is partially correct but lacks current information and contains incorrect ward numbers. Model 2 is mostly correct with the number of elected members but misses ward details.
--------------------------------------------------------------------------------
Question [16/20]: How many times a year does the Full Council meet?
  • Expected Answer : 5 times a year.
  • No-RAG Answer   : I don't have specific information on the frequency of Full Council meetings. However, it's common for councils to meet at least quarterly or bi-annually, but this can vary depending on the council and its needs. (2/5 pts)
  • RAG Answer      : The Full Council meets five times a year. (5/5 pts)
  • Judge Reason    : Model 1 is partially correct but lacks specific information, while Model 2 provides an exact number and demonstrates a clear understanding of the expected answer.
--------------------------------------------------------------------------------
Question [17/20]: At what spinal column point (SCP) threshold are employees restricted from engaging in political activities?
  • Expected Answer : Spinal column point (SCP) 46 or above.
  • No-RAG Answer   : I couldn't find specific information on a "Spinal Column Point" (SCP) threshold. However, I can tell you that the Fair Labor Standards Act (FLSA) prohibits federal employees from engaging in certain political activities, and this is typically governed by agency policies rather than a specific spinal column point. (2/5 pts)
  • RAG Answer      : There is no mention of a "spinal column point" threshold in the provided context. The context only discusses restrictions on political activity for certain employees, but does not specify a particular SCP threshold. (2/5 pts)
  • Judge Reason    : Both models failed to provide a specific SCP threshold, with Model 1 providing general information on FLSA and Model 2 stating there was no mention of SCP in the context.
--------------------------------------------------------------------------------
Question [18/20]: Within how many days must an employee lodge an appeal against a formal sickness warning or dismissal?
  • Expected Answer : Within 5 days of receiving written confirmation.
  • No-RAG Answer   : In the UK, an employee typically has 3 days to lodge an appeal against a formal sickness warning or dismissal. (2/5 pts)
  • RAG Answer      : An employee must lodge an appeal against a formal sickness warning or dismissal within 5 working days. (4/5 pts)
  • Judge Reason    : Model 1 is partially correct but lacks the 'working days' detail. Model 2 is mostly correct with an exact key number/metric.
--------------------------------------------------------------------------------
Question [19/20]: What is the maximum length of a councillor's term of office before re-election?
  • Expected Answer : A maximum of 4 years.
  • No-RAG Answer   : I don't have specific information on the maximum length of a councillor's term of office. However, it varies by jurisdiction and country, with some places having no limit and others having a fixed term. (2/5 pts)
  • RAG Answer      : A Councillor can only serve for a maximum of 4 years before submitting themselves to the electoral process. (4/5 pts)
  • Judge Reason    : Model 1 is partially correct but lacks specificity and exact numbers. Model 2 is mostly correct with the key detail of a maximum term length, but incorrectly states 'submitting themselves' instead of 're-election'.
--------------------------------------------------------------------------------
Question [20/20]: Under what circumstance is alcohol allowed on Council premises during working hours?
  • Expected Answer : When specifically approved by the Town Clerk.
  • No-RAG Answer   : I don't have specific information about the circumstances under which alcohol may be allowed on council premises. However, it's likely that such permission would be granted for official events or functions with prior approval from council authorities. (2/5 pts)
  • RAG Answer      : Alcohol is permitted on Council premises during working hours only for serving at a civic function. (3/5 pts)
  • Judge Reason    : Model 1 is partially correct as it mentions prior approval from council authorities, but lacks specificity. Model 2 is mostly correct, missing the detail that alcohol can be served at civic functions during working hours.
--------------------------------------------------------------------------------

================================================================================
 OPTIMIZED RAG SCOREBOARD
================================================================================
 Model Tested         : llama3.2
 Total Questions      : 20
 Max Score Possible   : 100 pts
 No-RAG Total Score   : 41 / 100 pts (41.0%)
 RAG Total Score      : 77 / 100 pts (77.0%)
 Net Gain             : +36 points
================================================================================ 
```