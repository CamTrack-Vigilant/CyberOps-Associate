# Module 13: Attackers and Their Tools - Study & Test Revision Guide

**Course:** Cisco Certified CyberOps Associate (CBROPS 200-201)  
**Curriculum Alignment:** Cisco Networking Academy (NetAcad) Module 13  
**Core Objective:** Categorize threat actors by motive and capability, and understand the technical toolsets used to perform reconnaissance, scanning, cracking, and exploitation.

---

## 13.0 Introduction
To defend an enterprise network, a Tier 1 SOC analyst must think like an adversary. Threat actors range from unsophisticated amateurs looking for internet bragging rights to state-sponsored military units running multi-year cyber-espionage operations.

---

## 13.1 Threat Actor Categories & Motivations

### 1. The Hacker Spectrum
* **White Hat (Ethical Hackers):** Authorized security professionals who discover and report vulnerabilities through legal channels with written authorization.
* **Black Hat (Criminal Hackers):** Unauthorized malicious actors motivated by personal gain, financial theft, or operational disruption.
* **Gray Hat (Uninvited Hackers):** Individuals who find vulnerabilities without authorization, but report them to the vendor (sometimes demanding payment) without explicitly exploiting them for malice.

### 2. Threat Actor Profiles (High-Yield Test Matching)
| Threat Actor Profile | Primary Motivation | Technical Skill Level | Typical Tactics / Targets |
| :--- | :--- | :--- | :--- |
| **Script Kiddie** | Notoriety, ego, curiosity | Low (relies on pre-written tools/scripts) | Mass ping sweeps, basic DoS tools (LOIC), automated exploit scripts. |
| **Vulnerability Broker** | Financial gain | High (specialized vulnerability research) | Finds Zero-Day vulnerabilities and sells them to governments, defense contractors, or dark web markets. |
| **Hacktivist** | Political, ideological, or social causes | Low to Moderate | Website defacements, DDoS attacks (e.g., Anonymous), public data leaks of target corporations/governments. |
| **Cybercriminal** | Financial profit | Moderate to High | Ransomware-as-a-Service (RaaS), banking trojans, credit card harvesting, business email compromise (BEC). |
| **State-Sponsored APT (Advanced Persistent Threat)** | National defense, espionage, geopolitical power | Ultra-High (Military/Intelligence funding) | Highly targeted spear-phishing, custom zero-day exploits, long dwell times (months/years undetected), critical infrastructure sabotage. |
| **Malicious Insider** | Revenge, financial kickback, grievance | Variable (already holds valid credentials) | Data exfiltration via authorized USB/cloud, privilege abuse, logic bombs before termination. |

---

## 13.2 Attacker Toolsets by Functional Category

Cisco CyberOps categorizes offensive tools into specific functional categories:

### 1. Packet Crafting & Sniffing Tools
* **Packet Sniffers:** Capture raw network frames passing over a network interface set to **promiscuous mode**.
  * *Tools:* **Wireshark**, **tcpdump**, **TShark**.
* **Packet Crafters:** Create custom packet headers and payloads to test firewall rule boundaries or forge packets.
  * *Tools:* **Scapy**, **Hping3**, **Packeth**.

### 2. Network Scanning & Enumeration
* **Port Scanners:** Send probes across ranges of IP addresses and TCP/UDP ports to discover active hosts and open services.
  * *Tools:* **Nmap**, **Masscan**, **Zenmap** (Nmap GUI).
* **Vulnerability Scanners:** Interrogate open ports against databases of known CVE vulnerabilities.
  * *Tools:* **Nessus**, **OpenVAS**, **Qualys**, **Nikto** (web-specific).

### 3. Password Attack Tools
* **Online Password Attacks (Active Network):** Tries combinations over live protocols (SSH, FTP, HTTP) at the risk of triggering account lockouts.
  * *Tools:* **Hydra**, **Medusa**.
* **Offline Password Attacks (Cracking Hashes):** Extracts password hashes from compromised systems (e.g., SAM hive, `/etc/shadow`, NTDS.dit) and cracks them offline using GPU compute without network detection.
  * *Tools:* **John the Ripper**, **Hashcat**, **Ophcrack** (uses precomputed Rainbow Tables).

### 4. Exploitation Frameworks
Integrated suites containing modular exploits, payloads, listeners, and post-exploitation tools.
* **Metasploit Framework:** Premier open-source exploitation framework.
* **Cobalt Strike:** Commercial adversary emulation tool used extensively by red teams and ransomware syndicates (uses "Beacons" for C2).
* **Empire / BloodHound:** Post-exploitation active directory graph analysis tools.

### 5. Wireless Hacking & Rootkits
* **Wireless Tools:** **Aircrack-ng** (suite for WEP/WPA handshake cracking), **Kismet** (passive wireless detector), **Wifite**.
* **Binary Disassemblers / Reverse Engineering:** **Ghidra** (NSA tool), **IDA Pro**, **x64dbg**.

---

## 13.3 High-Yield Test & Exam Review (Trap Alerts)

1. **Which threat actor has the longest dwell time?**
   * **State-Sponsored APTs.** Their goal is stealth and long-term espionage, not immediate destruction.
2. **What differentiates an offline password attack from an online attack?**
   * Online attacks attempt logins against live servers (limited by rate-limits/lockouts); **offline attacks crack stolen hashes locally with zero network traffic or lockout risk**.
3. **What is the function of Ophcrack?**
   * It cracks Windows LM/NTLM hashes using precomputed **Rainbow Tables**.
4. **What is a Vulnerability Broker?**
   * An individual or company that discovers zero-day vulnerabilities and sells the information to vendors, third parties, or dark web buyers.
5. **Which tool is both a packet crafter and TCP/IP pinging tool?**
   * **Hping3**.
