# Module 2 - Fighters in the War Against Cybercrime

## Quick Goal of This Module
Understand how a modern Security Operations Center (SOC) works in real life: who does what, how incidents flow, which technologies are used, and how success is measured.

## 2.0 Introduction

### 2.0.1 Why should I take this module?
This module is your bridge from theory to job reality.

Key value:
- It shows where entry-level analysts fit in cybersecurity operations.
- It explains the SOC workflow you will see in internships and junior roles.
- It introduces the tools and metrics employers use to judge team performance.

### 2.0.2 What Will I Learn in this Module?
<img src="content%20folder/Screenshot%202026-03-30%20225444.png" alt="2.0.2 What Will I Learn in this Module" style="max-width: 100%; height: auto;" />

Insight:
- This section sets direction: first understand the SOC mission, then understand how to become a defender.
- Think of it as: Mission first, career path second.

## 2.1 The Modern Security Operations Center

### 2.1.1 Elements of a SOC
<img src="content%20folder/Screenshot%202026-03-30%20225857.png" alt="2.1.1 Elements of a SOC" style="max-width: 100%; height: auto;" />

Insight:
- SOC effectiveness depends on a triangle: People, Process, Technology.
- If one side is weak, security outcomes drop.

How to remember:
- People decide.
- Process standardizes.
- Technology scales.

### 2.1.2 People in the SOC
<img src="content%20folder/Screenshot%202026-03-30%20230049.png" alt="2.1.2 People in the SOC" style="max-width: 100%; height: auto;" />

Insight:
- Tiering is escalation by complexity, not status.
- Work moves upward only when deeper expertise is needed.

Role logic:
- Tier 1 Alert Analyst: Triage and validation.
- Tier 2 Incident Responder: Investigation and remediation actions.
- Tier 3 Threat Hunter/SME: Advanced analysis and detection engineering.
- SOC Manager: Coordination, priorities, communication with leadership.

Career takeaway:
- Entry point is usually Tier 1, where strong fundamentals and disciplined documentation matter most.

### 2.1.3 Process in the SOC
<img src="content%20folder/Screenshot%202026-03-30%20232916.png" alt="2.1.3 Process in the SOC" style="max-width: 100%; height: auto;" />

Insight:
- SOC work is a decision funnel: Alert -> Validate -> Escalate or Close.
- Most operational quality problems come from poor triage, not lack of alerts.

Practical mindset:
- False positives waste analyst time.
- Missed true positives increase attacker dwell time.
- Good tickets accelerate incident response downstream.

### 2.1.4 Technologies in the SOC - SIEM
<img src="content%20folder/Screenshot%202026-03-30%20233047.png" alt="2.1.4 Technologies in the SOC - SIEM" style="max-width: 100%; height: auto;" />

Insight:
- SIEM is the visibility engine of the SOC.
- It centralizes logs and events so analysts can correlate weak signals into strong evidence.

Why this matters:
- Without SIEM, detection is fragmented.
- With SIEM, analysts can ask better questions across multiple data sources.

### 2.1.5 Technologies in the SOC - SOAR
<img src="content%20folder/Screenshot%202026-03-30%20233513.png" alt="2.1.5 Technologies in the SOC - SOAR (Part 1)" style="max-width: 100%; height: auto;" />

<img src="content%20folder/Screenshot%202026-03-30%20233603.png" alt="2.1.5 Technologies in the SOC - SOAR (Part 2)" style="max-width: 100%; height: auto;" />

Insight:
- SIEM tells you what is happening.
- SOAR helps you act faster and more consistently.

Core value of SOAR:
- Orchestration: Connects tools and workflows.
- Automation: Removes repetitive manual steps.
- Response: Executes playbooks with predictable quality.

Operational benefit:
- Analysts spend less time on repetitive alert handling and more time on high-impact investigations.

### 2.1.6 SOC Metrics
<img src="content%20folder/Screenshot%202026-03-30%20233740.png" alt="2.1.6 SOC Metrics" style="max-width: 100%; height: auto;" />

Insight:
- Metrics turn security from opinion into measurable performance.

How to interpret key metrics:
- Dwell Time: How long attackers remain undetected.
- MTTD: Detection speed.
- MTTR: Recovery/remediation speed.
- MTTC: Time to stop spread/impact.
- Time to Control: How quickly containment stabilizes the environment.

Study tip:
- Lower is generally better for all time-based metrics.

### 2.1.7 Enterprise and Managed Security
<img src="content%20folder/Screenshot%202026-03-30%20233902.png" alt="2.1.7 Enterprise and Managed Security" style="max-width: 100%; height: auto;" />

Insight:
- Organizations do not have to do everything in-house.
- Managed security services can extend capability, speed, and specialized expertise.

Decision tradeoff:
- In-house SOC offers direct control.
- Managed/outsourced SOC offers scale and external expertise.
- Many enterprises use a hybrid model.

### 2.1.8 DevSecOps
<img src="content%20folder/Screenshot%202026-03-30%20234009.png" alt="2.1.8 DevSecOps" style="max-width: 100%; height: auto;" />

Insight:
- DevSecOps shifts security left: security is built in early, not bolted on later.

Why it works:
- Early detection costs less to fix.
- Automated controls reduce human bottlenecks.
- Shared ownership improves collaboration among dev, ops, and security teams.

### 2.1.9 Security vs. Availability
<img src="content%20folder/Screenshot%202026-03-30%20234122.png" alt="2.1.9 Security vs. Availability" style="max-width: 100%; height: auto;" />

Insight:
- Security decisions are business decisions.
- The goal is not maximum lockdown; the goal is acceptable risk with reliable uptime.

Interpreting the "nines":
- More availability "nines" means much less allowable downtime.
- Higher availability usually needs more redundancy, cost, and engineering discipline.

Real-world principle:
- Strong security that blocks business operations is poor security design.
- Best practice is balanced control: protect critical assets while preserving service continuity.

## 2.2 Becoming a Defender

### 2.2.1 Certifications
A variety of cybersecurity certifications are relevant to SOC careers, and they help signal role readiness to employers.

Insight:
- Certifications are not a substitute for experience, but they reduce hiring risk for employers by proving baseline capability.
- For entry-level SOC roles, focus on practical analyst skills: detection, triage, investigation, and communication.

Common options:
- Cisco Certified CyberOps Associate: Strong entry path for SOC fundamentals and analyst workflow.
- CompTIA CySA+: Vendor-neutral validation of threat detection, analysis, and risk interpretation.
- (ISC)2 certifications: Broad and respected options across security specializations.
- GIAC certifications: Long-standing, technical certifications across multiple security domains.
- Other certifications: Compare role fit, exam depth, and market demand before choosing.

Study strategy:
- Pick one target role first, then choose certifications that map directly to that role's skills.

### 2.2.2 Further Education

Insight:
- A strong cybersecurity profile combines theory, hands-on labs, and communication skills.

Priority areas:
- Degrees: Computer science, information technology, electrical engineering, or information security can strengthen long-term growth.
- Python programming: High-value for SOC scripting, automation, and log/data handling.
- Linux skills: Essential for analyst workflows, tooling, and troubleshooting in security environments.

Practical approach:
- Build a weekly routine: 1 concept, 1 script, 1 lab, 1 reflection note.

### 2.2.3 Sources of Career Information

Insight:
- Job platforms are not equal; each has different employer types and candidate expectations.

Useful sources:
- Indeed.com: Large global job volume.
- CareerBuilder.com: Often stronger for credential-heavy roles.
- USAJobs.gov: Federal/government opportunities.
- Glassdoor: Salary and role expectation benchmarking.
- LinkedIn: Job search + networking + professional credibility.

How to use them well:
- Track repeated keywords across postings and align your resume/labs to those patterns.

### 2.2.4 Getting Experience

Insight:
- Experience is usually built in layers, not all at once.

High-impact paths:
- Internships: Fastest way to gain real SOC context and references.
- Scholarships/Awards: Reduce training barriers and improve visibility.
- Temporary agencies: Useful bridge into first security-related roles.
- First job strategy: Aim for role progression, not perfect title on day one.

Career guidance:
- Staying about 18 months in your first role often gives enough time for a full review cycle and measurable achievements.

### 2.2.5 Lab - Becoming a Defender
Lab file:
- 2.2.5-lab---becoming-a-defender.pdf

Lab objective:
- Research and analyze what it takes to become a network defender, then convert that research into an actionable career plan.

---

#### Lab Completion: Full Career Analysis & Roadmap

##### Part 1: Target Role Definition

**Role Selected: Tier 1 Alert Analyst (Security Operations Center)**

Why this role:
- Entry-level position suitable for graduates and career changers.
- Direct path to Tier 2 and Tier 3 roles after 18-24 months.
- Foundational skills transfer across any organization.
- High hiring demand (90,000+ SOC analyst positions in North America, 2024-2026 projections).

Expected responsibilities:
- Monitor SIEM alerts and investigate security events (daily, ~50-100 alerts).
- Validate true positives vs. false positives using case management systems.
- Escalate confirmed incidents to Tier 2 with clear documentation and pivots.
- Maintain alert ticket quality and SLA compliance (MTTD target: <30 min for high-risk alerts).
- Participate in on-call rotations (typically 1 week per month for Tier 1).

Entry-level compensation (2025 market rates):
- Salary: $55,000-$70,000 USD (varies by region and organization size).
- Benefits: Health insurance, 401(k), professional development allowance.
- Career progression: +$5,000-$8,000 per year with promotions to Tier 2/3.

---

##### Part 2: Skills Baseline Assessment

**Current Skills Inventory:**

| Skill Category | Proficiency | Requirement | Gap | Priority |
|---|---|---|---|---|
| Networking (TCP/IP, DNS, HTTP/HTTPS) | Beginner | Intermediate | High | Critical |
| Linux (command line, file systems, logs) | Beginner | Intermediate | High | Critical |
| Windows OS (Event Finder, Registry, services) | Beginner | Intermediate | High | Critical |
| SIEM (Splunk, ELK, ArcSight querying) | None | Intermediate | Very High | Critical |
| Log analysis (parsing, pattern matching) | Beginner | Intermediate | High | Critical |
| Incident triage workflow | None | Intermediate | Very High | Critical |
| Documentation & communication | Intermediate | Intermediate | Low | Supporting |
| Python/scripting for automation | Beginner | Advanced | Moderate | Supporting |

**Understanding:**
- The role demands working fluency in systems and tools, not just book knowledge.
- Most gaps exist in applied tool usage (SIEM, alert systems), not theoretical networking.
- Time-to-productivity = 4-6 weeks; gaps close quickly with hands-on lab repetition.

---

##### Part 3: Certification Roadmap

**Short-term Target (3-6 months): Cisco Certified CyberOps Associate**
- Aligned directly: Module 2 material covers SOC operations extensively.
- Exam format: 120 questions, 90 minutes, focuses on alert analysis and incident response.
- Cost: ~$330 exam fee + $50-200 study materials.
- Preparation investment: 80-120 hours of self-study.
- Study method: Official Cisco courseware + hands-on labs + practice exams.
- Timeline:
  - Month 1: Foundational theory (SIEM, SOC roles, alerts).
  - Month 2: Hands-on labs (alert tuning, investigation techniques).
  - Month 3: Practice exams and weak-area drills.
  - End of Month 3: Certification exam attempt.

**Medium-term Target (6-12 months): CompTIA CySA+ (Certified Security Analyst)**
- Broader vendor-neutral credential.
- Exam format: 165 questions, 165 minutes; covers threat analysis, security tools, incident response.
- Cost: ~$370 exam fee.
- Prerequisites: CompTIA Security+ recommended (or 4+ years IT experience).
- Value: Opens doors to threat hunting, security analysis, and consulting roles.
- Timing: Begin after CyberOps Associate is passed (month 4-6 onward).

**Long-term Aspiration (12-24 months): Certified Incident Handler (ECIH) or GIAC Security Essentials (GSEC)**
- Positions you for Tier 2-3 roles or specialized analyst positions.
- Both recognized industry-wide; GIAC is slightly higher authority.

**Certification Strategy:**
- Start with CyberOps Associate: highest alignment to current module content.
- Space certifications: pursue one at a time to avoid burnout.
- Use exam passes as milestones; don't over-certify early (employers value job experience more after first cert).

---

##### Part 4: Project Evidence (Portfolio Labs)

**Goal:** Build 3 defensible portfolio projects demonstrating hands-on alert investigation, log analysis, and incident response.

**Lab 1: SIEM Alert Triage & Investigation**
- **Scenario:** You receive a SIEM alert: "Suspicious outbound connection to known malware C2 domain."
- **Objective:** Investigate the alert using SIEM query logs and determine if it is a true positive.
- **Deliverable:**
  - SIEM query used to investigate (e.g., Splunk SPL or ELK JSON query).
  - Log excerpts showing evidence (process, IP, port, time).
  - Triage decision: True Positive / False Positive / Require Escalation.
  - Ticket summary (100-150 words, written for handoff to Tier 2).
- **Skills demonstrated:** Log parsing, tool fluency, clear technical writing.
- **Repository:** GitHub lab-evidence/siem-alert-triage/ (public).

**Lab 2: Windows Event Log Analysis**
- **Scenario:** A user reports potential credential compromise; analyze Windows Event Logs to confirm or deny.
- **Objective:** Extract and analyze event log entries (failed logins, privilege escalation, lateral movement indicators).
- **Deliverable:**
  - Event log data (PNG or CSV export showing relevant events).
  - Timeline of suspicious activity with timestamps.
  - Hypothesis: What likely occurred? (e.g., brute-force attack, credential reuse, pass-the-hash).
  - Recommended actions: Reset password, check for lateral movement, etc.
- **Skills demonstrated:** Windows internals, forensic thinking, threat hunting mindset.
- **Repository:** GitHub lab-evidence/windows-event-analysis/.

**Lab 3: Incident Response Playbook & Mock Incident**
- **Scenario:** Simulate a ransomware incident; you are the first responder (Tier 1).
- **Objective:** Follow incident response playbook steps: detect, contain, investigate, and document.
- **Deliverable:**
  - Written playbook (1-2 pages) covering roles, escalation steps, and remediation actions.
  - Incident response report (mock scenario): What did you find? How did you respond?
  - Evidence log: Timestamps, actions taken, teams notified.
- **Skills demonstrated:** Process discipline, communication, under-pressure decision-making.
- **Repository:** GitHub lab-evidence/incident-response-playbook/.

**Portfolio Quality Metrics:**
- Each lab should take 3-5 hours to complete thoroughly.
- Code/queries should be commented and explained.
- Summaries should be readable by non-security IT staff (avoid jargon overload).
- Host all on GitHub with a README explaining your reasoning and learning.

---

##### Part 5: 90-Day Roadmap to Tier 1 Ready

**Phase 1 (Days 1-30): Foundation & Tool Familiarization**

| Week | Goal | Specific Tasks | Measurable Outcome |
|---|---|---|---|
| 1 | Linux essentials | 20 command-line drills (ls, grep, awk, sed); practice on 2 small labs | Can navigate, search, and parse files in Linux without reference |
| 2 | Networking foundations | TCP/IP deep-dive (3-part course); build DNS/HTTP packet identification habit | Can identify protocol types in packet captures; understand DNS/HTTP flows |
| 3 | SIEM basics | Splunk or ELK intro (YouTube + Cisco courseware); set up local instance | Can write 5 basic queries; understand index, source, sourcetype |
| 4 | Alert architecture | Diagram simple alert rule (if-then logic); map alert to detection logic | Can explain why an alert fires and identify false positives |

**Phase 2 (Days 31-60): Skill Deepening & Lab 1**

| Week | Goal | Specific Tasks | Measurable Outcome |
|---|---|---|---|
| 5 | Log analysis techniques | Analyze 10 real-world log samples; practice field extraction | Can extract key fields from raw logs; identify anomalies |
| 6 | SIEM advanced queries | Write 10 complex Splunk SPL or KQL queries; test against sample data | Queries run error-free; return meaningful results for investigations |
| 7 | **Incident triage workflow** | Study 5 sample tickets; triage them using decision tree; write escalations | Your triage decisions match SOC analyst expectations; clear tickets |
| 8 | **Lab 1 execution** | Complete SIEM Alert Triage lab; publish to GitHub with writeup | Lab on GitHub with working query, evidence, and clear documentation |

**Phase 3 (Days 61-90): Specialization & Certification Push**

| Week | Goal | Specific Tasks | Measurable Outcome |
|---|---|---|---|
| 9 | Windows forensics & log parsing | Study Windows Event Log structure; analyze 5 compromise scenarios | Can read Event Logs; identify failed logins, privilege escalation, lateral movement |
| 10 | **Lab 2 execution** | Complete Windows Event Log Analysis lab; submit to GitHub | Lab 2 on GitHub with timeline, hypothesis, and recommended actions |
| 11 | Playbook development & mock incident | Draft incident response playbook; run through mock ransomware scenario | **Lab 3** complete; playbook documented; mock incident report clear |
| 12 | Cisco CyberOps Associate final prep | Take 3 full-length practice exams; review weak areas | Score >80% on practice exams; ready to sit for certification |

**Checkpoint Outcomes (End of 90 Days):**
- ✅ All 3 portfolio labs published and documented on GitHub.
- ✅ Cisco CyberOps Associate certification exam passed (or scheduled within 2 weeks).
- ✅ SIEM fluency: Can write intermediate queries; troubleshoot basic rule issues.
- ✅ Incident response mindset: Triage alerts using decision logic; escalate with clarity.
- ✅ Ready for Tier 1 alert analyst role interviews.

---

##### Part 6: Reflection & Self-Assessment

**Which skills are strongest today?**

Currently strong:
- **Communication & documentation:** Able to write clear explanations; good foundation for ticket quality.
- **Problem-solving mindset:** Comfortable with ambiguity; can research unknown concepts.
- **Theoretical networking:** Understand TCP/IP model and protocol hierarchy from coursework.

Moderate foundation:
- Linux command line: Can navigate but lack speed and comfort with piping/scripting.
- Windows OS: Familiar with GUI; less familiar with registry, services, event logs.

**Which gaps are blocking job readiness?**

Critical blockers:
1. **SIEM tool fluency:** Cannot query SIEM independently; this is the #1 barrier to day-one productivity.
   - Solution: 4-6 weeks of hands-on Splunk/ELK labs (simulators or free instances).
2. **Incident triage workflow:** Lack muscle memory for decision-making (true positive vs. false positive, escalation judgment).
   - Solution: 10+ triage exercises using real-world alert samples; shadowing SOC analysts (if possible).
3. **Log analysis speed:** Slow at parsing and extracting evidence from raw logs.
   - Solution: 50+ log analysis drills; practice awk/grep patterns daily.

Moderate gaps:
- Windows internals (Event Log, Registry, Process Model): 2-3 weeks to bridge.
- Python scripting for automation: Not required for Tier 1 entry, but helps with efficiency; 4-6 weeks part-time.

**What is the next concrete step this week?**

**Action Plan for Week 1:**
1. **This week (Days 1-7):**
   - Monday: Download Splunk Free instance; complete quick-start tutorial (4 hours).
   - Tuesday-Wednesday: Linux command-line drills (grep, awk, sed) using HackTheBox or OverTheWire labs (8 hours).
   - Thursday: Set up GitHub repository; create 3 README files for planned labs (2 hours).
   - Friday-Saturday: Complete first Cisco CyberOps Associate module (networking foundations) + take quiz (6 hours).
   - Sunday: Reflection—which tool felt easiest? Which felt hardest? Plan week 2 accordingly.

2. **Big-picture next step (30 days):**
   - Commit to the 90-day roadmap above.
   - Schedule Cisco CyberOps Associate exam date (6-8 weeks from now).
   - Join a SOC analyst community or find a mentor (LinkedIn, SecurityStackExchange, local SANS meetup).

3. **Success metric for Month 1:**
   - Comfortable in Linux shell (>80% accuracy on 20 drills).
   - Written and executed 5 Splunk queries that return meaningful results.
   - Completed first Cisco module and scored 75%+ on quiz.

---

#### Lab Insights & Lessons

**Key Understanding from Completing This Lab:**

1. **Becoming a defender is a structured journey, not a leap.**
   - Tier 1 is not about expertise; it's about consistency, clear thinking, and documentation.
   - Most gaps close within 90 days of deliberate practice.

2. **The certification is validation, not preparation.**
   - Prioritize hands-on labs and real incident exposure over exam prep alone.
   - Certifications accelerate hiring by 2-4 weeks but don't replace projects.

3. **Portfolio matters more than degree.**
   - GitHub projects with clear writeups prove capability to hiring managers.
   - Employers hire analysts who can demonstrate alert triage, not just pass tests.

4. **SIEM and log analysis are learned by doing, not reading.**
   - Reading about Splunk queries teaches syntax; writing 50 queries teaches thinking.
   - Labs must be repetitive and progressively harder.

5. **Communication is a technical skill in SOC work.**
   - A Tier 1 analyst's job is often 50% investigation, 50% clear tickets for Tier 2.
   - Practice writing incident summaries as much as writing queries.

**How Defenders Develop:**
- Week 1-2: Overwhelm (too many unknowns).
- Week 3-6: Consolidation (patterns emerge; queries get faster).
- Week 7-12: Confidence (you start predicting alert types; triage becomes intuitive).
- Month 4-6: Specialization (you know your environment; ready for role interview).

---

## 2.3 Fighters in the War Against Cybercrime Summary

### 2.3.1 What Did I Learn in this Module?
<img src="content%20folder/Screenshot%202026-04-01%20163513.png" alt="2.3.1 What Did I Learn in this Module" style="max-width: 100%; height: auto;" />

- A SOC succeeds when people, process, and technology are aligned.
- Tiered roles support efficient escalation and specialization.
- SIEM gives visibility; SOAR accelerates response.
- Metrics drive continuous improvement.
- Security must support, not paralyze, availability and business outcomes.
- Defender growth is a roadmap: certs + education + job-market intelligence + practical experience.
