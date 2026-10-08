"""
Generate Lab 10.6.7 Solution PDF:
Module 10 - Network Services
Lab 10.6.7: Lab - Using Wireshark to Examine HTTP and HTTPS Traffic
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
        content: "HTTP CLEAR-TEXT VS. HTTPS/TLS TRAFFIC ANALYSIS REPORT";
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

LAB_10_6_7_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Lab 10.6.7 - Using Wireshark to Examine HTTP and HTTPS Traffic Solution</title>
<style>
{CSS}
</style>
</head>
<body>

<div class="doc-header">
    <div class="badge">Cisco Certified CyberOps Associate (CBROPS 200-201)</div>
    <h1>Lab 10.6.7: Using Wireshark to Examine HTTP & HTTPS Traffic</h1>
    <div class="subtitle">Packet Capture Automation with tcpdump, Cleartext Credential Interception & TLS Cryptographic Dissection</div>
</div>

<div class="meta-grid">
    <div class="meta-item">
        <div class="meta-label">Course Module</div>
        <div class="meta-value">Module 10: Network Services</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Protocols Inspected</div>
        <div class="meta-value">HTTP (TCP 80) & HTTPS / TLS (TCP 443)</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">CLI & GUI Tools</div>
        <div class="meta-value">tcpdump & Wireshark Analyzer</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Workstation Environment</div>
        <div class="meta-value">CyberOps Workstation VM (analyst)</div>
    </div>
</div>

<h2>Objectives</h2>
<ul>
    <li><strong>Part 1: Capture and View Cleartext HTTP Traffic</strong> &mdash; Use <code class="inline">tcpdump</code> to capture unencrypted HTTP web traffic to <code class="inline">httpdump.pcap</code> and extract cleartext authentication credentials from HTTP POST forms in Wireshark.</li>
    <li><strong>Part 2: Capture and View Encrypted HTTPS Traffic</strong> &mdash; Record TLS-encrypted web sessions to <code class="inline">httpsdump.pcap</code>, dissect the TLS Record Layer, and analyze encrypted application data obfuscation.</li>
    <li><strong>Reflection & Security Architecture Evaluation</strong> &mdash; Evaluate the cryptographic triad (Confidentiality, Integrity, Authentication) of HTTPS and examine how adversaries abuse SSL/TLS certificates for malicious operations.</li>
</ul>

<h2>Background / Scenario</h2>
<p>
The HyperText Transfer Protocol (HTTP) is the foundational application-layer protocol of the World Wide Web. However, legacy HTTP transmits all data &mdash; including web pages, session cookies, form inputs, and authentication credentials &mdash; in plain, unencrypted ASCII text.
</p>
<p>
HyperText Transfer Protocol Secure (HTTPS) secures web communications by encapsulating HTTP inside the Transport Layer Security (TLS) protocol. Through symmetric encryption, asymmetric key exchange, and X.509 digital certificates, HTTPS protects data from interception, tampering, and impersonation.
</p>
<p>
In this lab, network security analysts practice automated command-line packet sniffing using <code class="inline">tcpdump</code> and forensic packet dissection in Wireshark to contrast unencrypted HTTP against encrypted HTTPS traffic.
</p>

<h2>Part 1: Capture and View Cleartext HTTP Traffic</h2>

<h3>Step 1 & 2: Interface Discovery & Automated tcpdump Execution</h3>
<p>Checking network interfaces on the CyberOps Workstation VM:</p>

<div class="terminal">
<span class="prompt">[analyst@secOps ~]$ </span><span class="cmd">ip address</span>
<span class="output">1: lo: &lt;LOOPBACK,UP,LOWER_UP&gt; mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet <span class="highlight">127.0.0.1/8</span> scope host lo
2: enp0s3: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether <span class="highlight">08:00:27:da:28:83</span> brd ff:ff:ff:ff:ff:ff
    inet <span class="highlight">192.168.8.10/24</span> brd 192.168.8.255 scope global dynamic enp0s3</span>
</div>

<div class="qa-card">
    <div class="question-title">Step 2.b &mdash; Interface & Addressing Identification</div>
    <div class="question-text">List the interfaces and their IP addresses displayed in the ip address output.</div>
    <div class="answer-box">
        <div class="answer-label">Analyst Finding:</div>
        <ul>
            <li><strong><code class="inline">lo</code> (Loopback Interface):</strong> IPv4 address <code class="inline">127.0.0.1/8</code> (and IPv6 <code class="inline">::1/128</code>), used for internal inter-process communication.</li>
            <li><strong><code class="inline">enp0s3</code> (Ethernet Adapter):</strong> IPv4 address <code class="inline">192.168.8.10/24</code> (or VM IP <code class="inline">10.0.2.15/24</code>) with MAC address <code class="inline">08:00:27:da:28:83</code>, connecting the workstation to the local network and internet.</li>
        </ul>
    </div>
</div>

<h3>Starting tcpdump Capture & Generating HTTP Traffic</h3>
<p>
The command-line packet analyzer <code class="inline">tcpdump</code> is initiated to write full packet snapshots to disk:
</p>

<div class="terminal">
<span class="prompt">[analyst@secOps ~]$ </span><span class="cmd">sudo tcpdump -i enp0s3 -s 0 -w httpdump.pcap</span>
<span class="output">[sudo] password for analyst: cyberops
tcpdump: listening on enp0s3, link-type EN10MB (Ethernet), capture size 262144 bytes</span>
</div>

<table class="data-table">
    <thead>
        <tr>
            <th>tcpdump Flag</th>
            <th>Argument Provided</th>
            <th>Technical Purpose & SOC Best Practice</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code class="inline">-i</code></td>
            <td><code class="inline">enp0s3</code></td>
            <td>Binds packet capture specifically to the active Ethernet interface.</td>
        </tr>
        <tr>
            <td><code class="inline">-s</code></td>
            <td><code class="inline">0</code> (or 262144)</td>
            <td>Sets Snapshot Length (<code class="inline">snaplen</code>) to capture full packet payloads without truncation.</td>
        </tr>
        <tr>
            <td><code class="inline">-w</code></td>
            <td><code class="inline">httpdump.pcap</code></td>
            <td>Writes raw libpcap binary capture data directly to file for Wireshark analysis.</td>
        </tr>
    </tbody>
</table>

<p>
The analyst navigates to the unencrypted test banking portal: <code class="inline">http://www.altoromutual.com/login.jsp</code> and logs in using username <code class="inline">Admin</code> and password <code class="inline">Admin</code>. Capture is terminated with <kbd>Ctrl + C</kbd>.
</p>

<h3>Step 3: Forensic Wireshark Analysis of httpdump.pcap</h3>
<p>
Opening <code class="inline">httpdump.pcap</code> in Wireshark and applying display filter <code class="inline">http</code> isolates the HTTP conversation. Selecting the <code class="inline">POST /doLogin</code> request reveals the HTML Form URL Encoded payload:
</p>

<div class="terminal">
<span class="danger"># Wireshark Packet Details (Frame 54 - HTTP POST /doLogin):</span>
Hypertext Transfer Protocol
    POST /doLogin HTTP/1.1\r\n
    Host: www.altoromutual.com\r\n
    Content-Type: application/x-www-form-urlencoded\r\n
    Content-Length: 38\r\n
HTML Form URL Encoded: application/x-www-form-urlencoded
    Form item: "<span class="danger">uid</span>" = "<span class="danger">Admin</span>"
    Form item: "<span class="danger">passw</span>" = "<span class="danger">Admin</span>"
    Form item: "btnSubmit" = "Login"
</div>

<div class="qa-card security">
    <div class="question-title">Step 3.d &mdash; Cleartext Credential Interception</div>
    <div class="question-text">What two pieces of information are displayed?</div>
    <div class="answer-box">
        <div class="answer-label">SOC Incident Evidence:</div>
        <p>
        Expanding the <code class="inline">HTML Form URL Encoded: application/x-www-form-urlencoded</code> tree exposes the user's sensitive login credentials in <strong>completely unencrypted plaintext</strong>:
        </p>
        <ol>
            <li><strong>Username Field (<code class="inline">uid</code>):</strong> <strong style="color: #dc2626;"><code class="inline">Admin</code></strong></li>
            <li><strong>Password Field (<code class="inline">passw</code>):</strong> <strong style="color: #dc2626;"><code class="inline">Admin</code></strong></li>
        </ol>
        <p><em>Security Impact:</em> Any attacker eavesdropping on the local network (via Wi-Fi sniffing, ARP spoofing, or rogue gateway) captures full administrative credentials with zero decryption effort.</p>
    </div>
</div>

<h2>Part 2: Capture and View Encrypted HTTPS Traffic</h2>

<h3>Step 1: Capture HTTPS Traffic to httpsdump.pcap</h3>
<div class="terminal">
<span class="prompt">[analyst@secOps ~]$ </span><span class="cmd">sudo tcpdump -i enp0s3 -s 0 -w httpsdump.pcap</span>
<span class="output">[sudo] password for analyst: cyberops
tcpdump: listening on enp0s3, link-type EN10MB (Ethernet), capture size 262144 bytes</span>
</div>

<p>The browser navigates to the secure portal: <code class="inline">https://www.netacad.com</code>, and authentication is initiated.</p>

<div class="qa-card">
    <div class="question-title">Step 1.b &mdash; URL Scheme & Security Indicators</div>
    <div class="question-text">What do you notice about the website URL?</div>
    <div class="answer-box">
        <div class="answer-label">Analyst Observation:</div>
        <ul>
            <li><strong>Protocol Prefix:</strong> The URL begins with <strong><code class="inline">https://</code></strong> (HyperText Transfer Protocol Secure) rather than <code class="inline">http://</code>.</li>
            <li><strong>Security Padlock Indicator:</strong> A visual padlock icon appears in the browser address bar, confirming that the session is secured via <strong>Transport Layer Security (TLS)</strong> encryption validated by a trusted public Certificate Authority (CA).</li>
            <li><strong>Standard Port:</strong> Traffic is directed over <strong>TCP Port 443</strong> instead of standard HTTP Port 80.</li>
        </ul>
    </div>
</div>

<h3>Step 2: Forensic Wireshark Analysis of httpsdump.pcap</h3>
<p>
Filtering by <code class="inline">tcp.port == 443</code> or <code class="inline">tls</code> displays the TLS Handshake (Client Hello, Server Hello, Certificate Exchange, Key Exchange) followed by bidirectional <strong>Application Data</strong> records:
</p>

<div class="qa-card">
    <div class="question-title">Step 2.d &mdash; Protocol Layer Replacement</div>
    <div class="question-text">What has replaced the HTTP section that was in the previous capture file?</div>
    <div class="answer-box">
        <div class="answer-label">Dissection Finding:</div>
        <p>
        The plain-text <code class="inline">Hypertext Transfer Protocol</code> application layer has been completely replaced by the <strong><code class="inline">Transport Layer Security (TLS)</code> / <code class="inline">Secure Sockets Layer (SSL)</code></strong> protocol layer (e.g., <em>TLSv1.2 / TLSv1.3 Record Layer: Application Data Protocol: http-over-tls</em>).
        </p>
    </div>
</div>

<div class="qa-card">
    <div class="question-title">Step 2.f &mdash; Ciphertext & Application Data Inspection</div>
    <div class="question-text">Is the application data in a plaintext or readable format?</div>
    <div class="answer-box">
        <div class="answer-label">Cryptographic Verification:</div>
        <p>
        <strong>No.</strong> The application data is completely unreadable, represented as high-entropy pseudorandom <strong>Encrypted Application Data (Ciphertext)</strong>:
        </p>
        <div class="terminal">
<span class="output">Transport Layer Security
    TLSv1.2 Record Layer: Application Data Protocol: http-over-tls
        Content Type: Application Data (23)
        Version: TLS 1.2 (0x0303)
        Length: 1424
        <span class="highlight">Encrypted Application Data: 7f8a91b4c3e201d4a8f9021... [1424 bytes]</span></span>
        </div>
        <p>All HTTP headers, URLs, cookies, usernames, and passwords are encrypted by symmetric session ciphers (e.g., AES-GCM, ChaCha20-Poly1305), preventing passive sniffing.</p>
    </div>
</div>

<h2>Reflection Questions & Threat Analysis</h2>

<div class="qa-card reflection">
    <div class="question-title">Reflection Question 1 &mdash; Core Advantages of HTTPS over HTTP</div>
    <div class="question-text">What are the advantages of using HTTPS instead of HTTP?</div>
    <div class="answer-box">
        <div class="answer-label">Security Triad & Architectural Benefits:</div>
        <ol>
            <li><strong>Data Confidentiality (Encryption):</strong> Protects all transmitted data (PII, passwords, credit cards, medical records) from network eavesdropping, packet sniffing, and unauthorized interceptors.</li>
            <li><strong>Data Integrity (Anti-Tampering):</strong> Employs Message Authentication Codes (MAC / AEAD) ensuring packets cannot be altered, modified, or injected with malware/ads in transit without instant connection termination.</li>
            <li><strong>Mutual Authentication & Trust:</strong> Digital X.509 certificates cryptographically verify that the user is connecting to the authentic domain owner and not a spoofed phishing server or DNS clone.</li>
            <li><strong>Regulatory & Privacy Compliance:</strong> Mandated by security standards worldwide (PCI-DSS, GDPR, HIPAA, ISO 27001).</li>
        </ol>
    </div>
</div>

<div class="qa-card security">
    <div class="question-title">Reflection Question 2 &mdash; The HTTPS Trust Fallacy in Modern Threat Landscapes</div>
    <div class="question-text">Are all websites that use HTTPS considered trustworthy?</div>
    <div class="answer-box">
        <div class="answer-label">Critical SOC Threat Intelligence Insight:</div>
        <p>
        <strong>NO. Absolutely not.</strong>
        </p>
        <p>
        <strong>Detailed Rationale:</strong> HTTPS only guarantees that the connection between the client browser and the server is <em>encrypted</em> and that the domain matches the issued digital certificate. It provides <strong>zero guarantee regarding the legitimacy, safety, or moral intent of the website owner</strong>.
        </p>
        <ul>
            <li><strong>Abuse by Threat Actors:</strong> Cybercriminals easily obtain free, valid TLS certificates (via Let's Encrypt, Cloudflare, ZeroSSL) for malicious phishing websites, fake banking portals, and malware distribution points.</li>
            <li><strong>C2 Channel Obfuscation:</strong> Modern malware and Command and Control (C2) frameworks (Cobalt Strike, Sliver, Meterpreter) routinely use HTTPS over Port 443 specifically to blend in with legitimate enterprise web traffic and evade legacy firewall deep packet inspection.</li>
            <li><strong>User Deception:</strong> Many users mistakenly believe the "secure padlock" means the site is safe to enter credentials, making HTTPS-enabled phishing portals exceptionally dangerous.</li>
        </ul>
    </div>
</div>

<div class="key-takeaways">
    <h3>SOC Analyst Protocol Comparison Matrix</h3>
    <table class="data-table">
        <thead>
            <tr>
                <th>Security Property</th>
                <th>HTTP (HyperText Transfer Protocol)</th>
                <th>HTTPS (HTTP over TLS/SSL)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Default Port</strong></td>
                <td>TCP Port 80</td>
                <td>TCP Port 443</td>
            </tr>
            <tr>
                <td><strong>Wire Payload</strong></td>
                <td>Plaintext ASCII (Completely readable)</td>
                <td>Encrypted Ciphertext (AES-GCM / ChaCha20)</td>
            </tr>
            <tr>
                <td><strong>Vulnerability to Sniffing</strong></td>
                <td>Critical &mdash; Instant credential theft</td>
                <td>Protected &mdash; Requires TLS decryption key / MitM proxy</td>
            </tr>
            <tr>
                <td><strong>Identity Verification</strong></td>
                <td>None (Vulnerable to spoofing)</td>
                <td>X.509 Certificate Authority Validation</td>
            </tr>
            <tr>
                <td><strong>SOC Inspection Strategy</strong></td>
                <td>Direct payload analysis with Snort/Suricata</td>
                <td>TLS Decryption / SSL Forward Proxy / JA3 Fingerprinting</td>
            </tr>
        </tbody>
    </table>
</div>

</body>
</html>"""

def main():
    print("Generating Lab 10.6.7 Solution PDF...")
    output_pdf = os.path.join(LABS_DIR, "10.6.7-Lab-Using-Wireshark-to-Examine-HTTP-and-HTTPS-Traffic-Solution.pdf")
    
    temp_html = os.path.join(TEMP_DIR, "temp_lab_10_6_7.html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(LAB_10_6_7_HTML)
    
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    user_data_dir = os.path.join(TEMP_DIR, "edge-pdf-lab-10-6-7")
    
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
