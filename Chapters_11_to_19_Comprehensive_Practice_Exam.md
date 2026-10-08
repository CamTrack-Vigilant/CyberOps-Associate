# Cisco CyberOps Associate: Chapters 11 to 19 Comprehensive Practice Exam

**Coverage:** Module 11 to Module 19 (NetAcad Curriculum)  
**Total Questions:** 45 Questions (5 High-Yield Questions Per Module)  
**Format:** Multiple Choice with Detailed Explanations & Exam Trap Tips  

---

## 📑 Module 11: Network Communication Devices

### Q1. What action does a Layer 2 switch take when it receives a frame with an unknown destination MAC address?
* A) It drops the frame and sends an ICMP destination unreachable message.
* B) It forwards the frame only to the default gateway router.
* C) It floods the frame out of all ports within the same VLAN except the port on which the frame arrived.
* D) It buffers the frame until an ARP broadcast is resolved.
> **Correct Answer:** **C**  
> **Explanation:** If a destination MAC address is not present in the switch's MAC Address Table (CAM table), the switch treats it as an "unknown unicast" and floods it out all active ports in the same broadcast domain (VLAN) except the ingress port.

### Q2. Which 802.11 wireless standard feature was introduced in WPA3 to eliminate vulnerability to offline dictionary attacks?
* A) Pre-Shared Key (PSK)
* B) Simultaneous Authentication of Equals (SAE)
* C) Temporal Key Integrity Protocol (TKIP)
* D) Counter Mode Cipher Block Chaining MAC Protocol (CCMP)
> **Correct Answer:** **B**  
> **Explanation:** WPA3 replaces the vulnerable PSK exchange with SAE (Simultaneous Authentication of Equals, based on Dragonfly handshake), which prevents attackers from capturing the 4-way handshake and performing offline brute-force attacks.

### Q3. How many non-overlapping channels exist in the 2.4 GHz wireless spectrum under standard North American / European regulatory domains?
* A) 14
* B) 11
* C) 3 (Channels 1, 6, and 11)
* D) 5 (Channels 1, 3, 6, 9, and 11)
> **Correct Answer:** **C**  
> **Explanation:** In the 2.4 GHz band, each channel is 20 MHz or 22 MHz wide with only 5 MHz spacing between channel centers. Consequently, only channels 1, 6, and 11 can operate simultaneously without adjacent channel interference.

### Q4. An administrator types `copy running-config startup-config` on a Cisco switch. Between which storage media is data transferred?
* A) From Flash to NVRAM
* B) From ROM to RAM
* C) From RAM to NVRAM
* D) From NVRAM to Flash
> **Correct Answer:** **C**  
> **Explanation:** The active configuration (`running-config`) resides in volatile RAM. The saved boot configuration (`startup-config`) resides in Non-Volatile RAM (NVRAM), which persists across power cycles.

### Q5. Which command mode on a Cisco device is indicated by the prompt `Router(config-if)#`?
* A) User EXEC Mode
* B) Privileged EXEC Mode
* C) Global Configuration Mode
* D) Interface Configuration Mode
> **Correct Answer:** **D**  
> **Explanation:** `Router(config-if)#` indicates specific interface configuration sub-mode, accessed from global configuration via `interface <name>`.

---

## 📑 Module 12: Network Security Infrastructure

### Q6. At which layer of the Cisco 3-tier hierarchical network design model should Access Control Lists (ACLs) and packet filtering be avoided to ensure ultra-low latency?
* A) Access Layer
* B) Distribution Layer
* C) Core Layer
* D) Core and Access Layers
> **Correct Answer:** **C**  
> **Explanation:** The Core layer is the high-speed backbone designed solely for rapid, redundant packet forwarding. Packet filtering, ACLs, and CPU-intensive operations belong at the Distribution layer.

### Q7. What fundamental security capability does the IPsec Encapsulating Security Payload (ESP) protocol provide that the Authentication Header (AH) protocol does NOT?
* A) Data integrity verification
* B) Data confidentiality (Encryption)
* C) Anti-replay protection
* D) Data origin authentication
> **Correct Answer:** **B**  
> **Explanation:** AH (IP protocol 51) provides only authentication and integrity; it does NOT encrypt the payload. ESP (IP protocol 50) provides encryption (confidentiality) in addition to integrity and authentication.

### Q8. How does a stateful firewall handle inbound return traffic from an external web server that matches an active outbound TCP connection initiated by an internal client?
* A) It drops the packet unless an explicit inbound ACL rule permits port 80.
* B) It forwards the packet directly to the DMZ for inspection.
* C) It dynamically permits the packet because it matches an established entry in its State Table.
* D) It converts the packet to an ICMP redirect message.
> **Correct Answer:** **C**  
> **Explanation:** Stateful firewalls track TCP handshakes, sequence numbers, and IP/port pairs in a dynamic State Table. Inbound packets matching an active state entry are permitted automatically.

### Q9. Which Cisco security appliance is specifically engineered to analyze email reputation, prevent spam, and protect against malicious attachments and outbound data loss?
* A) Cisco Web Security Appliance (WSA)
* B) Cisco Identity Services Engine (ISE)
* C) Cisco Email Security Appliance (ESA)
* D) Cisco Adaptive Security Appliance (ASA)
> **Correct Answer:** **C**  
> **Explanation:** Cisco ESA provides comprehensive email hygiene, phishing detection, anti-spam, and Data Loss Prevention (DLP) for SMTP traffic.

### Q10. What is the primary difference between IPsec Transport Mode and Tunnel Mode?
* A) Transport mode encrypts the entire original IP packet; Tunnel mode encrypts only the payload.
* B) Transport mode leaves the original IP header unencrypted; Tunnel mode encrypts the entire original packet and adds a new IP header.
* C) Transport mode is used for site-to-site VPNs; Tunnel mode is used only for LANs.
* D) Transport mode requires AH; Tunnel mode requires ESP.
> **Correct Answer:** **B**  
> **Explanation:** Transport mode protects only the payload and is used for host-to-host links. Tunnel mode encapsulates the original IP header and payload into a new IP packet, which is mandatory for site-to-site VPNs.

---

## 📑 Module 13: Attackers and Their Tools

### Q11. Which classification describes a threat actor motivated primarily by ideological, religious, or political causes who launches DDoS attacks or defaces websites?
* A) Script Kiddie
* B) Vulnerability Broker
* C) Hacktivist
* D) State-Sponsored APT
> **Correct Answer:** **C**  
> **Explanation:** Hacktivists utilize cyber attacks (e.g., website defacements, data leaks, DDoS) to promote political or social agendas.

### Q12. What distinct operational characteristic separates a State-Sponsored Advanced Persistent Threat (APT) from an amateur cybercriminal?
* A) APTs only utilize automated public scripts from GitHub.
* B) APTs exhibit long dwell times, stealthy persistence, and military/governmental backing.
* C) APTs demand immediate ransom payments in Bitcoin.
* D) APTs target only wireless access points.
> **Correct Answer:** **B**  
> **Explanation:** State-sponsored APTs focus on stealth, geopolitical intelligence gathering, and maintaining multi-month/multi-year persistent access inside target networks.

### Q13. An analyst needs to perform an offline password attack on a captured Windows SAM database file. Which tool is designed specifically for this purpose?
* A) Hydra
* B) Medusa
* C) John the Ripper
* D) Nmap
> **Correct Answer:** **C**  
> **Explanation:** John the Ripper (and Hashcat) are offline password crackers that crack hashes locally using wordlists, rules, and brute-force. Hydra and Medusa are *online* network password attack tools.

### Q14. What type of tool is Nessus or OpenVAS?
* A) Packet Crafter
* B) Vulnerability Scanner
* C) Wireless Sniffer
* D) Binary Disassembler
> **Correct Answer:** **B**  
> **Explanation:** Nessus and OpenVAS scan network targets to discover unpatched services and known CVE vulnerabilities.

### Q15. How do Rainbow Tables accelerate the password cracking process in tools like Ophcrack?
* A) By using live brute-force over the network with multiple threads.
* B) By querying an online active database server.
* C) By utilizing precomputed cryptographic hash tables to trade storage space for time.
* D) By bypassing the operating system kernel.
> **Correct Answer:** **C**  
> **Explanation:** Rainbow tables store precomputed hashes for millions of plaintext combinations, allowing instantaneous reverse-lookup of hashes by trading storage memory for computation time.

---

## 📑 Module 14: Common Threats and Attacks

### Q16. Which type of malware possesses the capability to self-replicate and spread across networks autonomously without requiring a host file or human intervention?
* A) Macro Virus
* B) Trojan Horse
* C) Worm
* D) Logic Bomb
> **Correct Answer:** **C**  
> **Explanation:** Worms are standalone malicious programs that exploit network vulnerabilities to replicate and spread automatically from system to system without human interaction.

### Q17. During a TCP SYN Flood attack, what specific server resource is exhausted by the attacker?
* A) The DNS resolver cache
* B) The half-open connection backlog queue
* C) The dynamic routing table
* D) The physical NVRAM storage
> **Correct Answer:** **B**  
> **Explanation:** The victim allocates memory in its SYN backlog table for every incoming SYN packet. Because the attacker spoofs source IPs, the final ACK never arrives, filling the queue and blocking legitimate users.

### Q18. How does an attacker amplify traffic in a traditional Smurf attack?
* A) By sending thousands of TCP FIN packets to an open port.
* B) By sending an ICMP Echo Request with the victim's spoofed IP to a subnet's directed broadcast address.
* C) By altering the TTL field in IP headers.
* D) By poisoning the local ARP table of the default gateway.
> **Correct Answer:** **B**  
> **Explanation:** In a Smurf attack, an ICMP Echo Request is sent to a directed broadcast address with the victim's spoofed source IP, causing all hosts on that broadcast domain to flood the victim with replies.

### Q19. An employee receives a personalized email from what appears to be the corporate CEO, urgently demanding a wire transfer to a vendor. What social engineering attack is this?
* A) Vishing
* B) Smishing
* C) Whaling / Spear Phishing
* D) Quid Pro Quo
> **Correct Answer:** **C**  
> **Explanation:** Highly targeted phishing aimed at or impersonating high-profile executives is known as Whaling (or Spear Phishing).

### Q20. What type of malware installs at Ring 0 (kernel level) to hide files, active processes, and network connections from the operating system?
* A) Spyware
* B) Keylogger
* C) Rootkit
* D) Adware
> **Correct Answer:** **C**  
> **Explanation:** Rootkits modify kernel code and system API tables to disguise their presence, making them invisible to standard operating system utilities.

---

## 📑 Module 15: Network Monitoring and Tools

### Q21. Which seven specific attributes define a unique unidirectional flow in Cisco NetFlow?
* A) Source IP, Dest IP, Source Port, Dest Port, Protocol, Ingress Interface, ToS
* B) MAC Address, IP Address, VLAN, TCP Flag, TTL, Payload Size, Window Size
* C) Source IP, Dest IP, Gateway, Subnet Mask, DNS, Hostname, Timestamp
* D) Ingress Interface, Egress Interface, Packet Count, Byte Count, Error Count, CRC, MTU
> **Correct Answer:** **A**  
> **Explanation:** The NetFlow 7-tuple consists of: Source IP, Destination IP, Source Port, Destination Port, Layer 3 Protocol, Ingress Interface, and IP Type of Service (ToS).

### Q22. How many NetFlow flow records are generated when an internal client performs a single, complete HTTP GET exchange with an external web server?
* A) 1 flow record
* B) 2 flow records
* C) 4 flow records
* D) 7 flow records
> **Correct Answer:** **B**  
> **Explanation:** NetFlow is strictly **unidirectional**. The outbound request from client to server constitutes one flow; the return traffic from server to client constitutes a second flow.

### Q23. What critical advantage does a physical Network TAP offer over switch SPAN port mirroring?
* A) TAPs are completely free and require no additional hardware.
* B) TAPs can be configured remotely over an IP management network.
* C) TAPs capture 100% of full-duplex traffic, including corrupted frames and Layer 1/2 errors, without burdening switch CPU.
* D) TAPs automatically decrypt TLS 1.3 traffic.
> **Correct Answer:** **C**  
> **Explanation:** TAPs are dedicated hardware devices that do not drop packets during traffic spikes and capture malformed frames, whereas SPAN drops corrupted frames and impacts switch CPU.

### Q24. What primary operational limitation distinguishes a passive Intrusion Detection System (IDS) from an in-line Intrusion Prevention System (IPS)?
* A) An IDS cannot analyze application layer traffic.
* B) An IDS operates out-of-band and cannot directly block or drop malicious packets in real time.
* C) An IDS introduces significant latency to the production network.
* D) An IDS cannot generate alerts or log events.
> **Correct Answer:** **B**  
> **Explanation:** An IDS analyzes a mirrored copy of traffic out-of-band. Because packets do not flow *through* the IDS, it cannot drop packets; it can only alert or send reactive TCP RSTs.

### Q25. Which open-source platform in the Security Onion suite is dedicated to parsing application protocols into structured, searchable transaction logs (e.g., `http.log`, `dns.log`)?
* A) Snort
* B) Zeek (formerly Bro)
* C) Wireshark
* D) Sguil
> **Correct Answer:** **B**  
> **Explanation:** Zeek is a powerful behavioral analysis engine that translates live network streams into detailed protocol log files.

---

## 📑 Module 16: Attacking the Foundation

### Q26. Which attack abuses the IP fragmentation reassembly process by sending overlapping fragment offset values that crash the victim's operating system?
* A) Teardrop Attack
* B) Smurf Attack
* C) SYN Flood
* D) Ping of Death
> **Correct Answer:** **A**  
> **Explanation:** A Teardrop attack sends overlapping, oversized IP fragments. When the victim OS attempts to reassemble the fragments, memory allocation bugs trigger a system crash.

### Q27. Which TCP control flag can be forged by an on-path attacker to abruptly terminate an active TCP session between two endpoints?
* A) SYN
* B) ACK
* C) RST
* D) URG
> **Correct Answer:** **C**  
> **Explanation:** The RST (Reset) flag immediately breaks a TCP connection without a 4-way FIN handshake.

### Q28. What diagnostic message does a host return when a port scanner sends a UDP datagram to a CLOSED UDP port?
* A) TCP RST packet
* B) ICMP Type 3, Code 3 (Destination Unreachable: Port Unreachable)
* C) ICMP Echo Reply
* D) No response is ever returned for UDP
> **Correct Answer:** **B**  
> **Explanation:** Under RFC 792, if a UDP packet arrives at a closed port, the host operating system generates an ICMP Destination Unreachable (Port Unreachable) error.

### Q29. What is the fundamental vulnerability of the original IPv4 and ICMP protocol design that enables spoofing?
* A) IP addresses are limited to 32 bits.
* B) IP and ICMP headers have no built-in cryptographic authentication or verification of the source IP address.
* C) ICMP packets can only travel 64 hops.
* D) IPv4 requires mandatory IPsec encryption.
> **Correct Answer:** **B**  
> **Explanation:** IPv4 and ICMP headers do not validate whether the sender owns the IP address written in the Source IP field.

### Q30. How does a Ping of Death attack differ from a standard ICMP Flood DoS?
* A) Ping of Death sends packets with a forged TTL.
* B) Ping of Death sends an IP packet whose reassembled size exceeds the maximum legal limit of 65,535 bytes, crashing legacy systems.
* C) Ping of Death requires an open recursive DNS resolver.
* D) Ping of Death floods the network with UDP port 7 packets.
> **Correct Answer:** **B**  
> **Explanation:** Ping of Death exploits an integer overflow by crafting fragmented IP packets that exceed 65,535 bytes when reassembled.

---

## 📑 Module 17: Attacking What We Do

### Q31. Which switch security technology protects against ARP poisoning attacks by validating ARP replies against the DHCP Snooping binding database?
* A) Port Security
* B) Dynamic ARP Inspection (DAI)
* C) BPDU Guard
* D) Storm Control
> **Correct Answer:** **B**  
> **Explanation:** Dynamic ARP Inspection (DAI) intercepts all ARP requests and responses on untrusted ports, verifying valid IP-to-MAC bindings before forwarding.

### Q32. What technique do threat actors use to exfiltrate sensitive data or conduct C2 communications by encoding data inside the subdomain queries of DNS requests?
* A) Fast-Flux DNS
* B) DNS Cache Poisoning
* C) DNS Tunneling
* D) DNS Reflection
> **Correct Answer:** **C**  
> **Explanation:** DNS Tunneling encodes payloads into subdomains (e.g., `<encoded_data>.attacker.com`), allowing data to pass through corporate firewalls that permit outbound port 53.

### Q33. An attacker uses the tool Yersinia to flood a switch with thousands of DHCP Discover packets with random MAC addresses. What attack is being executed?
* A) DHCP Spoofing
* B) DHCP Starvation
* C) Rogue DHCP Server
* D) Smurf Attack
> **Correct Answer:** **B**  
> **Explanation:** DHCP Starvation exhausts the DHCP server's available IP address pool, denying IP leases to legitimate new hosts.

### Q34. An input field in a vulnerable web application accepts the payload `' OR '1'='1 --`. What type of application attack is this?
* A) Cross-Site Scripting (XSS)
* B) Cross-Site Request Forgery (CSRF)
* C) SQL Injection (SQLi)
* D) Buffer Overflow
> **Correct Answer:** **C**  
> **Explanation:** This is a classic SQL Injection payload designed to alter backend database queries, evaluating to TRUE and bypassing authentication.

### Q35. What is the role of DMARC in email security?
* A) It encrypts email message bodies using PGP.
* B) It allows domain owners to specify what policy receiving mail servers should enforce if SPF and DKIM checks fail.
* C) It converts SMTP commands to IMAP over SSL.
* D) It prevents port scanning on port 25.
> **Correct Answer:** **B**  
> **Explanation:** DMARC leverages SPF and DKIM to tell receiving mail exchangers whether to accept, quarantine, or reject unauthorized spoofed emails.

---

## 📑 Module 18: Understanding Defense

### Q36. In SOC alert triage, what term describes the worst-case operational scenario where an actual attack is occurring, but security monitoring systems generate NO alert?
* A) True Positive (TP)
* B) False Positive (FP)
* C) True Negative (TN)
* D) False Negative (FN)
> **Correct Answer:** **D**  
> **Explanation:** A False Negative occurs when malicious activity bypasses sensors undetected, leaving the organization unaware of an intrusion.

### Q37. What metric measures the maximum tolerable duration of system downtime before catastrophic organizational damage occurs?
* A) Recovery Point Objective (RPO)
* B) Recovery Time Objective (RTO)
* C) Mean Time to Acknowledge (MTTA)
* D) Mean Time Between Failures (MTBF)
> **Correct Answer:** **B**  
> **Explanation:** RTO represents the maximum acceptable duration of downtime. RPO represents the maximum acceptable data loss measured in time.

### Q38. Which disaster recovery backup site provides a fully configured facility with real-time synchronized data and redundant hardware that can be brought online in minutes to hours?
* A) Cold Site
* B) Warm Site
* C) Hot Site
* D) Mobile Site
> **Correct Answer:** **C**  
> **Explanation:** A Hot Site is an active duplicate data center with real-time data replication, allowing immediate operational failover.

### Q39. What are the five core continuous functions of the NIST Cybersecurity Framework (CSF)?
* A) Authenticate, Authorize, Audit, Alert, Archive
* B) Identify, Protect, Detect, Respond, Recover
* C) Plan, Do, Check, Act, Report
* D) Prevent, Block, Log, Isolate, Eradicate
> **Correct Answer:** **B**  
> **Explanation:** The NIST CSF core consists of Identify, Protect, Detect, Respond, and Recover.

### Q40. In enterprise security documentation, what is the key difference between a "Standard" and a "Guideline"?
* A) Standards are optional suggestions; Guidelines are legally mandatory.
* B) Standards are mandatory technical baseline requirements; Guidelines are recommended best practices.
* C) Standards are written only for end users; Guidelines are written only for executives.
* D) Standards change daily; Guidelines never change.
> **Correct Answer:** **B**  
> **Explanation:** Standards establish compulsory, measurable baselines. Guidelines provide non-mandatory advice.

---

## 📑 Module 19: Access Control

### Q41. Which statement correctly identifies a key architectural difference between TACACS+ and RADIUS?
* A) TACACS+ uses UDP; RADIUS uses TCP.
* B) TACACS+ encrypts only the password field; RADIUS encrypts the entire packet payload.
* C) TACACS+ uses TCP port 49 and encrypts the entire packet payload; RADIUS uses UDP and encrypts only the password field.
* D) TACACS+ combines authentication and authorization; RADIUS strictly separates them.
> **Correct Answer:** **C**  
> **Explanation:** TACACS+ (TCP port 49) encrypts the entire payload (except header) and separates AAA. RADIUS (UDP 1812/1813) encrypts only the password and combines authentication/authorization.

### Q42. Which access control model grants or restricts access based on classification security labels (e.g., Top Secret, Secret, Confidential) compared against user clearance levels?
* A) Discretionary Access Control (DAC)
* B) Mandatory Access Control (MAC)
* C) Role-Based Access Control (RBAC)
* D) Rule-Based Access Control (RBAC)
> **Correct Answer:** **B**  
> **Explanation:** Mandatory Access Control (MAC) uses centrally defined security labels and clearance levels (e.g., SELinux or military models).

### Q43. In an IEEE 802.1X implementation, what role is played by the local network switch or wireless access point?
* A) Supplicant
* B) Authenticator
* C) Authentication Server
* D) Certificate Authority
> **Correct Answer:** **B**  
> **Explanation:** The switch/AP acts as the Authenticator, controlling physical access and passing EAP authentication packets between the client (Supplicant) and the backend RADIUS server (Authentication Server).

### Q44. An administrator configures switch port security with the `shutdown` violation mode. What happens when an unauthorized device connects?
* A) The switch drops frames silently without logging.
* B) The switch generates a syslog message and increments a counter, but leaves the port active.
* C) The switch immediately places the port into an `err-disable` state and shuts down the interface.
* D) The switch sends a TCP Reset to the host.
> **Correct Answer:** **C**  
> **Explanation:** The default `shutdown` violation mode shuts down the port, sets its status to `err-disable`, increments the counter, and sends a syslog message.

### Q45. An employee uses a username, password, and a 6-digit TOTP code generated by a smartphone authenticator app to log into the corporate VPN. What form of authentication is this?
* A) Single-factor authentication
* B) Two-factor authentication (Something you know + Something you have)
* C) Three-factor authentication
* D) Mandatory Access Control
> **Correct Answer:** **B**  
> **Explanation:** The password is "Something you know" and the smartphone/TOTP generator is "Something you have". This constitutes valid two-factor authentication (2FA/MFA).
