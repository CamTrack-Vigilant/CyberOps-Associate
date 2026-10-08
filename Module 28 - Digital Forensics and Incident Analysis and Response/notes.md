# Module 28: Digital Forensics and Incident Analysis and Response

---

## 28.0 Introduction

### 28.0.1 Why Should I Take this Module?
You have learned all about the different attack vectors you may need to protect, tools and practices to protect your system with. In this final module, you will learn what to do when an attack actually happens.

### 28.0.2 What Will I Learn in this Module?
* **Module Title:** Incident Response Models
* **Module Objective:** Explain how the CyberOps Associate responds to cybersecurity incidents.

| Topic Title | Topic Objective |
| :--- | :--- |
| **Evidence Handling and Attack Attribution** | Explain the role of digital forensics processes. |
| **The Cyber Kill Chain** | Identify the steps in the Cyber Kill Chain. |
| **The Diamond Model of Intrusion Analysis** | Classify an intrusion event using the Diamond Model. |
| **Incident Response** | Apply the NIST 800-61r2 incident handling procedures to a given incident scenario. |

---

## 28.1 Evidence Handling and Attack Attribution

### 28.1.1 Digital Forensics
Now that you have investigated and identified valid alerts, what do you do with the evidence? The cybersecurity analyst will inevitably uncover evidence of criminal activity. In order to protect the organization and to prevent cybercrime, it is necessary to identify threat actors, report them to the appropriate authorities, and provide evidence to support prosecution. Tier 1 cybersecurity analysts are often the first to uncover wrongdoing. Cybersecurity analysts must know how to properly handle evidence and attribute it to threat actors.

**Digital forensics** is the recovery and investigation of information found on digital devices as it relates to criminal activity. **Indicators of compromise (IoCs)** are the evidence that a cybersecurity incident has occurred. This information could be:
* Data on storage devices
* Volatile computer memory (RAM)
* Traces of cybercrime preserved in network data, such as pcaps and logs

It is essential that all indicators of compromise be preserved for future analysis and attack attribution.

#### Internal vs. External Investigations
* **Private (Internal) Investigations:** Concerned with individuals inside the organization. These individuals could simply be behaving in ways that violate user agreements or other non-criminal conduct. When individuals are suspected of involvement in criminal activity involving the theft or destruction of intellectual property, an organization may choose to involve law enforcement authorities, in which case the investigation becomes public. Internal users could also have used the organization’s network to conduct other criminal activities that are unrelated to the organizational mission but are in violation of various legal statutes. In this case, public officials will carry out the investigation.
* **External Attacks & Regulatory Compliance:** When an external attacker has exploited a network and stolen or altered data, evidence needs to be gathered to document the scope of the exploit. Various regulatory bodies specify a range of actions that an organization must take when various types of data have been compromised. The results of forensic investigation can help to identify the actions that need to be taken.
  * *HIPAA Example:* Under US HIPAA regulations, if a data breach has occurred that involves patient information, notification of the breach must be made to the affected individuals. If the breach involves more than 500 individuals in a state or jurisdiction, the media, as well as the affected individuals, must be notified. Digital forensic investigation must be used to determine which individuals were affected, and to certify the number of affected individuals so that appropriate notification can be made in compliance with HIPAA regulations.
* **The Organization Under Investigation:** It is possible that the organization itself could be the subject of an investigation. Cybersecurity analysts may find themselves in direct contact with digital forensic evidence that details the conduct of members of the organization. Analysts must know the requirements regarding the preservation and handling of such evidence. Failure to do so could result in criminal penalties for the organization and even the cybersecurity analyst if the intention to destroy evidence is established.

---

### 28.1.2 The Digital Forensics Process
It is important that an organization develop well-documented processes and procedures for digital forensic analysis. Regulatory compliance may require this documentation, and this documentation may be inspected by authorities in the event of a public investigation.

**NIST Special Publication 800-86** (*Guide to Integrating Forensic Techniques into Incident Response*) is a valuable resource for organizations that require guidance in developing digital forensics plans. It recommends that forensics be performed using a four-phase process:

```
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│ 1. Collection   │ ───> │ 2. Examination  │ ───> │   3. Analysis   │ ───> │  4. Reporting   │
│    (Media)      │      │     (Data)      │      │  (Information)  │      │   (Evidence)    │
└─────────────────┘      └─────────────────┘      └─────────────────┘      └─────────────────┘
```

1. **Collection (Media):** Identification of potential sources of forensic data and acquisition, handling, and storage of that data. This stage is critical because special care must be taken not to damage, lose, or omit important data.
2. **Examination (Data):** Processing collected data to extract relevant digital artifacts and filter out routine/benign noise.
3. **Analysis (Information):** Correlating artifacts to deduce what happened, reconstruct the chronological incident timeline, and derive actionable conclusions.
4. **Reporting (Evidence):** Documenting findings, techniques, and conclusions into formal reports suitable for stakeholders, executive leadership, or legal proceedings.

---

### 28.1.4 Types of Evidence
In legal proceedings, evidence is broadly classified as either direct or indirect:
* **Direct evidence:** Evidence that was indisputably in the possession of the accused, or is eyewitness evidence from someone who directly observed criminal behavior.
* **Indirect evidence (Circumstantial evidence):** Evidence that, in combination with other facts, establishes a hypothesis. For example, evidence that an individual has committed similar crimes can support the assertion that the person committed the crime of which they are accused.

Evidence is further classified as:
* **Best evidence:** This is evidence that is in its original state. This evidence could be storage devices used by an accused, or archives of files that can be proven to be unaltered (e.g., verified bit-stream forensic disk images).
* **Corroborating evidence:** This is evidence that supports an assertion that is developed from best evidence (e.g., secondary server logs confirming an alert found on an endpoint drive).

---

### 28.1.6 Evidence Collection Order (RFC 3227)
**IETF RFC 3227** provides guidelines for the collection of digital evidence based on the volatility of the data. Data stored in RAM is the most volatile, and it will be lost when the device is turned off. In addition, important data in volatile memory could be overwritten by routine machine processes. Therefore, the collection of digital evidence should begin with the most volatile evidence and proceed to the least volatile:

```
▲ MOST VOLATILE (Disappears on reboot or power loss)
│  1. Memory registers, caches
│  2. Routing table, ARP cache, process table, kernel statistics, RAM
│  3. Temporary file systems
│  4. Non-volatile media, fixed and removable (Hard disks, SSDs, USBs)
│  5. Remote logging and monitoring data (Syslog, SIEM, NetFlow)
│  6. Physical interconnections and topologies (Cables, switch ports, network layout)
▼  7. Archival media, tape or other backups
LEAST VOLATILE (Persists indefinitely)
```

Details of the systems from which the evidence was collected, including who has access to those systems and at what level of permissions, should be recorded. Such details should include hardware and software configurations for the systems from which the data was obtained.

---

### 28.1.7 Chain of Custody
Although evidence may have been gathered from sources that support attribution to an accused individual, it can be argued that the evidence could have been altered or fabricated after it was collected. In order to counter this argument, a rigorous **chain of custody** must be defined and followed.

Chain of custody involves the collection, handling, and secure storage of evidence. Detailed records should be kept of the following:
* **Who** discovered and collected the evidence?
* **All details** about the handling of evidence including times, places, and personnel involved.
* **Who has primary responsibility** for the evidence, when responsibility was assigned, and when custody changed?
* **Who has physical access** to the evidence while it was stored? Access should be restricted to only the most essential personnel.

---

### 28.1.8 Data Integrity and Preservation
When collecting data, it is important that it is preserved in its original condition:
* **Preserving Timestamps:** Timestamping of files should be preserved. For this reason, the original evidence should be copied, and analysis should only be conducted on copies of the original. This is to avoid accidental loss or alteration of the evidence. Because timestamps may be part of the evidence, opening files from the original media should be avoided.
* **Bit-Level Copies:** The process used to create copies of the evidence that is used in the investigation should be recorded. Whenever possible, the copies should be direct bit-level copies of the original storage volumes. It should be possible to compare the archived disk image and the investigated disk image to identify whether the contents of the investigated disk have been tampered with. For this reason, it is important to archive and protect the original disk to keep it in its original, untampered condition.
* **Volatile Memory Preservation:** Volatile memory could contain forensic evidence, so special tools should be used to preserve that evidence before the device is shut down and evidence is lost. Users should **not** disconnect, unplug, or turn off infected machines unless explicitly told to do so by security personnel.

Following these processes will ensure that any evidence of wrongdoing will be preserved, and any indicators of compromise can be identified.

---

### 28.1.9 Attack Attribution
After the extent of the cyberattack has been assessed and evidence collected and preserved, incident response can move to identifying the source of the attack.
* **Threat Attribution Definition:** The act of determining the individual, organization, or nation responsible for a successful intrusion or attack incident.
* **Threat Actor Spectrum:** Ranges from disgruntled individuals, hackers, cybercriminals and criminal gangs, to nation states. Some criminals act from inside the network, while others can be on the other side of the world. Sophistication varies from highly trained nation-state units hiding their tracks to amateur threat actors bragging about exploits.
* **Systematic & Evidence-Based Investigation:** Identifying responsible threat actors should occur through the principled and systematic investigation of the evidence. While it may be useful to also speculate as to motivations, it is important **not** to let speculation bias the investigation (e.g., attributing an attack to a commercial competitor may lead investigators away from a nation-state actor).
* **Correlation of TTPs:** Incident response teams correlate **Tactics, Techniques, and Procedures (TTP)** used in the incident with other known exploits. Threat intelligence sources map TTPs to known sources. However, cybercrime evidence is seldom direct; identifying commonalities between TTPs is circumstantial evidence.
* **Attribution Artifacts:** Location of originating hosts/domains, malware code features, tools used, and specific techniques. At the national security level, threats sometimes cannot be openly attributed because doing so would expose sensitive defense methods and capabilities.
* **Internal Threats:** Asset management plays a major role. IP addresses, MAC addresses, DHCP logs, and **AAA (Authentication, Authorization, and Accounting) logs** are critical because they record who accessed what network resources at what time.

---

### 28.1.10 The MITRE ATT&CK Framework
One way to attribute an attack is to model threat actor behavior. The **MITRE Adversarial Tactics, Techniques & Common Knowledge (ATT&CK)** Framework enables the ability to detect attacker tactics, techniques, and procedures (TTP) as part of threat defense and attack attribution:
* **Tactics:** The technical goals that an attacker must accomplish in order to execute an attack (represented as matrix columns).
* **Techniques:** The means by which the tactics are accomplished (arranged beneath each tactic column).
* **Procedures:** The specific documented real-world actions taken by threat actors using identified techniques.

The MITRE ATT&CK Framework is a global knowledge base of threat actor behavior based on real-world exploits, describing the behavior of the attacker, not the attack itself. It enables automated information sharing via defined data structures between user communities and MITRE. Selecting a technique provides detailed procedures used by specific malware instances alongside definitions, explanations, and examples.

---

## 28.2 The Cyber Kill Chain

Developed by **Lockheed Martin**, the Cyber Kill Chain is a framework designed to identify, understand, and prevent cyber intrusions by breaking down an attack into seven distinct, sequential stages. The defensive goal is to detect and disrupt the threat actor as early as possible—**if the chain is broken at any point, the attack fails**, preventing damage and limiting what the adversary learns about the environment.

```
[ Reconnaissance ] ──> [ Weaponization ] ──> [ Delivery ] ──> [ Exploitation ]
                                                                     │
[ Actions on Objectives ] <── [ Command & Control (C2) ] <── [ Installation ]
```

### The 7 Steps of the Cyber Kill Chain

#### 1. Reconnaissance
* **Adversary Activity:** Researching the target, harvesting intelligence (emails, social media, public relations, network scans, open ports), and identifying exposed or neglected systems.
* **SOC Defense:** Analyzing web logs and browser analytics, monitoring for scanning/recon activity, and prioritizing defensive controls around high-value targeting.

#### 2. Weaponization
* **Adversary Activity:** Pairing an exploit targeting identified vulnerabilities with a payload/backdoor (often using automated weaponizers or zero-day exploits to evade detection).
* **SOC Defense:** Keeping IDS/IPS signatures current, analyzing malware artifacts, profiling weaponizer behaviors, and determining whether tools are custom or off-the-shelf.

#### 3. Delivery
* **Adversary Activity:** Transmitting the weaponized payload to the target environment via email attachments, phishing links, compromised websites, or infected USB drives.
* **SOC Defense:** Inspecting delivery vectors and infrastructure paths, filtering malicious email attachments, and logging web/mail traffic for forensic reconstruction.

#### 4. Exploitation
* **Adversary Activity:** Triggering the malicious code to exploit software, operating system, or human vulnerabilities to gain execution rights.
* **SOC Defense:** Security awareness training, regular penetration testing, endpoint hardening, vulnerability patching, and secure coding practices.

#### 5. Installation
* **Adversary Activity:** Establishing persistence within the environment (e.g., adding unauthorized services, registry Run keys, or installing web shells) so access survives reboots and routine cleanups.
* **SOC Defense:** Deploying Host-based Intrusion Prevention Systems (HIPS), monitoring for abnormal file creations or unauthorized privilege escalation, and auditing endpoint activity.

#### 6. Command and Control (CnC / C2)
* **Adversary Activity:** Opening a bi-directional communication channel back to the attacker’s infrastructure (commonly over HTTP/HTTPS, DNS, or IRC) to direct the compromised host.
* **SOC Defense:** Detecting anomalous outbound traffic or beaconing, sinkholing or blocking malicious domains (especially Dynamic DNS), and inspecting proxy/DNS logs. This represents the final window to block the adversary before they fulfill their core mission.

#### 7. Actions on Objectives
* **Adversary Activity:** Executing the primary goal of the operation, such as credential theft, lateral movement, data exfiltration, ransom extortion, data wiping, or unauthorized resource usage (e.g., botnets or cryptomining).
* **SOC Defense:** Rapid incident triage, packet capture analysis, lateral movement detection, establishing containment playbooks, and performing damage assessments.

---

## 28.3 The Diamond Model of Intrusion Analysis

### 28.3.1 Diamond Model Overview
The Diamond Model of Intrusion Analysis represents a security incident or event. In the Diamond Model, an **event** is a time-bound activity that is restricted to a specific step in which an adversary uses a capability over infrastructure to attack a victim to achieve a specific result.

```
                          [ ADVERSARY ]
                                ▲
                               │
               ┌───────────────┴───────────────┐
               │                               │
               ▼                               ▼
        [ CAPABILITY ]                   [ INFRASTRUCTURE ]
               │                               │
               └───────────────┬───────────────┘
                               │
                               ▼
                           [ VICTIM ]
```

#### The Four Core Features of an Intrusion Event
1. **Adversary:** The parties responsible for the intrusion.
2. **Capability:** A tool or technique that the adversary uses to attack the victim.
3. **Infrastructure:** The network path or paths that the adversaries use to establish and maintain command and control over their capabilities.
4. **Victim:** The target of the attack. However, a victim might be the target initially and then used as part of the infrastructure to launch other attacks.

*The model can be interpreted as: "The adversary uses the infrastructure to connect to the victim. The adversary develops capability to exploit the victim."* For example, a capability like malware might be used over email infrastructure by an adversary to exploit a victim.

#### The Six Meta-Features
* **Timestamp:** Indicates the start and stop time of an event; an integral part of grouping malicious activity.
* **Phase:** Analogous to steps in the Cyber Kill Chain; malicious activity includes two or more steps executed in succession to achieve the desired result.
* **Result:** Delineates what the adversary gained from the event (e.g., confidentiality compromised, integrity compromised, availability compromised).
* **Direction:** Indicates the direction of the event across the model (Adversary-to-Infrastructure, Infrastructure-to-Victim, Victim-to-Infrastructure, Infrastructure-to-Adversary).
* **Methodology:** Classifies the general type of event (e.g., port scan, phishing, content delivery attack, SYN flood).
* **Resources:** External resources used by the adversary (software, knowledge, stolen credentials, funds, facilities, hardware, network access).

---

### 28.3.2 Pivoting Across the Diamond Model
As a cybersecurity analyst, you may be called on to use the Diamond Model of Intrusion Analysis to diagram a series of intrusion events. The Diamond Model is ideal for illustrating how the adversary pivots from one event to the next.

**Example Scenario:** An employee reports abnormal computer behavior. A host scan reveals malware infection. Malware analysis discovers a list of Command and Control (CnC) domain names resolving to IP addresses. These IPs reveal the adversary and uncover firewall logs indicating additional infected victims.

#### Diamond Model Characterization of an Exploit Steps:
1. **Victim discovers malware** (Victim to Capability)
2. **Malware contains CnC domain** (Capability to Infrastructure)
3. **CnC Domain resolves to CnC IP address** (Infrastructure)
4. **Firewall logs reveal further victims contacting CnC IP address** (Infrastructure to Victim)
5. **IP address ownership details reveal adversary** (Infrastructure to Adversary)

---

### 28.3.3 The Diamond Model and the Cyber Kill Chain
Adversaries do not operate in a single event. Instead, events are threaded together in a chain in which each event must be successfully completed before the next event. This thread of events maps directly to the Cyber Kill Chain.

#### End-to-End Attack Thread Example (Gadgets, Inc. & Interesting Research Inc.)
*(Modification of the U.S. Department of Defense example from "The Diamond Model of Intrusion Analysis")*

1. Adversary conducts a web search for victim company **Gadgets, Inc.**, receiving as part of the results the domain name `gadgets.com`.
2. Adversary uses the newly discovered domain `gadgets.com` for a new search *"network administrator gadgets.com"* and discovers forum postings from users claiming to be network administrators of `gadgets.com`. The user profiles reveal their email addresses.
3. Adversary sends phishing emails with a Trojan horse attached to the network administrators of `gadgets.com`.
4. One network administrator (**NA1**) of `gadgets.com` opens the malicious attachment. This executes the enclosed exploit allowing for further code execution.
5. NA1’s compromised host sends an HTTP Post message to an IP address, registering it with a CnC controller. NA1’s compromised host receives an HTTP Response in return.
6. Reverse engineering reveals that the malware has additional IP addresses configured to act as backups if the first controller does not respond.
7. Through a CnC HTTP response message sent to NA1’s host, the malware begins to act as a web proxy for new TCP connections.
8. Through information from the proxy running on NA1’s host, the Adversary does a web search for *"most important research ever"* and finds Victim 2, **Interesting Research Inc.**
9. Adversary checks NA1’s email contact list for contacts from Interesting Research Inc. and discovers the contact for the **Chief Research Officer**.
10. Chief Research Officer of Interesting Research Inc. receives a spear-phish email from Gadget Inc.’s NA1 email address sent directly from NA1’s host with the same payload observed in Event 3.
11. **Outcome:** The adversary now has two compromised victims from which additional attacks can be launched (e.g., mining contacts for additional victims or setting up another proxy to exfiltrate all Chief Research Officer files).

---

## 28.4 Incident Response

### 28.4.1 Establishing an Incident Response Capability
Incident Response involves the methods, policies, and procedures used by an organization to respond to a cyberattack.
* **Aims:** Limit the impact of the attack, assess the damage caused, and implement recovery procedures.
* **NIST SP 800-61 Rev 2:** *Computer Security Incident Handling Guide* provides guidelines for incident handling, analyzing incident-related data, and determining appropriate response independent of hardware, OS, protocols, or applications. *(Covers four major exam topics for the Understanding Cisco Cybersecurity Operations Fundamentals exam).*
* **CSIRC:** The first step is establishing a **Computer Security Incident Response Capability (CSIRC)** through policies, plans, and procedures.

#### 1. Policy Elements
Details how incidents should be handled based on organizational mission, size, and function:
* Statement of management commitment
* Purpose and objectives of the policy
* Scope of the policy
* Definition of computer security incidents and related terms
* Organizational structure and definition of roles, responsibilities, and levels of authority
* Prioritization of severity ratings of incidents
* Performance measures
* Reporting and contact forms

#### 2. Plan Elements
Minimizes damage, incorporates lessons learned, and clarifies cross-departmental expectations:
* Mission
* Strategies and goals
* Senior management approval
* Organizational approach to incident response
* How the team communicates with the rest of the organization and external organizations
* Metrics for measuring incident response capacity
* How the program fits into the overall organization

#### 3. Procedure Elements (Standard Operating Procedures - SOPs)
SOPs minimize errors caused by personnel operating under high stress:
* Technical processes
* Using techniques
* Filling out forms
* Following checklists

---

### 28.4.3 Incident Response Stakeholders
* **Management:** Creates policy, designs budgets, staffs departments, coordinates with stakeholders, and minimizes business damage.
* **Information Assurance:** Implements changes such as firewall rule updates during containment or recovery.
* **IT Support:** Understands the organization's technology infrastructure deeply, performs actions to mitigate attack impact, and assists in evidence preservation.
* **Legal Department:** Reviews policies and procedures against local/federal guidelines; handles prosecution, evidence collection legality, and lawsuits.
* **Public Affairs and Media Relations:** Handles notifications to the media and the public when personal data is compromised.
* **Human Resources (HR):** Coordinates disciplinary actions if an internal employee causes an incident.
* **Business Continuity Planners:** Assesses security incident impacts on operational continuity, adjusting risk assessments and recovery plans.
* **Physical Security and Facilities Management:** Involved in physical attacks (tailgating, shoulder surfing) and secures physical facilities housing forensic evidence.

#### The Cybersecurity Maturity Model Certification (CMMC)
Created to assess the ability of organizations performing functions for the U.S. Department of Defense (DoD) to protect the military supply chain from disruptions or losses. CMMC specifies 17 domains rated by maturity levels. The **Incident Response** domain has four maturity levels (Levels 2 to 5):
* **Level 2:** Establish an incident response plan following the NIST process. Detect, report, and prioritize events. Respond following predefined procedures. Analyze incident causes to mitigate future issues.
* **Level 3:** Document and report incidents to stakeholders identified in the response plan. Test the incident response capability.
* **Level 4:** Use knowledge of attacker TTPs to refine incident response planning and execution. Establish a Security Operations Center (SOC) facilitating a 24/7 response capability.
* **Level 5:** Utilize accepted and systematic computer forensic data gathering techniques including secure handling and storage. Develop and utilize manual and automated real-time responses to potential incidents following known patterns.

---

### 28.4.4 NIST Incident Response Life Cycle
NIST SP 800-61r2 defines four phases in the incident response process life cycle:

```
┌─────────────────────────────────────────────────────────────┐
│                       1. PREPARATION                        │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                  2. DETECTION AND ANALYSIS                  │
└──────────────────────────────┬──────────────────────────────┘
                               │ ▲
                 Feedback Loop │ │
                               ▼ │
┌─────────────────────────────────────────────────────────────┐
│           3. CONTAINMENT, ERADICATION, AND RECOVERY         │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                 4. POST-INCIDENT ACTIVITIES                 │
└─────────────────────────────────────────────────────────────┘
```

The incident response life cycle is a **self-reinforcing learning process** whereby each incident informs and improves future handling.

---

### 28.4.5 Preparation
The preparation phase is when the CSIRT is created, trained, and equipped:
* **Communication processes:** Contact info for stakeholders, external CSIRTs, law enforcement, issue tracking systems, smartphones, encryption software.
* **Facilities:** Hosting facilities for the response team and the SOC.
* **Hardware & Software:** Forensic software, spare computers, servers, network devices, backup systems, packet sniffers, protocol analyzers.
* **Controls & Hardening:** Risk assessments to implement controls limiting incidents; validation of security deployments on endpoints and network devices; security awareness training.
* **Incident Analysis Resources:** Critical asset lists, network diagrams, port lists, hashes of critical files, baseline readings of normal activity, clean OS and application images for system recovery.
* **The Jump Kit:** A portable emergency kit containing a pre-configured laptop with forensic software, backup media, cabling, and response tools. Inspected regularly to install updates and practiced with the CSIRT.

---

### 28.4.6 Detection and Analysis
Because incidents take countless forms, instructions cannot cover every permutation. Organizations prepare by focusing on the most common attack vectors:
* **Web:** Attacks initiated from a website or web-hosted application.
* **Email:** Attacks initiated from an email message or attachment.
* **Loss or Theft:** Lost or stolen equipment (laptops, phones) providing attack information.
* **Impersonation:** Replacing something or someone for malicious intent (spoofing, rogue devices).
* **Attrition:** Attacks using brute force against devices, networks, or services (DoS/DDoS, brute-force logins).
* **Media:** Attacks initiated from external storage or removable media (USB drives).

---

### 28.4.7 Containment, Eradication, and Recovery
Once an incident is validated, it must be contained before widespread damage occurs. Predefined strategies determine the response:

#### Containment Strategy Evaluation Criteria:
1. How long will it take to implement and complete a solution?
2. How much time and how many resources are needed?
3. What is the process to preserve evidence?
4. Can the attacker be redirected to a sandbox to safely document their methodology?
5. What is the impact on service availability?
6. What is the extent of damage to resources or assets?
7. How effective is the strategy?

> **Caution Regarding Network Disconnection:**
> During containment, additional damage may be incurred. For example, it is **not always advisable to unplug the compromised host from the network**. Malicious processes may detect disconnection from the CnC controller and automatically trigger a data wiper or drive encryption bomb on the target.

---

### 28.4.8 Post-Incident Activities (Lessons Learned)
After threats are eradicated and recovery is underway, a "lessons learned" meeting is held to review handling effectiveness and harden existing security controls.

#### The 10 Lessons Learned Review Questions:
1. Exactly what happened, and when?
2. How well did the staff and management perform while dealing with the incident?
3. Were the documented procedures followed? Were they adequate?
4. What information was needed sooner?
5. Were any steps or actions taken that might have inhibited recovery?
6. What would staff and management do differently next time?
7. How could information sharing with other organizations be improved?
8. What corrective actions can prevent similar incidents in the future?
9. What precursors or indicators should be watched for in the future?
10. What additional tools or resources are needed to detect, analyze, and mitigate future incidents?

---

### 28.4.9 Incident Data Collection and Retention
Data collected during post-incident reviews is used to calculate incident costs, assess CSIRT effectiveness, and identify system weaknesses:
* **Incident Metrics:** A higher number of incidents handled may indicate flawed methodology or CSIRT incompetence, while a lower number could reflect improved security or a failure in detection. Breaking counts down by specific incident types targets where weaknesses reside.
* **Time Metrics:** Tracking total labor hours, duration of each response phase, time to initial response, and escalation speed.

#### Objective Assessment Activities (NIST SP 800-61):
* Reviewing logs, forms, reports, and documentation for adherence to policies and procedures.
* Identifying which precursors and indicators were recorded to determine logging effectiveness.
* Determining whether damage occurred before detection.
* Determining if the actual cause was identified (vector, vulnerability, victim characteristics).
* Determining if the incident is a recurrence of a previous incident.
* Calculating estimated monetary damages.
* Measuring the delta between initial and final impact assessments.
* Identifying measures that could have prevented the incident.

#### Subjective Assessment:
Team members assess their own performance and peer performance. Input is gathered from resource owners to evaluate satisfaction and efficiency.

#### Evidence Retention Factors:
* **Prosecution:** When prosecuting an attacker, retain evidence until all legal proceedings conclude (months to years). Legal policies may mandate evidence involved in litigation is never destroyed.
* **Data Type:** Policies define retention by data category (e.g., standard email/chat for 90 days; incident response evidence for 3 years or more).
* **Cost:** Long-term storage of physical drives and functional legacy hardware can become expensive.

---

### 28.4.10 Reporting Requirements and Information Sharing
* **Regulatory Reporting:** Legal counsel determines specific reporting responsibilities under government regulations. Management decides communication with customers, partners, and the public.
* **Information Sharing:** NIST recommends coordinating with external bodies and databases, such as logging incidents in the **VERIS (Vocabulary for Event Recording and Incident Sharing)** community database.

#### NIST Critical Recommendations for Information Sharing:
1. **Plan incident coordination with external parties before incidents occur.**
2. **Consult with the legal department before initiating any coordination efforts.**
3. **Perform incident information sharing throughout the entire incident response life cycle.**
4. **Attempt to automate as much of the information sharing process as possible.**
5. **Balance the benefits of information sharing with the drawbacks of sharing sensitive information.**
