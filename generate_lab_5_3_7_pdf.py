"""
Generate Lab 5.3.7 Solution PDF:
Module 5 - Network Protocols
Lab 5.3.7: Lab - Introduction to Wireshark
"""

import os
import subprocess

LABS_DIR = r"C:\Users\fanele\CyberOps Associate\CyberOps-Associate\Module 5 - Network Protocols\Labs"
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
        content: "Module 5: Network Protocols | Lab Solution";
        font-family: 'Inter', sans-serif;
        font-size: 7.5pt;
        color: #64748b;
        font-weight: 500;
    }
    @bottom-left {
        content: "WIRESHARK PACKET ANALYSIS & MININET TOPOLOGY REPORT";
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

LAB_5_3_7_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Lab 5.3.7 - Introduction to Wireshark Solution</title>
<style>
{CSS}
</style>
</head>
<body>

<div class="doc-header">
    <div class="badge">Cisco Certified CyberOps Associate (CBROPS 200-201)</div>
    <h1>Lab 5.3.7: Introduction to Wireshark</h1>
    <div class="subtitle">Mininet Network Virtualization, PDU Layer Encapsulation, Local vs. Remote ICMP Traffic Analysis</div>
</div>

<div class="meta-grid">
    <div class="meta-item">
        <div class="meta-label">Course Module</div>
        <div class="meta-value">Module 5: Network Protocols</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Core Protocols</div>
        <div class="meta-value">Ethernet II, IPv4, ICMP (RFC 792)</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Simulation Engine</div>
        <div class="meta-value">Mininet SDN Emulator (OpenFlow)</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Workstation Environment</div>
        <div class="meta-value">CyberOps Workstation VM</div>
    </div>
</div>

<h2>Objectives</h2>
<ul>
    <li><strong>Part 1: Install and Verify the Mininet Topology</strong> &mdash; Execute Python topology orchestration scripts (<code class="inline">cyberops_topo.py</code>), launch host terminals (<code class="inline">xterm</code>), and baseline IP/MAC configurations.</li>
    <li><strong>Part 2: Capture and Analyze ICMP Data in Wireshark</strong> &mdash; Capture local LAN ping sequences (H1 &rarr; H2), dissect 3-pane Wireshark structures, and analyze remote subnet packet routing (H1 &rarr; H4 via Router R1).</li>
    <li><strong>Protocol Encapsulation Analysis</strong> &mdash; Correlate how Protocol Data Units (PDUs) transition down the OSI stack from Application payload to Layer 2 Ethernet frames.</li>
</ul>

<h2>Background / Scenario</h2>
<p>
Wireshark is the industry-standard software packet analyzer and protocol dissection tool used by Security Operations Center (SOC) analysts, network engineers, and forensic investigators. Wireshark captures network frames traversing physical or virtual interfaces and decodes their protocol layers according to RFC specifications.
</p>
<p>
In this lab, the Mininet software-defined network emulator is utilized within the CyberOps VM to construct a multi-node virtual topology containing hosts (H1, H2, H3, H4), an OpenFlow switch (S1), and a perimeter router (R1). Analysts observe and compare packet encapsulation during local LAN communication versus inter-network routed communication.
</p>

<h2>Part 1: Install and Verify the Mininet Topology</h2>

<h3>Step 1 & 2: Launch Topology Orchestration Script</h3>
<div class="terminal">
<span class="prompt">[analyst@secOps ~]$ </span><span class="cmd">sudo ~/lab.support.files/scripts/cyberops_topo.py</span>
<span class="output">[sudo] password for analyst: cyberops
*** Creating network
*** Adding controller
*** Adding hosts:
H1 H2 H3 H4 R1 
*** Adding switches:
s1 
*** Adding links:
(H1, s1) (H2, s1) (H3, s1) (s1, R1) (R1, H4) 
*** Starting CLI:
mininet> </span>
</div>

<h3>Step 3: Host Addressing Baseline Configuration Table</h3>
<p>Launching host terminals: <code class="inline">mininet> xterm H1 H2</code> and executing <code class="inline">ip address</code> on each node:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Host Node & Interface</th>
            <th>IPv4 Address / Subnet</th>
            <th>MAC Address (Layer 2)</th>
            <th>Subnet Placement & Role</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>H1 (H1-eth0)</strong></td>
            <td><code class="inline">10.0.0.11/24</code></td>
            <td><code class="inline">ba:d4:1d:7b:f3:61</code> (or simulated MAC)</td>
            <td>Local LAN Host (Initiating endpoint).</td>
        </tr>
        <tr>
            <td><strong>H2 (H2-eth0)</strong></td>
            <td><code class="inline">10.0.0.12/24</code></td>
            <td><code class="inline">ba:d4:1d:7b:f3:62</code> (or simulated MAC)</td>
            <td>Local LAN Host (Same broadcast domain).</td>
        </tr>
        <tr>
            <td><strong>H3 (H3-eth0)</strong></td>
            <td><code class="inline">10.0.0.13/24</code></td>
            <td><code class="inline">5a:d0:1d:01:9f:be</code></td>
            <td>Local LAN Host.</td>
        </tr>
        <tr>
            <td><strong>R1 (R1-eth1)</strong></td>
            <td><code class="inline">10.0.0.1/24</code></td>
            <td><code class="inline">00:00:00:00:00:01</code></td>
            <td>Default Gateway Router Interface for LAN <code class="inline">10.0.0.0/24</code>.</td>
        </tr>
        <tr>
            <td><strong>R1 (R1-eth2)</strong></td>
            <td><code class="inline">172.16.0.1/24</code></td>
            <td><code class="inline">00:00:00:00:00:02</code></td>
            <td>Gateway Interface for Remote Subnet <code class="inline">172.16.0.0/24</code>.</td>
        </tr>
        <tr>
            <td><strong>H4 (H4-eth0)</strong></td>
            <td><code class="inline">172.16.0.40/24</code></td>
            <td><code class="inline">ba:d4:1d:7b:f3:64</code></td>
            <td>Remote Simulated Enterprise Server.</td>
        </tr>
    </tbody>
</table>

<h2>Part 2: Capture and Analyze ICMP Data in Wireshark</h2>

<h3>Wireshark Three-Pane Architecture</h3>
<ul>
    <li><strong>Packet List Pane (Top):</strong> Summarizes all captured frames chronologically (Frame #, Time, Source, Destination, Protocol, Length, Info).</li>
    <li><strong>Packet Details Pane (Middle):</strong> Displays hierarchical protocol encapsulation breakdown (Frame &rarr; Ethernet II &rarr; IPv4 &rarr; ICMP).</li>
    <li><strong>Packet Bytes Pane (Bottom):</strong> Displays raw payload data in synchronized hexadecimal and ASCII representation.</li>
</ul>

<h3>Step 1: Local LAN Traffic Analysis (H1 Ping &rarr; H2 10.0.0.12)</h3>
<p>
Wireshark is started on node H1 (<code class="inline">wireshark &</code>) listening on interface <code class="inline">H1-eth0</code>. Five ping packets are sent: <code class="inline">ping -c 5 10.0.0.12</code>. Applying display filter <code class="inline">icmp</code> isolates the ICMP Echo Requests and Replies.
</p>

<div class="qa-card">
    <div class="question-title">Step 1.g &mdash; Local Subnet Frame Header Verification</div>
    <div class="question-text">
        1. Does the Source MAC address match H1's interface?<br>
        2. Does the Destination MAC address in Wireshark match H2's MAC address?
    </div>
    <div class="answer-box">
        <div class="answer-label">Dissection Findings:</div>
        <ul>
            <li><strong>1. Source MAC Match:</strong> <strong>Yes.</strong> The Source MAC in the Ethernet II frame matches the physical hardware address of <code class="inline">H1-eth0</code> (<code class="inline">ba:d4:1d:7b:f3:61</code>).</li>
            <li><strong>2. Destination MAC Match:</strong> <strong>Yes.</strong> The Destination MAC in the Ethernet II frame matches the exact physical MAC address of host H2 (<code class="inline">ba:d4:1d:7b:f3:62</code>).</li>
        </ul>
        <p><em>Networking Insight:</em> Because host H1 and host H2 reside on the same local Layer 3 subnet (<code class="inline">10.0.0.0/24</code>), H1 resolves H2's MAC directly using ARP. Frames are switched directly across Switch S1 without requiring routing by Default Gateway R1.</p>
    </div>
</div>

<div class="terminal">
<span class="prompt"># Protocol Data Unit (PDU) Encapsulation Stack:</span>
+-------------------------------------------------------------+
| Layer 2: Ethernet II Header (Src: H1 MAC &rarr; Dst: H2 MAC)    |
+-------------------------------------------------------------+
| Layer 3: IPv4 Header        (Src: 10.0.0.11 &rarr; Dst: 10.0.0.12)|
+-------------------------------------------------------------+
| Layer 4: ICMP Echo Request  (Type: 8, Code: 0, Seq: 1)     |
+-------------------------------------------------------------+
| Payload Data (Timestamp & Random Diagnostic Padding)        |
+-------------------------------------------------------------+
</div>

<h3>Step 2: Remote Subnet Traffic Analysis (H1 Ping &rarr; H4 172.16.0.40)</h3>
<p>
Terminals for remote host H4 and router R1 are launched (<code class="inline">mininet> xterm H4 R1</code>). A new Wireshark capture is started on <code class="inline">H1-eth0</code> and H1 pings the remote server: <code class="inline">ping -c 5 172.16.0.40</code>.
</p>

<div class="qa-card security">
    <div class="question-title">Step 2.e &mdash; Remote Routing Addressing Dissection</div>
    <div class="question-text">
        Review the captured data in Wireshark. List the destination IP and MAC addresses for the ping to H4.
    </div>
    <div class="answer-box">
        <div class="answer-label">Dissection Results:</div>
        <ul>
            <li><strong>Destination IPv4 Address:</strong> <strong style="color: #0369a1;"><code class="inline">172.16.0.40</code></strong> (Remote Server Host H4).</li>
            <li><strong>Destination MAC Address:</strong> <strong style="color: #dc2626;"><code class="inline">00:00:00:00:00:01</code></strong> (MAC address of router interface <strong><code class="inline">R1-eth1</code></strong> / Default Gateway <code class="inline">10.0.0.1</code>).</li>
        </ul>
        <p><strong>Core CyberOps Analysis:</strong></p>
        <p>
        Host H1 recognizes that destination <code class="inline">172.16.0.40</code> is on a remote subnet outside of <code class="inline">10.0.0.0/24</code>. Therefore, while the Layer 3 IP header maintains the end-to-end destination IP (<code class="inline">172.16.0.40</code>), the Layer 2 Ethernet frame is addressed to the <strong>Default Gateway's MAC address (<code class="inline">R1-eth1</code>)</strong>. Router R1 decapsulates the Layer 2 frame, routes the packet out interface <code class="inline">R1-eth2</code>, and re-encapsulates it with H4's MAC address.
        </p>
    </div>
</div>

<h3>Step 3: Mininet Graceful Shutdown & Environment Cleanup</h3>
<div class="terminal">
<span class="prompt"># 1. Exit Mininet CLI:</span>
<span class="prompt">mininet> </span><span class="cmd">quit</span>

<span class="prompt"># 2. Execute Mininet Deep Process Cleanup:</span>
<span class="prompt">[analyst@secOps ~]$ </span><span class="cmd">sudo mn -c</span>
<span class="output">[sudo] password for analyst: cyberops
*** Removing excess controllers/datapaths/pings
*** Removing junk from /tmp
*** Removing OVS datapaths
*** Killing stale mininet node processes
*** Cleanup complete.</span>
</div>

<div class="key-takeaways">
    <h3>CyberOps Protocol Analysis Summary</h3>
    <ul>
        <li><span class="badge-tag badge-blue">Local Switching</span> On a local LAN, Destination MAC matches the target host's physical NIC.</li>
        <li><span class="badge-tag badge-red">Remote Routing</span> When communicating across subnets, Destination MAC points to the <strong>Default Gateway router</strong>, while Destination IP remains the remote destination host.</li>
        <li><span class="badge-tag badge-green">PDU Encapsulation</span> Upper-layer protocols (ICMP/TCP/UDP) are encapsulated within IPv4 packets, which are further encapsulated inside Ethernet II frames.</li>
        <li><span class="badge-tag badge-purple">Process Cleanup</span> Always run <code class="inline">sudo mn -c</code> after Mininet sessions to prevent orphaned OpenFlow switch datapaths and virtual interface leaks.</li>
    </ul>
</div>

</body>
</html>"""

def main():
    print("Generating Lab 5.3.7 Solution PDF...")
    output_pdf = os.path.join(LABS_DIR, "5.3.7-Lab-Introduction-to-Wireshark-Solution.pdf")
    
    temp_html = os.path.join(TEMP_DIR, "temp_lab_5_3_7.html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(LAB_5_3_7_HTML)
    
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    user_data_dir = os.path.join(TEMP_DIR, "edge-pdf-lab-5-3-7")
    
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
