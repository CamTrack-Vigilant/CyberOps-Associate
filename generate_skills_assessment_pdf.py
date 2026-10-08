"""
Generate Professional PDF Report for CyberOps Associate v1.0 - Skills Assessment: Pushdo Trojan Analysis
Course: Cisco CyberOps Associate
"""

import os
import subprocess

WORKSPACE_DIR = r"c:\Users\fanele\CyberOps Associate\CyberOps-Associate"
TEMP_DIR = os.environ.get("TEMP", r"C:\Users\fanele\AppData\Local\Temp")
OUTPUT_PDF = os.path.join(WORKSPACE_DIR, "CyberOps_Associate_Skills_Assessment_Pushdo_Trojan.pdf")

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>CyberOps Associate v1.0 - Skills Assessment: Pushdo Trojan Analysis</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

@page {
    size: A4;
    margin: 14mm 12mm 14mm 12mm;
    @top-left {
        content: "Cisco Networking Academy | CyberOps Associate v1.0";
        font-family: 'Inter', sans-serif;
        font-size: 7.5pt;
        font-weight: 700;
        color: #0284c7;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    @top-right {
        content: "Skills Assessment: Pushdo Trojan Forensic Report";
        font-family: 'Inter', sans-serif;
        font-size: 7.5pt;
        color: #64748b;
        font-weight: 500;
    }
    @bottom-left {
        content: "CONFIDENTIAL | INCIDENT RESPONSE INVESTIGATION & THREAT VERIFICATION";
        font-family: 'Inter', sans-serif;
        font-size: 6.5pt;
        color: #94a3b8;
        font-weight: 600;
    }
    @bottom-right {
        content: "Page " counter(page) " of " counter(pages);
        font-family: 'Inter', sans-serif;
        font-size: 7.5pt;
        font-weight: 600;
        color: #0369a1;
    }
}

*, *::before, *::after {
    box-sizing: border-box;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    font-size: 8.5pt;
    line-height: 1.5;
    color: #1e293b;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
}

/* Header & Banner */
.header-container {
    border-bottom: 2.5px solid #0284c7;
    padding-bottom: 10px;
    margin-bottom: 14px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
}

.title-area h1 {
    font-size: 16pt;
    font-weight: 800;
    color: #0f172a;
    margin: 0 0 3px 0;
    letter-spacing: -0.02em;
}

.title-area h2 {
    font-size: 10pt;
    font-weight: 600;
    color: #0284c7;
    margin: 0;
}

.badge-box {
    text-align: right;
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.5pt;
    color: #64748b;
}

.badge-tag {
    display: inline-block;
    padding: 2.5px 7px;
    border-radius: 4px;
    font-weight: 700;
    text-transform: uppercase;
    font-size: 6.5pt;
    margin-bottom: 3px;
}

.badge-blue { background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; }
.badge-green { background: #dcfce7; color: #15803d; border: 1px solid #bbf7d0; }
.badge-red { background: #fee2e2; color: #b91c1c; border: 1px solid #fecaca; }
.badge-purple { background: #f3e8ff; color: #7e22ce; border: 1px solid #e9d5ff; }

/* Section Headers */
h3.section-header {
    font-size: 10.5pt;
    font-weight: 700;
    color: #0f172a;
    border-left: 4px solid #0284c7;
    padding-left: 8px;
    margin: 14px 0 8px 0;
    text-transform: uppercase;
    letter-spacing: 0.03em;
}

h4.subsection-header {
    font-size: 9.5pt;
    font-weight: 700;
    color: #0369a1;
    margin: 10px 0 5px 0;
    display: flex;
    align-items: center;
    gap: 6px;
}

/* Cards & Callouts */
.card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 9px 12px;
    margin-bottom: 9px;
    page-break-inside: avoid;
}

.card-title {
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 4px;
    font-size: 9pt;
}

.alert-box {
    border-radius: 5px;
    padding: 8px 12px;
    margin: 8px 0;
    font-size: 8pt;
    page-break-inside: avoid;
}

.alert-danger {
    background-color: #fef2f2;
    border-left: 4px solid #ef4444;
    color: #991b1b;
}

.alert-info {
    background-color: #f0f9ff;
    border-left: 4px solid #0284c7;
    color: #075985;
}

.alert-success {
    background-color: #f0fdf4;
    border-left: 4px solid #22c55e;
    color: #166534;
}

/* Question & Answer Blocks */
.qa-block {
    margin-bottom: 10px;
    page-break-inside: avoid;
}

.question-text {
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 3px;
    font-size: 8.5pt;
}

.answer-box {
    background-color: #f1f5f9;
    border: 1px solid #cbd5e1;
    border-left: 3.5px solid #0284c7;
    border-radius: 4px;
    padding: 6px 10px;
    color: #0f172a;
    font-size: 8.5pt;
}

.answer-highlight {
    color: #b91c1c;
    font-weight: 700;
}

/* Code Blocks */
pre, code {
    font-family: 'JetBrains Mono', Consolas, monospace;
}

code {
    background-color: #f1f5f9;
    color: #b91c1c;
    padding: 1px 4px;
    border-radius: 3px;
    font-size: 8pt;
}

pre {
    background-color: #0f172a;
    color: #f8fafc;
    padding: 8px 12px;
    border-radius: 5px;
    font-size: 7.5pt;
    line-height: 1.45;
    overflow-x: auto;
    margin: 6px 0;
    page-break-inside: avoid;
}

pre .comment { color: #64748b; }
pre .green { color: #4ade80; }
pre .cyan { color: #38bdf8; }
pre .yellow { color: #fde047; }
pre .red { color: #f87171; }

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    font-size: 8pt;
    page-break-inside: avoid;
}

table th {
    background-color: #0f172a;
    color: #ffffff;
    font-weight: 700;
    text-align: left;
    padding: 6px 8px;
    border: 1px solid #0f172a;
    text-transform: uppercase;
    font-size: 7pt;
    letter-spacing: 0.5px;
}

table td {
    padding: 5px 8px;
    border: 1px solid #e2e8f0;
    vertical-align: top;
}

table tr:nth-child(even) td {
    background-color: #f8fafc;
}

.page-break {
    page-break-before: always;
}

.hash-text {
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.5pt;
    word-break: break-all;
    color: #0f172a;
    font-weight: 600;
}
</style>
</head>
<body>

<!-- Header -->
<div class="header-container">
    <div class="title-area">
        <h1>CyberOps Associate v1.0</h1>
        <h2>Hands-On Skills Assessment: Pushdo Trojan Forensic Analysis</h2>
    </div>
    <div class="badge-box">
        <span class="badge-tag badge-red">Malware Investigation</span><br>
        <span class="badge-tag badge-blue">Security Onion v16.04</span><br>
        Date: October 2026 | Score: 100%
    </div>
</div>

<!-- Introduction & Metadata Box -->
<div class="card" style="background:#f0f9ff; border-color:#bae6fd;">
    <div class="card-title" style="color:#0369a1;">Scenario Overview & Assessment Scope</div>
    <p style="margin:2px 0 4px 0;">
        You are acting as a junior security analyst in a Security Operations Center (SOC). As part of incident response training, you were tasked with determining malicious activity associated with the <strong>Pushdo Trojan</strong> on the company network using a <strong>Security Onion</strong> monitoring environment (Sguil, Kibana, NetworkMiner, and Wireshark) alongside external threat intelligence (VirusTotal).
    </p>
    <div style="font-size:7.5pt; color:#475569; display:flex; justify-content:space-between; margin-top:4px;">
        <span><strong>Target Subject:</strong> Pushdo (Downloader/Cutwail botnet)</span>
        <span><strong>Incident Timeline:</strong> 2017-06-27</span>
        <span><strong>Primary Tools:</strong> Sguil, NetworkMiner, tshark, VirusTotal</span>
    </div>
</div>

<!-- Part 1 -->
<h3 class="section-header">Part 1: Gather the Basic Information</h3>

<h4 class="subsection-header">Step 1: Verify the status of services</h4>
<div class="qa-block">
    <div class="question-text">a. Log into Security Onion VM with username <code>analyst</code> and password <code>cyberops</code>.</div>
    <div class="question-text">b. Open a terminal window. Enter the <code>sudo so-status</code> command to verify that all services are ready.</div>
    <pre><span class="cyan">analyst@SecOnion:~$</span> sudo so-status
<span class="comment">Status: securityonion</span>
  * sguil server                                                       [  <span class="green">OK</span>  ]
<span class="comment">Status: seconion-import</span>
  * pcap_agent (sguil)                                                 [  <span class="green">OK</span>  ]
  * snort_agent-1 (sguil)                                              [  <span class="green">OK</span>  ]
  * barnyard2-1 (spooler, unified2 format)                             [  <span class="green">OK</span>  ]
<span class="comment">Status: Elastic stack</span>
  * so-elasticsearch                                                   [  <span class="green">OK</span>  ]
  * so-logstash                                                        [  <span class="green">OK</span>  ]
  * so-kibana                                                          [  <span class="green">OK</span>  ]
  * so-freqserver                                                      [  <span class="green">OK</span>  ]</pre>
    <div class="question-text">c. Launch Sguil or Kibana using credentials <code>analyst</code> / <code>cyberops</code>. Click <strong>Select All</strong> to select sensor interfaces and click <strong>Start SGUIL</strong>.</div>
</div>

<h4 class="subsection-header">Step 2: Gather basic information</h4>

<div class="qa-block">
    <div class="question-text">a. Identify the time frame of the Pushdo trojan attack, including the date and approximate time.</div>
    <div class="answer-box">
        <span class="answer-highlight">2017-06-27 from 13:38:34 to 13:44:32 UTC</span>
        <div style="font-size:7.5pt; color:#475569; margin-top:2px;">
            The initial HTTP GET payload request occurs at <strong>13:38:32 UTC</strong>. The first NIDS alert triggers at <strong>13:38:34 UTC</strong>, and the final Tor SSL alert concludes at <strong>13:44:32 UTC</strong>.
        </div>
    </div>
</div>

<div class="qa-block">
    <div class="question-text">b. List the alerts noted during this time frame associated with the trojan.</div>
    <div class="answer-box">
        <ul style="margin:2px 0; padding-left:18px;">
            <li><code>ET CURRENT_EVENTS WinHttpRequest Downloading EXE</code></li>
            <li><code>ET POLICY PE EXE or DLL Windows file download HTTP</code></li>
            <li><code>ET CURRENT_EVENTS Terse alphanumeric executable downloader high likelihood of being hostile</code></li>
            <li><code>ET POLICY External IP Lookup Domain (myip.opendns .com in DNS lookup)</code></li>
            <li><code>ET TROJAN Backdoor.Win32.Pushdo.s Checkin</code></li>
            <li><code>ET TROJAN Pushdo.S CnC response</code></li>
            <li><code>ET POLICY TLS possible TOR SSL traffic</code></li>
        </ul>
    </div>
</div>

<div class="qa-block">
    <div class="question-text">c. List the internal IP addresses and external IP addresses involved.</div>
    <div class="answer-box">
        <div style="display:flex; gap:20px;">
            <div style="flex:1;">
                <strong>Internal IP Address (Victim Host):</strong>
                <ul style="margin:2px 0; padding-left:18px;">
                    <li><code>192.168.1.96</code> (Infected Windows Workstation)</li>
                </ul>
            </div>
            <div style="flex:1.5;">
                <strong>External IP Addresses (Infrastructure & C2):</strong>
                <ul style="margin:2px 0; padding-left:18px;">
                    <li><code>119.28.70.207</code> &mdash; Serves <code>matied.com</code> (<code>/gerv.gun</code>) & <code>centler.at</code></li>
                    <li><code>145.131.10.21</code> &mdash; Serves <code>lounge-haarstudio.nl</code> (<code>/oud/trow.exe</code>)</li>
                    <li><code>143.95.151.192</code> &mdash; Serves <code>vantagepointtechnologies.com</code> (<code>/wp.exe</code>)</li>
                    <li><code>208.67.222.222</code> &mdash; OpenDNS Resolver (DNS query for <code>myip.opendns.com</code>)</li>
                    <li><code>198.1.85.250</code> &mdash; Pushdo Trojan C2 Check-in Server (Port 80)</li>
                    <li><code>62.210.140.158</code> &mdash; Pushdo C2 Command & Control Response Server</li>
                    <li><code>208.83.223.34</code> &mdash; External Tor SSL / TLS endpoint</li>
                </ul>
            </div>
        </div>
    </div>
</div>

<!-- Page Break for Clean Presentation -->
<div class="page-break"></div>

<!-- Part 2 -->
<h3 class="section-header">Part 2: Learn about the Exploit</h3>

<h4 class="subsection-header">Step 1: Infected Host</h4>

<div class="qa-block">
    <div class="question-text">a. Based on the alerts, what is the IP and MAC addresses of the infected computer? Based on the MAC address, what is the vendor of the NIC chipset?</div>
    <div class="answer-box">
        <span class="answer-highlight">IP Address: 192.168.1.96</span><br>
        <span class="answer-highlight">MAC Address: 00:15:C5:DE:C7:3B</span><br>
        <span class="answer-highlight">NIC Vendor: Dell Inc.</span> (OUI <code>00:15:C5</code> belongs to Dell Inc.)<br>
        <span style="font-size:7.5pt; color:#475569;"><em>(Host Name identified via NetBIOS/DHCP packets: <strong>FlashGordon-PC</strong>)</em></span>
        <div style="font-size:7.5pt; color:#334155; margin-top:3px;">
            <strong>Verification Method:</strong> In Sguil, right-click Alert ID <strong>5410</strong> &rarr; Select <strong>NetworkMiner</strong> &rarr; Open the <strong>Hosts</strong> tab and inspect the <code>192.168.1.96</code> entry.
        </div>
    </div>
</div>

<div class="qa-block">
    <div class="question-text">b. Based on the alerts, when (date and time in UTC) and how was the PC infected? How did the malware infect the PC?</div>
    <div class="answer-box">
        <span class="answer-highlight">Infection Timestamp: 2017-06-27 13:38:32 UTC</span><br>
        <strong>Infection Vector & Mechanism:</strong>
        <p style="margin:3px 0;">
            The user on <code>192.168.1.96</code> initiated an HTTP connection via the Windows <code>WinHttpRequest</code> library to <code>matied.com/gerv.gun</code>. The downloaded payload <strong><code>gerv.gun</code></strong> was a compiled Windows 32-bit PE executable masquerading under a non-standard file extension.
        </p>
        <p style="margin:3px 0;">
            Once executed, <strong>Pushdo</strong> functioned as a <strong>downloader trojan</strong>. Pushdo reports back to hardcoded command-and-control (C2) servers over TCP port 80, masquerading as an Apache web server. Before requesting additional malware, Pushdo harvests detailed host intelligence, including:
        </p>
        <ul style="margin:2px 0; padding-left:18px; font-size:8pt;">
            <li>Victim user administrative privilege status.</li>
            <li>Primary hard drive hardware serial number (queried via <code>SMART_RCV_DRIVE_DATA</code> IO control code).</li>
            <li>Filesystem type check (determining if the system is NTFS).</li>
            <li>Windows operating system version (retrieved via the <code>GetVersionEx</code> Win32 API call).</li>
            <li>Execution counter tracking how many times Pushdo has run on the endpoint.</li>
        </ul>
    </div>
</div>

<h4 class="subsection-header">Step 2: Examine the Exploit</h4>

<div class="qa-block">
    <div class="question-text">a. Based on the alerts associated with HTTP GET requests, what files were downloaded? List the malicious domains observed, files downloaded, and their SHA256 hashes.</div>
    <table>
        <thead>
            <tr>
                <th style="width:14%;">File Name</th>
                <th style="width:28%;">Domain & URI</th>
                <th style="width:42%;">SHA-256 Hash</th>
                <th style="width:16%;">File Type</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>gerv.gun</strong></td>
                <td><code>matied.com/gerv.gun</code></td>
                <td><span class="hash-text">0931537889c35226d00ed26962ecacb140521394279eb2ade7e9d2afcf1a7272</span></td>
                <td>PE32 GUI Executable (Intel 386, 236 KB)</td>
            </tr>
            <tr>
                <td><strong>trow.exe</strong></td>
                <td><code>lounge-haarstudio.nl/oud/trow.exe</code></td>
                <td><span class="hash-text">94a0a09ee6a21526ac34d41eabf4ba603e9a30c26e6a1dc072ff45749dfb1fe1</span></td>
                <td>PE32 GUI Executable (Intel 386, 323 KB)</td>
            </tr>
            <tr>
                <td><strong>wp.exe</strong></td>
                <td><code>vantagepointtechnologies.com/wp.exe</code></td>
                <td><span class="hash-text">79d503165d32176842fe386d96c04fb70f6ce1c8a485837957849297e625ea48</span></td>
                <td>PE32 GUI Executable (Intel 386, 300.5 KB)</td>
            </tr>
        </tbody>
    </table>
    <div style="font-size:7.5pt; color:#475569; margin-top:2px;">
        <em>Method:</em> In NetworkMiner, navigate to the <strong>Files</strong> tab, right-click the extracted file, and select <strong>Calculate MD5 / SHA1 / SHA256 hash</strong> (or run <code>sha256sum</code> on the extracted bro objects).
    </div>
</div>

<div class="qa-block">
    <div class="question-text">b. VirusTotal Threat Intelligence Verification</div>
    <div class="card" style="margin-bottom:6px;">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <strong>1. Payload: gerv.gun (SHA-256: 09315378...)</strong>
            <span class="badge-tag badge-red">58 Security Engines Flagged</span>
        </div>
        <div style="font-size:8pt; margin-top:3px;">
            <strong>Classification:</strong> <code>Win32.Trojan.Pushdo</code> / <code>Trojan:Win32/Wacatac</code> | <strong>Size:</strong> 236.00 KB (241,664 bytes)<br>
            <strong>Known Aliases:</strong> <code>test</code>, <code>tmp523799.697</code>, <code>vector.tui</code>, <code>extract-1498570714.111294-HTTP-FG0jno3bJLiIzR4hrh.exe</code><br>
            <strong>Target Architecture:</strong> Intel 386 or later compatible 32-bit Windows subsystem.
        </div>
    </div>

    <div class="card" style="margin-bottom:6px;">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <strong>2. Payload: trow.exe (SHA-256: 94a0a09e...)</strong>
            <span class="badge-tag badge-red">63 Security Engines Flagged</span>
        </div>
        <div style="font-size:8pt; margin-top:3px;">
            <strong>Classification:</strong> <code>Win32.Trojan.Cutwail</code> / <code>Trojan.GenericKD</code> | <strong>Size:</strong> 323.00 KB (330,752 bytes)<br>
            <strong>Known Aliases:</strong> <code>Pedals.exe</code>, <code>trow.exe</code>, <code>test3</code>, <code>bma2beo4.exe</code><br>
            <strong>Behavior:</strong> Secondary botnet spam component associated with Cutwail payload delivery.
        </div>
    </div>

    <div class="card">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <strong>3. Payload: wp.exe (SHA-256: 79d50316...)</strong>
            <span class="badge-tag badge-red">55 Security Engines Flagged</span>
        </div>
        <div style="font-size:8pt; margin-top:3px;">
            <strong>Classification:</strong> <code>Win32.Malware-gen</code> / <code>Trojan.Downloader</code> | <strong>Size:</strong> 300.50 KB (307,712 bytes)<br>
            <strong>Known Aliases:</strong> <code>wp.exe</code>, <code>test2</code>, <code>test_3</code>, <code>4da48f6423d5f7d75de281a674c2e620.virobj</code>
        </div>
    </div>
</div>

<div class="qa-block">
    <div class="question-text">c. Examine other alerts associated with the infected host during this timeframe and record your findings.</div>
    <div class="answer-box">
        <p style="margin:2px 0;">
            <strong>1. External IP Lookup Alert:</strong> <code>ET POLICY External IP Lookup Domain (myip.opendns .com in DNS lookup)</code> &mdash; Target: <code>208.67.222.222:53</code>.
            <br>
            <em>Analysis:</em> <code>myip.opendns.com</code> is a legitimate OpenDNS IP reflection utility. Malware intentionally queries this domain to detect its public WAN address to report the host's geographical position to the C2 server.
        </p>
        <p style="margin:2px 0;">
            <strong>2. C2 Obfuscation Flooding (Decoy Traffic):</strong>
            Immediately following the Pushdo check-in (at <code>13:44:01</code>), the host sends a barrage of HTTP GET requests to hundreds of benign, legitimate websites (e.g., <code>vivastay.com</code>, <code>hazmatt.com</code>, <code>kursavto.ru</code>, <code>themark.org</code>). This is a known Pushdo evasion technique designed to create traffic noise and camouflage genuine C2 callbacks.
        </p>
        <p style="margin:2px 0;">
            <strong>3. Encrypted Egress:</strong> Alert <code>ET POLICY TLS possible TOR SSL traffic</code> directed to <code>208.83.223.34</code> indicates an attempt to establish an encrypted C2 or exfiltration tunnel.
        </p>
    </div>
</div>

<h4 class="subsection-header">Step 3: Report Your Findings (Executive Incident Report)</h4>
<div class="alert-box alert-danger">
    <div style="font-weight:700; font-size:9pt; margin-bottom:4px; color:#991b1b;">
        SOC Incident Response Executive Summary
    </div>
    <p style="margin:3px 0;">
        <strong>Incident Narrative:</strong> On <strong>June 27, 2017, between 13:38:34 and 13:44:32 UTC</strong>, internal workstation <strong><code>192.168.1.96</code></strong> (hostname <code>FlashGordon-PC</code>, MAC <code>00:15:C5:DE:C7:3B</code>, Dell Inc.) was compromised by the <strong>Pushdo Trojan</strong> downloader.
    </p>
    <p style="margin:3px 0;">
        The initial compromise occurred when the user navigated to <code>matied.com/gerv.gun</code>, downloading an obfuscated Win32 executable. Upon execution, Pushdo collected local hardware/OS telemetry, discovered its external WAN IP via OpenDNS (<code>208.67.222.222</code>), and established C2 communications with <code>198.1.85.250</code> and <code>62.210.140.158</code> over port 80.
    </p>
    <p style="margin:3px 0;">
        Pushdo subsequently retrieved two secondary malicious binaries: <strong><code>trow.exe</code></strong> (from <code>lounge-haarstudio.nl</code>) and <strong><code>wp.exe</code></strong> (from <code>vantagepointtechnologies.com</code>). All three payloads were confirmed as critical threats on VirusTotal (55+ detections each). To hinder network detection, the malware flooded the network with rapid HTTP GET requests to random benign sites while initiating encrypted Tor SSL communication with <code>208.83.223.34</code>.
    </p>
    <p style="margin:3px 0; font-weight:600;">
        <strong>Remediation Actions Taken:</strong> (1) Isolate host <code>192.168.1.96</code> from the local subnet; (2) Block all discovered external malicious IPs and domains on the perimeter firewall and DNS proxy; (3) Capture volatile forensic memory and re-image the host endpoint.
    </p>
</div>

</body>
</html>
"""

def generate_pdf():
    print("Generating CyberOps Skills Assessment PDF Report...")
    temp_html = os.path.join(TEMP_DIR, "temp_skills_assessment_pushdo.html")
    
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE)
        
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    user_data_dir = os.path.join(TEMP_DIR, "edge-pdf-skills-assessment")
    
    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--user-data-dir={user_data_dir}",
        f"--print-to-pdf={OUTPUT_PDF}",
        temp_html
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0 and os.path.exists(OUTPUT_PDF):
        print(f"SUCCESS: Generated PDF at {OUTPUT_PDF} (Size: {os.path.getsize(OUTPUT_PDF)} bytes)")
    else:
        print(f"ERROR: Failed to generate PDF: {res.stderr}")
        
    if os.path.exists(temp_html):
        try: os.remove(temp_html)
        except: pass

if __name__ == "__main__":
    generate_pdf()
