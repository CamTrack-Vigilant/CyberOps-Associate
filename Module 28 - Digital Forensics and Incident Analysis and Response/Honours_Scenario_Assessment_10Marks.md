# Honours-Level Scenario-Based Assessment (10 Marks)
**Course:** Cisco Certified CyberOps Associate (CBROPS 200-201)  
**Module:** Module 28 – Digital Forensics and Incident Analysis and Response  
**Degree Level:** Honours / Postgraduate Degree Examination  

### Candidate Details (Group Submission)
* **Student 1:** Thabang Nhlokoma Buthelezi — **Student ID:** `230011908`
* **Student 2:** Simphiwe Mbatha — **Student ID:** `230000110`

---

## 🚨 Scenario Description: Operation "Phantom Beacon"
**Target Entity:** Apex Financial Services (Core Banking Infrastructure)  
**Classification:** Critical Incident / High Severity Tier-1  
**Timestamp:** Friday, 23:42 SAST  
**Compromised Asset:** `CORE-DB-01` (`10.140.20.15`), Oracle Real Application Clusters hosting transactional ledgers and customer identities.

### Incident Telemetry & Diagnostic Findings
1. **Outbound Beaconing:** Zeek and Suricata network monitors detect periodic HTTPS beaconing on port `8443` directed at an unclassified bulletproof hosting IP (`194.26.29.112`) located in Eastern Europe. Beacons recur every 45 seconds with jitter.
2. **Endpoint Detection & Response (EDR / Sysmon):**
   * **23:38:12 SAST (Event ID 1 - Process Creation):** `spoolsv.exe` (Print Spooler service) spawned `powershell.exe` with hidden window flags and a heavily obfuscated Base64 command (`-NonI -W Hidden -Enc JABj...`).
   * **23:39:44 SAST (Event ID 8 - CreateRemoteThread):** Injected shellcode observed from PowerShell (PID: `4892`) targeting `lsass.exe` (Local Security Authority Subsystem Service, PID: `672`) to dump LSASS process memory.
3. **Physical & Peripheral Records:**
   * At **22:15 SAST**, server room electronic badge access registered a third-party HVAC/electrical contractor.
   * At **22:20 SAST**, a USB storage device (`VID_0781 / PID_5583` SanDisk Cruzer 64GB) was mounted to the server console.
4. **Operational Crisis:**
   * The on-duty junior system administrator panicked upon seeing outbound traffic graphs and moved to immediately pull the dual AC power cords from `CORE-DB-01` to "stop data theft".
   * Meanwhile, the bank is actively settling over 1,200 international Swift interbank transactions per minute.

---

## 📋 Assessment Questions & Marking Rubric (Total: 10.0 Marks)

---

### Question 1: Order of Volatility (RFC 3227) & Acquisition Strategy [3.0 Marks]
Critique the junior administrator's proposal to immediately pull the physical power cords from `CORE-DB-01`.
1. Referring strictly to the **RFC 3227 Order of Volatility**, identify **three specific volatile forensic artifacts** that would be irreversibly destroyed by this action and explain the investigative consequence of losing each artifact. *(1.5 Marks)*
2. Formulate the correct, scientifically valid procedure the CyberOps SOC must follow to isolate the host without cutting power or contaminating evidence. *(1.5 Marks)*

#### Model Solution:
* **Part 1 (1.5 Marks - 0.5 per artifact):**
  * **Physical RAM (Order of Volatility Priority 2):** Contains unencrypted Cobalt Strike payload binaries, symmetric TLS/AES session keys, and cleartext credentials extracted from `lsass.exe`. Cutting power empties memory capacitors, losing these keys permanently.
  * **Active Network Sockets & ARP Cache (Priority 2):** Live TCP connections in `ESTABLISHED` state pointing to `194.26.29.112:8443` proving active data exfiltration channels and peer IPs.
  * **Volatile Process Tree & Thread Injections (Priority 2):** Parent-child process relationships (`spoolsv.exe` $\rightarrow$ `powershell.exe` $\rightarrow$ injected thread in `lsass.exe`) that legally prove unauthorized exploitation and privilege escalation.
* **Part 2 (1.5 Marks):**
  * **Layer 2/3 Logical Isolation:** Isolate `CORE-DB-01` via EDR software quarantine or switch-port ACLs to break external C2 routing while keeping the operating system alive.
  * **Live Memory Dump:** Perform volatile memory capture using write-blocked sterile media or command-line forensic agents (e.g., `WinPmem`, `DumpIt`, `FTK Imager CLI`) to save `memory.dmp` before altering system state.

---

### Question 2: Evidence Integrity, Chain of Custody & Judicial Admissibility [2.0 Marks]
During the initial investigation, an analyst made a logical copy (regular copy-paste) of the database directory to a USB thumb drive, left the drive on an unmonitored desk over the weekend, and computed an SHA-256 hash on Monday morning before submitting it to legal counsel.
1. Evaluate whether this evidence complies with the **Best Evidence Rule** and explain whether it is admissible in court. *(1.0 Mark)*
2. Identify **two critical breaches of the Chain of Custody** and explain how defense counsel would exploit these flaws to suppress the evidence. *(1.0 Mark)*

#### Model Solution:
* **Part 1 (1.0 Mark):**
  * **Inadmissible under the Best Evidence Rule:** A logical file copy captures only active directory files, modifying file system Last Accessed ($MACB$) metadata timestamps. It fails to preserve unallocated space, slack space, and deleted artifacts. The Best Evidence Rule requires the original physical drive or an exact, verified **bit-stream forensic duplicate** (`.dd` or `.E01`) captured via a hardware write-blocker.
* **Part 2 (1.0 Mark - 0.5 per breach):**
  * *Breach 1 (Unmonitored Physical Storage):* Leaving the USB on an open desk over the weekend creates an undocumented custody gap where unauthorized access, tampering, or drive substitution cannot be disproven.
  * *Breach 2 (Belated Hash Calculation):* Generating the SHA-256 hash 48 hours post-extraction destroys mathematical proof of origin. Defense attorneys will file a motion to suppress, arguing evidence was tainted.

---

### Question 3: NIST SP 800-61 Rev 2 Containment & Operational Trade-offs [3.0 Marks]
In **Phase 3 (Containment, Eradication, and Recovery)** of the NIST Incident Handling Lifecycle:
1. Differentiate between **Short-Term Containment** and **Long-Term Containment** actions required for this banking database intrusion. *(1.5 Marks)*
2. The Chief Operating Officer demands that the database remain online to complete $50 million in pending transactions, while the Lead Security Analyst insists on immediate network shutdown. Propose a balanced technical containment strategy that mitigates data exfiltration while satisfying operational continuity. *(1.5 Marks)*

#### Model Solution:
* **Part 1 (1.5 Marks):**
  * *Short-Term Containment:* Immediate egress filtering at perimeter firewalls blackholing `194.26.29.112`, disabling compromised service account credentials, and terminating the rogue Print Spooler process.
  * *Long-Term Containment:* Full enterprise credential revocation, installing vendor security patches for print spooler vulnerabilities, and enforcing micro-segmentation restricting database access solely to verified application servers.
* **Part 2 (1.5 Marks):**
  * *Targeted Egress Blackholing & Host Micro-Segmentation:*
    1. Null-route the external C2 IP (`194.26.29.112`) at edge border gateways and proxy layers, instantly preventing data exfiltration.
    2. Configure host-level firewall rules allowing only incoming SQL queries on port `1521` from authenticated internal application tiers (`10.140.10.0/24`), while dropping all outbound traffic and lateral SMB/RPC protocols. This preserves transaction processing while neutralizing the adversary.

---

### Question 4: Incident Classification (VERIS 4A Model) & Lessons Learned [2.0 Marks]
1. Categorize this security incident using the **VERIS 4A Model** (Actors, Actions, Assets, Attributes). *(1.0 Mark)*
2. Formulate **two institutional remediation policies** to be presented at the 14-day blameless Post-Mortem meeting. *(1.0 Mark)*

#### Model Solution:
* **Part 1: VERIS 4A Model (1.0 Mark - 0.25 each):**
  * **Actors:** External (State-sponsored APT / Organized Crime) collaborating with or exploiting Physical Partner (Facility Contractor).
  * **Actions:** Physical (unauthorized USB attachment) + Malware (Cobalt Strike C2) + Hacking (Print Spooler exploit & LSASS memory injection).
  * **Assets:** Server (`CORE-DB-01` Oracle Database Server).
  * **Attributes:** Confidentiality (compromised via LSASS credential harvesting and customer records exfiltration attempt) and Integrity (unauthorized remote execution).
* **Part 2: Institutional Remediation Policies (1.0 Mark):**
  1. *Hardware Peripheral Lockdown (USB Device Control):* Deploy global GPO and EDR device control blocking all removable storage devices on server infrastructure.
  2. *Two-Person Escort & CCTV Policy for Data Centers:* Mandate dual-custody physical escort and continuous video recording for external contractors accessing physical server rooms.

---

## 📊 Evaluation Summary Matrix

| Question | Syllabus Focus | Evaluation Criteria | Marks |
| :--- | :--- | :--- | :---: |
| **Q1: Volatility & Memory Acquisition** | Sec 28.1 (Evidence Handling) | RFC 3227 priority analysis & live dump procedure | **3.0** |
| **Q2: Chain of Custody & Integrity** | Sec 28.1 (Evidence Integrity) | Best Evidence Rule & chain of custody breaches | **2.0** |
| **Q3: Incident Containment Strategy** | Sec 28.2 (Incident Handling) | Short vs Long containment & business risk balance | **3.0** |
| **Q4: VERIS & Lessons Learned** | Sec 28.3 (Incident Models) | VERIS 4A categorization & institutional post-mortem | **2.0** |
| **TOTAL** | | | **10.0** |
