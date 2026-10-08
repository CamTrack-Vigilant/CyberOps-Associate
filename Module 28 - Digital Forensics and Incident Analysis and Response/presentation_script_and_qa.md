# Module 28 Presentation Delivery Script, Defense Q&A & Live Demo Guide

**Course:** Cisco Certified CyberOps Associate (CBROPS 200-201)  
**Module 28:** Digital Forensics and Incident Analysis & Response  
**Target Delivery Time:** 12 to 15 Minutes  
**Slide Deck File:** [`presentation_deck.html`](file:///c:/Users/fanele/CyberOps%20Associate/CyberOps-Associate/Module%2028%20-%20Digital%20Forensics%20and%20Incident%20Analysis%20and%20Response/presentation_deck.html)

---

## ⏱️ Presentation Timing Roadmap

| Slide # | Slide Title | Allotted Time | Key Focus |
| :---: | :--- | :---: | :--- |
| **1** | Title & Welcome | 0:00 - 1:00 | Hook the audience: "It's not IF, but WHEN." |
| **2** | When Minutes Matter (Chaos vs Methodology) | 1:00 - 2:15 | Contrast panic vs SOC discipline |
| **3** | The Scientific Forensic Process | 2:15 - 3:30 | Collection, Examination, Analysis, Reporting |
| **4** | Evidence Integrity & The Golden Rule | 3:30 - 5:00 | Never touch original; Bit-stream vs Logical; Hashing |
| **5** | Order of Volatility (RFC 3227) | 5:00 - 6:30 | The hierarchy: Registers $\rightarrow$ RAM $\rightarrow$ Disk |
| **6** | Chain of Custody & Evidence Types | 6:30 - 7:45 | Legal admissibility; Best vs Circumstantial |
| **7** | NIST SP 800-61 Rev 2 Lifecycle | 7:45 - 9:00 | The 4 core phases and continuous feedback loop |
| **8** | Detection & Analysis (Precursors vs IoCs) | 9:00 - 10:15 | Future threats vs Active breach signs |
| **9** | Containment, Eradication & Recovery | 10:15 - 11:30 | Stopping the bleeding without alerting the attacker |
| **10** | Post-Incident Lessons Learned | 11:30 - 12:30 | The 14-day blameless post-mortem |
| **11** | Case Study: The 2 AM Ransomware Alert | 12:30 - 13:45 | End-to-end real incident narrative |
| **12** | CSIRT Models, Sharing Communities & VERIS | 13:45 - 14:30 | FIRST, ISACs, CERT/CC, VERIS 4A framework |
| **13-14**| Summary, Live Demo & Q&A | 14:30 - 16:00+ | Interactive PowerShell demo & answering questions |

---

## 🎙️ Word-for-Word Speaking Script

### Slide 1: Title & Overview (0:00 - 1:00)
> *"Good morning/afternoon everyone. Today, I am presenting **Module 28: Digital Forensics and Incident Analysis and Response** from the Cisco CyberOps curriculum.*
> 
> *There is a foundational axiom in modern cybersecurity: 'There are two types of organizations in the world: those who have been breached, and those who don't know it yet.'*
> 
> *Prevention tools like firewalls and antiviruses will eventually be bypassed. When that happens, success does not depend on luck — it depends on disciplined forensic science and structured incident handling. In this chapter, we explore how a Security Operations Center preserves legal evidence, traces sophisticated adversaries, and restores business operations without destroying critical telemetry."*

---

### Slide 2: When Minutes Matter: Chaos vs. Methodology (1:00 - 2:15)
> *"Let us look at what happens when a breach is detected at 2 AM.*
> 
> *In an untrained organization, panic takes over. A system administrator logs into the infected server, starts opening files, or worse — reboots the machine. By doing that, they have just obliterated the volatile RAM where the attacker's decryption keys, active network sockets, and fileless malware reside. Furthermore, because they modified file access timestamps and kept no logs, any evidence they try to bring to court will be thrown out.*
> 
> *By contrast, a professional CyberOps SOC follows a pre-established Incident Response Plan. They know exactly how to isolate the machine without tipping off the adversary, how to acquire live volatile memory, and how to verify evidence integrity down to the exact bit."*

---

### Slide 3: The Scientific Forensic Process (2:15 - 3:30)
> *"Digital forensics is defined as the application of science to identify, collect, examine, and analyze digital evidence while preserving its integrity.*
> 
> *The process follows four strictly defined stages:*
> 1. *First, **Collection**: Identifying physical machines, virtual disks, or network logs, labeling them, and acquiring exact clones using write-blockers.*
> 2. *Second, **Examination**: Filtering out the noise. In a typical 1 Terabyte drive, 95% of files are standard operating system binaries. Using databases like the NIST National Software Reference Library, we de-NIST the image to focus only on modified, anomalous, or deleted files.*
> 3. *Third, **Analysis**: The analytical heart. We reconstruct timelines, look for timestomping where malware modified file timestamps, inspect process injection, and answer: Who, What, Where, When, and How.*
> 4. *And fourth, **Reporting**: Creating clear, factual documentation that can serve both technical leadership and stand up to cross-examination in a court of law."*

---

### Slide 4: Evidence Integrity & The Golden Rule (3:30 - 5:00)
> *"If you only remember one sentence from this presentation, let it be this: **Never perform forensic analysis on original evidence.** That is the #1 Golden Rule of Forensics.*
> 
> *Why? Because simply booting up a Windows or Linux machine alters hundreds of registry keys, logs, and temp files.*
> 
> *Instead, we use **Hardware Write-Blockers** — physical bridges that let us read data from the suspect disk while physically severing the write-signal line. We create a **Bit-Stream Image** — not a regular copy-paste, but an exact bit-for-bit image of every sector, including deleted files and unallocated slack space.*
> 
> *To prove in court that our copy is 100% identical, we use **Cryptographic Hashing** like SHA-256. If the hash of the source drive matches the hash of our target image, we have mathematical proof of integrity. If someone changes a single 0 to a 1, the entire hash string changes completely due to the avalanche effect."*

---

### Slide 5: Order of Volatility (RFC 3227) (5:00 - 6:30)
> *"Now, when you arrive at a crime scene, what do you collect first?*
> 
> *RFC 3227 establishes the **Order of Volatility** — ranking evidence from the most perishable to the most permanent:*
> * At the top are **CPU registers and cache**, which vanish in nanoseconds.
> * Immediately following is **RAM, routing tables, ARP caches, and active process tables**.
> * Then temporary filesystems and swap space.
> * Below that is **local hard disk storage**.
> * And at the bottom are remote logs and archival backups.*
> 
> *Notice what this means: **Never pull the power cord!** If you pull the plug, everything in levels 1 and 2 disappears forever. Today's most dangerous malware executes fileless inside RAM. That is why our first response is always live memory acquisition using tools like WinPmem or FTK Imager CLI before shutting down."*

---

### Slide 6: Chain of Custody & Evidence Admissibility (6:30 - 7:45)
> *"Now, what if you have the best technical evidence in the world, but your paperwork is sloppy? It gets dismissed.*
> 
> *The **Chain of Custody** is a chronological, unbroken document proving who collected the evidence, where it was stored, who accessed it, when, and why. If there is a 24-hour gap where a hard drive was left unattended on an open desk, opposing attorneys will argue the evidence was tampered with.*
> 
> *Courts recognize four main evidence types:*
> * **Best Evidence:** The original physical media or its verified bitstream forensic clone.
> * **Direct Evidence:** Directly proves a fact, like security camera footage showing an insider at the keyboard.
> * **Circumstantial Evidence:** Indirect correlation, like an IP login timestamp matching badge access.
> * **Corroborating Evidence:** Supporting data, such as a Snort IDS alert backed up by a firewall drop log."*

---

### Slide 7: NIST SP 800-61 Rev 2 Incident Handling Lifecycle (7:45 - 9:00)
> *"Turning from forensics to incident management, the gold standard framework is **NIST Special Publication 800-61 Revision 2**.*
> 
> *It defines a four-phase lifecycle:*
> 1. *Phase 1: **Preparation***
> 2. *Phase 2: **Detection and Analysis***
> 3. *Phase 3: **Containment, Eradication, and Recovery***
> 4. *Phase 4: **Post-Incident Activity***
> 
> *Notice the arrows in the diagram: Detection and Containment form an iterative feedback loop. As you contain a threat, you discover new indicators, which refines your analysis."*

---

### Slide 8: Detection & Analysis (Precursors vs. IoCs) (9:00 - 10:15)
> *"In Phase 2, how do we know an incident is occurring? We must understand the distinction between a **Precursor** and an **Indicator of Compromise (IoC)**:*
> 
> *A **Precursor** is an early warning sign that an attack *might* happen in the future. For example: a port scan against your firewall, or dark web chatter mentioning your company name.*
> 
> *An **Indicator of Compromise (IoC)** is proof that an attack *is actively occurring or has already occurred*. Examples include: an antivirus alert for a known ransomware hash, a new unauthorized domain admin account, or an outgoing beacon to a Command-and-Control server.*
> 
> *Analysts use SIEMs and EDRs to prioritize incidents based on business functional impact, data sensitivity, and recoverability effort."*

---

### Slide 9: Containment, Eradication & Recovery (10:15 - 11:30)
> *"Once an incident is confirmed, Phase 3 stops the bleeding:*
> 
> * **Short-Term Containment:** Isolating the infected host immediately (such as network quarantine via EDR or port shutdown) so malware cannot move laterally across the subnet.*
> * **Long-Term Containment:** Implementing temporary firewall blocks, rotating compromised API keys, and routing traffic through security proxies.*
> * **Eradication:** Scrubbing the environment — deleting malicious scheduled tasks, registry persistence keys, and remediating the root-cause vulnerability.*
> * **Recovery:** Restoring systems from verified, clean offline backups. We reconnect systems in phases under **Enhanced Monitoring** to verify the threat actor hasn't retained backdoors."*

---

### Slide 10: Post-Incident Activity (Lessons Learned) (11:30 - 12:30)
> *"The final, and most frequently overlooked phase, is **Post-Incident Activity**.*
> 
> *Within two weeks of closing the incident, the CSIRT conducts a **blameless Lessons Learned meeting**. The goal is never to find a scapegoat — it is to improve the organization's immunity.*
> 
> *We ask four critical questions:*
> 1. *What exactly happened, and when?*
> 2. *Did our documented playbooks work, or did analysts have to improvise?*
> 3. *What early indicators were missed?*
> 4. *How do we automate detection so this specific attack can never succeed again?*
> 
> *This produces the final Incident Report and mandates legal evidence retention, usually between 3 to 7 years."*

---

### Slide 11: Case Study: The 2 AM Ransomware Alert (12:30 - 13:45)
> *"To tie this all together into a real-world scenario:*
> 
> *At 02:14 AM, our EDR detects an encoded PowerShell command spawning from an Excel invoice on a finance workstation. This is an active IoC.*
> 
> *At 02:22 AM, the on-call analyst initiates **Short-Term Containment**: the host is isolated from the network via EDR, an automated live RAM dump is initiated, and the user's Active Directory account is disabled.*
> 
> *By 04:15 AM during **Eradication**, forensic memory analysis reveals a Cobalt Strike beacon. The malicious macro hash is pushed to the global email filter, and lateral persistence keys are purged.*
> 
> *At 08:00 AM during **Recovery**, the laptop is reimaged from a clean corporate image, financial spreadsheets are restored from immutable cloud backups, and the user is back to work safely by 9 AM without paying a single dollar in ransom."*

---

### Slide 12: Frameworks, Sharing & VERIS (13:45 - 14:30)
> *"Finally, Section 28.3 highlights that no SOC defends alone.*
> 
> *Organizations participate in **ISACs (Information Sharing and Analysis Centers)** to share sector-specific threat intelligence. They coordinate with **FIRST** and **CERT/CC**.*
> 
> *For standardized metrics and breach reporting, the industry relies on **VERIS (Vocabulary for Event Recording and Incident Sharing)**. VERIS structures incidents under the **4A Model**:*
> * **Actors:** Who attacked? (Nation-state, insider, cybercriminal)
> * **Actions:** What did they do? (Malware, social engineering, credential misuse)
> * **Assets:** What was affected? (Database, point-of-sale terminal, cloud VM)
> * **Attributes:** Which leg of the CIA triad was violated?"*

---

### Slide 13 & 14: Conclusion & Live Demonstration (14:30+)
> *"In summary: Digital Forensics provides the scientific integrity to reconstruct past events, while the NIST Incident Handling Lifecycle gives us the structured playbook to survive active crises.*
> 
> *I would now be delighted to answer any questions from the class and instructor, or demonstrate a quick live verification of digital evidence integrity using PowerShell. Thank you!"*

---

## 🛡️ Anticipated Class & Instructor Questions (Defense Prep)

### Question 1: *"Why do we prioritize RAM over Hard Drives if hard drives contain 99% of the file data?"*
* **Bulletproof Answer:**  
  *"Because of the fundamental law of volatility: hard drive data is non-volatile magnetic or flash storage — it will still be there tomorrow even if unpowered. Volatile RAM, however, loses all charge the second power is cut. Furthermore, modern threat actors heavily rely on 'fileless malware' and memory injection (like Cobalt Strike or Meterpreter) that executes purely in RAM without writing an executable binary to disk. If you pull the plug or focus on the hard drive first, you permanently destroy active network sockets, decrypted encryption keys, and running malware processes."*

---

### Question 2: *"What is the difference between an Adverse Event and a Security Incident?"*
* **Bulletproof Answer:**  
  *"According to NIST SP 800-61, an **Event** is any observable occurrence in a system, like a firewall rule match or DNS query. An **Adverse Event** is an event with negative consequences, such as a server crashing from high CPU or a power outage. A **Security Incident** specifically involves a confirmed violation — or imminent threat of violation — of computer security policies, acceptable use policies, or standard security practices, such as unauthorized data exfiltration or malware infection."*

---

### Question 3: *"Why can't an investigator simply copy-paste (logical copy) suspect files onto a USB flash drive?"*
* **Bulletproof Answer:**  
  *"A logical file copy only grabs the files indexed by the operating system's filesystem. It completely misses deleted files, file slack (the leftover padding space in disk clusters), unallocated space, and hidden partitions where attackers frequently hide rootkits or staged exfiltration archives. Furthermore, a logical copy alters the file's 'Last Accessed' timestamp ($MACB$ attributes). A true forensic acquisition must be a bit-stream raw duplicate (`.dd` or `.E01`) taken with a physical write-blocker to guarantee zero alteration of metadata."*

---

### Question 4: *"What is the difference between an Attack Precursor and an Indicator of Compromise (IoC)?"*
* **Bulletproof Answer:**  
  *"The timing and probability: A **Precursor** points to the future (an attack might happen), such as vulnerability scanner traffic in web logs or dark web chatter. An **Indicator of Compromise (IoC)** points to the present or past (an attack is actively happening or already succeeded), such as a known malware hash running in memory, anomalous outbound traffic over port 4444, or unauthorized admin account creation."*

---

### Question 5: *"Why is the Lessons Learned meeting required to happen within two weeks?"*
* **Bulletproof Answer:**  
  *"Because human memory decays rapidly. If a team waits 2 or 3 months to conduct a post-mortem, analysts forget the exact sequence of events, subtle technical anomalies, or operational friction they experienced during the incident. Holding the meeting within 14 days ensures accurate recollection, enables immediate closing of security holes, and prevents the same vector from being exploited again."*

---

## 🧪 2-Minute Live Classroom Demonstration (PowerShell)

Show this on the classroom projector to get instant bonus points for practical technical mastery:

### Step 1: Open PowerShell and create a mock "Digital Evidence File"
```powershell
# Create an evidence text file
"Confidential Financial Transaction Data - Original State" | Out-File -FilePath evidence.txt -Encoding utf8
```

### Step 2: Compute its original SHA-256 Hash
```powershell
Get-FileHash -Path evidence.txt -Algorithm SHA256
```
*(Explain to class: "This hash string represents our original evidence fingerprint.")*

### Step 3: Demonstrate the "Avalanche Effect" (Tamper Simulation)
```powershell
# Simulate an unauthorized modification of just ONE punctuation mark
"Confidential Financial Transaction Data - Original State." | Out-File -FilePath evidence.txt -Encoding utf8

# Re-compute the hash
Get-FileHash -Path evidence.txt -Algorithm SHA256
```
*(Explain to class: "Notice how changing a single period produced a completely different cryptographic hash string. In a courtroom, this proves beyond doubt whether digital evidence was altered or preserved in its pure original state.")*
