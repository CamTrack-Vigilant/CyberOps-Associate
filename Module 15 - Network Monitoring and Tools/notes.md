# Module 15: Network Monitoring and Tools - Study & Test Revision Guide

**Course:** Cisco Certified CyberOps Associate (CBROPS 200-201)  
**Curriculum Alignment:** Cisco Networking Academy (NetAcad) Module 15  
**Core Objective:** Master network telemetry collection methods (SPAN vs. TAP), flow technologies (NetFlow/IPFIX), and Network Security Monitoring systems (IDS/IPS, SIEM, Security Onion).

---

## 15.0 Introduction
A Security Operations Center cannot defend what it cannot see. SOC analysts rely on two primary telemetry streams: **Full Packet Capture (PCAP)** for microscopic payload inspection, and **Flow-based metadata (NetFlow)** for macroscopic traffic behavior analysis.

---

## 15.1 Telemetry Collection: SPAN vs. Network TAPs

To feed network traffic into an IDS, IPS, or packet recorder, analysts use either Port Mirroring or physical hardware TAPs:

### 1. SPAN (Switched Port Analyzer / Port Mirroring)
* **How it works:** A software feature built into Cisco switches that duplicates traffic from designated source ports/VLANs and forwards it to a destination monitoring port connected to a sensor.
* **Flavors:**
  * **Local SPAN:** Source and destination ports are on the **same physical switch**.
  * **RSPAN (Remote SPAN):** Transports mirrored traffic across multiple switches over a dedicated **RSPAN VLAN** (Layer 2).
  * **ERSPAN (Encapsulated Remote SPAN):** Encapsulates mirrored frames into **GRE (Generic Routing Encapsulation)** packets (IP Protocol 47), routing traffic across Layer 3 networks.
* **Limitations of SPAN:**
  * Consumes switch CPU and bus resources.
  * Drops frames during high traffic volume (switch prioritizes production traffic over SPAN).
  * Drops malformed frames or Layer 1/2 errors (CRC errors, runts, giants).

### 2. Network TAPs (Test Access Points)
* **How it works:** A purpose-built physical hardware device spliced directly into the physical cabling between two network nodes.
* **Passive Optical TAPs:** Use glass splitters for fiber optics. Completely unpowered; splits the light beam (e.g., 70% production, 30% monitor). Zero latency, impossible to hack (no IP address).
* **Active TAPs:** Used for copper cabling; requires power. Features **fail-safe bypass circuitry** (if power fails, the physical link stays closed so traffic continues).

### 3. Comparison Table (High-Yield Test Topic)
| Feature | SPAN (Port Mirroring) | Network TAP |
| :--- | :--- | :--- |
| **Type** | Switch software configuration | Dedicated physical hardware |
| **Cost** | Free (built into switch) | Requires purchasing external hardware |
| **Performance Impact** | Can overload switch CPU; drops frames under load | Zero impact on switch; captures 100% of full-duplex traffic |
| **Corrupted Packets** | Drops Layer 1/2 and CRC errored frames | **Captures all malformed and corrupted frames** |
| **Placement** | Anywhere a manageable switch exists | Spliced in-line at critical network bottlenecks |

---

## 15.2 Flow Analysis: NetFlow & IPFIX

### 1. What is a "Flow"?
In Cisco NetFlow, a network flow is a **unidirectional** sequence of packets sharing the following **7 identical attributes (The 7-Tuple)**:
1. **Source IP Address**
2. **Destination IP Address**
3. **Source Port Number**
4. **Destination Port Number**
5. **Layer 3 Protocol Type** (e.g., TCP, UDP, ICMP)
6. **Ingress Interface**
7. **Type of Service (ToS) / IP Precedence**

*Note:* Because a flow is strictly **unidirectional**, a standard bidirectional TCP conversation generates **two separate NetFlow flow records**.

### 2. NetFlow Architecture Components
* **NetFlow Exporter:** The router, switch, or firewall monitoring packets, building flow cache tables, and transmitting flow records.
* **NetFlow Collector:** A server dedicated to receiving, storing, and parsing binary NetFlow export records (typically over UDP port **2055** or **9996**).
* **NetFlow Analyzer:** The GUI/dashboard analytics tool that visualizes bandwidth trends, top talkers, and anomalous volume spikes.
* **IPFIX (IP Flow Information Export - RFC 7011):** The IETF vendor-neutral international standard based directly on Cisco NetFlow Version 9.

### 3. Full Packet Capture (PCAP) vs. NetFlow
* **NetFlow:** "The phone bill." Tells you who called whom, when, on what port, and for how long. Extremely lightweight storage (megabytes per day).
* **Full PCAP:** "The wiretap / call recording." Contains the actual audio/payload (every single byte). Heavy storage requirements (terabytes per day).

---

## 15.3 Network Security Monitoring Systems (IDS vs. IPS)

### 1. IDS vs. IPS Deployment Modes
```
IN-LINE (IPS):
[Internet] ──> [ Firewall ] ──> [ IN-LINE IPS ] ──> [ Internal Switch ] ──> [ Hosts ]
                                  (Can DROP packets in real-time)

OUT-OF-BAND (IDS):
[Internet] ──> [ Firewall ] ──> [ Internal Switch ] ──> [ Hosts ]
                                        │ (SPAN / Mirror Port)
                                        ▼
                                  [ PASSIVE IDS ]
                                  (Can only ALERT or send TCP Resets)
```

* **IDS (Intrusion Detection System):**
  * Deployed **out-of-band / promiscuous mode** (via SPAN or TAP).
  * Analyzes a *copy* of traffic.
  * **Cannot stop malicious packets directly** (cannot drop packets). Can only generate alerts, log events, or send reactive TCP Reset packets.
* **IPS (Intrusion Prevention System):**
  * Deployed **in-line** directly in the packet path.
  * Packets physically enter one interface and exit another.
  * **Can drop malicious packets in real-time**, terminate TCP sessions, or rewrite packets (scrubbing).
  * *Downside:* Introduces slight latency; if an IPS fails or overloads, network connectivity is blocked.

### 2. Detection Methodologies
* **Signature-Based:** Compares traffic against a database of known exploit byte sequences (rules). Fast, high accuracy, but completely blind to zero-day attacks.
* **Anomaly-Based (Behavioral):** Establishes a baseline of normal network behavior (e.g., typical bandwidth, standard protocols). Alerts on statistical deviations (e.g., sudden spike in SSH traffic at 3 AM). Detects zero-days, but has a higher false-positive rate.
* **Policy-Based:** Alerts on violations of organizational security policies (e.g., an unauthorized Telnet connection on a production subnet).

---

## 15.4 Essential NSM Platforms & Open Source Tools

* **Snort:** The industry-standard open-source signature-based IDS/IPS rule engine developed by Cisco/Sourcefire.
* **Zeek (formerly Bro):** An open-source behavioral analysis platform that parses application-layer protocols into structured transaction logs (`conn.log`, `dns.log`, `http.log`).
* **Suricata:** A modern, multi-threaded IDS/IPS engine supporting hardware acceleration and full PCAP recording.
* **Security Onion:** A specialized Linux distribution for threat hunting that bundles **Snort/Suricata**, **Zeek**, **Sguil**, and the **Elastic Stack (Elasticsearch, Logstash, Kibana)**.
* **SIEM (Security Information and Event Management):** Centralized log aggregation, normalization, and correlation platform (e.g., Splunk, IBM QRadar, Microsoft Sentinel).

---

## 15.5 High-Yield Test & Exam Review (Trap Alerts)

1. **How many NetFlow records are generated by a single complete bidirectional TCP web session?**
   * **Two flow records** (NetFlow is strictly unidirectional).
2. **What happens if a SPAN port experiences excessive bandwidth overload?**
   * The switch **drops SPAN packets** to preserve production switching performance.
3. **What is ERSPAN?**
   * Encapsulated Remote SPAN; encapsulates mirrored packets in **GRE headers** to route across Layer 3 networks.
4. **Passive Optical TAP advantages:**
   * Requires **no electrical power**, introduces **zero latency**, and cannot be hacked over the network.
5. **IDS vs. IPS latency:**
   * IDS adds **zero latency** to production traffic (works on a copy); IPS adds **minimal processing latency** because packets pass in-line.
