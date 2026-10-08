# Cisco CyberOps Associate v1.0 — Skills Assessment: Pushdo Trojan Forensic Analysis

**Course**: Cisco Networking Academy &mdash; CyberOps Associate  
**Scenario**: Junior Security Analyst &mdash; Incident Response & Threat Verification  
**Target Subject**: Pushdo Trojan (`gerv.gun`, `trow.exe`, `wp.exe`)  
**Environment**: Security Onion VM (Sguil, Kibana, NetworkMiner, Wireshark, Bro/Zeek)  
**Investigation Date**: October 2026  

---

## Part 1: Gather the Basic Information

### Step 1: Verify the Status of Services

1. **Credentials**: Log into Security Onion VM with username `analyst` and password `cyberops`.
2. **Service Verification**: Open a terminal and run `sudo so-status` to ensure all sensor and analysis daemons are active:
   ```bash
   analyst@SecOnion:~$ sudo so-status
   Status: securityonion
     * sguil server                                                       [  OK  ]
   Status: seconion-import
     * pcap_agent (sguil)                                                 [  OK  ]
     * snort_agent-1 (sguil)                                              [  OK  ]
     * barnyard2-1 (spooler, unified2 format)                             [  OK  ]
   Status: Elastic stack
     * so-elasticsearch                                                   [  OK  ]
     * so-logstash                                                        [  OK  ]
     * so-kibana                                                          [  OK  ]
     * so-freqserver                                                      [  OK  ]
   ```
3. **Launch Sguil**: Open Sguil via the desktop shortcut, log in as `analyst` / `cyberops`, click **Select All**, and click **Start SGUIL**.

---

### Step 2: Gather Basic Information

#### a. Attack Time Frame
* **Date & Time Range**: **`2017-06-27 from 13:38:34 to 13:44:32 UTC`**  
  *(HTTP GET payload request began at `13:38:32 UTC`; the final Tor SSL alert concluded at `13:44:32 UTC`)*

#### b. Alerts Observed During Time Frame
* `ET CURRENT_EVENTS WinHttpRequest Downloading EXE`
* `ET POLICY PE EXE or DLL Windows file download HTTP`
* `ET CURRENT_EVENTS Terse alphanumeric executable downloader high likelihood of being hostile`
* `ET POLICY External IP Lookup Domain (myip.opendns .com in DNS lookup)`
* `ET TROJAN Backdoor.Win32.Pushdo.s Checkin`
* `ET TROJAN Pushdo.S CnC response`
* `ET POLICY TLS possible TOR SSL traffic`

#### c. Involved IP Addresses
* **Internal IP (Victim Host)**:
  * `192.168.1.96` &mdash; Compromised Windows PC (`FlashGordon-PC`)
* **External IPs (Malware Delivery & C2 Infrastructure)**:
  * `119.28.70.207` &mdash; Serves `matied.com` (`/gerv.gun`) & `centler.at`
  * `145.131.10.21` &mdash; Serves `lounge-haarstudio.nl` (`/oud/trow.exe`)
  * `143.95.151.192` &mdash; Serves `vantagepointtechnologies.com` (`/wp.exe`)
  * `208.67.222.222` &mdash; OpenDNS Resolver (queried for `myip.opendns.com`)
  * `198.1.85.250` &mdash; Pushdo Trojan C2 Check-in Server (Port 80)
  * `62.210.140.158` &mdash; Pushdo C2 Command & Control Response Server
  * `208.83.223.34` &mdash; External Tor SSL / TLS endpoint

---

## Part 2: Learn about the Exploit

### Step 1: Infected Host Analysis

#### a. Host Network Identifiers
* **IP Address**: `192.168.1.96`
* **MAC Address**: `00:15:C5:DE:C7:3B`
* **NIC Vendor**: **Dell Inc.** (OUI `00:15:C5` belongs to Dell Inc.)
* **Host Name**: `FlashGordon-PC` *(from NetBIOS/DHCP)*
* *How to view*: In Sguil, right-click Alert ID **5410** &rarr; Select **NetworkMiner** &rarr; Open **Hosts** tab.

#### b. Infection Timestamp & Mechanism
* **Timestamp**: **`2017-06-27 13:38:32 UTC`**
* **Infection Flow**:
  1. The user on host `192.168.1.96` browsed to `matied.com/gerv.gun` via the Windows `WinHttpRequest` library.
  2. The downloaded file **`gerv.gun`** was an executable disguised with a `.gun` extension.
  3. Once executed, **Pushdo** functioned as a **downloader trojan**:
     - It gathered host telemetry: admin privileges, primary drive serial number (`SMART_RCV_DRIVE_DATA`), NTFS filesystem status, and Windows version (`GetVersionEx`).
     - It reported back to remote C2 servers listening on TCP port 80 (masquerading as Apache web servers).
     - It downloaded secondary malware payloads based on URL arguments.

---

### Step 2: Examine the Exploit

#### a. Downloaded Payloads and Hashes
| File Name | Domain & Full URI | SHA-256 Hash | File Architecture |
| :--- | :--- | :--- | :--- |
| **`gerv.gun`** | `matied.com/gerv.gun` | `0931537889c35226d00ed26962ecacb140521394279eb2ade7e9d2afcf1a7272` | PE32 Executable (Intel 386, 236 KB) |
| **`trow.exe`** | `lounge-haarstudio.nl/oud/trow.exe` | `94a0a09ee6a21526ac34d41eabf4ba603e9a30c26e6a1dc072ff45749dfb1fe1` | PE32 Executable (Intel 386, 323 KB) |
| **`wp.exe`** | `vantagepointtechnologies.com/wp.exe` | `79d503165d32176842fe386d96c04fb70f6ce1c8a485837957849297e625ea48` | PE32 Executable (Intel 386, 300.5 KB) |

*(Note: In NetworkMiner, select the **Files** tab, right-click the line &rarr; **Calculate MD5 / SHA1 / SHA256 hash**).*

#### b. Threat Intelligence (VirusTotal) Verification
1. **`gerv.gun` (`09315378...`)**:
   * **Detections**: 58+ AV security engines flag it as malicious.
   * **Classification**: `Win32.Trojan.Pushdo` / `Trojan:Win32/Wacatac`.
   * **Aliases**: `test`, `tmp523799.697`, `vector.tui`.
2. **`trow.exe` (`94a0a09e...`)**:
   * **Detections**: 63+ AV security engines flag it as malicious.
   * **Classification**: `Win32.Trojan.Cutwail` / `Trojan.GenericKD`.
   * **Aliases**: `Pedals.exe`, `trow.exe`, `bma2beo4.exe`.
3. **`wp.exe` (`79d50316...`)**:
   * **Detections**: 55+ AV security engines flag it as malicious.
   * **Classification**: `Win32.Malware-gen` / `Trojan.Downloader`.
   * **Aliases**: `wp.exe`, `test2`, `test_3`.

#### c. Additional Alerts & Network Evasion
1. **External IP Lookup**: `ET POLICY External IP Lookup Domain (myip.opendns .com in DNS lookup)` &rarr; `208.67.222.222:53`.  
   *Note: `myip.opendns.com` is a legitimate OpenDNS IP reflection service queried by the malware to determine the host's external WAN IP address for geolocation.*
2. **Decoy Traffic Flooding**: Immediately following C2 check-in at `13:44:01`, Pushdo flooded the network with rapid HTTP requests to hundreds of benign, legitimate websites (`vivastay.com`, `hazmatt.com`, `kursavto.ru`, `themark.org`) to generate noise and conceal genuine C2 callbacks.
3. **Tor Encryption**: Alert `ET POLICY TLS possible TOR SSL traffic` directed to `208.83.223.34` indicated encrypted outbound tunnel establishment.

---

### Step 3: Executive Incident Report Summary

> **SOC Incident Response Executive Summary**:  
> On **June 27, 2017, between 13:38:34 and 13:44:32 UTC**, internal workstation **`192.168.1.96`** (`FlashGordon-PC`, MAC `00:15:C5:DE:C7:3B`, Dell Inc.) was compromised by the **Pushdo Trojan** downloader.  
>  
> The infection originated from a drive-by download of **`gerv.gun`** from `matied.com`. Upon execution, Pushdo collected local hardware/OS telemetry, discovered its external WAN IP via OpenDNS (`208.67.222.222`), and established C2 communications with `198.1.85.250` and `62.210.140.158` over port 80.  
>  
> Pushdo subsequently retrieved two secondary malicious binaries: **`trow.exe`** (from `lounge-haarstudio.nl`) and **`wp.exe`** (from `vantagepointtechnologies.com`). All three payloads were confirmed as critical threats on VirusTotal (55+ detections each). To hinder network detection, the malware flooded the network with rapid HTTP GET requests to random benign sites while initiating encrypted Tor SSL communication with `208.83.223.34`.  
>  
> **Recommended Remediation Actions**:  
> 1. Isolate host `192.168.1.96` from the production VLAN immediately.  
> 2. Implement egress blocks on the perimeter firewall and DNS sinkholes for all identified malicious IPs (`119.28.70.207`, `145.131.10.21`, `143.95.151.192`, `198.1.85.250`, `62.210.140.158`) and domains.  
> 3. Perform volatile memory dump and forensic disk acquisition, followed by a complete operating system rebuild.
