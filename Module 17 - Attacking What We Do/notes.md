# Module 17: Attacking What We Do - Study & Test Revision Guide

**Course:** Cisco Certified CyberOps Associate (CBROPS 200-201)  
**Curriculum Alignment:** Cisco Networking Academy (NetAcad) Module 17  
**Core Objective:** Understand how common network services (ARP, DNS, DHCP) and application protocols (HTTP/HTTPS, SMTP) are manipulated by adversaries, and master the switch and protocol countermeasures.

---

## 17.0 Introduction
While Module 16 covered foundation protocols (IP, TCP, UDP), Module 17 addresses the essential daily services that users and applications rely on: resolving names (DNS), obtaining IP addresses (DHCP), resolving MACs (ARP), browsing the web (HTTP), and sending email (SMTP).

---

## 17.1 Attacks on Core IP Services

### 1. ARP Vulnerabilities & Attacks
The Address Resolution Protocol (ARP) translates a known 32-bit IPv4 address into a 48-bit physical MAC address. Because ARP is stateless and unauthenticated, devices automatically accept **Gratuitous ARP** replies without ever verifying if a request was sent.

* **ARP Poisoning / ARP Spoofing:**
  * Attacker sends unsolicited, fake ARP replies to Host A and the Default Gateway.
  * Attacker tells Host A: *"I have the Gateway's IP address, my MAC is Attacker-MAC."*
  * Attacker tells Gateway: *"I have Host A's IP address, my MAC is Attacker-MAC."*
  * Both cache tables are corrupted; all traffic between Host A and the Internet passes through the attacker (**Man-in-the-Middle / MitM**).
* **Defensive Countermeasure:**
  * **Dynamic ARP Inspection (DAI):** A Cisco switch security feature that inspects all ARP requests/replies on untrusted ports and validates them against the **DHCP Snooping Binding Database**. Invalid mappings are immediately dropped.

---

### 2. DNS (Domain Name System) Attacks
DNS translates human-readable domain names (e.g., `cisco.com`) into IP addresses (UDP/TCP Port 53).

* **DNS Cache Poisoning (Spoofing):**
  * Attacker injects fraudulent DNS records into a caching DNS recursive resolver.
  * When clients query `bank.com`, the poisoned DNS cache directs them to the attacker's phishing server IP.
* **DNS Tunneling:**
  * Adversaries abuse DNS queries to bypass firewalls and exfiltrate data or maintain Command & Control (C2).
  * Data is encoded into the subdomains of DNS requests (e.g., `exfiltrated-creditcard-data.attacker.com`). The local DNS resolver forwards the query out to the attacker's authoritative nameserver, successfully bypassing edge firewall inspection.
* **Fast-Flux DNS:**
  * Cybercriminals rapidly change the A records of a domain (every few seconds) using thousands of compromised botnet nodes as proxies, making IP-based blocklists ineffective.
* **Domain Generation Algorithms (DGA):**
  * Malware generates hundreds of pseudorandom domains daily (e.g., `x78dfa91.biz`) to contact its C2 server; defenders must block the algorithm or reverse-engineer the seed.
* **Defensive Countermeasures:**
  * **DNSSEC (DNS Security Extensions):** Digitally signs DNS records using public key cryptography, ensuring authenticity and integrity.
  * **Cisco Umbrella:** Cloud-delivered DNS filtering that inspects and blocks requests to malicious or newly registered domains.

---

### 3. DHCP (Dynamic Host Configuration Protocol) Attacks
DHCP automatically allocates IP addresses, subnet masks, default gateways, and DNS servers (UDP Ports 67/68).

* **DHCP Starvation Attack:**
  * Attacker uses automated tools (e.g., **Gobbler**, **Yersinia**) to flood the DHCP server with thousands of DHCP Discover messages, each using a unique spoofed MAC address.
  * The DHCP server exhausts its entire pool of available IP addresses. Legitimate new network clients cannot obtain an IP and experience a Denial of Service.
* **Rogue DHCP Server / DHCP Spoofing:**
  * Attacker brings up an unauthorized DHCP server on the local subnet.
  * The rogue server responds faster than the legitimate server, assigning victims:
    * A fake **Default Gateway** (the attacker's IP, creating a MitM).
    * A fake **DNS Server** (directing users to phishing sites).
* **Defensive Countermeasure:**
  * **DHCP Snooping:** A switch security feature that categorizes switch ports into:
    * **Trusted Ports:** Connected to legitimate DHCP servers/uplinks; permitted to send DHCP Offers/Acks.
    * **Untrusted Ports:** Connected to end users; **drops all incoming DHCP Server messages** (Offers, Acks). It also builds the **DHCP Snooping Binding Database** (MAC-IP-VLAN-Port mapping).

---

## 17.2 Web and Application Layer Attacks

### 1. Web Application Attacks (OWASP Top 10)
| Attack Type | Mechanics | Typical Impact / Payload | Countermeasure |
| :--- | :--- | :--- | :--- |
| **SQL Injection (SQLi)** | Attacker inserts malicious SQL syntax into web form inputs or URL parameters. | Bypasses authentication (`' OR '1'='1 --`), extracts entire database, or modifies records. | **Prepared Statements (Parameterized Queries)**, input validation. |
| **Cross-Site Scripting (XSS)** | Malicious JavaScript injected into a legitimate website, executed inside the victim's browser. | Steals session cookies, hijacks accounts, performs unauthorized actions. | Contextual **output encoding**, input sanitization, **Content Security Policy (CSP)**. |
| **Cross-Site Request Forgery (CSRF)** | Forces an already authenticated user's browser to execute an unwanted action on a trusted site. | Transfers money or changes email without user awareness. | **Anti-CSRF Tokens (Synchronizer Tokens)**, SameSite cookie attributes. |

* **Three Flavors of XSS:**
  * *Stored (Persistent) XSS:* Injected script is stored permanently in the database (e.g., in a blog comment); executes for every user who views the page.
  * *Reflected (Non-Persistent) XSS:* Injected script is reflected off the web server in an error message or search result link.
  * *DOM-based XSS:* Vulnerability exists entirely within client-side JavaScript code.

---

### 2. Email Attacks & Protection Standards
Email (SMTP Port 25) inherently lacks sender verification.

* **Open Mail Relay:** An SMTP server misconfigured to accept and forward emails from any source to any destination without authentication; heavily abused by spammers.
* **Email Spoofing Countermeasures (The Triad):**
  1. **SPF (Sender Policy Framework - RFC 7208):** A DNS TXT record specifying which mail server IP addresses are authorized to send email on behalf of a domain.
  2. **DKIM (DomainKeys Identified Mail - RFC 6376):** Attaches a cryptographic digital signature to the email header, validated using the sender's public key published in DNS.
  3. **DMARC (Domain-based Message Authentication, Reporting, and Conformance):** Tells receiving mail servers what policy to enforce (`none`, `quarantine`, `reject`) if SPF and/or DKIM fail.

---

## 17.3 High-Yield Test & Exam Review (Trap Alerts)

1. **What switch security feature defeats ARP poisoning?**
   * **Dynamic ARP Inspection (DAI)**, which relies on the **DHCP Snooping binding database**.
2. **What does DHCP Snooping do to an unauthorized DHCP Offer packet received on an untrusted port?**
   * It **immediately drops the packet** and can disable the port (err-disable).
3. **What is the primary defense against SQL Injection?**
   * **Parameterized Queries (Prepared Statements)**.
4. **How does DNS Tunneling operate?**
   * It encodes non-DNS payload data inside the **subdomain labels of DNS queries** to bypass outbound firewall restrictions.
5. **What is the purpose of DMARC?**
   * It defines the enforcement policy (quarantine or reject) when an incoming email fails **SPF** or **DKIM** verification.
