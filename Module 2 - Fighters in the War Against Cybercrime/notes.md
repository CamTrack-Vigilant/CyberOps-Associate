# Module 2 - Fighters in the War Against Cybercrime

## 2.0 Introduction

### 2.0.1 Why should I take this module?

If you are taking this course, you may be considering a career in CyberOps security. What technologies do you need to be aware of? What types of jobs are available? Where can you find those jobs? This module helps answer those questions.

### 2.0.2 What Will I Learn in this Module?

<img src="Screenshot%202026-03-30%20225444.png" alt="2.0.2 What Will I Learn in this Module" style="max-width: 100%; height: auto;" />

- Module Title: Fighters in the War Against Cybercrime
- Module Objective: Explain how to prepare for a career in cybersecurity operations.

| Topic Title | Topic Objective |
|---|---|
| The Modern SOC | Explain the mission of the security operations center (SOC). |
| Becoming a Defender | Describe resources available to prepare for a career in cybersecurity operations. |

## 2.1 The Modern Security Operations Center

### 2.1.1 Elements of a SOC

<img src="Screenshot%202026-03-30%20225857.png" alt="2.1.1 Elements of a SOC" style="max-width: 100%; height: auto;" />

Defending against today's threats requires a formalized, structured, and disciplined approach. Organizations typically use the services of professionals in a Security Operations Center (SOC). SOCs provide a broad range of services, from monitoring and management to comprehensive threat solutions and hosted security that can be customized to meet customer needs. SOCs can be wholly in-house, owned and operated by a business, or elements of a SOC can be contracted out to security vendors.

As illustrated, the major elements of a SOC are:

- People
- Processes
- Technologies

### 2.1.2 People in the SOC

<img src="Screenshot%202026-03-30%20230049.png" alt="2.1.2 People in the SOC" style="max-width: 100%; height: auto;" />

Job roles in a SOC are rapidly evolving. Traditionally, SOCs assign job roles by tiers, according to the expertise and responsibilities required for each. First-tier jobs are more entry level, while third-tier jobs require extensive expertise.

- Tier 1 Alert Analyst: Monitors incoming alerts, verifies that a true incident has occurred, and forwards tickets to Tier 2 if necessary.
- Tier 2 Incident Responder: Performs deep investigation of incidents and advises remediation or action to be taken.
- Tier 3 Threat Hunter: Has expert-level skill in network, endpoint, threat intelligence, and malware reverse engineering. Traces malware behavior and impact, supports removal efforts, hunts for undetected threats, and implements threat detection tools.
- SOC Manager: Manages SOC resources and serves as the point of contact for the larger organization or customer.

This course offers preparation for a certification suitable for the position of Tier 1 Alert Analyst, also known as Cybersecurity Analyst or CyberOps Associate.

### 2.1.3 Process in the SOC

<img src="Screenshot%202026-03-30%20232916.png" alt="2.1.3 Process in the SOC" style="max-width: 100%; height: auto;" />

The day of a Cybersecurity Analyst typically begins with monitoring security alert queues. A ticketing system is frequently used to assign alerts to a queue for analysts to investigate. Because alert-generating software can trigger false alarms, one job of the Cybersecurity Analyst is to verify that an alert represents a true security incident. When verification is established, the incident can be forwarded to investigators or other security personnel to be acted upon. Otherwise, the alert may be dismissed as a false alarm.

If a ticket cannot be resolved, the Cybersecurity Analyst forwards it to a Tier 2 Incident Responder for deeper investigation and remediation. If the Incident Responder cannot resolve the ticket, it is forwarded to Tier 3 personnel with in-depth knowledge and threat-hunting skills.

Typical tier responsibilities:

- Tier 1: Monitors incidents, opens tickets, and performs basic threat mitigation.
- Tier 2: Deep investigation and remediation guidance.
- Tier 3: In-depth knowledge, threat hunting, and preventive measures.

### 2.1.4 Technologies in the SOC - SIEM

<img src="Screenshot%202026-03-30%20233047.png" alt="2.1.4 Technologies in the SOC - SIEM" style="max-width: 100%; height: auto;" />

A SOC needs a security information and event management system (SIEM), or its equivalent. SIEM makes sense of all the data that firewalls, network appliances, intrusion detection systems, and other devices generate.

SIEM systems are used for collecting and filtering data, detecting and classifying threats, and analyzing and investigating threats. SIEM systems may also help manage resources to implement preventive measures and address future threats.

SOC technologies can include one or more of the following:

- Event collection, correlation, and analysis
- Security monitoring
- Security control
- Log management
- Vulnerability assessment
- Vulnerability tracking
- Threat intelligence

### 2.1.5 Technologies in the SOC - SOAR

<img src="Screenshot%202026-03-30%20233513.png" alt="2.1.5 Technologies in the SOC - SOAR (Part 1)" style="max-width: 100%; height: auto;" />

<img src="Screenshot%202026-03-30%20233603.png" alt="2.1.5 Technologies in the SOC - SOAR (Part 2)" style="max-width: 100%; height: auto;" />

SIEM and security orchestration, automation, and response (SOAR) are often paired together because their capabilities complement each other.

Large security operations (SecOps) teams use both technologies to optimize their SOC.

SOAR platforms are similar to SIEMs in that they aggregate, correlate, and analyze alerts. SOAR goes a step further by integrating threat intelligence and automating incident investigation and response workflows based on playbooks developed by the security team.

SOAR components:

- Security
- Orchestration: Creates a customized platform that integrates and coordinates numerous security tools and resources.
- Automation: Executes security processes with minimal human intervention, helping address analyst shortages and increasing efficiency.
- Response: Prescribes and executes procedures to follow in response to security events, including rule-based runbooks for specific event types.

SOAR security platforms typically:

- Gather alarm data from each component of the system.
- Provide tools that enable cases to be researched, assessed, and investigated.
- Emphasize integration to automate complex incident response workflows for faster and more adaptive defense.
- Include pre-defined playbooks that enable automatic responses to specific threats, either initiated by rules or triggered by security personnel.

SOAR emphasizes integration and automation of SOC workflows. It orchestrates many manual processes (such as alert investigation), requiring human intervention only when necessary. This allows security personnel to focus on higher-value investigations and threat remediation.

SIEM systems often produce more alerts than SecOps teams can realistically investigate. SOAR can process many of these alerts automatically and enable personnel to focus on more complex and potentially damaging exploits.

### 2.1.6 SOC Metrics

<img src="Screenshot%202026-03-30%20233740.png" alt="2.1.6 SOC Metrics" style="max-width: 100%; height: auto;" />

A SOC is critically important to the security of an organization. Whether the SOC is internal or provides services to multiple organizations, it is important to understand how well the SOC is functioning so improvements can be made to people, processes, and technologies.

Many metrics, or key performance indicators (KPIs), can measure specific aspects of SOC performance. Common SOC metrics include:

- Dwell Time: The length of time threat actors have access to a network before detection and containment.
- Mean Time to Detect (MTTD): The average time for SOC personnel to identify that valid security incidents have occurred.
- Mean Time to Respond (MTTR): The average time to stop and remediate a security incident.
- Mean Time to Contain (MTTC): The time required to stop an incident from causing further damage to systems or data.
- Time to Control: The time required to stop malware spread in the network.

### 2.1.7 Enterprise and Managed Security

<img src="Screenshot%202026-03-30%20233902.png" alt="2.1.7 Enterprise and Managed Security" style="max-width: 100%; height: auto;" />

For medium and large networks, organizations benefit from implementing an enterprise-level SOC. The SOC can be fully in-house. However, many large organizations outsource at least part of SOC operations to security solutions providers.

Cisco offers incident response, preparedness, and management capabilities including:

- Cisco Smart Net Total Care Service for Rapid Problem Resolution
- Cisco Product Security Incident Response Team (PSIRT)
- Cisco Computer Security Incident Response Team (CSIRT)
- Cisco Managed Services
- Cisco Tactical Operations (TacOps)
- Cisco's Safety and Physical Security Program

### 2.1.8 DevSecOps

<img src="Screenshot%202026-03-30%20234009.png" alt="2.1.8 DevSecOps" style="max-width: 100%; height: auto;" />

DevSecOps stands for Development, Security, and Operations. It integrates security into the DevOps process, with the goal of making security an integral part of the software development lifecycle rather than something added at the end. By incorporating security from the beginning, DevSecOps aims to reduce vulnerabilities and improve the overall security of applications, systems, and environments.

DevSecOps provides:

- Faster Remediation: Security issues are identified early, reducing the time and cost to fix them.
- Reduced Risk: Continuous security checks minimize the chance of vulnerabilities reaching production.
- Increased Efficiency: Automating security tasks allows teams to focus on core responsibilities while security is consistently addressed.
- Improved Collaboration: Security is a shared responsibility, improving communication and teamwork between development, security, and operations teams.

DevSecOps promotes a culture where security is everyone's responsibility and is woven into every part of the development lifecycle.

### 2.1.9 Security vs. Availability

<img src="Screenshot%202026-03-30%20234122.png" alt="2.1.9 Security vs. Availability" style="max-width: 100%; height: auto;" />

Most enterprise networks must be up and running at all times. Security personnel understand that for an organization to accomplish its priorities, network availability must be preserved.

Each business or industry has a limited tolerance for network downtime. That tolerance is usually based on comparing downtime cost against the cost of protection. In a small retail business with one location, it may be acceptable to have a router as a single point of failure. However, if a large portion of sales is online, the owner may choose redundancy to ensure continuous availability.

Preferred uptime is often measured by annual downtime:

| Availability % | Downtime |
|---|---|
| 99.8% | 17.52 hours |
| 99.9% (three nines) | 8.76 hours |
| 99.99% (four nines) | 52.56 minutes |
| 99.999% (five nines) | 5.256 minutes |
| 99.9999% (six nines) | 31.56 seconds |
| 99.99999% (seven nines) | 3.16 seconds |

Security cannot be so strict that it interferes with business needs. In practice, it is always a tradeoff between strong security and efficient business operations.
