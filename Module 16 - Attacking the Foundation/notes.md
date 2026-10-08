# Module 16: Attacking the Foundation - Study & Test Revision Guide

**Course:** Cisco Certified CyberOps Associate (CBROPS 200-201)  
**Curriculum Alignment:** Cisco Networking Academy (NetAcad) Module 16  
**Core Objective:** Understand how foundational Layer 3 (IP, ICMP) and Layer 4 (TCP, UDP) protocols lack built-in security, and analyze specific protocol abuse techniques.

---

## 16.0 Introduction
The original TCP/IP protocol suite was engineered in the 1970s for operational survivability and trust, with virtually no built-in encryption, authentication, or anti-spoofing mechanisms. This chapter examines how adversaries exploit these structural design flaws at the foundation of networking.

---

## 16.1 IP (Internet Protocol) Vulnerabilities & Header Abuse

### 1. IP Address Spoofing
* **What it is:** The attacker modifies the 32-bit Source IP address field in the IPv4 header to impersonate another host.
* **Blind Spoofing:** Attacker sends packets with spoofed source IPs without being able to see the return traffic. Used primarily for DoS attacks (e.g., SYN floods, Smurf attacks, reflection attacks).
* **Non-Blind Spoofing:** Attacker resides on the same broadcast domain or along the routing path, allowing them to inspect replies, predict sequence numbers, and hijack sessions.

### 2. IP Fragmentation Attacks
Because different network links have different **Maximum Transmission Units (MTU)** (typically 1500 bytes for Ethernet), IPv4 routers divide oversized packets into smaller fragments using three header fields: **Identification (16 bits)**, **Flags (3 bits: Reserved, DF - Don't Fragment, MF - More Fragments)**, and **Fragment Offset (13 bits)**.

* **Teardrop Attack:** The attacker sends overlapping, oversized IP fragments with manipulated offset values. When the victim OS attempts to reassemble the fragments into memory, an integer underflow occurs, crashing the kernel (Blue Screen of Death).
* **Tiny Fragment Attack:** The attacker fragments the TCP header across multiple tiny IP packets so that the TCP port numbers (which firewalls filter on) are pushed into the second fragment, bypassing stateless packet-filtering firewalls.
* **Fragment Buffer Exhaustion:** Sending millions of incomplete fragmented packets where the final fragment is never sent, forcing the victim server to exhaust memory waiting for reassembly timeouts.

---

## 16.2 TCP & UDP Protocol Exploitation

### 1. TCP Handshake & Connection Vulnerabilities
TCP is a connection-oriented, stateful transport protocol that uses sequence and acknowledgment numbers to track bytes.

* **TCP SYN Flood:** Exhausts the target's half-open connection backlog table by flooding `SYN` packets with spoofed source IPs, never completing the third leg (`ACK`) of the handshake.
* **TCP Reset (RST) Attack:**
  * The `RST` control bit immediately terminates an active TCP connection without a graceful 4-way FIN close.
  * *Attack:* An attacker on the path snoops or guesses the 4-tuple (Source/Dest IP and Ports) and valid TCP Sequence Number, then forges a packet with the `RST` flag set, abruptly dropping the legitimate user's session (e.g., terminating an SSH session, BGP routing peering, or Tor circuit).
* **TCP Session Hijacking:**
  * Attacker predicts the **TCP Sequence Number (SEQ)** used between a client and server.
  * Once authenticated, the attacker floods the client with packets to desynchronize it, and forges packets with the correct SEQ numbers to execute unauthorized commands as the authenticated client.

### 2. UDP Vulnerabilities
* **Connectionless & Unreliable:** UDP does not use a handshake, maintains no state table, has no sequence numbers, and provides zero verification of source identity.
* **UDP Flood:** Floods a target server with arbitrary UDP packets across randomized destination ports (e.g., ports 1024–65535). The victim server must check for applications on each port, find none, and generate an `ICMP Port Unreachable` packet, exhausting server CPU and outbound bandwidth.
* **UDP Port Scanning Behavior:**
  * If a target UDP port is **Closed:** Target responds with an **ICMP Type 3, Code 3 (Destination Unreachable: Port Unreachable)**.
  * If a target UDP port is **Open:** Target either responds with application-layer data (e.g., DNS reply) or **silently ignores** the packet (no ICMP returned).

---

## 16.3 ICMP (Internet Control Message Protocol) Exploitation

ICMP (IP Protocol 1) is designed for diagnostic and error messaging, but has no authentication mechanism:

| ICMP Attack | Mechanism | Defensive Countermeasure |
| :--- | :--- | :--- |
| **Ping of Death** | Attacker crafts an IP packet that exceeds the maximum legal IPv4 size (**65,535 bytes**) via malicious fragmentation. When reassembled, it triggers a buffer overflow and system crash. | Modern operating systems patch reassembly buffers; drop packets exceeding 65,535 bytes at edge. |
| **Smurf Attack** | Attacker broadcasts an ICMP Echo Request (Ping) to a subnet's directed broadcast address with the **spoofed source IP of the victim**. All hosts on the subnet reply to the victim. | Disable **directed broadcast** on all router interfaces (`no ip directed-broadcast`). |
| **ICMP Redirect Attack** | Attacker sends a forged **ICMP Type 5 (Redirect)** message claiming a closer, better default gateway exists, rerouting traffic through the attacker's machine for eavesdropping. | Disable ICMP redirects on end hosts and interior routers (`no ip redirects`). |
| **ICMP Router Discovery (IRDP) Spoofing** | Attacker responds to IRDP solicitation messages with fake router advertisement messages, spoofing the default gateway. | Use secure routing protocols or disable IRDP. |
| **ICMP Ping Sweep** | Sending ICMP Echo Requests across an entire subnet (`/24`) to map live IP addresses. | Rate-limit or block ICMP Echo at network perimeters. |

---

## 16.4 High-Yield Test & Exam Review (Trap Alerts)

1. **Which TCP flag is used to tear down an active TCP session abruptly without graceful closure?**
   * The **RST (Reset)** flag.
2. **What Cisco IOS command blocks Smurf attack amplification?**
   * `no ip directed-broadcast` on router interfaces.
3. **What happens when an Nmap UDP scan probes a closed port?**
   * The victim sends an **ICMP Type 3, Code 3 (Port Unreachable)** message.
4. **Why is UDP so frequently used in reflection and DDoS attacks?**
   * Because UDP is **connectionless and lacks sequence validation**, making it trivial to spoof the victim's source IP address.
5. **What is a Teardrop attack?**
   * An IP fragmentation attack where **overlapping fragment offset fields** cause an error when the victim operating system reassembles the packet.
