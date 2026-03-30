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
<img src="Screenshot%202026-03-30%20225444.png" alt="2.0.2 What Will I Learn in this Module" style="max-width: 100%; height: auto;" />

Insight:
- This section sets direction: first understand the SOC mission, then understand how to become a defender.
- Think of it as: Mission first, career path second.

## 2.1 The Modern Security Operations Center

### 2.1.1 Elements of a SOC
<img src="Screenshot%202026-03-30%20225857.png" alt="2.1.1 Elements of a SOC" style="max-width: 100%; height: auto;" />

Insight:
- SOC effectiveness depends on a triangle: People, Process, Technology.
- If one side is weak, security outcomes drop.

How to remember:
- People decide.
- Process standardizes.
- Technology scales.

### 2.1.2 People in the SOC
<img src="Screenshot%202026-03-30%20230049.png" alt="2.1.2 People in the SOC" style="max-width: 100%; height: auto;" />

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
<img src="Screenshot%202026-03-30%20232916.png" alt="2.1.3 Process in the SOC" style="max-width: 100%; height: auto;" />

Insight:
- SOC work is a decision funnel: Alert -> Validate -> Escalate or Close.
- Most operational quality problems come from poor triage, not lack of alerts.

Practical mindset:
- False positives waste analyst time.
- Missed true positives increase attacker dwell time.
- Good tickets accelerate incident response downstream.

### 2.1.4 Technologies in the SOC - SIEM
<img src="Screenshot%202026-03-30%20233047.png" alt="2.1.4 Technologies in the SOC - SIEM" style="max-width: 100%; height: auto;" />

Insight:
- SIEM is the visibility engine of the SOC.
- It centralizes logs and events so analysts can correlate weak signals into strong evidence.

Why this matters:
- Without SIEM, detection is fragmented.
- With SIEM, analysts can ask better questions across multiple data sources.

### 2.1.5 Technologies in the SOC - SOAR
<img src="Screenshot%202026-03-30%20233513.png" alt="2.1.5 Technologies in the SOC - SOAR (Part 1)" style="max-width: 100%; height: auto;" />

<img src="Screenshot%202026-03-30%20233603.png" alt="2.1.5 Technologies in the SOC - SOAR (Part 2)" style="max-width: 100%; height: auto;" />

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
<img src="Screenshot%202026-03-30%20233740.png" alt="2.1.6 SOC Metrics" style="max-width: 100%; height: auto;" />

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
<img src="Screenshot%202026-03-30%20233902.png" alt="2.1.7 Enterprise and Managed Security" style="max-width: 100%; height: auto;" />

Insight:
- Organizations do not have to do everything in-house.
- Managed security services can extend capability, speed, and specialized expertise.

Decision tradeoff:
- In-house SOC offers direct control.
- Managed/outsourced SOC offers scale and external expertise.
- Many enterprises use a hybrid model.

### 2.1.8 DevSecOps
<img src="Screenshot%202026-03-30%20234009.png" alt="2.1.8 DevSecOps" style="max-width: 100%; height: auto;" />

Insight:
- DevSecOps shifts security left: security is built in early, not bolted on later.

Why it works:
- Early detection costs less to fix.
- Automated controls reduce human bottlenecks.
- Shared ownership improves collaboration among dev, ops, and security teams.

### 2.1.9 Security vs. Availability
<img src="Screenshot%202026-03-30%20234122.png" alt="2.1.9 Security vs. Availability" style="max-width: 100%; height: auto;" />

Insight:
- Security decisions are business decisions.
- The goal is not maximum lockdown; the goal is acceptable risk with reliable uptime.

Interpreting the "nines":
- More availability "nines" means much less allowable downtime.
- Higher availability usually needs more redundancy, cost, and engineering discipline.

Real-world principle:
- Strong security that blocks business operations is poor security design.
- Best practice is balanced control: protect critical assets while preserving service continuity.

## Module 2 Summary (What to Retain)
- A SOC succeeds when people, process, and technology are aligned.
- Tiered roles support efficient escalation and specialization.
- SIEM gives visibility; SOAR accelerates response.
- Metrics drive continuous improvement.
- Security must support, not paralyze, availability and business outcomes.
