"""
Generate Lab 15.2.7 Solution PDF:
Module 15 - Network Monitoring and Tools
Lab 15.2.7: Packet Tracer - Logging Network Activity
"""

import os
import subprocess

LABS_DIR = r"C:\Users\fanele\CyberOps Associate\CyberOps-Associate\Module 15 - Network Monitoring and Tools\Labs"
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
        content: "Module 15: Network Monitoring and Tools | Lab Solution";
        font-family: 'Inter', sans-serif;
        font-size: 7.5pt;
        color: #64748b;
        font-weight: 500;
    }
    @bottom-left {
        content: "PACKET TRACER SECURITY LAB & SYSLOG MONITORING REPORT";
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

LAB_15_2_7_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Lab 15.2.7 - Logging Network Activity Solution</title>
<style>
{CSS}
</style>
</head>
<body>

<div class="doc-header">
    <div class="badge">Cisco Certified CyberOps Associate (CBROPS 200-201)</div>
    <h1>Lab 15.2.7: Packet Tracer &mdash; Logging Network Activity</h1>
    <div class="subtitle">Packet Sniffing, Plaintext Protocol Exploitation, Syslog Analysis & NAT Visibility</div>
</div>

<div class="meta-grid">
    <div class="meta-item">
        <div class="meta-label">Course Module</div>
        <div class="meta-value">Module 15: Network Monitoring & Tools</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Core Protocols</div>
        <div class="meta-value">FTP (TCP 21), Syslog (UDP 514), ICMP, Telnet</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Environment</div>
        <div class="meta-value">Cisco Packet Tracer / Multi-Subnet Topology</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Key Concepts</div>
        <div class="meta-value">Traffic Sniffing, NAT Obfuscation, Log Triage</div>
    </div>
</div>

<h2>Addressing Table</h2>
<table class="data-table">
    <thead>
        <tr>
            <th>Device</th>
            <th>Interface</th>
            <th>Private IP Address</th>
            <th>Public IP Address</th>
            <th>Role in Lab Scenario</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>FTP_Server</strong></td>
            <td>Gig0/0</td>
            <td><code class="inline">192.168.30.253</code></td>
            <td><code class="inline">209.165.200.227</code></td>
            <td>Enterprise FTP repository storing client files.</td>
        </tr>
        <tr>
            <td><strong>SYSLOG_SERVER</strong></td>
            <td>FastEthernet0</td>
            <td><code class="inline">192.168.11.254</code></td>
            <td><code class="inline">209.165.200.229</code></td>
            <td>Centralized syslog daemon collecting router debug events.</td>
        </tr>
        <tr>
            <td><strong>Router2</strong></td>
            <td>Serial0/0/1</td>
            <td>N/A</td>
            <td><code class="inline">209.165.200.226</code></td>
            <td>Core perimeter router generating ICMP debug telemetry.</td>
        </tr>
        <tr>
            <td><strong>Sniffer1</strong></td>
            <td>Port0 / Port1</td>
            <td>N/A (Passive)</td>
            <td>N/A (Passive)</td>
            <td>Inline packet capturing appliance monitoring Router2 links.</td>
        </tr>
        <tr>
            <td><strong>PC-A / PC-B / PC-C</strong></td>
            <td>NIC</td>
            <td><code class="inline">192.168.1.x / 192.168.2.x</code></td>
            <td>NAT Overload IP</td>
            <td>Internal client hosts generating FTP, Telnet & Ping traffic.</td>
        </tr>
    </tbody>
</table>

<h2>Objectives</h2>
<ul>
    <li><strong>Part 1: Create FTP Traffic</strong> &mdash; Activate packet sniffer, establish remote FTP session to <code class="inline">209.165.200.227</code>, authenticate, and perform file transfer (<code class="inline">clientinfo.txt</code>).</li>
    <li><strong>Part 2: Investigate FTP Traffic</strong> &mdash; Dissect captured packets on Sniffer1, expose plaintext credential transmission, and define mitigation strategies.</li>
    <li><strong>Part 3: View Syslog Messages</strong> &mdash; Enable <code class="inline">debug ip icmp</code> logging on Router2 via Telnet, generate test ICMP traffic across endpoints, and analyze the impact of Network Address Translation (NAT) on security logging.</li>
</ul>

<h2>Part 1: Create FTP Traffic</h2>

<h3>Step 1: Activate the Sniffing Device</h3>
<p>
The passive sniffing appliance <code class="inline">Sniffer1</code> is powered on via its <strong>Physical</strong> tab and the sniffing service is enabled in the <strong>GUI</strong> tab. Sniffer1 monitors all frames traversing the link between Router2 and the server subnet.
</p>

<h3>Step 2: Establish Remote FTP Connection from PC-B</h3>
<p>From host <code class="inline">PC-B</code> Command Prompt, an FTP session is initiated to the public IP of <code class="inline">FTP_Server</code>:</p>

<div class="terminal">
<span class="prompt">PC-B:\> </span><span class="cmd">ftp 209.165.200.227</span>
<span class="output">Connected to 209.165.200.227.
220 Service ready for new user.
User (209.165.200.227:(none)): </span><span class="cmd">cisco</span>
<span class="output">331 User name okay, need password for cisco.
Password: </span><span class="cmd">cisco</span>
<span class="output">230 User logged in, proceed.</span>
</div>

<h3>Step 3: Upload Sensitive Client File (<code class="inline">clientinfo.txt</code>)</h3>
<div class="terminal">
<span class="prompt">ftp> </span><span class="cmd">dir</span>
<span class="output">226 Transfer complete.</span>
<span class="prompt">ftp> </span><span class="cmd">put clientinfo.txt</span>
<span class="output">200 PORT command successful.
150 Opening BINARY mode data connection for clientinfo.txt.
226 Transfer complete.
File transfer in progress: 100% complete.</span>
<span class="prompt">ftp> </span><span class="cmd">dir</span>
<span class="output">-rw-r--r-- 1 ftp ftp 1048 Aug 17 08:30 clientinfo.txt
226 Transfer complete.</span>
<span class="prompt">ftp> </span><span class="cmd">quit</span>
<span class="output">221 Service closing control connection.</span>
</div>

<h2>Part 2: Investigate the FTP Traffic on Sniffer1</h2>
<p>
Opening the <code class="inline">Sniffer1</code> GUI tab and inspecting the captured TCP/FTP packet stream reveals the Application Layer control channel commands:
</p>

<div class="terminal">
<span class="output">Packet #12: FTP Control (Port 21) &rarr; Command: </span><span class="danger">USER cisco</span>
<span class="output">Packet #14: FTP Control (Port 21) &rarr; Command: </span><span class="danger">PASS cisco</span>
<span class="output">Packet #22: FTP Data    (Port 20) &rarr; Payload: </span><span class="highlight">[CONFIDENTIAL CLIENT RECORDS & ACCOUNT NUMBERS]</span>
</div>

<div class="qa-card security">
    <div class="question-title">Part 2 &mdash; FTP Vulnerability Analysis</div>
    <div class="question-text">What is the security vulnerability presented by FTP?</div>
    <div class="answer-box">
        <div class="answer-label">SOC Analyst Security Finding:</div>
        <p>
        The fundamental security vulnerability of the File Transfer Protocol (FTP - RFC 959) is that it <strong>transmits all control and data traffic in unencrypted cleartext</strong>.
        </p>
        <ul>
            <li><strong>Credential Sniffing:</strong> Authentication credentials (<code class="inline">USER cisco</code> and <code class="inline">PASS cisco</code>) are sent over the wire in plain ASCII with zero cryptographic protection.</li>
            <li><strong>Confidentiality Breach:</strong> Transferred files (such as <code class="inline">clientinfo.txt</code>) can be eavesdropped, reconstructed, and stolen by any adversary with access to an inline sniffer, mirrored switchport, or compromised transit router.</li>
            <li><strong>Data Tampering (MitM):</strong> Cleartext streams lack cryptographic integrity checks, enabling Man-in-the-Middle attackers to modify file payloads in transit without detection.</li>
        </ul>
    </div>
</div>

<div class="qa-card">
    <div class="question-title">Part 2 &mdash; Vulnerability Mitigation Strategy</div>
    <div class="question-text">What should be done to mitigate this vulnerability?</div>
    <div class="answer-box">
        <div class="answer-label">SOC Defensive Engineering Controls:</div>
        <ol>
            <li><strong>Enforce Encrypted File Transfer Protocols:</strong>
                <ul>
                    <li><strong>SFTP (SSH File Transfer Protocol):</strong> Replaces FTP with a single secure channel running over SSH (TCP Port 22), providing strong public-key/password authentication and symmetric encryption (AES-256-GCM).</li>
                    <li><strong>FTPS (FTP Secure / FTP over TLS):</strong> Upgrades legacy FTP by wrapping both control (Port 21) and data connections in Transport Layer Security (TLS 1.3).</li>
                    <li><strong>HTTPS / Secure WebDAV:</strong> Secure RESTful or web-based file management over TLS (TCP Port 443).</li>
                </ul>
            </li>
            <li><strong>Transport Encryption & Segmentation:</strong> If legacy FTP cannot be immediately deprecated, encapsulate all transit traffic through an <strong>IPsec VPN tunnel</strong> or encrypted site-to-site GRE over IPsec.</li>
            <li><strong>Access Control Lists (ACLs):</strong> Restrict FTP server access strictly to authorized management IP ranges.</li>
        </ol>
    </div>
</div>

<h2>Part 3: View Syslog Messages & Network Visibility Analysis</h2>

<h3>Step 1: Remotely Enable ICMP Debugging on Router2</h3>
<p>From PC-B, Telnet is used to access Router2 and activate real-time ICMP packet debugging:</p>

<div class="terminal">
<span class="prompt">PC-B:\> </span><span class="cmd">telnet 209.165.200.226</span>
<span class="output">User Access Verification
Username: </span><span class="cmd">ADMIN</span>
<span class="output">Password: </span><span class="cmd">CISCO</span>
<span class="prompt">Router2# </span><span class="cmd">debug ip icmp</span>
<span class="output">ICMP packet debugging is on</span>
<span class="prompt">Router2# </span><span class="cmd">logout</span>
</div>

<h3>Step 2: Generate Traffic and Inspect Syslog Server Records</h3>
<p>
Ping packets are transmitted to Router2 (<code class="inline">209.165.200.226</code>) from host <code class="inline">PC-B</code> and host <code class="inline">PC-A</code>. The SYSLOG_SERVER captures the router's ICMP debug output:
</p>

<div class="terminal">
<span class="output">SYS-5-CONFIG_I: Configured from console by ADMIN on vty0 (209.165.200.230)
ICMP: echo reply sent, src 209.165.200.226, dst 209.165.200.230, topology BASE, dscp 0 topoid 0
ICMP: echo reply sent, src 209.165.200.226, dst 209.165.200.230, topology BASE, dscp 0 topoid 0
ICMP: echo reply sent, src 209.165.200.226, dst 209.165.200.230, topology BASE, dscp 0 topoid 0
ICMP: echo reply sent, src 209.165.200.226, dst 209.165.200.230, topology BASE, dscp 0 topoid 0</span>
</div>

<div class="qa-card">
    <div class="question-title">Part 3.h &mdash; NAT Obfuscation & Log Attribution Analysis</div>
    <div class="question-text">Can you tell which echo replies are for PC-A and PC-B from the destination addresses? Explain.</div>
    <div class="answer-box">
        <div class="answer-label">SOC Forensic Analysis:</div>
        <p>
        <strong>No, it is impossible to distinguish between PC-A and PC-B solely from the destination IP addresses in the syslog messages.</strong>
        </p>
        <p>
        <strong>Technical Explanation:</strong> Both PC-A and PC-B reside in private IPv4 address spaces (RFC 1918). As their packets traverse the perimeter NAT/PAT gateway (Router1/Edge Router), their private source IP addresses are translated via <strong>Port Address Translation (NAT Overload)</strong> into a single shared public IPv4 address (<code class="inline">209.165.200.230</code>).
        </p>
        <p>
        When Router2 generates ICMP echo replies, it addresses them to this shared public NAT address. From the perspective of Router2 and the centralized Syslog server, all ICMP replies share the exact same destination IP (<code class="inline">209.165.200.230</code>). To correlate which reply corresponds to which physical endpoint, an analyst must correlate router syslog events with the edge gateway's internal NAT translation table (<code class="inline">show ip nat translations</code>) using port/sequence mappings.
        </p>
    </div>
</div>

<div class="qa-card">
    <div class="question-title">Part 3.i &mdash; PC-C Ping Behavior Prediction</div>
    <div class="question-text">Ping Router2 from PC-C. What will the destination address for the replies be?</div>
    <div class="answer-box">
        <div class="answer-label">Technical Observation:</div>
        <p>
        The destination address for the echo replies generated for PC-C will also be the <strong>public NAT interface address</strong> (<code class="inline">209.165.200.230</code> or the specific public NAT pool address assigned to PC-C's gateway subnet).
        </p>
        <p>
        Because PC-C also resides behind an edge NAT boundary, its private IP address is hidden, and Router2 replies directly to the translated public address visible on the WAN link.
        </p>
    </div>
</div>

<div class="key-takeaways">
    <h3>SOC Analyst Architecture Takeaways</h3>
    <ul>
        <li><span class="badge-tag badge-red">Legacy Risk</span> Plaintext protocols (FTP, Telnet, HTTP) must be prohibited across enterprise networks due to passive sniffing vulnerabilities.</li>
        <li><span class="badge-tag badge-blue">NAT Blindness</span> NAT hides internal network host identities from external routers and centralized logs. SOC log ingestion pipelines must ingest both <strong>perimeter NAT flow logs</strong> and <strong>internal DHCP/endpoint logs</strong> to enable IP-to-hostname attribution.</li>
        <li><span class="badge-tag badge-green">Centralized Syslog</span> Syslog (UDP/TCP 514) provides centralized real-time telemetry. In production, <strong>TLS-encrypted Syslog (RFC 5425)</strong> should be used to prevent tampering with security event logs in transit.</li>
    </ul>
</div>

</body>
</html>"""

def main():
    print("Generating Lab 15.2.7 Solution PDF...")
    output_pdf = os.path.join(LABS_DIR, "15.2.7-Packet-Tracer-Logging-Network-Activity-Solution.pdf")
    
    temp_html = os.path.join(TEMP_DIR, "temp_lab_15_2_7.html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(LAB_15_2_7_HTML)
    
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    user_data_dir = os.path.join(TEMP_DIR, "edge-pdf-lab-15-2-7")
    
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
