"""
Generate Lab 10.2.7 Solution PDF:
Module 10 - Network Services
Lab 10.2.7: Lab - Using Wireshark to Examine a UDP DNS Capture
"""

import os
import subprocess

LABS_DIR = r"C:\Users\fanele\CyberOps Associate\CyberOps-Associate\Module 10 - Network Services\Labs"
TEMP_DIR = os.environ.get("TEMP", r"C:\Users\fanele\AppData\Local\Temp")

CSS = """
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
        content: "Module 10: Network Services | Lab Solution";
        font-family: 'Inter', sans-serif;
        font-size: 7.5pt;
        color: #64748b;
        font-weight: 500;
    }
    @bottom-left {
        content: "WIRESHARK UDP & DNS PROTOCOL DISSECTION REPORT";
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

p { margin: 0 0 8px 0; }
ul, ol { margin: 0 0 10px 0; padding-left: 18px; }
li { margin-bottom: 3px; }

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

.qa-card.security {
    background: #fef2f2;
    border-color: #fecaca;
    border-left-color: #dc2626;
}

.qa-card.warning {
    background: #fffbeb;
    border-color: #fde68a;
    border-left-color: #d97706;
}

.qa-card .question-title {
    font-weight: 700;
    color: #0369a1;
    font-size: 8.5pt;
    margin-bottom: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.qa-card.security .question-title { color: #991b1b; }
.qa-card.reflection .question-title { color: #86198f; }

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

.terminal .prompt { color: #38bdf8; font-weight: 600; }
.terminal .cmd { color: #f8fafc; font-weight: 700; }
.terminal .output { color: #94a3b8; }
.terminal .highlight { color: #facc15; font-weight: 700; }
.terminal .danger { color: #f87171; font-weight: 700; }
.terminal .success { color: #4ade80; font-weight: 700; }

code.inline {
    background-color: #f1f5f9;
    color: #0f172a;
    padding: 1px 4px;
    border-radius: 3px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 8pt;
    border: 1px solid #e2e8f0;
}

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

table.data-table tr:nth-child(even) { background-color: #f8fafc; }

.key-takeaways {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 12px 14px;
    margin-top: 14px;
    page-break-inside: avoid;
}

.key-takeaways h3 { color: #0f172a; margin-top: 0; margin-bottom: 6px; }

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

LAB_10_2_7_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Lab 10.2.7 - Using Wireshark to Examine a UDP DNS Capture Solution</title>
<style>
{CSS}
</style>
</head>
<body>

<div class="doc-header">
    <div class="badge">Cisco Certified CyberOps Associate (CBROPS 200-201)</div>
    <h1>Lab 10.2.7: Using Wireshark to Examine a UDP DNS Capture</h1>
    <div class="subtitle">Transport Layer Analysis, UDP Header Mechanics, DNS Query/Response Dissection & Layer 2/3 Address Resolution</div>
</div>

<div class="meta-grid">
    <div class="meta-item">
        <div class="meta-label">Course Module</div>
        <div class="meta-value">Module 10: Network Services</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Protocols Analyzed</div>
        <div class="meta-value">UDP (RFC 768) & DNS (RFC 1035)</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Analysis Tool</div>
        <div class="meta-value">Wireshark & Linux Network CLI</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Environment</div>
        <div class="meta-value">CyberOps Workstation VM (enp0s3)</div>
    </div>
</div>

<h2>Objectives</h2>
<ul>
    <li><strong>Part 1: Record IP Configuration Information of the PC</strong> &mdash; Document MAC address, IPv4 address, DNS nameserver configuration, and default gateway routing table.</li>
    <li><strong>Part 2: Use Wireshark to Capture DNS Queries and Responses</strong> &mdash; Capture live traffic on interface <code class="inline">enp0s3</code> while resolving <code class="inline">www.google.com</code>.</li>
    <li><strong>Part 3: Analyze Captured DNS or UDP Packets</strong> &mdash; Dissect the 8-byte UDP transport header, inspect DNS query/response structures, and evaluate Layer 2 (MAC) vs. Layer 3 (IP) routing dynamics.</li>
    <li><strong>Reflection & Architectural Evaluation</strong> &mdash; Assess the performance, scalability, and overhead advantages of UDP vs. TCP for DNS transport.</li>
</ul>

<h2>Background / Scenario</h2>
<p>
The User Datagram Protocol (UDP) is an unacknowledged, connectionless Transport Layer protocol operating at OSI Layer 4. Unlike TCP, UDP introduces minimal protocol overhead (a fixed 8-byte header) and requires no connection setup handshake or state tracking. Because DNS lookups require rapid, lightweight transactions, UDP port 53 is the primary protocol used for domain name queries.
</p>
<p>
In this lab, network parameters of the CyberOps Workstation VM are recorded, followed by packet capture and forensic dissection of a live DNS resolution sequence in Wireshark.
</p>

<h2>Part 1: Record the IP Configuration Information of the PC</h2>
<p>
Executing network diagnostic commands from the CyberOps Workstation CLI reveals the host's networking baseline:
</p>

<div class="terminal">
<span class="prompt"># 1. Inspect Physical Interface and MAC Address:</span>
<span class="prompt">[analyst@secOps ~]$ </span><span class="cmd">ip link</span>
<span class="output">2: enp0s3: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether <span class="highlight">08:00:27:da:28:83</span> brd ff:ff:ff:ff:ff:ff</span>

<span class="prompt"># 2. Inspect Assigned IPv4 Address and Subnet Mask:</span>
<span class="prompt">[analyst@secOps ~]$ </span><span class="cmd">ip addr</span>
<span class="output">2: enp0s3: ...
    inet <span class="highlight">192.168.8.10/24</span> brd 192.168.8.255 scope global dynamic enp0s3</span>

<span class="prompt"># 3. Inspect Configured DNS Resolvers:</span>
<span class="prompt">[analyst@secOps ~]$ </span><span class="cmd">cat /etc/resolv.conf</span>
<span class="output">nameserver <span class="highlight">8.8.4.4</span>
nameserver 8.8.8.8
nameserver 209.165.200.235</span>

<span class="prompt"># 4. Display Kernel IP Routing Table & Default Gateway:</span>
<span class="prompt">[analyst@secOps ~]$ </span><span class="cmd">netstat -rn</span>
<span class="output">Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
0.0.0.0         <span class="highlight">192.168.8.1</span>     0.0.0.0         UG        0 0          0 enp0s3
192.168.8.0     0.0.0.0         255.255.255.0   U         0 0          0 enp0s3</span>
</div>

<table class="data-table">
    <thead>
        <tr>
            <th>Network Parameter</th>
            <th>Recorded Host Value</th>
            <th>Diagnostic Source Command</th>
            <th>Role in DNS Query Transmission</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Host MAC Address</strong></td>
            <td><code class="inline">08:00:27:da:28:83</code></td>
            <td><code class="inline">ip link</code> / <code class="inline">ifconfig</code></td>
            <td>Layer 2 Source Hardware Address for all outgoing frames.</td>
        </tr>
        <tr>
            <td><strong>Host IPv4 Address</strong></td>
            <td><code class="inline">192.168.8.10</code></td>
            <td><code class="inline">ip addr</code></td>
            <td>Layer 3 Source IP in query packets.</td>
        </tr>
        <tr>
            <td><strong>Subnet Mask</strong></td>
            <td><code class="inline">255.255.255.0 (/24)</code></td>
            <td><code class="inline">ip addr</code></td>
            <td>Defines local broadcast domain boundary.</td>
        </tr>
        <tr>
            <td><strong>Default Gateway IP</strong></td>
            <td><code class="inline">192.168.8.1</code></td>
            <td><code class="inline">netstat -rn</code> / <code class="inline">ip route</code></td>
            <td>Next-hop router interface for off-subnet packets.</td>
        </tr>
        <tr>
            <td><strong>DNS Server IP</strong></td>
            <td><code class="inline">8.8.4.4</code> (Google Public DNS)</td>
            <td><code class="inline">cat /etc/resolv.conf</code></td>
            <td>Layer 3 Destination IP for domain queries.</td>
        </tr>
    </tbody>
</table>

<h2>Part 2: Use Wireshark to Capture DNS Queries and Responses</h2>
<p>
Wireshark is launched on interface <code class="inline">enp0s3</code>. A web browser navigates to <code class="inline">www.google.com</code> (or alternatively <code class="inline">ping -c 2 www.google.com</code> is run in terminal). Once Google's IP is resolved, capture is stopped and filtered with <code class="inline">dns</code>.
</p>

<h2>Part 3: Analyze Captured DNS and UDP Packets</h2>

<h3>Step 1 & 2: Dissect the DNS Query Packet (Frame 429)</h3>

<div class="qa-card">
    <div class="question-title">Step 2.b &mdash; Layer 2 Source MAC Verification</div>
    <div class="question-text">Is the source MAC address the same as the one recorded from Part 1 for the VM?</div>
    <div class="answer-box">
        <div class="answer-label">Analyst Finding:</div>
        <p>
        <strong>Yes.</strong> The Source MAC address displayed in the Ethernet II frame (<code class="inline">08:00:27:da:28:83</code>) is identical to the physical MAC address recorded for the VM's active network interface (<code class="inline">enp0s3</code>) in Part 1.
        </p>
    </div>
</div>

<div class="qa-card">
    <div class="question-title">Step 2.c &mdash; Layer 2 vs. Layer 3 Addressing Identification</div>
    <div class="question-text">Can you identify the IP and MAC addresses for the source and destinations of this packet?</div>
    <div class="answer-box">
        <div class="answer-label">Addressing Matrix:</div>
        <table class="data-table" style="margin-top: 4px;">
            <thead>
                <tr>
                    <th>Device Role</th>
                    <th>IPv4 Address (Layer 3)</th>
                    <th>MAC Address (Layer 2)</th>
                    <th>Routing / Encapsulation Explanation</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Source Workstation (VM)</strong></td>
                    <td><code class="inline">192.168.8.10</code></td>
                    <td><code class="inline">08:00:27:da:28:83</code></td>
                    <td>Originating endpoint that generated the DNS lookup.</td>
                </tr>
                <tr>
                    <td><strong>Destination (DNS Server / Gateway)</strong></td>
                    <td><code class="inline">8.8.4.4</code> (DNS Server)</td>
                    <td><code class="inline">50:c7:bf:dc:3a:41</code> (Default Gateway)</td>
                    <td><strong>Crucial Concept:</strong> The Destination IP is the ultimate endpoint (DNS server <code class="inline">8.8.4.4</code>), but the Destination MAC is the <strong>local Default Gateway router</strong>, which forwards the frame off the local LAN.</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>

<h3>UDP Transport Header Anatomy (RFC 768)</h3>
<p>
The UDP segment header contains exactly <strong>4 fields (8 bytes total)</strong>, with each field occupying exactly 16 bits (2 bytes):
</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Field Name</th>
            <th>Field Size</th>
            <th>Captured Packet Value</th>
            <th>Technical Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Source Port</strong></td>
            <td>16 bits (2 bytes)</td>
            <td><code class="inline">58029</code></td>
            <td>Dynamically allocated client ephemeral port used to track the response.</td>
        </tr>
        <tr>
            <td><strong>Destination Port</strong></td>
            <td>16 bits (2 bytes)</td>
            <td><code class="inline">53</code></td>
            <td>Well-known port reserved for DNS servers listening for incoming queries.</td>
        </tr>
        <tr>
            <td><strong>Length</strong></td>
            <td>16 bits (2 bytes)</td>
            <td><code class="inline">40 bytes</code></td>
            <td>Total length of UDP segment: 8 bytes (header) + 32 bytes (DNS payload).</td>
        </tr>
        <tr>
            <td><strong>Checksum</strong></td>
            <td>16 bits (2 bytes)</td>
            <td><code class="inline">0x7d2e [verified]</code></td>
            <td>Validates segment data integrity across network transit.</td>
        </tr>
    </tbody>
</table>

<div class="qa-card">
    <div class="question-title">Step 2.d &mdash; Address Correlation Verification</div>
    <div class="question-text">
        1. Is the source IP address the same as the local PC's IP address you recorded in Part 1?<br>
        2. Is the destination IP address the same as the default gateway noted in Part 1?
    </div>
    <div class="answer-box">
        <div class="answer-label">Analyst Findings:</div>
        <ul>
            <li><strong>1. Source IP Correlation:</strong> <strong>Yes.</strong> The source IP (<code class="inline">192.168.8.10</code>) matches the VM's assigned IP address recorded in Part 1.</li>
            <li><strong>2. Destination IP Correlation:</strong> <strong>No (in general).</strong> The destination IP address (<code class="inline">8.8.4.4</code>) is the configured public DNS recursive resolver from <code class="inline">/etc/resolv.conf</code>, whereas the default gateway is <code class="inline">192.168.8.1</code>. (Note: While the destination <em>MAC</em> address matches the Default Gateway router, the destination <em>IP</em> is the upstream DNS server).</li>
        </ul>
    </div>
</div>

<h3>Step 3: Dissect the DNS Response Packet (Frame 488)</h3>

<div class="qa-card">
    <div class="question-title">Step 3.b &mdash; Ethernet II Addressing Roles in Response</div>
    <div class="question-text">In the Ethernet II frame for the DNS response, what device is the source MAC address and what device is the destination MAC address?</div>
    <div class="answer-box">
        <div class="answer-label">Dissection Finding:</div>
        <ul>
            <li><strong>Source MAC Address:</strong> The Default Gateway router's LAN interface MAC address (<code class="inline">50:c7:bf:dc:3a:41</code>).</li>
            <li><strong>Destination MAC Address:</strong> The Workstation VM's virtual NIC MAC address (<code class="inline">08:00:27:da:28:83</code>).</li>
        </ul>
    </div>
</div>

<div class="qa-card">
    <div class="question-title">Step 3.c &mdash; Network & Transport Layer Role Reversal</div>
    <div class="question-text">
        1. What is the destination IP address?<br>
        2. What is the source IP address?<br>
        3. What happened to the roles of source and destination for the VM and default gateway?
    </div>
    <div class="answer-box">
        <div class="answer-label">SOC Analytical Answers:</div>
        <ul>
            <li><strong>1. Destination IP Address:</strong> <code class="inline">192.168.8.10</code> (CyberOps Workstation VM).</li>
            <li><strong>2. Source IP Address:</strong> <code class="inline">8.8.4.4</code> (DNS Server).</li>
            <li><strong>3. Role Inversion Analysis:</strong> The roles of source and destination across <strong>all OSI layers (Layer 2 MAC, Layer 3 IP, and Layer 4 Port numbers) are completely reversed/inverted</strong>. The DNS server replies back to the exact ephemeral port (<code class="inline">58029</code>) and host IP that initiated the query, allowing the host OS to route the response to the requesting application.</li>
        </ul>
    </div>
</div>

<h2>Reflection Question & Architectural Evaluation</h2>

<div class="qa-card reflection">
    <div class="question-title">Reflection Question &mdash; Transport Layer Protocol Selection (UDP vs. TCP for DNS)</div>
    <div class="question-text">What are the benefits of using UDP instead of TCP as a transport protocol for DNS?</div>
    <div class="answer-box">
        <div class="answer-label">Comprehensive Engineering & CyberOps Evaluation:</div>
        <ol>
            <li>
                <strong>Minimal Protocol Overhead & Reduced Bandwidth:</strong>
                <br>A UDP header is fixed at only <strong>8 bytes</strong>, whereas a TCP header consumes a minimum of <strong>20 bytes</strong> (up to 60 bytes with options). For short query-response cycles, UDP significantly reduces bandwidth consumption across high-volume networks.
            </li>
            <li>
                <strong>Zero Handshake Latency (No 3-Way Handshake):</strong>
                <br>UDP is connectionless. A DNS client sends its query datagram immediately without establishing a connection. In contrast, TCP requires a 3-way handshake (<code class="inline">SYN &rarr; SYN-ACK &rarr; ACK</code>) and teardown (<code class="inline">FIN/RST</code>), which introduces at least 1.5 to 2 Round Trip Times (RTT) of added latency before query data can be transmitted.
            </li>
            <li>
                <strong>Stateless Scalability on DNS Servers:</strong>
                <br>Root and recursive DNS servers handle millions of queries per second. With UDP, the server processes datagrams statelessly without allocating operating system memory buffers or maintaining Transmission Control Blocks (TCBs) for sequence numbers, window sizing, and retransmission timers.
            </li>
            <li>
                <strong>Application-Layer Reliability Handling:</strong>
                <br>Because DNS queries are idempotent (repeating a query produces the same result without side effects), DNS client applications handle retransmissions directly with a simple retry timer, rendering heavy TCP retransmission mechanisms unnecessary for small standard lookups.
            </li>
        </ol>
        <p><em>When DNS Uses TCP Port 53:</em> TCP is used when DNS response payloads exceed 512 bytes (without EDNS0), for <strong>DNS Zone Transfers (AXFR / IXFR)</strong> between primary and secondary nameservers, and for <strong>DNS over TLS (DoT - RFC 7858)</strong> on port 853.</p>
    </div>
</div>

<div class="key-takeaways">
    <h3>CyberOps Protocol Analysis Summary</h3>
    <ul>
        <li><span class="badge-tag badge-blue">Layer 2 vs 3 Dynamics</span> IP routing ensures packets reach remote destination IPs (<code class="inline">8.8.4.4</code>), while Ethernet MAC addressing directs frames hop-by-hop to local default gateways (<code class="inline">192.168.8.1</code>).</li>
        <li><span class="badge-tag badge-green">UDP Simplicity</span> UDP provides fast, lightweight 8-byte transport without connection overhead for time-sensitive application lookups.</li>
        <li><span class="badge-tag badge-red">Security Implication</span> Because UDP is connectionless and unauthenticated, standard DNS is vulnerable to <strong>IP spoofing</strong> and <strong>DNS amplification DDoS attacks</strong>, mandating defensive measures like <strong>Response Rate Limiting (RRL)</strong> and <strong>DNSSEC</strong>.</li>
    </ul>
</div>

</body>
</html>"""

def main():
    print("Generating Lab 10.2.7 Solution PDF...")
    output_pdf = os.path.join(LABS_DIR, "10.2.7-Lab-Using-Wireshark-to-Examine-a-UDP-DNS-Capture-Solution.pdf")
    
    temp_html = os.path.join(TEMP_DIR, "temp_lab_10_2_7.html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(LAB_10_2_7_HTML)
    
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    user_data_dir = os.path.join(TEMP_DIR, "edge-pdf-lab-10-2-7")
    
    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--user-data-dir={user_data_dir}",
        f"--print-to-pdf={output_pdf}",
        temp_html
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error: {res.stderr}")
    else:
        print(f"Created: {os.path.basename(output_pdf)} ({os.path.getsize(output_pdf)} bytes)")
    
    if os.path.exists(temp_html):
        try: os.remove(temp_html)
        except: pass

if __name__ == "__main__":
    main()
