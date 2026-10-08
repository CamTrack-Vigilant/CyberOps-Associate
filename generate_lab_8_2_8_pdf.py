"""
Generate Lab 8.2.8 Solution PDF:
Module 8 - Address Resolution Protocol
Lab 8.2.8: Lab - Using Wireshark to Examine Ethernet Frames
"""

import os
import subprocess

LABS_DIR = r"C:\Users\fanele\CyberOps Associate\CyberOps-Associate\Module 8 - Address Resolution Protocol\Labs"
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
        content: "Module 8: Address Resolution Protocol | Lab Solution";
        font-family: 'Inter', sans-serif;
        font-size: 7.5pt;
        color: #64748b;
        font-weight: 500;
    }
    @bottom-left {
        content: "ETHERNET II FRAME DISSECTION & ARP ANALYSIS REPORT";
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

LAB_8_2_8_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Lab 8.2.8 - Using Wireshark to Examine Ethernet Frames Solution</title>
<style>
{CSS}
</style>
</head>
<body>

<div class="doc-header">
    <div class="badge">Cisco Certified CyberOps Associate (CBROPS 200-201)</div>
    <h1>Lab 8.2.8: Using Wireshark to Examine Ethernet Frames</h1>
    <div class="subtitle">Layer 2 Ethernet II Frame Structure, OUI Identification, Broadcast ARP Mechanics & Layer 2 vs. Layer 3 Routing Dynamics</div>
</div>

<div class="meta-grid">
    <div class="meta-item">
        <div class="meta-label">Course Module</div>
        <div class="meta-value">Module 8: Address Resolution Protocol</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Protocol & Framing</div>
        <div class="meta-value">Ethernet II (DIX) & ARP (RFC 826)</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Tools Used</div>
        <div class="meta-value">Wireshark, Mininet, Linux CLI</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Topology</div>
        <div class="meta-value">CyberOps Mininet Topology (H3, R1, S1)</div>
    </div>
</div>

<h2>Objectives</h2>
<ul>
    <li><strong>Part 1: Examine the Header Fields in an Ethernet II Frame</strong> &mdash; Review standard Ethernet II fields (Preamble, SFD, Destination/Source MAC, EtherType, Data, FCS) and analyze ARP broadcast frame parameters.</li>
    <li><strong>Part 2: Use Wireshark to Capture and Analyze Ethernet Frames</strong> &mdash; Launch Mininet network simulation, clear host ARP caches, capture ICMP/ARP traffic for local vs. remote destinations, and evaluate Layer 2 hop-by-hop delivery.</li>
    <li><strong>Reflection & Physical Layer Synchronization</strong> &mdash; Understand the role of the 8-byte Preamble / Start Frame Delimiter (SFD) and why it is omitted from software packet captures.</li>
</ul>

<h2>Background / Scenario</h2>
<p>
When upper-layer protocols (such as IPv4, IPv6, or ARP) transmit data across a local area network, the payload is encapsulated into a Layer 2 Data Link frame. In modern LAN architectures, the dominant framing standard is <strong>Ethernet II</strong>.
</p>
<p>
Ethernet II frames rely on 48-bit Media Access Control (MAC) addresses for local hardware delivery. Understanding the distinction between local Layer 2 frame forwarding (MAC hop-to-hop) and end-to-end Layer 3 packet routing (IP source-to-destination) is foundational for CyberOps security analysts monitoring network perimeters, analyzing ARP spoofing attacks, and investigating traffic captures.
</p>

<h2>Part 1: Examine Header Fields in an Ethernet II Frame</h2>

<h3>Ethernet II Frame Structure & Field Specifications</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Field Name</th>
            <th>Field Length</th>
            <th>Hexadecimal / Binary Content</th>
            <th>Protocol Function</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Preamble + SFD</strong></td>
            <td>8 Bytes (7 + 1)</td>
            <td><code class="inline">0xAA...AA</code> + <code class="inline">0xAB</code> (SFD)</td>
            <td>Hardware clock synchronization and start of frame indication. (Stripped by NIC).</td>
        </tr>
        <tr>
            <td><strong>Destination MAC</strong></td>
            <td>6 Bytes (48 bits)</td>
            <td><code class="inline">ff:ff:ff:ff:ff:ff</code> (or Unicast)</td>
            <td>Hardware address of target node or Layer 2 Broadcast.</td>
        </tr>
        <tr>
            <td><strong>Source MAC</strong></td>
            <td>6 Bytes (48 bits)</td>
            <td><code class="inline">f4:8c:50:62:62:6d</code></td>
            <td>Hardware address of the originating Network Interface Card (NIC).</td>
        </tr>
        <tr>
            <td><strong>EtherType (Type)</strong></td>
            <td>2 Bytes (16 bits)</td>
            <td><code class="inline">0x0806</code> (ARP) / <code class="inline">0x0800</code> (IPv4)</td>
            <td>Identifies the encapsulated upper-layer network protocol in the payload.</td>
        </tr>
        <tr>
            <td><strong>Data Payload</strong></td>
            <td>46 &ndash; 1500 Bytes</td>
            <td>Upper-layer Protocol Data Unit (PDU)</td>
            <td>Encapsulated Layer 3 packet or ARP payload (padded to minimum 46 bytes).</td>
        </tr>
        <tr>
            <td><strong>FCS (CRC-32)</strong></td>
            <td>4 Bytes (32 bits)</td>
            <td>Cyclic Redundancy Check</td>
            <td>Error-detection checksum computed by sender and verified by receiver NIC.</td>
        </tr>
    </tbody>
</table>

<h3>Part 1 Questions & Detailed Solutions</h3>

<div class="qa-card">
    <div class="question-title">Part 1.Step 3 &mdash; Destination Address Significance</div>
    <div class="question-text">What is significant about the contents of the destination address field?</div>
    <div class="answer-box">
        <div class="answer-label">Analyst Finding:</div>
        <p>
        The Destination Address is <code class="inline">ff:ff:ff:ff:ff:ff</code> (all binary 1s / 48 bits set to 1). This is the <strong>Layer 2 Broadcast MAC Address</strong>.
        </p>
        <p>
        <strong>Significance:</strong> When access switches receive a frame addressed to the broadcast MAC, they flood it out all active switchports within the local VLAN/broadcast domain. Every host NIC on the LAN accepts and processes the frame up the protocol stack.
        </p>
    </div>
</div>

<div class="qa-card">
    <div class="question-title">Part 1.Step 3 &mdash; ARP Broadcast Mechanics</div>
    <div class="question-text">Why does the PC send out a broadcast ARP prior to sending the first ping request?</div>
    <div class="answer-box">
        <div class="answer-label">Protocol Resolution Mechanics:</div>
        <p>
        Before the sending host can construct and transmit an IP packet (ICMP Echo Request) over Ethernet, it requires the destination device's physical Layer 2 MAC address to populate the Ethernet II header.
        </p>
        <p>
        Because the target IP's MAC address is not currently stored in the host's local <strong>ARP Cache table</strong>, the host broadcasts an <strong>ARP Request</strong> (<em>"Who has IP 10.0.0.1? Tell 10.0.0.11"</em>) so the owner of that IP address responds with its MAC address.
        </p>
    </div>
</div>

<div class="qa-card">
    <div class="question-title">Part 1.Step 3 &mdash; MAC Address & OUI Anatomy</div>
    <div class="question-text">
        1. What is the MAC address of the source in the first frame?<br>
        2. What is the Vendor ID (OUI) of the Source's NIC?<br>
        3. What portion of the MAC address is the OUI?<br>
        4. What is the Source's NIC serial number?
    </div>
    <div class="answer-box">
        <div class="answer-label">MAC Address Breakdown (f4:8c:50:62:62:6d):</div>
        <ul>
            <li><strong>1. Source MAC Address:</strong> <code class="inline">f4:8c:50:62:62:6d</code></li>
            <li><strong>2. Vendor ID (OUI):</strong> <code class="inline">f4:8c:50</code> (Registered to <strong>Intel Corporate</strong>).</li>
            <li><strong>3. OUI Portion:</strong> The <strong>first 3 octets (first 24 bits / 6 hexadecimal characters)</strong> of the 48-bit MAC address comprise the <strong>Organizationally Unique Identifier (OUI)</strong> assigned to the hardware manufacturer by the IEEE.</li>
            <li><strong>4. NIC Serial Number:</strong> The <strong>last 3 octets (last 24 bits / 6 hexadecimal characters)</strong>: <code class="inline">62:62:6d</code> represents the unique, vendor-assigned Network Interface Controller serial identifier.</li>
        </ul>
    </div>
</div>

<h2>Part 2: Capture and Analyze Ethernet Frames in Mininet</h2>

<h3>Step 1: Inspect Network Configuration of Host H3</h3>
<div class="terminal">
<span class="prompt">[analyst@secOps ~]$ </span><span class="cmd">sudo ./lab.support.files/scripts/cyberops_topo.py</span>
<span class="prompt">mininet> </span><span class="cmd">xterm H3</span>

<span class="prompt"># On Node H3 Terminal:</span>
<span class="prompt">[root@secOps ~]# </span><span class="cmd">ip address</span>
<span class="output">2: H3-eth0: ...
    link/ether <span class="highlight">5a:d0:1d:01:9f:be</span> brd ff:ff:ff:ff:ff:ff
    inet <span class="highlight">10.0.0.13/24</span> brd 10.0.0.255 scope global H3-eth0</span>

<span class="prompt">[root@secOps ~]# </span><span class="cmd">netstat -r</span>
<span class="output">Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
default         <span class="highlight">10.0.0.1</span>        0.0.0.0         UG        0 0          0 H3-eth0
10.0.0.0        0.0.0.0         255.255.255.0   U         0 0          0 H3-eth0</span>
</div>

<div class="qa-card">
    <div class="question-title">Step 1.e &mdash; Default Gateway Verification</div>
    <div class="question-text">What is the IP address of the default gateway for the host H3?</div>
    <div class="answer-box">
        <div class="answer-label">Host Route Setting:</div>
        <p>The default gateway IP address for host H3 is <strong><code class="inline">10.0.0.1</code></strong>.</p>
    </div>
</div>

<h3>Step 2 to 5: Local Subnet Ping Capture & Dissection (H3 &rarr; Gateway 10.0.0.1)</h3>
<p>
After clearing the ARP cache (<code class="inline">arp -d 10.0.0.11</code>), Wireshark is started on <code class="inline">H3-eth0</code> and 5 ICMP packets are sent to <code class="inline">10.0.0.1</code>. Filtering by <code class="inline">icmp</code> isolates the ping frames:
</p>

<div class="qa-card">
    <div class="question-title">Step 5.c &mdash; Local ICMP Echo Request Frame Details</div>
    <div class="question-text">
        1. What is the MAC address of the PC's NIC?<br>
        2. What is the default gateway's MAC address?<br>
        3. What type of frame is displayed?
    </div>
    <div class="answer-box">
        <div class="answer-label">Dissection Findings (Echo Request):</div>
        <ul>
            <li><strong>1. Source MAC (H3 NIC):</strong> <code class="inline">5a:d0:1d:01:9f:be</code> (Host H3 virtual interface).</li>
            <li><strong>2. Destination MAC (Default Gateway):</strong> <code class="inline">00:00:00:00:00:01</code> (or router gateway interface MAC).</li>
            <li><strong>3. Frame Type:</strong> <strong><code class="inline">Ethernet II</code></strong> with EtherType field value <strong style="color: #0369a1;"><code class="inline">0x0800 (IPv4)</code></strong>.</li>
        </ul>
    </div>
</div>

<div class="qa-card">
    <div class="question-title">Step 5.e & 5.g &mdash; Addressing & Echo Reply Verification</div>
    <div class="question-text">
        1. What is the source and destination IP address in the Echo Request?<br>
        2. In the Echo Reply frame, what device and MAC address is displayed as the destination address?
    </div>
    <div class="answer-box">
        <div class="answer-label">Dissection Findings:</div>
        <ul>
            <li><strong>1. Echo Request IP Header:</strong> Source IP: <code class="inline">10.0.0.13</code> &rarr; Destination IP: <code class="inline">10.0.0.1</code>.</li>
            <li><strong>2. Echo Reply Frame Destination:</strong> Device: <strong>Host H3</strong> &nbsp;|&nbsp; Destination MAC: <code class="inline">5a:d0:1d:01:9f:be</code> (Source and destination MAC addresses reverse during the reply).</li>
        </ul>
    </div>
</div>

<h3>Step 6 & 7: Remote Subnet Ping Capture (H3 &rarr; Remote Server 172.16.0.40)</h3>
<p>From host H3, 5 ICMP echo requests are sent to off-subnet host <code class="inline">172.16.0.40</code>:</p>

<div class="terminal">
<span class="prompt">[root@secOps analyst]# </span><span class="cmd">ping -c 5 172.16.0.40</span>
<span class="output">PING 172.16.0.40 (172.16.0.40) 56(84) bytes of data.
64 bytes from 172.16.0.40: icmp_seq=1 ttl=63 time=0.082 ms
...</span>
</div>

<div class="qa-card">
    <div class="question-title">Step 7 &mdash; Remote Traffic Addressing Analysis</div>
    <div class="question-text">
        1. In the first echo request frame, what are the source and destination MAC addresses?<br>
        2. What are the source and destination IP addresses contained in the data field of the frame?
    </div>
    <div class="answer-box">
        <div class="answer-label">Captured Frame Attributes:</div>
        <ul>
            <li><strong>Source MAC:</strong> <code class="inline">5a:d0:1d:01:9f:be</code> (Host H3 NIC).</li>
            <li><strong>Destination MAC:</strong> <code class="inline">00:00:00:00:00:01</code> (Default Gateway Router LAN Interface).</li>
            <li><strong>Source IPv4 Address:</strong> <code class="inline">10.0.0.13</code> (Host H3).</li>
            <li><strong>Destination IPv4 Address:</strong> <strong style="color: #dc2626;"><code class="inline">172.16.0.40</code></strong> (Remote Server).</li>
        </ul>
    </div>
</div>

<div class="qa-card security">
    <div class="question-title">Step 7 &mdash; Core Layer 2 vs. Layer 3 Routing Dynamic</div>
    <div class="question-text">Why has the destination IP address changed, while the destination MAC address remained the same?</div>
    <div class="answer-box">
        <div class="answer-label">SOC Core Networking Principle:</div>
        <p>
        <strong>1. Layer 3 (IP) Routing Dynamics:</strong> IP addresses represent <strong>end-to-end logical addressing</strong>. The destination IP (<code class="inline">172.16.0.40</code>) identifies the final remote destination host across the entire internetwork and remains constant from origin to destination.
        </p>
        <p>
        <strong>2. Layer 2 (MAC) Delivery Dynamics:</strong> MAC addresses represent <strong>local hop-to-hop physical addressing</strong> and are only valid within the local broadcast domain (LAN).
        </p>
        <p>
        <strong>Conclusion:</strong> When host H3 compares the destination IP (<code class="inline">172.16.0.40</code>) against its local subnet mask (<code class="inline">255.255.255.0</code>), it determines that the target is on a <strong>remote network</strong>. Host H3 cannot directly deliver frames to remote MAC addresses; therefore, it encapsulates the IP packet inside an Ethernet II frame addressed to the <strong>MAC address of its local Default Gateway router (<code class="inline">10.0.0.1</code>)</strong>. The router decapsulates the Layer 2 header and forwards the packet toward the next hop.
        </p>
    </div>
</div>

<h2>Reflection Question & Physical Layer Synchronization</h2>

<div class="qa-card reflection">
    <div class="question-title">Reflection &mdash; The Ethernet Preamble & Start Frame Delimiter</div>
    <div class="question-text">Wireshark does not display the preamble field of a frame header. What does the preamble contain?</div>
    <div class="answer-box">
        <div class="answer-label">Physical Layer (PHY) Engineering Analysis:</div>
        <p>
        The Ethernet Preamble field contains an <strong>8-byte (64-bit) synchronization bit stream</strong> structured into two distinct parts:
        </p>
        <ol>
            <li>
                <strong>Preamble (7 Bytes / 56 bits):</strong> An alternating pattern of binary 1s and 0s:
                <br><code class="inline">10101010 10101010 10101010 10101010 10101010 10101010 10101010</code> (or <code class="inline">0xAA</code> in hex).
                <br><em>Purpose:</em> Allows the receiving Physical Layer (PHY) hardware transceiver to synchronize its clock timing with the incoming signal pulses.
            </li>
            <li>
                <strong>Start Frame Delimiter (SFD - 1 Byte / 8 bits):</strong> A specific pattern ending in two consecutive 1s:
                <br><code class="inline">10101011</code> (or <code class="inline">0xAB</code> in hex).
                <br><em>Purpose:</em> Explicitly signals to the receiving hardware that the synchronization sequence is complete and that the actual Destination MAC address begins on the very next bit.
            </li>
        </ol>
        <p>
        <strong>Why Wireshark does not display the Preamble:</strong> The Network Interface Card (NIC) hardware PHY controller consumes and strips the 8-byte Preamble/SFD during physical frame synchronization before handing the validated frame to the OS driver and packet capture engine (libpcap).
        </p>
    </div>
</div>

<div class="key-takeaways">
    <h3>CyberOps Analyst Layer 2 Security Summary</h3>
    <ul>
        <li><span class="badge-tag badge-blue">Address Scope</span> Layer 2 MAC addresses change at every router hop; Layer 3 IP addresses remain constant end-to-end.</li>
        <li><span class="badge-tag badge-green">ARP Cache Trust</span> ARP is stateless and unauthenticated; hosts accept unsolicited ARP replies, leaving networks vulnerable to <strong>ARP Poisoning / Man-in-the-Middle</strong> attacks.</li>
        <li><span class="badge-tag badge-purple">Switch Security</span> Enterprise networks must enforce <strong>Dynamic ARP Inspection (DAI)</strong> and <strong>Port Security</strong> to validate Layer 2 to Layer 3 bindings against a trusted DHCP Snooping binding database.</li>
    </ul>
</div>

</body>
</html>"""

def main():
    print("Generating Lab 8.2.8 Solution PDF...")
    output_pdf = os.path.join(LABS_DIR, "8.2.8-Lab-Using-Wireshark-to-Examine-Ethernet-Frames-Solution.pdf")
    
    temp_html = os.path.join(TEMP_DIR, "temp_lab_8_2_8.html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(LAB_8_2_8_HTML)
    
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    user_data_dir = os.path.join(TEMP_DIR, "edge-pdf-lab-8-2-8")
    
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
