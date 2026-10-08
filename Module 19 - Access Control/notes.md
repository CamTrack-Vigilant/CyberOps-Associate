# Module 19: Access Control - Study & Test Revision Guide

**Course:** Cisco Certified CyberOps Associate (CBROPS 200-201)  
**Curriculum Alignment:** Cisco Networking Academy (NetAcad) Module 19  
**Core Objective:** Master Authentication, Authorization, and Accounting (AAA), access control models (DAC, MAC, RBAC, ABAC), the TACACS+ vs. RADIUS architectural differences, and 802.1X Network Access Control.

---

## 19.0 Introduction to Access Control
Access control ensures that only authenticated and authorized users, devices, and applications can access network infrastructure and data. It forms the foundational gatekeeper for enterprise security.

---

## 19.1 The AAA Framework & Authentication Factors

### 1. The AAA Pillars
* **Authentication (Who are you?):** Proves identity via credentials (username/password, certificate, biometric).
* **Authorization (What can you do?):** Enforces specific privileges, permissions, and service access limits once authenticated (e.g., privilege level 15 vs. read-only guest).
* **Accounting (What did you do?):** Logs and tracks user activities, command history, session durations, and transferred bytes for auditing and compliance.

### 2. Multi-Factor Authentication (MFA)
MFA requires **two or more distinct factors** from different categories:
1. **Something You Know:** Password, passphrase, PIN.
2. **Something You Have:** Smart card, hardware token (YubiKey), smartphone authenticator app (TOTP), SMS OTP.
3. **Something You Are:** Biometric (fingerprint, facial recognition, retina scan).
4. **Somewhere You Are (Contextual):** Physical GPS location, internal enterprise IP range.

*Exam Alert:* Providing a password and a PIN is **NOT** two-factor authentication; both are "Something You Know" (Single factor).

---

## 19.2 Access Control Models (High-Yield Test Matching)

| Access Model | Decision Authority | Basis of Access | Typical Implementation |
| :--- | :--- | :--- | :--- |
| **DAC (Discretionary Access Control)** | **Resource Owner** (Data creator) | Discretion of the creator; sets Read/Write/Execute permissions. | Standard Windows NTFS permissions, Linux file permissions (`chmod`). |
| **MAC (Mandatory Access Control)** | **Central Security Policy / System** | Sensitivity labels (Top Secret, Secret, Confidential) vs. User Security Clearance. | Military systems, **SELinux**, trusted operating systems. |
| **RBAC (Role-Based Access Control)** | **System Administrator** | User's **job function or role** in the organization (e.g., HR, Auditor, Tier-1 Analyst). | Active Directory Security Groups, enterprise ERP systems. |
| **ABAC (Attribute-Based Access Control)** | **Dynamic Policy Engine** | Evaluates dynamic attributes: User, Resource, Action, and **Environment (time of day, device health, location)**. | Next-Gen Cloud IAM, Cisco ISE TrustSec. |

---

## 19.3 AAA Protocols: TACACS+ vs. RADIUS (The #1 Most Tested Topic)

Every Cisco CyberOps exam tests the exact architectural differences between TACACS+ and RADIUS:

| Feature / Attribute | TACACS+ (Terminal Access Controller Access-Control System Plus) | RADIUS (Remote Authentication Dial-In User Service) |
| :--- | :--- | :--- |
| **Standard Origin** | Cisco proprietary (later published as RFC 8907) | IETF Open Standard (RFC 2865 / 2866) |
| **Transport Protocol & Port** | **TCP Port 49** (Reliable transport) | **UDP Ports 1812 (Auth) / 1813 (Acct)** *(Legacy: 1645 / 1646)* |
| **Packet Encryption** | **Encrypts the ENTIRE packet payload** (everything except the TACACS+ header) | **Encrypts ONLY the password field**; usernames, attributes, and accounting are cleartext |
| **Separation of AAA** | **Strictly separates** Authentication, Authorization, and Accounting as distinct processes | **Combines** Authentication and Authorization into a single exchange |
| **Granular Command Authorization** | **Yes** (inspects and authorizes individual commands on per-keystroke basis) | Limited / Weak per-command authorization |
| **Primary Use Case** | **Device Administration** (securing CLI access to routers, switches, firewalls) | **Network Access Control** (802.1X Wi-Fi access, VPN endpoints, 802.1AE) |

---

## 19.4 Network Access Control (802.1X & Port Security)

### 1. IEEE 802.1X Architecture
802.1X defines port-based network access control to prevent unauthorized devices from connecting to physical switch ports or wireless networks.

```
[ Supplicant ] ────── (EAPoL) ──────> [ Authenticator ] ────── (RADIUS) ──────> [ Auth Server ]
(Workstation /                         (Switch / AP)                             (Cisco ISE /
 Phone)                                Port is BLOCKED                            RADIUS)
                                       until auth passes
```

* **Supplicant:** The software client running on the user device requesting access.
* **Authenticator:** The intermediary network device (Switch or Wireless LAN Controller). Holds the port in an unauthorized/blocked state, permitting only **EAPoL (EAP over LAN)** traffic until approved.
* **Authentication Server:** Centralized database (Cisco ISE, FreeRADIUS) that validates user credentials and returns an accept/reject packet.
* **EAP (Extensible Authentication Protocol):**
  * *EAP-TLS:* Highest security; requires **digital certificates on both the server and client**.
  * *PEAP (Protected EAP):* Requires server-side certificate; authenticates user via encrypted MS-CHAPv2 tunnel (common enterprise standard).

### 2. Cisco Switch Port Security
Restricts switch port access based on the connecting device's MAC address:
* **Static MAC:** Manually configured by administrator (`switchport port-security mac-address <MAC>`).
* **Dynamic MAC:** Learned dynamically and stored only in the MAC table (cleared at reboot).
* **Sticky MAC:** Learned dynamically and automatically written to the `running-config` in NVRAM (`switchport port-security mac-address sticky`).
* **Violation Modes (When an unauthorized MAC connects):**
  * **Protect:** Drops frames from unauthorized MACs. **No syslog alert, no counter increment.**
  * **Restrict:** Drops frames from unauthorized MACs. **Generates syslog alert, increments violation counter.**
  * **Shutdown (Default):** Drops frames, generates syslog, and **immediately disables the port (err-disable state)**. Port LED turns amber; requires admin `shutdown` / `no shutdown` to recover.

---

## 19.5 High-Yield Test & Exam Review (Trap Alerts)

1. **Which protocol encrypts the ENTIRE packet payload except the header?**
   * **TACACS+** (uses TCP Port 49).
2. **Which protocol encrypts ONLY the password field?**
   * **RADIUS** (uses UDP Ports 1812/1813).
3. **What are the three components of an 802.1X implementation?**
   * **Supplicant** (Client), **Authenticator** (Switch/AP), and **Authentication Server** (Cisco ISE / RADIUS).
4. **What does the default Port Security violation mode (Shutdown) do?**
   * It puts the port into an **err-disable state** and shuts down the interface.
5. **Which access control model relies on security labels (e.g., Top Secret)?**
   * **MAC (Mandatory Access Control)**.
6. **What is the difference between Sticky MAC and Dynamic MAC?**
   * Dynamic MAC is lost on reboot; **Sticky MAC is saved into the switch's running configuration**.
