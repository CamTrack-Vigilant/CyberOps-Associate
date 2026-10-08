# Module 11: Network Communication Devices - Study & Test Revision Guide

**Course:** Cisco Certified CyberOps Associate (CBROPS 200-201)  
**Curriculum Alignment:** Cisco Networking Academy (NetAcad) Module 11  
**Core Objective:** Master the hardware, architecture, wireless standards, and operating system basics of network communication devices from a security analyst perspective.

---

## 11.0 Introduction to Network Communication Devices
As a CyberOps SOC analyst, you cannot defend a network without understanding the intermediary devices that route, switch, and bridge traffic. Vulnerabilities in device configurations or firmware can lead to traffic eavesdropping, man-in-the-middle attacks, and network-wide downtime.

---

## 11.1 Network Devices & Functions

### 1. End Devices vs. Intermediary Devices
* **End Devices (Hosts):** The source or destination of a message (PCs, laptops, servers, smartphones, IP cameras, VoIP phones).
* **Intermediary Devices:** Interconnect end devices and ensure data flows across the network:
  * **Switches (Layer 2):** Forward frames based on **MAC addresses**. Maintain a **MAC Address Table** (CAM table). Break up **collision domains** per port, but share a single broadcast domain per VLAN.
  * **Routers (Layer 3):** Forward packets based on **IP addresses**. Connect different networks/subnets. Break up both **collision domains** and **broadcast domains**. Maintain a **Routing Table**.
  * **Access Points (APs):** Extend wired networks into wireless signals (Layer 1/2).
  * **Multilayer Switches (Layer 3 Switches):** Combine wire-speed Layer 2 switching with hardware-based Layer 3 IP routing.

### 2. MAC Address Table vs. Routing Table (Critical Exam Distinction)
| Feature | Layer 2 Switch (MAC Table) | Layer 3 Router (Routing Table) |
| :--- | :--- | :--- |
| **PDU Handled** | Frames | Packets |
| **Addressing Used** | Physical MAC Address (48-bit hex) | Logical IP Address (IPv4 32-bit / IPv6 128-bit) |
| **Unknown Destination** | **Floods** frame out all ports except arrival | **Drops** packet (sends ICMP Destination Unreachable) |
| **Broadcast Handling** | Forwards broadcast frames to all VLAN ports | **Drops broadcasts** (does not forward by default) |

---

## 11.2 Wireless Communications (WLANs)

### 1. 802.11 Standards & Frequencies
Wireless networks use radio frequencies defined by the IEEE 802.11 working group:
* **2.4 GHz Band:** Longer range, better obstacle penetration (walls), but crowded (only 3 non-overlapping channels: **1, 6, 11**), prone to interference from microwaves/Bluetooth.
* **5 GHz Band:** Shorter range, higher throughput, significantly more non-overlapping channels (24+ channels), less congestion.

### 2. WLAN Security Protocols
* **WEP (Wired Equivalent Privacy):** Highly insecure, uses static 40-bit/104-bit keys with weak 24-bit Initialization Vectors (IVs). Can be cracked in seconds via IV collisions.
* **WPA (Wi-Fi Protected Access):** Temporary fix using **TKIP** (Temporal Key Integrity Protocol), which dynamically rotates keys. Deprecated.
* **WPA2 (802.11i):** Uses **AES** (Advanced Encryption Standard) with **CCMP** (Counter Mode Cipher Block Chaining Message Authentication Code Protocol). Industry standard.
  * *WPA2-Personal (PSK):* Pre-Shared Key used by home networks. Vulnerable to offline dictionary brute-force attacks if 4-way handshake is captured.
  * *WPA2-Enterprise:* Uses an **802.1X / RADIUS** authentication server; each user has unique credentials (EAP-TLS, PEAP).
* **WPA3:** Modern standard; uses **SAE (Simultaneous Authentication of Equals)** replacing PSK to protect against offline dictionary attacks even with weak passwords, and mandates 192-bit cryptographic suite for Enterprise.

---

## 11.3 Cisco IOS Operating System Basics

### 1. Command Modes Hierarchy
```
User EXEC Mode      [ Switch> ]       Basic monitoring, view status, limited ping
       │
       ▼ (Command: enable)
Privileged EXEC     [ Switch# ]       Full debugging, show running-config, copy, reload
       │
       ▼ (Command: configure terminal)
Global Config       [ Switch(config)# ] System-wide settings (hostname, banner, domain)
       │
       ├── Interface Config   [ Switch(config-if)# ]   IP address, duplex, switchport mode
       ├── Line Config        [ Switch(config-line)# ] Console/VTY remote access passwords
       └── Routing Config     [ Switch(config-router)#] Routing protocol definitions (OSPF)
```

### 2. Essential Configuration Files
* **`startup-config`:** Stored in **NVRAM** (Non-Volatile RAM). Retained across reboots.
* **`running-config`:** Stored in **RAM** (Volatile). Active configuration; lost if power is interrupted without saving.
* **Saving command:** `copy running-config startup-config` or `write memory`.

### 3. Remote Management Security: Telnet vs. SSH
* **Telnet (Port 23):** Unencrypted, transmits usernames, passwords, and commands in cleartext. Trivial to sniff via Wireshark.
* **SSH (Port 22):** Uses asymmetric cryptography for key exchange and symmetric AES encryption for session traffic. Mandatory in secure environments.

---

## 11.4 High-Yield Test & Exam Review (Trap Alerts)

1. **Broadcast Domain vs. Collision Domain:**
   * A switch has **one collision domain per port**, but **one broadcast domain per VLAN**.
   * A router has **one broadcast domain per interface**.
2. **What does a switch do with an unknown unicast frame?**
   * It **floods** the frame out of all ports within the same VLAN, except the port on which it arrived.
3. **WPA2 Enterprise vs. Personal:**
   * Personal uses a single Pre-Shared Key (PSK). Enterprise uses an **802.1X authentication server (RADIUS)** with individual credentials.
4. **Non-overlapping channels in 2.4 GHz:**
   * Channels **1, 6, and 11**. Any other channel combination causes adjacent channel interference.
5. **Which command moves from Privileged EXEC to Global Configuration mode?**
   * `configure terminal` (abbreviated `conf t`).
