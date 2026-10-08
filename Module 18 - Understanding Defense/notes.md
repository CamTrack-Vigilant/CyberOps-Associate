# Module 18: Understanding Defense - Study & Test Revision Guide

**Course:** Cisco Certified CyberOps Associate (CBROPS 200-201)  
**Curriculum Alignment:** Cisco Networking Academy (NetAcad) Module 18  
**Core Objective:** Master defense-in-depth principles, enterprise security policy structures, regulatory compliance mandates, SOC metrics, and disaster recovery architectures.

---

## 18.0 Introduction
Effective cybersecurity is not defined by buying a single expensive appliance; it is defined by a comprehensive, layered defensive strategy that combines people, processes, and technology. As a SOC analyst, understanding defense-in-depth and compliance frameworks ensures your monitoring aligns with organizational risk tolerance.

---

## 18.1 Defense-in-Depth (Layered Defense)

The principle of **Defense-in-Depth** dictates that multiple independent defensive layers must be breached before an adversary can access critical assets. If one defensive barrier fails, adjacent layers contain the threat.

```
                  ┌─────────────────────────────────────────┐
                  │ 1. PHYSICAL (Locks, CCTV, Mantraps)     │
                  │  ┌────────────────────────────────────┐ │
                  │  │ 2. PERIMETER (Firewalls, VPN, IPS) │ │
                  │  │  ┌───────────────────────────────┐ │ │
                  │  │  │ 3. NETWORK (VLANs, ACLs, 802.1X│ │ │
                  │  │  │  ┌──────────────────────────┐ │ │ │
                  │  │  │  │ 4. HOST (EDR, Patching, AV│ │ │ │
                  │  │  │  │  ┌─────────────────────┐ │ │ │ │
                  │  │  │  │  │ 5. APP (WAF, Input) │ │ │ │ │
                  │  │  │  │  │  ┌────────────────┐ │ │ │ │ │
                  │  │  │  │  │  │ 6. DATA (AES, │ │ │ │ │ │
                  │  │  │  │  │  │    DLP, Backups│ │ │ │ │ │
                  │  │  │  │  │  └────────────────┘ │ │ │ │ │
                  │  │  │  │  └─────────────────────┘ │ │ │ │
                  │  │  │  └──────────────────────────┘ │ │ │
                  │  │  └───────────────────────────────┘ │ │
                  │  └────────────────────────────────────┘ │
                  └─────────────────────────────────────────┘
```

* **Physical Security:** Guards, badge access readers, mantraps, biometrics, CCTV, secure data center racks.
* **Perimeter Defense:** Edge firewalls, DMZ segmentation, DDoS mitigation, Next-Gen IPS.
* **Internal Network:** 802.1Q VLAN micro-segmentation, switch port security, internal ACLs, 802.1X network admission.
* **Host Security:** Endpoint Detection & Response (EDR), Host-based Firewalls, OS hardening (disabling unused services), patch management.
* **Application Security:** Web Application Firewalls (WAF), secure code reviews, input validation, API security.
* **Data Security:** Cryptographic encryption (AES-256 at rest and in transit), Data Loss Prevention (DLP), access controls.

---

## 18.2 Security Policy Framework & Compliance

### 1. The Documentation Hierarchy
* **Policies:** High-level executive statements of management intent, mandatory rules, and organizational philosophy (e.g., *Information Security Policy*). Non-technical, approved by C-level executives.
* **Standards:** Mandatory, measurable requirements and technical baselines (e.g., *"All passwords must be at least 14 characters long and rotated every 90 days"*).
* **Guidelines:** Recommended best practices, suggestions, or non-mandatory guidance (e.g., *"Users should avoid using personal names in passwords"*).
* **Procedures:** Step-by-step instructions or Standard Operating Procedures (SOPs) detailing exactly how to execute a task (e.g., *SOP for provisioning a new user in Active Directory*).

### 2. Essential Security Policies
* **Acceptable Use Policy (AUP):** Defines what employees can and cannot do with company hardware, networks, and internet connections. Crucial legal protection for employer monitoring.
* **Incident Response Policy:** Defines severity levels, escalation chains, roles, and mandatory reporting timelines.

### 3. Major Regulatory Frameworks
* **NIST Cybersecurity Framework (CSF):** Five continuous functions: **Identify**, **Protect**, **Detect**, **Respond**, and **Recover**.
* **ISO/IEC 27001:** Premier international standard for establishing, implementing, and continually improving an **Information Security Management System (ISMS)**.
* **PCI-DSS (Payment Card Industry Data Security Standard):** Technical and operational mandates for organizations that store, process, or transmit payment cardholder data.
* **HIPAA:** US healthcare standard protecting Protected Health Information (PHI).
* **GDPR (General Data Protection Regulation):** European Union privacy regulation mandating data minimization, the "Right to be Forgotten", and mandatory 72-hour breach notifications.

---

## 18.3 SOC Operational Metrics & Alert Triage

| Metric / Term | Definition | Ideal Goal |
| :--- | :--- | :---: |
| **MTTD (Mean Time to Detect)** | Average time elapsed from initial adversary compromise to detection by SOC analysts. | Minimize (Minutes) |
| **MTTA (Mean Time to Acknowledge)**| Average time from alert generation until an analyst begins investigation. | Minimize |
| **MTTR (Mean Time to Respond/Remediate)**| Average time required to contain, eradicate, and restore operations after an alert is verified. | Minimize (Hours) |
| **Alert Fatigue** | Condition where analysts are overwhelmed by high volumes of alerts, causing genuine critical alerts to be missed. | Mitigate via tuning |

### The Alert Classification Matrix (High-Yield Test Topic)
* **True Positive (TP):** An alert fires, and an actual malicious attack is occurring. *(Correct detection)*
* **False Positive (FP):** An alert fires, but the activity is legitimate, benign business traffic. *(Nuisance/noise)*
* **True Negative (TN):** No alert fires, and no malicious attack is occurring. *(Normal operation)*
* **False Negative (FN):** No alert fires, but an attacker successfully compromises the network. *(Worst-case failure)*

---

## 18.4 Business Continuity (BCP) & Disaster Recovery (DRP)

* **Business Continuity Plan (BCP):** Long-term operational plan to keep critical business functions running during and immediately following a disaster.
* **Disaster Recovery Plan (DRP):** Technical plan focused on restoring specific IT infrastructure, servers, and data after an outage.
* **BIA (Business Impact Analysis):** Identifies critical business functions and assesses the financial/operational consequences of an outage.

### 1. Key Recovery Metrics
* **RTO (Recovery Time Objective):** The **maximum acceptable duration of downtime** that a system can be offline without catastrophic business loss.
* **RPO (Recovery Point Objective):** The **maximum acceptable data loss measured in time** (e.g., if backups occur every 4 hours, the RPO is 4 hours).

### 2. Recovery Backup Site Classifications
* **Hot Site:** A fully operational duplicate data center with real-time synchronized data, active hardware, and network links. Systems failover in **minutes to hours**. Highest cost.
* **Warm Site:** Pre-installed hardware, power, and connectivity present, but backups must be restored and software configured before going live. Recovery takes **days**. Moderate cost.
* **Cold Site:** An empty facility with power, cooling, and network jacks, but **no computing hardware**. Hardware must be ordered and installed. Recovery takes **weeks**. Lowest cost.

---

## 18.5 High-Yield Test & Exam Review (Trap Alerts)

1. **What is the worst-case scenario in alert classification?**
   * **False Negative (FN)**, where an attack occurs undetected.
2. **What is the difference between RTO and RPO?**
   * **RTO is about TIME (downtime duration)**; **RPO is about DATA (how much data loss in hours/minutes is tolerable)**.
3. **What backup site type has real-time data replication and ready-to-run hardware?**
   * **Hot Site.**
4. **Which NIST CSF function focuses on developing safeguards to ensure delivery of critical services?**
   * **Protect** function.
5. **What is an Acceptable Use Policy (AUP)?**
   * A policy that outlines authorized and prohibited activities for employees using organizational IT assets.
