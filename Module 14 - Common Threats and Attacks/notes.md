# Module 14: Common Threats and Attacks - Study & Test Revision Guide

**Course:** Cisco Certified CyberOps Associate (CBROPS 200-201)  
**Curriculum Alignment:** Cisco Networking Academy (NetAcad) Module 14  
**Core Objective:** Master the taxonomy of malware, execution mechanics of network access/DoS attacks, and psychological vectors of social engineering.

---

## 14.0 Introduction
Attacks exploit vulnerabilities in hardware, software, network protocols, or human behavior. Understanding the mechanics of malware self-propagation and social engineering allows SOC analysts to quickly classify incidents and select appropriate containment playbooks.

---

## 14.1 Malware Classifications & Propagation

### 1. Viruses vs. Worms vs. Trojans (Crucial Test Distinction)
| Malware Type | Requires Host File? | Requires Human Execution? | Self-Propagating over Network? | Primary Characteristic |
| :--- | :---: | :---: | :---: | :--- |
| **Virus** | **Yes** (attaches to `.exe`, `.docx`) | **Yes** (user must open/run file) | No | Modifies other computer programs by inserting its own malicious code. |
| **Worm** | **No** (standalone binary) | **No** (exploits system vulnerabilities autonomously) | **Yes** (rapidly replicates across subnets) | Consumes network bandwidth; exploits remote network bugs (e.g., WannaCry using MS17-010 EternalBlue). |
| **Trojan Horse**| Standalone or bundled | **Yes** (user installs thinking it is benign) | No | Masquerades as legitimate software (e.g., free game, PDF reader) while executing hidden payload. |

### 2. Specialized Malware Taxonomy
* **Ransomware:** Encrypts user files or locks operating systems using asymmetric/symmetric cryptography, demanding payment in cryptocurrency for the decryption key.
* **Rootkit:** Infiltrates the operating system at the kernel level (Ring 0). Hides malicious processes, network sockets, and files from standard operating system APIs and Task Manager.
* **Spyware / Keylogger:** Passively logs keystrokes, clipboard contents, and web browsing habits, transmitting exfiltrated credentials to a remote server.
* **Adware:** Delivers unwanted, aggressive advertising; often bundled with freeware.
* **Logic Bomb:** Dormant code embedded within an application that detonates only when specific conditions are met (e.g., a specific date, or if a specific user account is deleted from Active Directory).
* **Backdoor:** Bypasses normal authentication mechanisms to maintain persistent remote access.

---

## 14.2 Network Attack Classifications

Network intrusions fall into three primary categories:

### 1. Reconnaissance Attacks
The discovery and mapping of systems, services, and vulnerabilities prior to exploitation.
* *Passive Reconnaissance:* Gathering intelligence without directly touching target infrastructure (OSINT, Whois, LinkedIn employee profiling, DNS lookups).
* *Active Reconnaissance:* Directly probing target ports and services (Ping sweeps, Nmap port scanning).

### 2. Access Attacks
Unauthorized acquisition of user accounts, elevated privileges, or system control.
* **Password Attacks:** Brute-force, dictionary attacks, credential stuffing, password spraying.
* **Trust Exploitation:** Compromising an unprivileged machine that has a pre-existing trusted relationship with a high-value core server (e.g., compromising a jumpbox).
* **Port Redirection:** Using a compromised host as an intermediary pivot point to route traffic into an otherwise unreachable internal network segment.
* **Man-in-the-Middle (MitM):** Positioning the attacker between two communicating parties to intercept, modify, or replay traffic (e.g., via ARP poisoning or rogue Wi-Fi evil twins).
* **Buffer Overflow:** Sending data that exceeds the capacity of an application's allocated memory buffer, overwriting adjacent memory (return address pointer) to execute arbitrary shellcode.

### 3. Denial of Service (DoS and DDoS) Attacks
Preventing legitimate users from accessing services by exhausting network bandwidth, CPU, or memory.
* **Botnet:** A network of compromised internet-connected devices (zombies) controlled by a **Botmaster** via a **Command and Control (C2)** channel (IRC, HTTP/S, or peer-to-peer).

---

## 14.3 Denial of Service (DoS) Mechanics

### 1. TCP SYN Flood Attack
* Exploit mechanism: Abuses the **TCP 3-way handshake**.
* The attacker sends a rapid flood of `TCP SYN` packets with spoofed source IP addresses.
* The victim server responds with `SYN-ACK` and allocates memory to the **half-open connection queue** (SYN backlog).
* Because the source IP is fake, the final `ACK` is never received. The server's connection table fills completely, rejecting legitimate incoming client connections.

### 2. Smurf Attack (ICMP Amplification)
* The attacker sends an **ICMP Echo Request (ping)** to the **directed broadcast address** of a third-party intermediary network.
* The attacker **spoofs the source IP address** to be the victim's IP.
* Every single host on the intermediary network sends an ICMP Echo Reply back to the victim, overwhelming the victim's network link.

### 3. DNS / NTP Amplification (Reflection + Amplification)
* **Reflection:** Attacker sends requests with the spoofed source IP of the victim to open internet servers (open recursive DNS resolvers or NTP servers).
* **Amplification:** The attacker crafts small requests (e.g., 60-byte DNS query for `ANY .`) that trigger massive responses (3,000+ byte responses with DNSSEC records). The victim is bombarded with huge responses without the attacker generating large bandwidth.

---

## 14.4 Social Engineering Vectors

Attacks targeting the human vulnerability layer through psychological manipulation:

| Technique | Description | Key Indicator / Scenario |
| :--- | :--- | :--- |
| **Phishing** | Bulk, untargeted fraudulent emails sent to thousands of recipients. | Fake bank email: "Click here to verify your account." |
| **Spear Phishing** | Highly tailored, customized email targeting a specific individual or organization. | Email to HR referencing the specific company health plan. |
| **Whaling** | High-value spear-phishing targeting C-level executives (CEO, CFO). | Urgent email requesting emergency wire transfer authorization. |
| **Vishing** | Voice phishing over telephone/VoIP. | Caller pretending to be IT Helpdesk asking for VPN token. |
| **Smishing** | Phishing via SMS text messaging. | Text saying: "Your package delivery failed, click link." |
| **Pretexting** | Creating an invented scenario (pretext) to persuade the victim to release info. | Impersonating an auditor conducting a compliance review. |
| **Baiting** | Leaving physical infected media in places where victims will find it. | Dropping a USB labelled "Executive Salaries 2026" in the parking lot. |
| **Quid Pro Quo** | Offering a fake service or benefit in exchange for sensitive information. | Fake IT technician offering to "speed up your computer" if you give password. |
| **Shoulder Surfing**| Physically looking over someone's shoulder to steal credentials or PINs. | Watching an employee type their password at an ATM or laptop. |
| **Dumpster Diving** | Searching through corporate trash bins for sensitive printouts/documents. | Finding un-shredded customer invoices or password notes. |

---

## 14.5 High-Yield Test & Exam Review (Trap Alerts)

1. **What makes a worm fundamentally different from a virus?**
   * **A worm does NOT need a host file and does NOT require human intervention to propagate; it replicates autonomously across network vulnerabilities.**
2. **In a SYN flood attack, what state are connections left in?**
   * **Half-open state** (waiting for the client's final ACK that never comes).
3. **What is the difference between phishing and spear phishing?**
   * Phishing is broad and untargeted; spear phishing is customized for a specific target.
4. **How does a Smurf attack amplify traffic?**
   * By sending a spoofed ICMP request to a **directed broadcast address**, causing all devices on the network to reply to the victim.
5. **What type of malware installs at Ring 0 to hide its existence from the OS?**
   * **Rootkit.**
