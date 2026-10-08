"""
Generate Chapters 11 to 19 Master Test Prep Guide & High-Yield Review PDF
Course: Cisco Certified CyberOps Associate (CBROPS 200-201)
Scope: NetAcad Modules 11 to 19
"""

import os
import subprocess

WORKSPACE_DIR = r"C:\Users\fanele\CyberOps Associate\CyberOps-Associate"
TEMP_DIR = os.environ.get("TEMP", r"C:\Users\fanele\AppData\Local\Temp")

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

@page {
    size: A4;
    margin: 14mm 14mm 15mm 14mm;
    @top-left {
        content: "CISCO CYBEROPS ASSOCIATE | CHAPTERS 11 TO 19 MASTER TEST PREPARATION";
        font-family: 'Inter', sans-serif;
        font-size: 7pt;
        font-weight: 700;
        color: #0284c7;
        letter-spacing: 0.5px;
    }
    @top-right {
        content: "HIGH-YIELD REVISION & EXAM REVIEW GUIDE";
        font-family: 'Inter', sans-serif;
        font-size: 7pt;
        color: #64748b;
        font-weight: 600;
    }
    @bottom-left {
        content: "CISCO NETWORKING ACADEMY (NETACAD) CURRICULUM ALIGNED";
        font-family: 'Inter', sans-serif;
        font-size: 7pt;
        color: #0369a1;
        font-weight: 600;
    }
    @bottom-right {
        content: "Page " counter(page) " of " counter(pages);
        font-family: 'Inter', sans-serif;
        font-size: 7.5pt;
        font-weight: 700;
        color: #0f172a;
    }
}

*, *::before, *::after {
    box-sizing: border-box;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    font-size: 8.5pt;
    line-height: 1.45;
    color: #1e293b;
    background-color: #ffffff;
}

.header-banner {
    border-bottom: 2.5px solid #0284c7;
    padding-bottom: 8px;
    margin-bottom: 12px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
}

.title-box h1 {
    font-size: 16pt;
    font-weight: 900;
    color: #0f172a;
    margin: 0 0 2px 0;
    letter-spacing: -0.02em;
    text-transform: uppercase;
}

.title-box h2 {
    font-size: 9.5pt;
    font-weight: 700;
    color: #0284c7;
    margin: 0;
}

.badge-box {
    text-align: right;
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.5pt;
    color: #475569;
}

.badge-tag {
    display: inline-block;
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: 700;
    text-transform: uppercase;
    font-size: 6.5pt;
}

.badge-blue { background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; }
.badge-green { background: #dcfce7; color: #15803d; border: 1px solid #bbf7d0; }
.badge-red { background: #fee2e2; color: #b91c1c; border: 1px solid #fecaca; }
.badge-purple { background: #f3e8ff; color: #7e22ce; border: 1px solid #e9d5ff; }

h3.section-header {
    font-size: 10pt;
    font-weight: 800;
    color: #0f172a;
    border-left: 4px solid #0284c7;
    padding-left: 8px;
    margin: 12px 0 8px 0;
    text-transform: uppercase;
    letter-spacing: 0.03em;
}

.grid-2 {
    display: flex;
    gap: 10px;
    margin-bottom: 10px;
}

.grid-2 > div {
    flex: 1;
}

.card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 8px 10px;
    margin-bottom: 8px;
}

.card h4 {
    margin: 0 0 4px 0;
    font-size: 8.5pt;
    font-weight: 800;
    color: #0f172a;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 6px 0 10px 0;
    font-size: 7.5pt;
}

th {
    background-color: #0f172a;
    color: #ffffff;
    font-weight: 600;
    text-align: left;
    padding: 5px 6px;
    border: 1px solid #0f172a;
}

td {
    padding: 4px 6px;
    border: 1px solid #e2e8f0;
    vertical-align: top;
}

tr:nth-child(even) td {
    background-color: #f8fafc;
}

.code-box {
    background: #0f172a;
    color: #f8fafc;
    font-family: 'JetBrains Mono', monospace;
    font-size: 7pt;
    padding: 6px 8px;
    border-radius: 4px;
    margin: 4px 0;
    line-height: 1.35;
}

.alert-box {
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    border-left: 4px solid #2563eb;
    padding: 6px 10px;
    border-radius: 4px;
    margin: 8px 0;
    font-size: 7.8pt;
}

ul {
    margin: 2px 0 6px 0;
    padding-left: 16px;
}

li {
    margin-bottom: 2px;
}

.page-break {
    page-break-before: always;
}
"""

REPORT_HTML = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Chapters 11 to 19 Master Test Prep Guide</title>
<style>{CSS}</style>
</head>
<body>

<div class="header-banner">
    <div class="title-box">
        <h1>Modules 11 to 19 Master Exam Prep Guide</h1>
        <h2>Cisco Certified CyberOps Associate (CBROPS 200-201)</h2>
    </div>
    <div class="badge-box">
        <span class="badge-tag badge-blue">OFFICIAL CURRICULUM REVIEW</span><br>
        Scope: Chapters 11, 12, 13, 14, 15, 16, 17, 18, 19<br>
        Format: High-Yield Knowledge & Exam Traps
    </div>
</div>

<h3 class="section-header">1. Key Comparison Matrices (The Top Most-Tested Concepts)</h3>

<div class="grid-2">
    <div>
        <h4 style="font-size: 8pt; color: #0284c7; margin: 0 0 4px 0;">TACACS+ vs. RADIUS (Module 19)</h4>
        <table>
            <thead>
                <tr>
                    <th>Feature</th>
                    <th>TACACS+</th>
                    <th>RADIUS</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Protocol / Port</strong></td>
                    <td><strong>TCP Port 49</strong></td>
                    <td><strong>UDP Ports 1812 / 1813</strong></td>
                </tr>
                <tr>
                    <td><strong>Encryption</strong></td>
                    <td><strong>Entire packet payload</strong></td>
                    <td><strong>Password field only</strong></td>
                </tr>
                <tr>
                    <td><strong>AAA Separation</strong></td>
                    <td>Strictly separates Auth/Authz</td>
                    <td>Combines Auth/Authz</td>
                </tr>
                <tr>
                    <td><strong>Primary Role</strong></td>
                    <td>Device Administration</td>
                    <td>Network Access (802.1X/VPN)</td>
                </tr>
            </tbody>
        </table>
    </div>
    <div>
        <h4 style="font-size: 8pt; color: #0284c7; margin: 0 0 4px 0;">SPAN vs. Network TAP (Module 15)</h4>
        <table>
            <thead>
                <tr>
                    <th>Feature</th>
                    <th>SPAN (Port Mirror)</th>
                    <th>Network TAP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Nature</strong></td>
                    <td>Switch software feature</td>
                    <td>Dedicated physical hardware</td>
                </tr>
                <tr>
                    <td><strong>Switch Impact</strong></td>
                    <td>Consumes CPU; drops frames</td>
                    <td><strong>Zero load</strong> on network switches</td>
                </tr>
                <tr>
                    <td><strong>Corrupted Packets</strong></td>
                    <td>Drops CRC/runt frames</td>
                    <td><strong>Captures 100%</strong> of malformed frames</td>
                </tr>
                <tr>
                    <td><strong>Power Needed</strong></td>
                    <td>Powered via switch</td>
                    <td>Passive fiber TAPs require <strong>no power</strong></td>
                </tr>
            </tbody>
        </table>
    </div>
</div>

<div class="grid-2">
    <div>
        <h4 style="font-size: 8pt; color: #0284c7; margin: 0 0 4px 0;">IPsec Protocols & Modes (Module 12)</h4>
        <table>
            <thead>
                <tr>
                    <th>Protocol / Mode</th>
                    <th>Confidentiality (Encryption)</th>
                    <th>Integrity / Auth</th>
                    <th>IP Header Behavior</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>AH (Protocol 51)</strong></td>
                    <td>NO (Cleartext payload)</td>
                    <td>YES</td>
                    <td>Protects original IP header</td>
                </tr>
                <tr>
                    <td><strong>ESP (Protocol 50)</strong></td>
                    <td><strong>YES (AES/3DES)</strong></td>
                    <td>YES</td>
                    <td>Protects payload + ESP trailer</td>
                </tr>
                <tr>
                    <td><strong>Transport Mode</strong></td>
                    <td>Encrypted payload only</td>
                    <td>YES</td>
                    <td>Keeps original IP header</td>
                </tr>
                <tr>
                    <td><strong>Tunnel Mode</strong></td>
                    <td>Encrypted original packet</td>
                    <td>YES</td>
                    <td><strong>Adds a NEW outer IP header</strong></td>
                </tr>
            </tbody>
        </table>
    </div>
    <div>
        <h4 style="font-size: 8pt; color: #0284c7; margin: 0 0 4px 0;">Access Control Models (Module 19)</h4>
        <table>
            <thead>
                <tr>
                    <th>Model</th>
                    <th>Decision Basis</th>
                    <th>Authority</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>DAC</strong></td>
                    <td>Resource Owner's discretion</td>
                    <td>Data Creator (NTFS, chmod)</td>
                </tr>
                <tr>
                    <td><strong>MAC</strong></td>
                    <td>Sensitivity labels vs. clearance</td>
                    <td>Central OS / Military (SELinux)</td>
                </tr>
                <tr>
                    <td><strong>RBAC</strong></td>
                    <td>Organizational job role</td>
                    <td>System Administrator (AD Groups)</td>
                </tr>
                <tr>
                    <td><strong>ABAC</strong></td>
                    <td>Dynamic attributes (time, device)</td>
                    <td>Policy Engine (Cloud IAM, ISE)</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>

<h3 class="section-header">2. Layer-by-Layer Attack & Defense Summary (Modules 16 & 17)</h3>
<table>
    <thead>
        <tr>
            <th style="width: 15%;">Protocol Layer</th>
            <th style="width: 25%;">Primary Attack Vectors</th>
            <th style="width: 35%;">Mechanics / Indicators</th>
            <th style="width: 25%;">Defensive Countermeasure</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Layer 2: ARP</strong></td>
            <td>ARP Poisoning / Spoofing</td>
            <td>Forged Gratuitous ARP replies corrupt local ARP caches, creating a Man-in-the-Middle (MitM).</td>
            <td><strong>Dynamic ARP Inspection (DAI)</strong> with DHCP Snooping binding table.</td>
        </tr>
        <tr>
            <td><strong>Layer 2: DHCP</strong></td>
            <td>DHCP Starvation & Rogue DHCP</td>
            <td>Flooding fake MACs (Yersinia) exhausts IP pool; rogue DHCP server assigns fake gateway and DNS.</td>
            <td><strong>DHCP Snooping</strong> (Untrusted ports drop incoming DHCP offers).</td>
        </tr>
        <tr>
            <td><strong>Layer 3: IP</strong></td>
            <td>Teardrop & IP Spoofing</td>
            <td>Overlapping fragment offset fields crash reassembly buffers; spoofed source IPs bypass filters.</td>
            <td>Drop overlapping fragments; egress/ingress anti-spoofing ACLs (RFC 2827).</td>
        </tr>
        <tr>
            <td><strong>Layer 3: ICMP</strong></td>
            <td>Smurf & Ping of Death</td>
            <td>Smurf sends spoofed ping to directed broadcast; Ping of Death exceeds 65,535-byte IP size.</td>
            <td><code class="inline">no ip directed-broadcast</code> on Cisco router interfaces.</td>
        </tr>
        <tr>
            <td><strong>Layer 4: TCP</strong></td>
            <td>SYN Flood & TCP Reset (RST)</td>
            <td>Exhausts half-open connection backlog table; forged RST packets terminate active sessions.</td>
            <td>TCP SYN cookies, stateful inspection, TCP sequence number randomization.</td>
        </tr>
        <tr>
            <td><strong>Layer 7: DNS</strong></td>
            <td>DNS Tunneling & Cache Poisoning</td>
            <td>Exfiltrates data inside subdomain queries (exfil.attacker.com); injects fake IP mappings.</td>
            <td><strong>DNSSEC</strong> cryptographic signing; Cisco Umbrella DNS filtering.</td>
        </tr>
        <tr>
            <td><strong>Layer 7: Web</strong></td>
            <td>SQLi, XSS, and CSRF</td>
            <td>SQLi extracts database records; XSS executes client-side scripts; CSRF hijacks user state.</td>
            <td><strong>Parameterized Queries</strong>, input validation, Anti-CSRF synchronizer tokens.</td>
        </tr>
    </tbody>
</table>

<div class="page-break"></div>

<div class="header-banner">
    <div class="title-box">
        <h1>Modules 11 to 19 Master Exam Prep Guide (Part 2)</h1>
        <h2>Cisco Certified CyberOps Associate • Operations, Metrics & Architecture</h2>
    </div>
    <div class="badge-box">
        <span class="badge-tag badge-purple">SOC OPERATIONS & PROTOCOLS</span>
    </div>
</div>

<h3 class="section-header">3. SOC Operations, Metrics & Disaster Recovery (Module 18)</h3>

<div class="grid-2">
    <div class="card">
        <h4><span class="badge-tag badge-red">SOC ALERT MATRIX</span> The 4 Alert Classifications</h4>
        <ul>
            <li><strong>True Positive (TP):</strong> Malicious attack occurring $\rightarrow$ Alert generated. *(Accurate detection)*</li>
            <li><strong>False Positive (FP):</strong> Benign business traffic $\rightarrow$ Alert generated. *(Nuisance alert / noise)*</li>
            <li><strong>True Negative (TN):</strong> Normal traffic $\rightarrow$ No alert generated. *(Proper operation)*</li>
            <li><strong>False Negative (FN):</strong> Malicious attack occurring $\rightarrow$ <strong>NO alert generated</strong>. *(Worst-case catastrophic failure)*</li>
        </ul>
    </div>
    <div class="card">
        <h4><span class="badge-tag badge-blue">METRICS & DRP</span> Disaster Recovery Objectives</h4>
        <ul>
            <li><strong>RTO (Recovery Time Objective):</strong> Maximum tolerable <strong>downtime duration</strong> before business catastrophe.</li>
            <li><strong>RPO (Recovery Point Objective):</strong> Maximum tolerable <strong>data loss measured in time</strong>.</li>
            <li><strong>Hot Site:</strong> Real-time replicated data and live hardware; failover in <strong>minutes/hours</strong>.</li>
            <li><strong>Warm Site:</strong> Hardware present; software/data must be loaded; failover in <strong>days</strong>.</li>
            <li><strong>Cold Site:</strong> Empty facility with power/HVAC; hardware must be ordered; failover in <strong>weeks</strong>.</li>
        </ul>
    </div>
</div>

<h3 class="section-header">4. High-Yield Must-Know Port Numbers & Protocol Checklist</h3>
<table>
    <thead>
        <tr>
            <th style="width: 15%;">Port Number</th>
            <th style="width: 20%;">Protocol Name</th>
            <th style="width: 15%;">Transport</th>
            <th style="width: 50%;">Exam Relevance & Trap Warning</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>22</strong></td>
            <td>SSH</td>
            <td>TCP</td>
            <td>Encrypted terminal management. Replaces unencrypted Telnet (Port 23).</td>
        </tr>
        <tr>
            <td><strong>49</strong></td>
            <td>TACACS+</td>
            <td>TCP</td>
            <td>Cisco AAA device admin. <strong>Encrypts ENTIRE payload</strong>, separates authentication and authorization.</td>
        </tr>
        <tr>
            <td><strong>53</strong></td>
            <td>DNS</td>
            <td>UDP / TCP</td>
            <td>UDP for regular queries (&lt;512 bytes); <strong>TCP for Zone Transfers (AXFR)</strong> and responses &gt;512 bytes.</td>
        </tr>
        <tr>
            <td><strong>67 / 68</strong></td>
            <td>DHCP</td>
            <td>UDP</td>
            <td>Port 67 = Server; Port 68 = Client. Targeted by starvation and rogue server attacks.</td>
        </tr>
        <tr>
            <td><strong>123</strong></td>
            <td>NTP</td>
            <td>UDP</td>
            <td>Network Time Protocol. Crucial for forensic log correlation; abused in reflection DDoS attacks.</td>
        </tr>
        <tr>
            <td><strong>514</strong></td>
            <td>Syslog</td>
            <td>UDP</td>
            <td>System logging messages. Severity levels range from 0 (Emergency) to 7 (Debugging).</td>
        </tr>
        <tr>
            <td><strong>1812 / 1813</strong></td>
            <td>RADIUS</td>
            <td>UDP</td>
            <td>Port 1812 = Auth; Port 1813 = Acct. <strong>Encrypts ONLY password</strong>; combines auth and authorization.</td>
        </tr>
        <tr>
            <td><strong>IP Proto 50</strong></td>
            <td>IPsec ESP</td>
            <td>Layer 3</td>
            <td>Encapsulating Security Payload: provides <strong>encryption</strong>, authentication, and integrity.</td>
        </tr>
        <tr>
            <td><strong>IP Proto 51</strong></td>
            <td>IPsec AH</td>
            <td>Layer 3</td>
            <td>Authentication Header: provides authentication and integrity ONLY (<strong>NO encryption</strong>).</td>
        </tr>
    </tbody>
</table>

<h3 class="section-header">5. Switch Port Security & 802.1X Access Control (Module 19)</h3>
<div class="grid-2">
    <div class="card">
        <h4>Port Security Violation Modes</h4>
        <ul>
            <li><strong>Protect:</strong> Drops unauthorized frames. Does NOT send syslog or increment violation counter.</li>
            <li><strong>Restrict:</strong> Drops unauthorized frames. Sends a syslog message and increments violation counter.</li>
            <li><strong>Shutdown (Default):</strong> Drops frames, sends syslog, and disables port into <code class="inline">err-disable</code>.</li>
            <li><strong>Sticky MAC:</strong> Dynamically learned MAC address automatically written to <code class="inline">running-config</code>.</li>
        </ul>
    </div>
    <div class="card">
        <h4>802.1X Architecture Triad</h4>
        <ul>
            <li><strong>Supplicant:</strong> The client software on the end device requesting network access.</li>
            <li><strong>Authenticator:</strong> The intermediary switch or Wireless LAN Controller (WLC) enforcing the port block.</li>
            <li><strong>Authentication Server:</strong> The centralized database (Cisco ISE / RADIUS) verifying user identity.</li>
            <li><strong>EAP-TLS:</strong> Requires certificates on <strong>both client and server</strong>.</li>
        </ul>
    </div>
</div>

</body>
</html>
"""

def generate_pdf():
    print("Generating Chapters 11 to 19 Master Test Prep Guide PDF...")
    output_pdf = os.path.join(WORKSPACE_DIR, "Chapters_11_to_19_Master_Test_Prep_Guide.pdf")
    temp_html = os.path.join(TEMP_DIR, "temp_master_prep_guide.html")
    
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(REPORT_HTML)
        
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    user_data_dir = os.path.join(TEMP_DIR, "edge-pdf-master-prep")
    
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
    if res.returncode == 0:
        print(f"Created: {output_pdf} ({os.path.getsize(output_pdf)} bytes)")
    else:
        print(f"Error: {res.stderr}")
        
    if os.path.exists(temp_html):
        try: os.remove(temp_html)
        except: pass

if __name__ == "__main__":
    generate_pdf()
