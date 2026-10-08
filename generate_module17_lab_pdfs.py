"""
Comprehensive PDF Solution Generator for Cisco CyberOps Associate - Module 17 Labs
Module 17: Attacking What We Do
1. Lab 17.1.7: Exploring DNS Traffic
2. Lab 17.2.6: Attacking a MySQL Database
3. Lab 17.2.7: Reading Server Logs
"""

import os
import subprocess

LABS_DIR = r"C:\Users\fanele\CyberOps Associate\CyberOps-Associate\Module 17 - Attacking What We Do\Labs"
TEMP_DIR = os.environ.get("TEMP", r"C:\Users\fanele\AppData\Local\Temp")

SHARED_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

@page {
    size: A4;
    margin: 16mm 14mm 16mm 14mm;
    @top-left {
        content: "Cisco Networking Academy | CyberOps Associate";
        font-family: 'Inter', sans-serif;
        font-size: 7.5pt;
        font-weight: 600;
        color: #0284c7;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    @top-right {
        content: "Module 17: Attacking What We Do | Official Lab Solution";
        font-family: 'Inter', sans-serif;
        font-size: 7.5pt;
        color: #64748b;
        font-weight: 500;
    }
    @bottom-left {
        content: "SECURITY OPERATIONS CENTER (SOC) PRACTICAL LAB REPORT";
        font-family: 'Inter', sans-serif;
        font-size: 7pt;
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
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    font-size: 9pt;
    line-height: 1.55;
    color: #1e293b;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
}

/* Header Banner */
.doc-header {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 45%, #0369a1 100%);
    color: #ffffff;
    padding: 20px 22px;
    border-radius: 8px;
    margin-bottom: 16px;
    box-shadow: 0 4px 10px rgba(15, 23, 42, 0.12);
}

.doc-header .badge {
    display: inline-block;
    background-color: #38bdf8;
    color: #0f172a;
    font-size: 7pt;
    font-weight: 800;
    padding: 3px 8px;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 6px;
}

.doc-header h1 {
    font-size: 16pt;
    font-weight: 800;
    margin: 0 0 4px 0;
    color: #ffffff;
    line-height: 1.2;
    letter-spacing: -0.2px;
}

.doc-header .subtitle {
    font-size: 9pt;
    color: #93c5fd;
    margin: 0;
    font-weight: 500;
}

/* Metadata Grid */
.meta-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
    background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 10px 14px;
    margin-bottom: 16px;
}

.meta-label {
    color: #64748b;
    font-weight: 600;
    text-transform: uppercase;
    font-size: 6.5pt;
    letter-spacing: 0.5px;
    margin-bottom: 2px;
}

.meta-value {
    color: #0f172a;
    font-weight: 700;
    font-size: 8pt;
}

/* Section Headings */
h2 {
    font-size: 11.5pt;
    font-weight: 700;
    color: #0f172a;
    border-bottom: 2px solid #0284c7;
    padding-bottom: 4px;
    margin-top: 18px;
    margin-bottom: 10px;
    page-break-after: avoid;
}

h3 {
    font-size: 10pt;
    font-weight: 700;
    color: #0369a1;
    margin-top: 14px;
    margin-bottom: 6px;
    page-break-after: avoid;
}

h4 {
    font-size: 9pt;
    font-weight: 600;
    color: #334155;
    margin-top: 10px;
    margin-bottom: 4px;
    page-break-after: avoid;
}

p {
    margin: 0 0 8px 0;
}

ul, ol {
    margin: 0 0 10px 0;
    padding-left: 18px;
}

li {
    margin-bottom: 3px;
}

/* Question & Answer Card */
.qa-card {
    background: #f0f9ff;
    border: 1px solid #bae6fd;
    border-left: 4px solid #0284c7;
    border-radius: 6px;
    padding: 10px 12px;
    margin: 10px 0;
    page-break-inside: avoid;
}

.qa-card.reflection {
    background: #fdf4ff;
    border-color: #f0abfc;
    border-left-color: #c026d3;
}

.qa-card.warning {
    background: #fffbeb;
    border-color: #fde68a;
    border-left-color: #d97706;
}

.qa-card.security {
    background: #fef2f2;
    border-color: #fecaca;
    border-left-color: #dc2626;
}

.qa-card .question-title {
    font-weight: 700;
    color: #0369a1;
    font-size: 8.5pt;
    margin-bottom: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.qa-card.reflection .question-title {
    color: #86198f;
}

.qa-card.security .question-title {
    color: #991b1b;
}

.qa-card .question-text {
    font-weight: 600;
    color: #1e293b;
    margin-bottom: 6px;
    font-size: 8.5pt;
}

.qa-card .answer-box {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 8px 10px;
    font-size: 8.5pt;
    color: #0f172a;
}

.qa-card .answer-label {
    font-weight: 700;
    color: #047857;
    font-size: 7pt;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 3px;
}

/* Code and Terminal Blocks */
.terminal {
    background-color: #0f172a;
    color: #f1f5f9;
    border-radius: 5px;
    padding: 8px 12px;
    font-family: 'JetBrains Mono', Consolas, Monaco, monospace;
    font-size: 7.5pt;
    line-height: 1.4;
    margin: 8px 0 10px 0;
    border: 1px solid #334155;
    white-space: pre-wrap;
    word-break: break-all;
    page-break-inside: avoid;
}

.terminal .prompt {
    color: #38bdf8;
    font-weight: 600;
}

.terminal .cmd {
    color: #f8fafc;
    font-weight: 700;
}

.terminal .output {
    color: #94a3b8;
}

.terminal .highlight {
    color: #facc15;
    font-weight: 700;
}

.terminal .danger {
    color: #f87171;
    font-weight: 700;
}

.terminal .success {
    color: #4ade80;
    font-weight: 700;
}

code.inline {
    background-color: #f1f5f9;
    color: #0f172a;
    padding: 1px 4px;
    border-radius: 3px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 8pt;
    border: 1px solid #e2e8f0;
}

/* Tables */
table.data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0;
    font-size: 8pt;
    page-break-inside: avoid;
}

table.data-table th {
    background-color: #0f172a;
    color: #ffffff;
    text-align: left;
    padding: 6px 8px;
    font-weight: 600;
    font-size: 7.5pt;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border: 1px solid #1e293b;
}

table.data-table td {
    padding: 6px 8px;
    border: 1px solid #e2e8f0;
    vertical-align: top;
}

table.data-table tr:nth-child(even) {
    background-color: #f8fafc;
}

/* Callout Box */
.info-box {
    background-color: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-left: 4px solid #16a34a;
    border-radius: 5px;
    padding: 8px 12px;
    margin: 10px 0;
    font-size: 8pt;
    page-break-inside: avoid;
}

.info-box .title {
    font-weight: 700;
    color: #15803d;
    font-size: 8pt;
    margin-bottom: 2px;
}

.key-takeaways {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 12px 14px;
    margin-top: 14px;
    page-break-inside: avoid;
}

.key-takeaways h3 {
    color: #0f172a;
    margin-top: 0;
    margin-bottom: 6px;
}

.badge-tag {
    display: inline-block;
    padding: 1px 5px;
    border-radius: 3px;
    font-size: 7pt;
    font-weight: 700;
}
.badge-blue { background: #e0f2fe; color: #0369a1; }
.badge-green { background: #dcfce7; color: #15803d; }
.badge-red { background: #fee2e2; color: #b91c1c; }
.badge-purple { background: #f3e8ff; color: #7e22ce; }
"""

def generate_pdf_from_html(html_content, output_pdf_path):
    temp_html = os.path.join(TEMP_DIR, "temp_lab_doc.html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    user_data_dir = os.path.join(TEMP_DIR, "edge-pdf-" + os.path.basename(output_pdf_path).replace(".pdf", ""))
    
    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--user-data-dir={user_data_dir}",
        f"--print-to-pdf={output_pdf_path}",
        temp_html
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error generating {output_pdf_path}: {res.stderr}")
    else:
        print(f"Created: {os.path.basename(output_pdf_path)} ({os.path.getsize(output_pdf_path)} bytes)")
    
    if os.path.exists(temp_html):
        try:
            os.remove(temp_html)
        except:
            pass


# ==========================================
# LAB 1: 17.1.7 - Exploring DNS Traffic
# ==========================================
LAB_17_1_7_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Lab 17.1.7 - Exploring DNS Traffic Solution</title>
<style>
{SHARED_CSS}
</style>
</head>
<body>

<div class="doc-header">
    <div class="badge">Cisco Certified CyberOps Associate (CBROPS 200-201)</div>
    <h1>Lab 17.1.7: Exploring DNS Traffic</h1>
    <div class="subtitle">Comprehensive Packet Analysis, Protocol Dissection, and Security Threat Evaluation</div>
</div>

<div class="meta-grid">
    <div class="meta-item">
        <div class="meta-label">Course Module</div>
        <div class="meta-value">Module 17: Attacking What We Do</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Protocol & Port</div>
        <div class="meta-value">DNS / UDP & TCP Port 53</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Analysis Tool</div>
        <div class="meta-value">Wireshark & CLI (nslookup)</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Workstation Environment</div>
        <div class="meta-value">CyberOps Workstation VM</div>
    </div>
</div>

<h2>Objectives</h2>
<ul>
    <li><strong>Part 1: Capture DNS Traffic</strong> &mdash; Configure packet capture environment, purge local resolver caches, and generate active DNS lookup traffic.</li>
    <li><strong>Part 2: Explore DNS Query Traffic</strong> &mdash; Dissect protocol layers (Ethernet II, IPv4, UDP, DNS Application header), analyze bit flags, and correlate addressing.</li>
    <li><strong>Part 3: Explore DNS Response Traffic</strong> &mdash; Inspect resolver response records, verify recursion capabilities, analyze CNAME aliasing, and correlate with CLI output.</li>
    <li><strong>Security Reflection & Threat Analysis</strong> &mdash; Evaluate DNS reconnaissance risks, cleartext vulnerabilities, data exfiltration vectors, and SOC defensive controls.</li>
</ul>

<h2>Background / Scenario</h2>
<p>
The Domain Name System (DNS) is foundational to internet and enterprise operations, translating human-readable Fully Qualified Domain Names (FQDNs) into routable IP addresses. However, because standard DNS is unencrypted and connectionless (UDP port 53), it is frequently targeted by threat actors for network reconnaissance, cache poisoning (DNS spoofing), unauthorized exfiltration (DNS tunneling), and amplification Denial-of-Service (DoS) attacks.
</p>
<p>
In this lab, Wireshark is utilized as a protocol analyzer to capture and dissect live DNS transactions, evaluate header fields across the OSI stack, inspect recursive resolution mechanisms, and analyze the security implications of unencrypted DNS traffic within enterprise security operations.
</p>

<h2>Part 1: Capture DNS Traffic</h2>

<h3>Step 1: Download, Install, and Initialize Wireshark</h3>
<p>
Wireshark is launched on the CyberOps Workstation. When prompted during installation on physical environments, USBPcap is avoided to prevent driver conflicts on operational USB interfaces.
</p>

<h3>Step 2: Clear the DNS Cache and Generate Queries</h3>
<p>
To ensure Wireshark captures fresh over-the-network DNS queries rather than satisfying requests from local operating system cache, the resolver cache must be cleared prior to capture initialization:
</p>

<div class="terminal">
<span class="prompt"># Windows DNS Cache Purge:</span>
<span class="prompt">C:\> </span><span class="cmd">ipconfig /flushdns</span>
<span class="output">Successfully flushed the DNS Resolver Cache.</span>

<span class="prompt"># Linux (CyberOps Workstation VM - Systemd-Resolved):</span>
<span class="prompt">analyst@secOps ~$ </span><span class="cmd">systemd-resolve --flush-caches</span>
<span class="prompt">analyst@secOps ~$ </span><span class="cmd">sudo systemctl restart systemd-resolved.service</span>

<span class="prompt"># macOS:</span>
<span class="prompt">bash-3.2$ </span><span class="cmd">sudo killall -HUP mDNSResponder</span>
</div>

<p>Interactive <code class="inline">nslookup</code> session is executed to generate DNS traffic for <code class="inline">www.cisco.com</code>:</p>

<div class="terminal">
<span class="prompt">analyst@secOps ~$ </span><span class="cmd">nslookup</span>
<span class="output">> </span><span class="cmd">www.cisco.com</span>
<span class="output">Server:         192.168.1.1
Address:        192.168.1.1#53

Non-authoritative answer:
www.cisco.com   canonical name = origin-www.cisco.com.akadns.net.
origin-www.cisco.com.akadns.net canonical name = e2867.dsca.akamaiedge.net.
Name:   e2867.dsca.akamaiedge.net
Address: 23.44.184.225
> </span><span class="cmd">exit</span>
</div>

<h2>Part 2: Explore DNS Query Traffic</h2>
<p>
Applying display filter <code class="inline">udp.port == 53</code> or <code class="inline">dns</code> isolates DNS packets. Selecting the <em>Standard query 0x0001 A www.cisco.com</em> packet reveals the encapsulation stack:
</p>

<div class="qa-card">
    <div class="question-title">Step 2.d &mdash; Ethernet II Data Link Layer Analysis</div>
    <div class="question-text">What are the source and destination MAC addresses? Which network interfaces are these MAC addresses associated with?</div>
    <div class="answer-box">
        <div class="answer-label">SOC Analyst Technical Finding:</div>
        <ul>
            <li><strong>Source MAC Address:</strong> e.g., <code class="inline">08:00:27:da:28:83</code> (CyberOps Workstation Virtual NIC).</li>
            <li><strong>Destination MAC Address:</strong> e.g., <code class="inline">50:c7:bf:dc:3a:41</code> (Default Gateway Router / Virtual NAT Gateway interface).</li>
            <li><strong>Interface Association:</strong> The Source MAC belongs to the host PC's active physical/virtual Network Interface Card (NIC <code class="inline">enp0s3</code> / Ethernet adapter). The Destination MAC is associated with the local Default Gateway router's LAN interface, resolved via ARP prior to transmission.</li>
        </ul>
    </div>
</div>

<div class="qa-card">
    <div class="question-title">Step 2.e &mdash; IPv4 Network Layer Analysis</div>
    <div class="question-text">What are the source and destination IP addresses? Which network interfaces are these IP addresses associated with?</div>
    <div class="answer-box">
        <div class="answer-label">SOC Analyst Technical Finding:</div>
        <ul>
            <li><strong>Source IPv4 Address:</strong> <code class="inline">192.168.1.100</code> (or VM IP <code class="inline">10.0.2.15</code>), assigned to the local host's active network adapter.</li>
            <li><strong>Destination IPv4 Address:</strong> <code class="inline">192.168.1.1</code> (or configured DNS resolver such as <code class="inline">209.165.200.225</code> / <code class="inline">8.8.8.8</code>).</li>
            <li><strong>Interface Association:</strong> Source IP is bound to the local host operating system NIC. Destination IP is assigned to the upstream recursive DNS server or gateway DNS relay agent.</li>
        </ul>
    </div>
</div>

<div class="qa-card">
    <div class="question-title">Step 2.f &mdash; Transport Layer Analysis (UDP)</div>
    <div class="question-text">What are the source and destination ports? What is the default DNS port number?</div>
    <div class="answer-box">
        <div class="answer-label">SOC Analyst Technical Finding:</div>
        <ul>
            <li><strong>Source Port:</strong> A dynamically assigned client ephemeral port (e.g., <code class="inline">53124</code> / <code class="inline">60481</code>, within range 49152&ndash;65535).</li>
            <li><strong>Destination Port:</strong> <code class="inline">53</code> (Well-known port assigned to DNS).</li>
            <li><strong>Default DNS Port:</strong> <strong>UDP Port 53</strong> is the universal default for standard queries and responses. (Note: TCP Port 53 is used for DNS Zone Transfers [AXFR/IXFR] and responses exceeding standard 512-byte UDP payload limits without EDNS0).</li>
        </ul>
    </div>
</div>

<div class="qa-card">
    <div class="question-title">Step 2.g &mdash; Address Resolution & Host Baseline Verification</div>
    <div class="question-text">Compare the MAC and IP addresses in the Wireshark results to the IP and MAC addresses obtained from ipconfig/arp. What is your observation?</div>
    <div class="answer-box">
        <div class="answer-label">SOC Analyst Technical Finding:</div>
        <p>
        The Source IP (<code class="inline">192.168.1.100</code>) and Source MAC (<code class="inline">08:00:27:da:28:83</code>) in the Wireshark frame perfectly match the Physical Address and IPv4 Address outputs from <code class="inline">ipconfig /all</code> (or Linux <code class="inline">ip addr</code>). Furthermore, the Destination MAC corresponds exactly to the ARP entry for the Default Gateway (<code class="inline">arp -a</code>), demonstrating that Layer 3 IP routing relies on Layer 2 MAC frame delivery across local broadcast domains.
        </p>
    </div>
</div>

<table class="data-table">
    <thead>
        <tr>
            <th>Protocol Layer</th>
            <th>Field Inspected</th>
            <th>DNS Query Value</th>
            <th>Technical SOC Significance</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Layer 2 (Data Link)</strong></td>
            <td>Ethernet II Frame</td>
            <td>Src: Host NIC &rarr; Dst: Gateway MAC</td>
            <td>Direct hop-to-hop frame transmission on the local LAN.</td>
        </tr>
        <tr>
            <td><strong>Layer 3 (Network)</strong></td>
            <td>IPv4 Header</td>
            <td>Src: 192.168.1.100 &rarr; Dst: 192.168.1.1</td>
            <td>Identifies initiating endpoint and configured DNS resolver.</td>
        </tr>
        <tr>
            <td><strong>Layer 4 (Transport)</strong></td>
            <td>User Datagram Protocol</td>
            <td>Src Port: 53124 &rarr; Dst Port: 53</td>
            <td>Connectionless transport minimizing lookup latency.</td>
        </tr>
        <tr>
            <td><strong>Layer 7 (Application)</strong></td>
            <td>DNS Query Header</td>
            <td>Flags: <code class="inline">0x0100</code> (Recursion Desired = 1)</td>
            <td>Client requests full recursive resolution from the server.</td>
        </tr>
    </tbody>
</table>

<h2>Part 3: Explore DNS Response Traffic</h2>
<p>
Inspecting the corresponding response frame (<em>Standard query response 0x0001 A www.cisco.com</em>) provides insight into server-side resolution:
</p>

<div class="qa-card">
    <div class="question-title">Step 3.a &mdash; Address & Port Symmetry Analysis</div>
    <div class="question-text">What are the source and destination MAC and IP addresses and port numbers? How do they compare to the addresses in the DNS query packets?</div>
    <div class="answer-box">
        <div class="answer-label">SOC Analyst Technical Finding:</div>
        <ul>
            <li><strong>Source MAC:</strong> Gateway MAC &nbsp;|&nbsp; <strong>Destination MAC:</strong> Host PC Virtual NIC.</li>
            <li><strong>Source IP:</strong> <code class="inline">192.168.1.1</code> (DNS Server) &nbsp;|&nbsp; <strong>Destination IP:</strong> <code class="inline">192.168.1.100</code> (Host PC).</li>
            <li><strong>Source Port:</strong> <code class="inline">53</code> &nbsp;|&nbsp; <strong>Destination Port:</strong> <code class="inline">53124</code> (Client Ephemeral Port).</li>
            <li><strong>Comparison:</strong> The Source and Destination addresses across Data Link (MAC), Network (IP), and Transport (UDP Port) layers are <strong>precisely inverted (swapped)</strong> compared to the query packet, confirming bidirectional communication symmetry.</li>
        </ul>
    </div>
</div>

<div class="qa-card">
    <div class="question-title">Step 3.c &mdash; DNS Recursion Flag Inspection</div>
    <div class="question-text">Can the DNS server do recursive queries?</div>
    <div class="answer-box">
        <div class="answer-label">SOC Analyst Technical Finding:</div>
        <p>
        <strong>Yes.</strong> Within the DNS Response Flags (<code class="inline">0x8180</code>), the <strong>Recursion Available (RA) bit is set to 1</strong> (<code class="inline">1... .... .... .... = Recursion available: Server can do recursive queries</code>). This confirms the DNS server possesses recursive resolution capabilities and queried upstream authoritative servers on behalf of the client.
        </p>
    </div>
</div>

<div class="qa-card">
    <div class="question-title">Step 3.d &mdash; DNS Record Correlation with CLI Output</div>
    <div class="question-text">Observe the CNAME and A records in the Answers details. How do the results compare to nslookup results?</div>
    <div class="answer-box">
        <div class="answer-label">SOC Analyst Technical Finding:</div>
        <p>
        The Wireshark DNS Answers section displays the complete resolution hierarchy:
        </p>
        <ol>
            <li><code class="inline">www.cisco.com</code> (CNAME) &rarr; <code class="inline">origin-www.cisco.com.akadns.net</code></li>
            <li><code class="inline">origin-www.cisco.com.akadns.net</code> (CNAME) &rarr; <code class="inline">e2867.dsca.akamaiedge.net</code></li>
            <li><code class="inline">e2867.dsca.akamaiedge.net</code> (A Record) &rarr; <code class="inline">23.44.184.225</code> (Akamai CDN Anycast IPv4 address)</li>
        </ol>
        <p>
        These results match the output obtained from the interactive <code class="inline">nslookup</code> command identically, confirming that <code class="inline">nslookup</code> formats and prints the exact payload returned in the DNS Answer resource records.
        </p>
    </div>
</div>

<h2>Reflection & Threat Analysis Questions</h2>

<div class="qa-card reflection">
    <div class="question-title">Reflection Question 1 &mdash; Passive Network Reconnaissance</div>
    <div class="question-text">From the Wireshark results, what else can you learn about the network when you remove the filter?</div>
    <div class="answer-box">
        <div class="answer-label">SOC Defensive Assessment:</div>
        <p>When display filters are removed, a packet capture exposes extensive operational intelligence across the broadcast domain:</p>
        <ul>
            <li><strong>Network Topology & Addressing Scheme:</strong> Internal IPv4/IPv6 subnets, DHCP lease servers, Default Gateway IP/MAC addresses.</li>
            <li><strong>Broadcast / Multicast Protocols:</strong> ARP discovery, LLMNR (Link-Local Multicast Name Resolution), mDNS (Bonjour), SSDP (UPnP devices), NBNS (NetBIOS).</li>
            <li><strong>Active Host Fingerprinting:</strong> Operating system telemetry, hostnames, background software update services, connected IoT hardware.</li>
            <li><strong>Cleartext Application Data:</strong> Unencrypted HTTP headers, FTP sessions, Telnet streams, plaintext NTP time sync requests, and unencrypted email (SMTP/IMAP).</li>
        </ul>
    </div>
</div>

<div class="qa-card security">
    <div class="question-title">Reflection Question 2 &mdash; Threat Actor Weaponization of Wireshark</div>
    <div class="question-text">How can an attacker use Wireshark to compromise your network security?</div>
    <div class="answer-box">
        <div class="answer-label">Threat Vector Analysis:</div>
        <p>Threat actors who obtain access to a network switchport (via ARP spoofing/port mirroring) or compromise an internal endpoint can utilize Wireshark for:</p>
        <ul>
            <li><strong>Credential & Session Sniffing:</strong> Extracting plaintext passwords, API keys, session tokens, and authentication cookies transmitted over unencrypted protocols.</li>
            <li><strong>DNS Profiling & Behavioral Surveillance:</strong> Monitoring DNS query requests to map all external domains, SaaS providers, and cloud services accessed by employees.</li>
            <li><strong>Man-in-the-Middle (MitM) Validation:</strong> Confirming successful execution of ARP cache poisoning, rogue DHCP server deployment, or DNS spoofing attacks.</li>
            <li><strong>Vulnerability Reconnaissance:</strong> Inspecting application banner exchanges (HTTP Server headers, SSH version strings, SMB dialects) to identify unpatched vulnerabilities for targeted exploitation.</li>
        </ul>
    </div>
</div>

<div class="key-takeaways">
    <h3>CyberOps SOC Analyst Remediation & Mitigation Summary</h3>
    <ul>
        <li><span class="badge-tag badge-blue">DNS Encryption</span> Deploy <strong>DNS over HTTPS (DoH - RFC 8484)</strong> or <strong>DNS over TLS (DoT - RFC 7858)</strong> to prevent eavesdropping and metadata profiling on the local network.</li>
        <li><span class="badge-tag badge-green">Integrity Protection</span> Enforce <strong>DNSSEC (DNS Security Extensions)</strong> validation on recursive resolvers to cryptographically prevent DNS cache poisoning.</li>
        <li><span class="badge-tag badge-red">Tunneling Detection</span> Implement DNS inspection on Next-Gen Firewalls (NGFW) to detect and block DNS tunneling tools (e.g., Iodine, dnscat2) and Domain Generation Algorithms (DGA).</li>
        <li><span class="badge-tag badge-purple">Layer 2 Hardening</span> Enable <strong>Dynamic ARP Inspection (DAI)</strong> and <strong>DHCP Snooping</strong> on access switches to prevent MitM packet sniffing.</li>
    </ul>
</div>

</body>
</html>"""


# ==========================================
# LAB 2: 17.2.6 - Attacking a MySQL Database
# ==========================================
LAB_17_2_6_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Lab 17.2.6 - Attacking a MySQL Database Solution</title>
<style>
{SHARED_CSS}
</style>
</head>
<body>

<div class="doc-header">
    <div class="badge">Cisco Certified CyberOps Associate (CBROPS 200-201)</div>
    <h1>Lab 17.2.6: Attacking a MySQL Database</h1>
    <div class="subtitle">Forensic PCAP Analysis of SQL Injection Exploitation, Hash Extraction & Cracking</div>
</div>

<div class="meta-grid">
    <div class="meta-item">
        <div class="meta-label">Course Module</div>
        <div class="meta-value">Module 17: Attacking What We Do</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Attack Type</div>
        <div class="meta-value">SQL Injection (CWE-89 / OWASP A03)</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Forensic Artifact</div>
        <div class="meta-value">SQL_Lab.pcap (441s duration)</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Attacker & Target</div>
        <div class="meta-value">10.0.2.4 &rarr; 10.0.2.15 (DVWA)</div>
    </div>
</div>

<h2>Objectives</h2>
<ul>
    <li><strong>Part 1: Load and Inspect PCAP File</strong> &mdash; Identify communicating endpoints, capture duration, and baseline HTTP traffic.</li>
    <li><strong>Part 2: Initial SQL Injection Discovery</strong> &mdash; Analyze boolean tautology bypass testing (<code class="inline">1=1</code>) in HTTP GET streams.</li>
    <li><strong>Part 3: Database & User Enumeration</strong> &mdash; Inspect UNION-based injection extracting current database schema and database execution user.</li>
    <li><strong>Part 4: Database Fingerprinting</strong> &mdash; Identify the exact database version and underlying Linux OS release.</li>
    <li><strong>Part 5: Schema & Metadata Harvesting</strong> &mdash; Dissect information schema queries enumerating tables and column definitions.</li>
    <li><strong>Part 6: Credential Extraction & Hash Cracking</strong> &mdash; Extract user credential hashes and execute cryptographic hash reversal.</li>
    <li><strong>Mitigation & Remediation Architecture</strong> &mdash; Detail parameterized queries, input validation, and least privilege hardening.</li>
</ul>

<h2>Background / Scenario</h2>
<p>
Structured Query Language (SQL) injection occurs when untrusted user input is directly concatenated into dynamic database queries without proper sanitization or parameterization. Attackers exploit this vulnerability to bypass authentication, manipulate backend database queries, exfiltrate sensitive data, tamper with database records, and execute administrative operating system commands.
</p>
<p>
In this lab, a forensic packet capture (<code class="inline">SQL_Lab.pcap</code>) capturing an 8-minute adversary attack against a vulnerable Damn Vulnerable Web Application (DVWA) instance is analyzed in Wireshark to reconstruct the attack progression from reconnaissance to full credential compromise.
</p>

<h2>Part 1: Open Wireshark and Load the PCAP File</h2>

<div class="qa-card">
    <div class="question-title">Part 1.e &mdash; Incident Endpoint Identification</div>
    <div class="question-text">What are the two IP addresses involved in this SQL injection attack based on the information displayed?</div>
    <div class="answer-box">
        <div class="answer-label">SOC Forensic Identification:</div>
        <ul>
            <li><strong>Attacker IP Address:</strong> <code class="inline">10.0.2.4</code> (Kali Linux attack workstation initiating HTTP GET requests).</li>
            <li><strong>Victim Web / DB Server IP:</strong> <code class="inline">10.0.2.15</code> (Apache/PHP web server hosting DVWA on port 80 backed by MySQL).</li>
        </ul>
        <p><em>Capture Timeline:</em> The total attack span is 441.2 seconds (~7.35 minutes), characterized by sequential HTTP GET parameter tampering.</p>
    </div>
</div>

<h2>Part 2: Initial SQL Injection Attack Probe (Line 13)</h2>
<p>
Following the TCP/HTTP stream on packet <strong>Line 13</strong> reveals the adversary's initial probe into the <code class="inline">vulnerabilities/sqli/?id=</code> parameter:
</p>

<div class="terminal">
<span class="danger"># Attacker HTTP Request (10.0.2.4):</span>
GET /vulnerabilities/sqli/?id=1%27+or+%271%27%3D%271&Submit=Submit HTTP/1.1
Host: 10.0.2.15
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0
Cookie: security=low; PHPSESSID=3d0ebbb...

<span class="success"># Server Response (10.0.2.15):</span>
HTTP/1.1 200 OK
Content-Type: text/html;charset=UTF-8

&lt;pre&gt;ID: 1&lt;br /&gt;First name: admin&lt;br /&gt;Surname: admin&lt;/pre&gt;
&lt;pre&gt;ID: 2&lt;br /&gt;First name: Gordon&lt;br /&gt;Surname: Brown&lt;/pre&gt;
&lt;pre&gt;ID: 3&lt;br /&gt;First name: Hack&lt;br /&gt;Surname: ME&lt;/pre&gt;
&lt;pre&gt;ID: 4&lt;br /&gt;First name: Pablo&lt;br /&gt;Surname: Picasso&lt;/pre&gt;
&lt;pre&gt;ID: 5&lt;br /&gt;First name: Bob&lt;br /&gt;Surname: Smith&lt;/pre&gt;
</div>

<p>
<strong>Attack Logic Breakdown:</strong> The backend PHP query is constructed as:
<code class="inline">SELECT first_name, last_name FROM users WHERE user_id = '$id';</code>. When the attacker inputs <code class="inline">1' OR '1'='1</code>, the SQL engine executes:
<code class="inline">SELECT first_name, last_name FROM users WHERE user_id = '1' OR '1'='1';</code>. Because <code class="inline">'1'='1'</code> is a boolean tautology (always TRUE), the query ignores user ID boundaries and dumps the entire user table.
</p>

<h2>Part 3: SQL Injection Enumeration Continues (Line 19)</h2>
<p>
In packet <strong>Line 19</strong>, the adversary escalates by injecting a UNION SELECT operator to query database metadata:
</p>

<div class="terminal">
<span class="danger"># Attacker Injected Query:</span>
GET /vulnerabilities/sqli/?id=1%27+or+1%3D1+union+select+database%28%29%2C+user%28%29%23&Submit=Submit HTTP/1.1
Decoded Payload: <span class="highlight">1' or 1=1 union select database(), user()#</span>
</div>

<p>
<strong>Findings Disclosed:</strong> The server executes the function calls and reveals:
</p>
<ul>
    <li><strong>Active Database Name:</strong> <code class="inline">dvwa</code></li>
    <li><strong>Database User Context:</strong> <code class="inline">root@localhost</code> (The web application is dangerously executing database queries with full administrative <code class="inline">root</code> privileges!).</li>
</ul>

<h2>Part 4: Database Version Fingerprinting (Line 22)</h2>

<div class="qa-card">
    <div class="question-title">Part 4.c &mdash; Database Version Identification</div>
    <div class="question-text">What is the version?</div>
    <div class="answer-box">
        <div class="answer-label">SOC Forensic Finding:</div>
        <p>The attacker injected the query: <code class="inline">1' or 1=1 union select null, version()#</code>.</p>
        <p>
        The HTTP response payload returned the database banner:
        <br><strong style="font-size: 10pt; color: #dc2626;"><code class="inline">5.5.47-0ubuntu0.14.04.1</code></strong>
        </p>
        <p>
        <em>Threat Intelligence Context:</em> This confirms the target is running <strong>MySQL 5.5.47</strong> on <strong>Ubuntu 14.04.1 LTS (Trusty Tahr)</strong>, allowing the attacker to search for OS and version-specific Local Privilege Escalation (LPE) exploits.
        </p>
    </div>
</div>

<h2>Part 5: Table and Schema Harvesting (Line 25)</h2>
<p>
In packet <strong>Line 25</strong>, the attacker queries <code class="inline">information_schema.tables</code> using:
<br><code class="inline">1' or 1=1 union select null, table_name from information_schema.tables#</code>.
</p>

<div class="qa-card">
    <div class="question-title">Part 5.c &mdash; Targeted Column Enumeration Analysis</div>
    <div class="question-text">What would the modified command of (1' OR 1=1 UNION SELECT null, column_name FROM INFORMATION_SCHEMA.columns WHERE table_name='users') do for the attacker?</div>
    <div class="answer-box">
        <div class="answer-label">SOC Technical Explanation:</div>
        <p>
        This targeted query instructs MySQL to inspect its data dictionary catalog (<code class="inline">INFORMATION_SCHEMA.columns</code>) and filter specifically for the column definitions belonging to the table named <code class="inline">'users'</code>.
        </p>
        <p>
        <strong>Tactical Value to Attacker:</strong> Rather than dumping thousands of system schema records, this returns the exact attribute schema of the authentication table &mdash; specifically revealing column names such as <code class="inline">user_id</code>, <code class="inline">first_name</code>, <code class="inline">last_name</code>, <code class="inline">user</code>, and <code class="inline">password</code>. With this exact schema blueprint, the attacker can craft precise queries to dump user credentials.
        </p>
    </div>
</div>

<h2>Part 6: Credential Extraction & Hash Cracking (Line 28)</h2>
<p>
In packet <strong>Line 28</strong>, the adversary concludes the attack by extracting user accounts and password hashes using:
<br><code class="inline">1' or 1=1 union select user, password from users#</code>.
</p>

<div class="qa-card">
    <div class="question-title">Part 6.b &mdash; Target User Identification</div>
    <div class="question-text">Which user has the password hash of 8d3533d75ae2c3966d7e0d4fcc69216b?</div>
    <div class="answer-box">
        <div class="answer-label">Extracted User Record:</div>
        <p>
        The user account associated with hash <code class="inline">8d3533d75ae2c3966d7e0d4fcc69216b</code> is <strong><code class="inline">admin</code></strong>.
        </p>
    </div>
</div>

<table class="data-table">
    <thead>
        <tr>
            <th>User Account</th>
            <th>Extracted MD5 Password Hash</th>
            <th>Cracked Plaintext Password</th>
            <th>Security Assessment</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>admin</strong></td>
            <td><code class="inline">8d3533d75ae2c3966d7e0d4fcc69216b</code></td>
            <td><strong style="color: #dc2626;">password</strong></td>
            <td>Critical &mdash; Default / Weakest Password</td>
        </tr>
        <tr>
            <td><strong>gordonb</strong></td>
            <td><code class="inline">e99a18c428cb38d5f260853678922e03</code></td>
            <td><strong style="color: #d97706;">abc123</strong></td>
            <td>High &mdash; Common Dictionary Password</td>
        </tr>
        <tr>
            <td><strong>1337</strong></td>
            <td><code class="inline">0d107d09f5bbe40ade3de5ec94a61001</code></td>
            <td><strong style="color: #d97706;">charley</strong></td>
            <td>High &mdash; Weak Name String</td>
        </tr>
        <tr>
            <td><strong>pablo</strong></td>
            <td><code class="inline">0d107d09f5bbe40ade3de5ec94a61001</code></td>
            <td><strong style="color: #d97706;">letmein</strong></td>
            <td>High &mdash; Standard Dictionary Word</td>
        </tr>
        <tr>
            <td><strong>smithy</strong></td>
            <td><code class="inline">5f4dcc3b5aa765d61d8327deb882cf99</code></td>
            <td><strong style="color: #dc2626;">password</strong></td>
            <td>Critical &mdash; Default Weak Password</td>
        </tr>
    </tbody>
</table>

<div class="qa-card">
    <div class="question-title">Part 6.c &mdash; Password Hash Cracking Result</div>
    <div class="question-text">Using a website such as https://crackstation.net/, copy the password hash into the password hash cracker and get cracking. What is the plain-text password?</div>
    <div class="answer-box">
        <div class="answer-label">Cracking Output:</div>
        <p>
        The plain-text password for hash <code class="inline">8d3533d75ae2c3966d7e0d4fcc69216b</code> is <strong><code class="inline">password</code></strong>.
        </p>
        <p>
        <em>Cryptographic Vulnerability Note:</em> The application utilized unsalted legacy MD5 hashing. Because MD5 is computationally trivial and lacks cryptographic salting, lookups against precomputed lookup tables (Rainbow Tables) reverse the hash instantly (&lt;0.01 seconds).
        </p>
    </div>
</div>

<h2>Reflection & Defensive Engineering Questions</h2>

<div class="qa-card reflection">
    <div class="question-title">Reflection Question 1 &mdash; Structural Risks of SQL Platforms</div>
    <div class="question-text">What is the risk of having platforms use the SQL language?</div>
    <div class="answer-box">
        <div class="answer-label">Comprehensive Threat Analysis:</div>
        <p>
        SQL is an interpreted data manipulation language that natively mixes control instructions with data values in the same string stream. If application code concatenates user-supplied input directly into SQL commands:
        </p>
        <ul>
            <li><strong>Complete Data Confidentiality Breach:</strong> Adversaries can dump the entire database, including PII, financial data, and credentials.</li>
            <li><strong>Data Integrity Destruction:</strong> Attackers can execute <code class="inline">UPDATE</code> or <code class="inline">DROP TABLE</code> commands to tamper with records or destroy data.</li>
            <li><strong>Authentication Bypass:</strong> Login mechanisms relying on SQL verification can be bypassed using tautologies (<code class="inline">' OR 1=1 --</code>).</li>
            <li><strong>Underlying Operating System Compromise:</strong> In advanced configurations, SQL injection allows attackers to read OS files (<code class="inline">LOAD_FILE()</code>), write web shells to web directories (<code class="inline">INTO OUTFILE '/var/www/shell.php'</code>), or execute system shell commands (e.g., MSSQL <code class="inline">xp_cmdshell</code>).</li>
        </ul>
    </div>
</div>

<div class="qa-card security">
    <div class="question-title">Reflection Question 2 &mdash; SQL Injection Prevention Methods</div>
    <div class="question-text">Browse the internet and perform a search on "prevent SQL injection attacks". What are 2 methods or steps that can be taken to prevent SQL injection attacks?</div>
    <div class="answer-box">
        <div class="answer-label">Defensive Architecture Controls:</div>
        <ol>
            <li>
                <strong>Primary Defense: Parameterized Queries (Prepared Statements):</strong>
                <br>Developers must use prepared statements with parameterized inputs (e.g., PHP PDO, Java PreparedStatement, Python psycopg2/SQLAlchemy). Parameterization forces the database engine to compile the SQL query structure first, treating user-supplied variables strictly as literal data rather than executable SQL syntax.
            </li>
            <li>
                <strong>Secondary Defense: Input Validation & Principle of Least Privilege:</strong>
                <br><strong>Input Validation:</strong> Implement strict positive allow-list validation (e.g., ensuring numeric IDs contain only digits <code class="inline">^[0-9]+$</code>).
                <br><strong>Least Privilege:</strong> Configure the web application to connect using a dedicated, unprivileged database service account with permissions limited solely to required tables, revoking access to <code class="inline">root</code>, administrative stored procedures, and file read/write operations.
            </li>
        </ol>
    </div>
</div>

<div class="key-takeaways">
    <h3>CyberOps Application Security Checklist</h3>
    <ul>
        <li><span class="badge-tag badge-green">Prepared Statements</span> Replace all dynamic string concatenation with parameterized SQL across all database tiers.</li>
        <li><span class="badge-tag badge-purple">Modern Password Hashing</span> Store credentials using salted, adaptive key-derivation functions (<strong>Argon2id</strong>, <strong>bcrypt</strong>, or <strong>PBKDF2</strong>) with high work factors.</li>
        <li><span class="badge-tag badge-blue">WAF Inspection</span> Deploy a Web Application Firewall (ModSecurity / AWS WAF) with OWASP Core Rule Set (CRS) to inspect and block SQLi signatures.</li>
        <li><span class="badge-tag badge-red">Disable Verbose Errors</span> Suppress database-specific error messages in production web responses to prevent information leakage.</li>
    </ul>
</div>

</body>
</html>"""


# ==========================================
# LAB 3: 17.2.7 - Reading Server Logs
# ==========================================
LAB_17_2_7_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Lab 17.2.7 - Reading Server Logs Solution</title>
<style>
{SHARED_CSS}
</style>
</head>
<body>

<div class="doc-header">
    <div class="badge">Cisco Certified CyberOps Associate (CBROPS 200-201)</div>
    <h1>Lab 17.2.7: Reading Server Logs</h1>
    <div class="subtitle">Log Analysis Utilities (cat, more, less, tail -f), Syslog Rotation, and Systemd Journalctl Operations</div>
</div>

<div class="meta-grid">
    <div class="meta-item">
        <div class="meta-label">Course Module</div>
        <div class="meta-value">Module 17: Attacking What We Do</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Log Architectures</div>
        <div class="meta-value">Plain-Text Syslog & Binary Journald</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Utilities Mastered</div>
        <div class="meta-value">cat, more, less, tail -f, journalctl</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Workstation Environment</div>
        <div class="meta-value">CyberOps Workstation VM (secOps)</div>
    </div>
</div>

<h2>Objectives</h2>
<ul>
    <li><strong>Part 1: Reading Log Files with Cat, More, Less, and Tail</strong> &mdash; Master CLI text utilities, compare navigation capabilities, and actively follow live log streams.</li>
    <li><strong>Part 2: Log Files and Syslog Architecture</strong> &mdash; Investigate centralized syslog formatting, analyze root permission requirements, and inspect log rotation mechanics.</li>
    <li><strong>Part 3: Log Files and Journalctl Operations</strong> &mdash; Query systemd binary journals, filter by boot ID, timestamp/UTC, kernel facility, and specific systemd services.</li>
    <li><strong>Comparative Evaluation & SIEM Integration</strong> &mdash; Rigorously compare Syslog vs. Systemd Journald advantages, limitations, and forensic considerations.</li>
</ul>

<h2>Background / Scenario</h2>
<p>
Server and application logs are the primary telemetry source for security analysts detecting intrusions, diagnosing system failures, and reconstructing incident timelines. Operating systems generate distinct log structures &mdash; ranging from legacy ASCII plain-text files managed by Syslog daemons to structured binary logs managed by systemd's <code class="inline">journald</code>.
</p>
<p>
A CyberOps analyst must be proficient with foundational Linux utilities (<code class="inline">cat</code>, <code class="inline">more</code>, <code class="inline">less</code>, <code class="inline">tail</code>) and advanced binary log management tools (<code class="inline">journalctl</code>) to rapidly extract actionable security intelligence during triage and active investigations.
</p>

<h2>Part 1: Reading Log Files with Cat, More, Less, and Tail</h2>

<h3>Step 1: Comparing Static File Viewers (cat, more, less)</h3>
<p>
Analysts examine an Apache access log file (<code class="inline">logstash-tutorial.log</code>) using three primary text viewers:
</p>
<ul>
    <li><code class="inline">cat /home/analyst/lab.support.files/logstash-tutorial.log</code> &mdash; Concatenates and dumps the entire file to stdout without paging. Fast for small files, but overflows terminal buffers for enterprise logs.</li>
    <li><code class="inline">more /home/analyst/lab.support.files/logstash-tutorial.log</code> &mdash; Paginates file output, advancing one screen per <kbd>Spacebar</kbd> and one line per <kbd>Enter</kbd>.</li>
    <li><code class="inline">less /home/analyst/lab.support.files/logstash-tutorial.log</code> &mdash; Advanced pager supporting bidirectional navigation, text searching, and memory-efficient chunk loading.</li>
</ul>

<div class="qa-card">
    <div class="question-title">Step 1.c &mdash; CLI Tool Evaluation</div>
    <div class="question-text">What is the drawback of using more?</div>
    <div class="answer-box">
        <div class="answer-label">Analyst Technical Evaluation:</div>
        <p>
        The primary drawback of <code class="inline">more</code> is that it is <strong>strictly unidirectional (forward-only)</strong>. Users can only advance downward through the file; they cannot scroll backward (upward) to review previously displayed lines without exiting and restarting the command.
        </p>
        <p>
        <em>Advantages of <code class="inline">less</code>:</em> In contrast, <code class="inline">less</code> ("less is more") provides full bidirectional scrolling (<kbd>&uarr;</kbd>/<kbd>&darr;</kbd>, <kbd>Page Up</kbd>/<kbd>Page Down</kbd>), forward searching (<code class="inline">/pattern</code>), backward searching (<code class="inline">?pattern</code>), and does not require loading the entire file into RAM before viewing.
        </p>
    </div>
</div>

<h3>Step 2: Actively Following Live Logs with tail -f</h3>
<p>
In security operations, analysts must observe logs in real time as events occur. Running <code class="inline">tail -f</code> continuously monitors a file descriptor for new append operations:
</p>

<div class="terminal">
<span class="prompt"># Terminal 1 (Live Monitoring):</span>
<span class="prompt">analyst@secOps ~$ </span><span class="cmd">sudo tail -f /home/analyst/lab.support.files/logstash-tutorial.log</span>

<span class="prompt"># Terminal 2 (Simulating Log Ingestion):</span>
<span class="prompt">analyst@secOps ~$ </span><span class="cmd">echo "this is a new entry to the monitored log file" >> lab.support.files/logstash-tutorial.log</span>
</div>

<p>
Terminal 1 instantly prints the appended string to the console without delay, demonstrating the real-time event streaming capability required for live intrusion monitoring.
</p>

<h2>Part 2: Log Files and Syslog Architecture</h2>
<p>
Syslog standardizes system and application event logging. The CyberOps VM records operating system events to <code class="inline">/var/log/syslog</code>.
</p>

<div class="qa-card">
    <div class="question-title">Part 2.a &mdash; Security Permissions & Access Control</div>
    <div class="question-text">Why did the cat command have to be executed as root?</div>
    <div class="answer-box">
        <div class="answer-label">SOC Security Policy Finding:</div>
        <p>
        System log files located in <code class="inline">/var/log/</code> contain sensitive security telemetry, including system authentication attempts, user activities, daemon errors, IP connections, and kernel diagnostics.
        </p>
        <p>
        To prevent unauthorized information disclosure and preserve confidentiality, POSIX permissions on <code class="inline">/var/log/syslog</code> are restricted (typically <code class="inline">-rw-r-----</code> or <code class="inline">0640</code> owned by <code class="inline">root:adm</code>). Standard non-privileged user accounts (such as <code class="inline">analyst</code>) lack read permissions and must elevate via <code class="inline">sudo</code>.
        </p>
    </div>
</div>

<div class="qa-card">
    <div class="question-title">Part 2.b &mdash; Network Time Protocol (NTP) & Log Synchronization</div>
    <div class="question-text">Can you think of a reason why it is so important to keep the time and date of computers correctly synchronized?</div>
    <div class="answer-box">
        <div class="answer-label">SOC Forensic & Incident Response Rationale:</div>
        <ul>
            <li><strong>Multi-Source Incident Reconstruction:</strong> Correlating security events across distributed firewalls, domain controllers, cloud workloads, and SIEM platforms requires microsecond-accurate, synchronized timestamps. Inaccurate time skews the attack narrative, making incident reconstruction impossible.</li>
            <li><strong>Authentication Protocol Validity:</strong> Cryptographic authentication mechanisms (Kerberos ticket granting, OAuth2/SAML assertion tokens, Time-based One-Time Passwords [TOTP]) fail if endpoint clocks drift beyond tight skew thresholds (typically &plusmn;5 minutes for Kerberos).</li>
            <li><strong>Certificate & Key Lifecycle:</strong> Validating X.509 TLS/SSL certificates, CRLs (Certificate Revocation Lists), and OCSP stapling relies on precise system time to enforce validity periods.</li>
            <li><strong>Legal Admissibility:</strong> Digital evidence presented in judicial proceedings or regulatory compliance audits (PCI-DSS, ISO 27001, HIPAA) requires a verifiable, synchronized chain of custody.</li>
        </ul>
    </div>
</div>

<h2>Part 3: Log Files and Systemd Journalctl Operations</h2>
<p>
Systemd's <code class="inline">journald</code> service stores system telemetry in an optimized, append-only binary format. The <code class="inline">journalctl</code> utility provides rich filtering capabilities:
</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Command</th>
            <th>Primary Function</th>
            <th>SOC Analytical Use Case</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code class="inline">journalctl</code></td>
            <td>Displays all recorded binary logs from beginning.</td>
            <td>Complete chronological system audit.</td>
        </tr>
        <tr>
            <td><code class="inline">sudo journalctl --utc</code></td>
            <td>Converts all displayed timestamps to UTC.</td>
            <td>Standardizing timeline against external SIEM logs.</td>
        </tr>
        <tr>
            <td><code class="inline">sudo journalctl -b</code></td>
            <td>Filters logs recorded only during the current boot.</td>
            <td>Diagnosing current session crashes and startups.</td>
        </tr>
        <tr>
            <td><code class="inline">sudo journalctl -u nginx.service --since today</code></td>
            <td>Filters by systemd unit (<code class="inline">nginx</code>) starting at 00:00:00 today.</td>
            <td>Investigating web application attacks occurring today.</td>
        </tr>
        <tr>
            <td><code class="inline">sudo journalctl -k</code></td>
            <td>Displays only Linux kernel messages (equivalent to <code class="inline">dmesg</code>).</td>
            <td>Hardware errors, kernel panics, driver issues.</td>
        </tr>
        <tr>
            <td><code class="inline">sudo journalctl -f</code></td>
            <td>Actively follows the live journal log stream in real time.</td>
            <td>Live threat hunting and real-time event monitoring.</td>
        </tr>
    </tbody>
</table>

<h2>Reflection & Comparative Architecture Analysis</h2>

<div class="qa-card reflection">
    <div class="question-title">Reflection Question &mdash; Syslog vs. Systemd Journald Evaluation</div>
    <div class="question-text">Compare Syslog and Journald. What are the advantages and disadvantages of each?</div>
    <div class="answer-box">
        <div class="answer-label">Comparative Technical Breakdown:</div>

        <table class="data-table" style="margin-top: 6px;">
            <thead>
                <tr>
                    <th>Dimension</th>
                    <th>Syslog Architecture (rsyslog / syslog-ng)</th>
                    <th>Systemd Journald Architecture (journalctl)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Storage Format</strong></td>
                    <td>Human-readable ASCII plain-text files (<code class="inline">/var/log/</code>).</td>
                    <td>Structured, indexed append-only binary files (<code class="inline">/var/log/journal/</code>).</td>
                </tr>
                <tr>
                    <td><strong>Metadata & Indexing</strong></td>
                    <td>Basic text: Timestamp, Hostname, Process[PID], Message.</td>
                    <td>Rich structured key-value metadata: PID, UID, GID, Unit, Boot ID, SELinux context.</td>
                </tr>
                <tr>
                    <td><strong>Tooling & Querying</strong></td>
                    <td>Standard text tools (<code class="inline">grep</code>, <code class="inline">awk</code>, <code class="inline">sed</code>, <code class="inline">cat</code>, <code class="inline">less</code>).</td>
                    <td>Requires <code class="inline">journalctl</code> utility; allows fast indexed filtering by field/service/time.</td>
                </tr>
                <tr>
                    <td><strong>Log Rotation</strong></td>
                    <td>Requires external service (<code class="inline">logrotate</code> cron job).</td>
                    <td>Built-in automatic size cap and retention rotation management.</td>
                </tr>
                <tr>
                    <td><strong>Tamper Resistance</strong></td>
                    <td>Low &mdash; Plain-text files can be modified if root is compromised.</td>
                    <td>High &mdash; Built-in <strong>Forward Secure Sealing (FSS)</strong> cryptographic verification.</td>
                </tr>
                <tr>
                    <td><strong>Network Centralization</strong></td>
                    <td>Native, ubiquitous protocol supported by virtually all network appliances.</td>
                    <td>Local host focus; requires forwarding daemon (<code class="inline">systemd-journal-remote</code> or <code class="inline">rsyslog</code>).</td>
                </tr>
                <tr>
                    <td><strong>Advantages</strong></td>
                    <td>Universal compatibility, plain-text simplicity, easy network forwarding.</td>
                    <td>Rich metadata, high query performance, early boot capture, tamper sealing.</td>
                </tr>
                <tr>
                    <td><strong>Disadvantages</strong></td>
                    <td>Unstructured text requires custom regex parsing; no binary integrity check.</td>
                    <td>Binary corruption can destroy logs; not portable across non-systemd OSes.</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>

<div class="key-takeaways">
    <h3>Enterprise Logging Best Practice Architecture</h3>
    <ul>
        <li><span class="badge-tag badge-blue">Hybrid Architecture</span> Utilize <strong>systemd-journald</strong> for high-fidelity local endpoint logging, forwarding structured events via <strong>rsyslog / syslog-ng</strong> to an enterprise SIEM (Splunk, Elastic Security, Microsoft Sentinel).</li>
        <li><span class="badge-tag badge-green">Cryptographic Sealing</span> Enable <strong>Forward Secure Sealing (FSS)</strong> in journald (<code class="inline">journalctl --setup-keys</code>) to detect any post-incident log tampering by rootkits.</li>
        <li><span class="badge-tag badge-purple">NTP Synchronization</span> Enforce network-wide chrony/NTP synchronization across all nodes to guarantee sub-millisecond timestamp alignment.</li>
        <li><span class="badge-tag badge-red">WORM Storage</span> Ingest centralized logs into Write-Once-Read-Many (WORM) cloud object storage or immutable log servers to satisfy compliance and evidentiary standards.</li>
    </ul>
</div>

</body>
</html>"""

def main():
    print("Generating Cisco CyberOps Associate Module 17 Lab Solution PDFs...")
    
    # Lab 1
    pdf1_path = os.path.join(LABS_DIR, "17.1.7-Lab-Exploring-DNS-Traffic-Solution.pdf")
    generate_pdf_from_html(LAB_17_1_7_HTML, pdf1_path)
    
    # Lab 2
    pdf2_path = os.path.join(LABS_DIR, "17.2.6-Lab-Attacking-a-MySQL-Database-Solution.pdf")
    generate_pdf_from_html(LAB_17_2_6_HTML, pdf2_path)
    
    # Lab 3
    pdf3_path = os.path.join(LABS_DIR, "17.2.7-Lab-Reading-Server-Logs-Solution.pdf")
    generate_pdf_from_html(LAB_17_2_7_HTML, pdf3_path)
    
    print("\nAll 3 Lab Solution PDFs generated successfully.")

if __name__ == "__main__":
    main()
