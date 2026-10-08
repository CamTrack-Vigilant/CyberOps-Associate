# Cisco CyberOps Associate: Modules 11 to 19 Master Cheat Sheet

**Exam Scope:** Chapters 11 to 19 (High-Yield Rapid Review)  
**Target:** Cisco Certified CyberOps Associate (CBROPS 200-201 / NetAcad Checkpoints)

---

## ⚡ Quick Protocol & Port Numbers Reference
| Protocol | Port / Protocol # | Transport | Security / Architectural Relevance |
| :--- | :--- | :--- | :--- |
| **SSH** | 22 | TCP | Encrypted terminal management; replaces cleartext Telnet (Port 23). |
| **DNS** | 53 | UDP / TCP | Name resolution. UDP for queries (<512B), TCP for zone transfers (AXFR). |
| **DHCP** | 67 (Server) / 68 (Client) | UDP | IP address configuration; vulnerable to starvation and rogue servers. |
| **TFTP** | 69 | UDP | Simple unauthenticated file transfer used in PXE and IOS backup. |
| **HTTP / HTTPS** | 80 / 443 | TCP | Cleartext vs. TLS-encrypted web application transport. |
| **NTP** | 123 | UDP | Network Time Protocol; vulnerable to reflection/amplification DoS. |
| **SNMP** | 161 / 162 | UDP | Network management; SNMPv3 adds authentication and encryption. |
| **Syslog** | 514 | UDP | System logging messages (Severities 0 to 7: Emergencies to Debugging). |
| **RADIUS** | 1812 (Auth) / 1813 (Acct) | UDP | AAA protocol; encrypts ONLY the password. |
| **TACACS+** | 49 | TCP | AAA protocol; encrypts the ENTIRE packet payload. |
| **IPsec AH** | IP Protocol **51** | Layer 3 | Authentication and integrity ONLY (**NO encryption**). |
| **IPsec ESP** | IP Protocol **50** | Layer 3 | Confidentiality (Encryption) + Authentication + Integrity. |
| **GRE** | IP Protocol **47** | Layer 3 | Generic Routing Encapsulation; used by ERSPAN to route mirrored packets. |
| **ICMP** | IP Protocol **1** | Layer 3 | Diagnostic messaging; Echo (Type 8), Echo Reply (Type 0), Unreachable (Type 3). |

---

## 📊 Core Comparison Matrices (High-Yield Exam Topics)

### 1. TACACS+ vs. RADIUS
| Attribute | TACACS+ | RADIUS |
| :--- | :--- | :--- |
| **Standard** | Cisco Proprietary (RFC 8907) | IETF Open Standard |
| **Transport** | **TCP Port 49** | **UDP Ports 1812 / 1813** |
| **Encryption** | **Entire packet payload** | **Password field only** |
| **AAA Separation** | **Separates** Authentication, Authorization, Accounting | **Combines** Authentication and Authorization |
| **Primary Use** | **Device Administration** (Routers, Switches) | **Network Access** (802.1X, Wi-Fi, VPNs) |

---

### 2. SPAN vs. Network TAP
| Attribute | SPAN (Port Mirroring) | Network TAP |
| :--- | :--- | :--- |
| **Implementation** | Switch software configuration | Dedicated physical hardware spliced into cable |
| **Cost** | Free | Additional hardware purchase |
| **Switch Load** | Consumes switch CPU and internal bus | **Zero impact** on network switch |
| **Dropped Frames** | Drops packets under heavy load; drops CRC/runts | **Captures 100% of packets**, including corrupted frames |

---

### 3. NetFlow vs. Full PCAP
| Attribute | NetFlow / IPFIX | Full Packet Capture (PCAP) |
| :--- | :--- | :--- |
| **Analogy** | "The Phone Bill" (Metadata) | "The Wiretap Recording" (Payload) |
| **Data Recorded** | Flow 7-tuple, timestamps, byte counts | Every single byte from Layer 2 to Layer 7 |
| **Storage Need** | Very low (Megabytes per day) | Very high (Terabytes per day) |
| **Payload Analysis** | None (cannot inspect malicious strings) | Complete (extracts malware binaries, text) |

---

### 4. Access Control Models
* **DAC (Discretionary):** Creator/owner sets permissions (e.g., Windows NTFS, Linux permissions).
* **MAC (Mandatory):** Central system enforces sensitivity labels (Top Secret, Secret) vs. user clearance (e.g., Military, SELinux).
* **RBAC (Role-Based):** Access based on user's job role/department (e.g., Active Directory security groups).
* **ABAC (Attribute-Based):** Dynamic policies evaluating user, resource, action, and environment (time, location, device health).

---

### 5. Switch Port Security Violation Modes
* **Protect:** Drops frames from unauthorized MACs. **No logging, no counter increment.**
* **Restrict:** Drops frames from unauthorized MACs. **Logs syslog message, increments counter.**
* **Shutdown (Default):** Drops frames, logs syslog, and **disables port into `err-disable` state**.

---

### 6. Switch Defense Technologies
* **DHCP Snooping:** Blocks unauthorized DHCP servers on untrusted ports; builds the **DHCP Snooping Binding Table**.
* **Dynamic ARP Inspection (DAI):** Intercepts and drops forged ARP replies on untrusted ports using the DHCP Snooping table.
* **Port Security:** Restricts switch port connectivity based on learned or configured MAC addresses.

---

### 7. Alert Classification (SOC Triage)
* **True Positive (TP):** Attack occurring $\rightarrow$ System alerted. *(Correct)*
* **False Positive (FP):** Benign traffic $\rightarrow$ System alerted. *(Nuisance noise)*
* **True Negative (TN):** No attack $\rightarrow$ No alert. *(Normal operation)*
* **False Negative (FN):** Attack occurring $\rightarrow$ **NO alert**. *(Worst-case security failure)*

---

### 8. Disaster Recovery (DRP) Metrics & Sites
* **RTO (Recovery Time Objective):** Maximum tolerable **duration of downtime**.
* **RPO (Recovery Point Objective):** Maximum tolerable **data loss in time**.
* **Hot Site:** Fully equipped duplicate facility with real-time data replication; failover in **minutes to hours**.
* **Warm Site:** Hardware present; backups must be loaded; failover in **days**.
* **Cold Site:** Empty building with power/cooling; no computers installed; failover in **weeks**.
