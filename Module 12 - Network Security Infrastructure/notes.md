# Module 12: Network Security Infrastructure - Study & Test Revision Guide

**Course:** Cisco Certified CyberOps Associate (CBROPS 200-201)  
**Curriculum Alignment:** Cisco Networking Academy (NetAcad) Module 12  
**Core Objective:** Understand enterprise hierarchical design, firewall classifications, web/email security appliances, and virtual private network (VPN) architectures.

---

## 12.0 Introduction to Security Infrastructure
Security architecture is not about adding a single firewall at the perimeter; it is about building layered defense rings throughout the enterprise network. As a SOC analyst, you must know how traffic traverses core, distribution, and access tiers, and how dedicated security appliances filter packets.

---

## 12.1 Enterprise Network Architecture: The 3-Tier Hierarchical Model

```
              ┌──────────────────────────────────────┐
              │           CORE LAYER (BACKBONE)      │
              │ High-speed packet switching, no ACLs │
              └──────────────────┬───────────────────┘
                                 │
              ┌──────────────────┴───────────────────┐
              │          DISTRIBUTION LAYER          │
              │ Policy boundary, routing, ACLs, VLANs │
              └──────────────────┬───────────────────┘
                                 │
              ┌──────────────────┴───────────────────┐
              │             ACCESS LAYER             │
              │ End-device connectivity, Port Security│
              └──────────────────────────────────────┘
```

1. **Access Layer:** Directly connects end devices (workstations, printers, IP phones). Controls access via **Port Security**, 802.1X, and VLAN tagging.
2. **Distribution Layer:** The policy boundary between access and core. Aggregates wiring closets, performs inter-VLAN routing, defines **Access Control Lists (ACLs)**, QoS, and security boundaries.
3. **Core Layer (Backbone):** Provides high-speed, redundant transport between distribution switches. **No packet manipulation or filtering (no ACLs)** should occur here to avoid latency.
4. **Collapsed Core Model:** Merges the Core and Distribution layers into one layer, typically deployed in smaller enterprise sites.

---

## 12.2 Security Devices & Appliance Classifications

### 1. Firewall Generations & Types (Critical Exam Topic)
* **Packet Filtering Firewalls (Stateless - Layer 3/4):** Inspects individual packet headers (Source/Dest IP, Source/Dest Port, Protocol). Does not maintain state; vulnerable to IP spoofing.
* **Stateful Inspection Firewalls (Stateful - Layer 4/5):** Tracks active connection states in a **State Table** (tracks TCP 3-way handshakes, sequence numbers, and dynamic ports). Inbound return traffic matching an established outbound connection is automatically permitted.
* **Application Layer Gateway (Proxy - Layer 7):** Operates as an intermediary at the application layer; inspects payload data (HTTP, FTP) and terminates the client connection before creating a separate connection to the server.
* **Next-Generation Firewalls (NGFW - Layer 7):** Combines stateful inspection with **Deep Packet Inspection (DPI)**, application awareness (identifies BitTorrent or Facebook even over port 80/443), integrated Next-Gen IPS (NGIPS), SSL decryption, and user-identity tracking (Active Directory integration).

### 2. Specialized Security Appliances
* **Cisco Web Security Appliance (WSA):** Focuses exclusively on web traffic (HTTP/HTTPS/FTP). Performs URL filtering, malware web reputation scanning, SSL offloading/inspection, and acceptable use enforcement.
* **Cisco Email Security Appliance (ESA):** Defends against spam, phishing, spear-phishing, and ransomware attachments. Uses **Cisco Talos** threat intelligence, reputation filtering, and Data Loss Prevention (DLP) to inspect outbound sensitive emails.
* **Network Admission Control / AAA Server (Cisco ISE - Identity Services Engine):** Centralized policy engine that authenticates users, checks host posture (OS patches, antivirus status), and assigns dynamic VLANs.

---

## 12.3 Security Services & Virtual Private Networks (VPNs)

### 1. Site-to-Site vs. Remote Access VPNs
* **Site-to-Site VPN:** Connects entire networks across untrusted links (e.g., Branch Office router to Headquarters firewall). Operates transparently to end users.
* **Remote Access VPN:** Connects individual mobile users/teleworkers to the corporate LAN using client software (e.g., Cisco AnyConnect) or browser-based clientless SSL.

### 2. IPsec (IP Security) Architecture (Must-Know for Tests)
IPsec operates at **Layer 3** and provides Confidentiality, Integrity, Authentication, and Anti-Replay.

* **Two Core Security Protocols:**
  1. **AH (Authentication Header - IP Protocol 51):** Provides authentication and integrity of the entire packet (including IP header). **NO ENCRYPTION / NO CONFIDENTIALITY**. Incompatible with NAT because NAT modifies the IP header.
  2. **ESP (Encapsulating Security Payload - IP Protocol 50):** Provides **Confidentiality (Encryption)**, integrity, and authentication. Encrypts the payload.
* **Two Operating Modes:**
  1. **Transport Mode:** Protects only the payload; leaves original IP header untouched. Used for host-to-host communications.
  2. **Tunnel Mode:** Encrypts the entire original IP packet and attaches a brand new IP header. Mandatory for site-to-site VPNs.
* **IKE (Internet Key Exchange - UDP Port 500 / 4500):**
  * **Phase 1:** Negotiates security association ($SA$) and establishes a secure tunnel to protect management traffic (Diffie-Hellman key exchange).
  * **Phase 2:** Negotiates IPsec $SA$ parameters used to encrypt the actual data payload.

### 3. Forward Proxy vs. Reverse Proxy
* **Forward Proxy:** Positioned in front of **internal clients** to regulate, inspect, and cache outbound requests to the external Internet (hides client IPs).
* **Reverse Proxy:** Positioned in front of **internal web servers** to protect them from external Internet users, providing load balancing, SSL termination, and WAF protection (hides server IPs).

---

## 12.4 High-Yield Test & Exam Review (Trap Alerts)

1. **Which layer of the 3-tier model should NEVER have ACLs configured?**
   * **Core Layer.** The core layer prioritizes ultra-low latency and maximum packet throughput; packet filtering creates latency bottlenecks.
2. **AH vs. ESP Difference:**
   * **AH provides integrity and authentication ONLY (NO encryption).**
   * **ESP provides encryption (confidentiality) + authentication.**
3. **Transport Mode vs. Tunnel Mode:**
   * Transport mode does not encrypt the outer IP header.
   * **Tunnel mode encrypts the entire original packet and adds a new IP header.**
4. **Stateful Firewall State Table:**
   * If an internal host initiates an outbound TCP connection, return packets from that specific external host and port are **automatically permitted** without needing an explicit inbound rule because they match an active entry in the state table.
5. **Cisco ESA primary function:**
   * Email hygiene: filtering spam, detecting phishing, analyzing malicious attachments, and preventing outbound data leakage (DLP).
