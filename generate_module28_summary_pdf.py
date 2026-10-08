"""
Generate Module 28 Comprehensive Study Guide & Lab 28.4.1 Solution PDF
Course: Cisco CyberOps Associate
Module 28: Digital Forensics and Incident Analysis and Response
"""

import os
import subprocess

MODULE_DIR = r"C:\Users\fanele\CyberOps Associate\CyberOps-Associate\Module 28 - Digital Forensics and Incident Analysis and Response"
LABS_DIR = os.path.join(MODULE_DIR, "Labs")
TEMP_DIR = os.environ.get("TEMP", r"C:\Users\fanele\AppData\Local\Temp")

os.makedirs(LABS_DIR, exist_ok=True)

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
        content: "Module 28: Digital Forensics & Incident Response | Executive Brief";
        font-family: 'Inter', sans-serif;
        font-size: 7.5pt;
        color: #64748b;
        font-weight: 500;
    }
    @bottom-left {
        content: "NIST SP 800-61 REV 2 & RFC 3227 ORDER OF VOLATILITY SPECIFICATION";
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
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    font-size: 9pt;
    line-height: 1.55;
    color: #1e293b;
    background-color: #ffffff;
}

.header-container {
    border-bottom: 2.5px solid #0284c7;
    padding-bottom: 12px;
    margin-bottom: 18px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
}

.title-area h1 {
    font-size: 17pt;
    font-weight: 800;
    color: #0f172a;
    margin: 0 0 4px 0;
    letter-spacing: -0.02em;
}

.title-area h2 {
    font-size: 10.5pt;
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
    padding: 3px 8px;
    border-radius: 4px;
    font-weight: 700;
    text-transform: uppercase;
    font-size: 6.5pt;
    margin-bottom: 4px;
}

.badge-blue { background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; }
.badge-green { background: #dcfce7; color: #15803d; border: 1px solid #bbf7d0; }
.badge-red { background: #fee2e2; color: #b91c1c; border: 1px solid #fecaca; }
.badge-purple { background: #f3e8ff; color: #7e22ce; border: 1px solid #e9d5ff; }

h3.section-header {
    font-size: 11pt;
    font-weight: 700;
    color: #0f172a;
    border-left: 4px solid #0284c7;
    padding-left: 8px;
    margin: 16px 0 10px 0;
    text-transform: uppercase;
    letter-spacing: 0.03em;
}

.grid-2 {
    display: flex;
    gap: 12px;
    margin-bottom: 12px;
}

.grid-2 > div {
    flex: 1;
}

.card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 10px 12px;
    margin-bottom: 10px;
}

.card h4 {
    margin: 0 0 6px 0;
    font-size: 9.5pt;
    font-weight: 700;
    color: #0f172a;
    display: flex;
    align-items: center;
    gap: 6px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0 14px 0;
    font-size: 8pt;
}

th {
    background-color: #0f172a;
    color: #ffffff;
    font-weight: 600;
    text-align: left;
    padding: 6px 8px;
    border: 1px solid #0f172a;
}

td {
    padding: 5.5px 8px;
    border: 1px solid #e2e8f0;
    vertical-align: top;
}

tr:nth-child(even) td {
    background-color: #f8fafc;
}

.code-block {
    background: #0f172a;
    color: #f8fafc;
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.5pt;
    padding: 8px 10px;
    border-radius: 5px;
    margin: 8px 0;
    line-height: 1.45;
}

.alert-box {
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    border-left: 4px solid #2563eb;
    padding: 8px 12px;
    border-radius: 4px;
    margin: 10px 0;
    font-size: 8.5pt;
}

ul, ol {
    margin: 4px 0 8px 0;
    padding-left: 18px;
}

li {
    margin-bottom: 3px;
}

.page-break {
    page-break-before: always;
}
"""

REPORT_HTML = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Module 28: Digital Forensics & Incident Response</title>
<style>{CSS}</style>
</head>
<body>

<div class="header-container">
    <div class="title-area">
        <h1>Module 28: Digital Forensics & Incident Analysis</h1>
        <h2>Cisco Certified CyberOps Associate (CBROPS 200-201)</h2>
    </div>
    <div class="badge-box">
        <span class="badge-tag badge-blue">CAPSTONE CERTIFICATION MODULE</span><br>
        Curriculum Reference: NetAcad Module 28<br>
        Standards: NIST SP 800-61 Rev 2 | RFC 3227
    </div>
</div>

<h3 class="section-header">1. Digital Forensics Principles & Evidence Handling</h3>

<div class="grid-2">
    <div class="card">
        <h4><span class="badge-tag badge-blue">CORE DEFINITION</span> Forensic Science in CyberOps</h4>
        <p><strong>Digital Forensics</strong> is the scientific identification, collection, examination, and analysis of digital evidence while preserving data integrity and maintaining an unbroken chain of custody for legal and operational purposes.</p>
        <ul>
            <li><strong>The Golden Rule:</strong> Never perform forensic examination on original physical evidence. Always clone a bit-stream duplicate and work solely on the forensic image.</li>
            <li><strong>Hardware Write-Blockers:</strong> Physical bridges that permit read commands while suppressing write signals to prevent forensic contamination.</li>
        </ul>
    </div>
    <div class="card">
        <h4><span class="badge-tag badge-green">VERIFICATION</span> Cryptographic Hashing</h4>
        <p>Evidence integrity is mathematically proven using cryptographic hashes (<strong>SHA-256</strong>). If the target forensic image hash matches the suspect physical drive, evidence is validated.</p>
        <div class="code-block">
# PowerShell Evidence Verification Syntax:
Get-FileHash -Path suspect_drive.dd -Algorithm SHA256
Hash: A5B78F49E3C29D120B44F8E... [MATCH = VALID]
        </div>
        <p style="font-size: 7.5pt; color: #64748b;">The <em>Avalanche Effect</em> guarantees that altering even a single bit completely changes the hash, proving tampering instantly.</p>
    </div>
</div>

<h3 class="section-header">2. Order of Volatility (RFC 3227) & Evidence Hierarchy</h3>
<p>When responding to an active security incident, evidence must be collected in order from <strong>most volatile</strong> (disappears immediately upon power loss) to <strong>least volatile</strong>:</p>

<table>
    <thead>
        <tr>
            <th style="width: 10%;">Priority</th>
            <th style="width: 30%;">Evidence Source</th>
            <th style="width: 25%;">Volatility Lifespan</th>
            <th style="width: 35%;">Forensic Value / Artifacts</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>1 (Highest)</strong></td>
            <td>CPU Registers, On-chip Cache</td>
            <td>Nanoseconds to Microseconds</td>
            <td>Immediate processor state, decrypted CPU instruction buffers.</td>
        </tr>
        <tr>
            <td><strong>2</strong></td>
            <td>Routing Table, ARP Cache, Process Table, RAM</td>
            <td>Seconds to Hours (Lost at reboot)</td>
            <td><strong>Physical RAM:</strong> Injected fileless malware, active TCP/UDP sockets, decrypted passwords, cryptographic keys.</td>
        </tr>
        <tr>
            <td><strong>3</strong></td>
            <td>Temporary File Systems, Swap Space</td>
            <td>Hours to Days</td>
            <td>Virtual memory paging files, temporary execution dumps.</td>
        </tr>
        <tr>
            <td><strong>4</strong></td>
            <td>Local Disk Storage (NVMe, SSD, HDD)</td>
            <td>Months to Years</td>
            <td>Master File Table ($MFT$), deleted file clusters, file slack, registry hives.</td>
        </tr>
        <tr>
            <td><strong>5</strong></td>
            <td>Remote Logging & Monitoring Data</td>
            <td>Weeks to Months (Retention-based)</td>
            <td>Syslog, SIEM correlation alerts, NetFlow / IPFIX traffic flow records.</td>
        </tr>
        <tr>
            <td><strong>6 (Lowest)</strong></td>
            <td>Archival Backups, Tapes, Optical Media</td>
            <td>Years to Decades</td>
            <td>Cold storage backups, disaster recovery tape archives.</td>
        </tr>
    </tbody>
</table>

<div class="alert-box">
    <strong>CRITICAL SOC OPERATIONAL RULE:</strong> <em>Never immediately pull the power plug or reboot a live compromised system!</em> Rebooting destroys CPU registers, cache, ARP tables, and RAM (Priority 1 & 2), destroying the only proof of fileless malware execution and C2 network sockets. Always perform a <strong>live volatile memory capture</strong> (WinPmem, FTK Imager CLI, LiME) before power down.
</div>

<div class="page-break"></div>

<div class="header-container">
    <div class="title-area">
        <h1>NIST SP 800-61 Rev 2 Incident Handling Lifecycle</h1>
        <h2>Standardized Incident Response Framework & Operating Procedure</h2>
    </div>
    <div class="badge-box">
        <span class="badge-tag badge-purple">NIST SPECIAL PUBLICATION</span><br>
        Computer Security Incident Handling Guide<br>
        Version: SP 800-61 Revision 2
    </div>
</div>

<h3 class="section-header">3. The 4 Phases of the Incident Response Lifecycle</h3>

<div class="grid-2">
    <div class="card">
        <h4><span class="badge-tag badge-blue">PHASE 1</span> Preparation</h4>
        <p>Establishing defense capabilities <em>before</em> an attack occurs:</p>
        <ul>
            <li>Creating pre-approved <strong>Incident Response Playbooks</strong> for ransomware, phishing, and DDoS.</li>
            <li>Preparing forensic hardware jump kits, sterile storage media, and write-blockers.</li>
            <li>Establishing <strong>out-of-band communication channels</strong> (signal groups, satellite phones) in case corporate email is compromised.</li>
            <li>Conducting regular Tabletop Exercises (TTX) and war games.</li>
        </ul>
    </div>
    <div class="card">
        <h4><span class="badge-tag badge-red">PHASE 2</span> Detection and Analysis</h4>
        <p>Identifying and prioritizing active security threats:</p>
        <ul>
            <li><strong>Precursors:</strong> Signs of future attacks (e.g., port scans, dark web reconnaissance chatter).</li>
            <li><strong>Indicators of Compromise (IoCs):</strong> Signs that an attack is occurring or has succeeded (e.g., AV alerts, C2 beacons, unauthorized admin accounts).</li>
            <li>Scoping incident severity based on <strong>functional impact</strong>, <strong>data sensitivity</strong>, and <strong>recoverability</strong>.</li>
        </ul>
    </div>
</div>

<div class="grid-2">
    <div class="card">
        <h4><span class="badge-tag badge-green">PHASE 3</span> Containment, Eradication & Recovery</h4>
        <p>Neutralizing the adversary and restoring operations safely:</p>
        <ul>
            <li><strong>Short-Term Containment:</strong> Isolating the infected host via network quarantine or VLAN change to stop lateral movement while preserving volatile memory.</li>
            <li><strong>Long-Term Containment:</strong> Applying temporary firewall filters, rotating domain admin credentials, and rerouting traffic through WAF proxies.</li>
            <li><strong>Eradication:</strong> Purging malware binaries, persistence registry keys, and remediating the root-cause vulnerability.</li>
            <li><strong>Recovery:</strong> Restoring from verified clean offline backups with <strong>enhanced monitoring</strong> for 30+ days.</li>
        </ul>
    </div>
    <div class="card">
        <h4><span class="badge-tag badge-purple">PHASE 4</span> Post-Incident Activity</h4>
        <p>Driving continuous defense improvement:</p>
        <ul>
            <li>Convening a <strong>Blameless Lessons Learned Meeting</strong> within <strong>14 days</strong> of ticket closure while recollection is clear.</li>
            <li>Answering: <em>What happened? Did playbooks work? What precursors were missed? How do we prevent recurrence?</em></li>
            <li>Generating formal executive incident post-mortems and archiving legal evidence according to retention policies (3–7 years).</li>
        </ul>
    </div>
</div>

<h3 class="section-header">4. Evidence Admissibility & Legal Classifications</h3>
<table>
    <thead>
        <tr>
            <th style="width: 25%;">Evidence Class</th>
            <th style="width: 40%;">Legal Standard / Meaning</th>
            <th style="width: 35%;">SOC / CyberOps Real Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Best Evidence (Original)</strong></td>
            <td>The original physical medium or an exact, verified bit-stream duplicate.</td>
            <td>The physical suspect NVMe drive or its bit-by-bit verified `.E01` raw image.</td>
        </tr>
        <tr>
            <td><strong>Direct Evidence</strong></td>
            <td>Directly proves a fact without requiring any presumption or inference.</td>
            <td>Security camera footage showing a rogue contractor typing on the console.</td>
        </tr>
        <tr>
            <td><strong>Circumstantial Evidence</strong></td>
            <td>Proves a fact through correlation and reasonable inference.</td>
            <td>A server login log from an overseas IP coinciding with badge gate entry.</td>
        </tr>
        <tr>
            <td><strong>Corroborating Evidence</strong></td>
            <td>Supplementary evidence that reinforces or validates primary evidence.</td>
            <td>A Snort IDS alert backed up by a firewall drop log and process creation event.</td>
        </tr>
    </tbody>
</table>

<h3 class="section-header">5. Global Coordination & The VERIS Framework</h3>
<ul>
    <li><strong>CSIRT Team Models:</strong> Centralized (single global SOC), Distributed (regional response teams), Coordinating (advisory role, e.g., US-CERT / CISA).</li>
    <li><strong>Threat Communities:</strong> FIRST (Forum of Incident Response and Security Teams), Sector ISACs (Financial, Healthcare).</li>
    <li><strong>VERIS (Vocabulary for Event Recording and Incident Sharing):</strong> The <strong>4A Model</strong> used in the Verizon DBIR:
        <strong>Actors</strong> (Who?), <strong>Actions</strong> (What did they do?), <strong>Assets</strong> (What was hit?), and <strong>Attributes</strong> (Which CIA pillar was violated?).</li>
</ul>

</body>
</html>
"""

def generate_pdf():
    print("Generating Module 28 Executive Study Guide PDF...")
    output_pdf = os.path.join(MODULE_DIR, "Module-28-Comprehensive-Study-Guide.pdf")
    temp_html = os.path.join(TEMP_DIR, "temp_mod28_study_guide.html")
    
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(REPORT_HTML)
        
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    user_data_dir = os.path.join(TEMP_DIR, "edge-pdf-mod28")
    
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
        print(f"Successfully generated: {output_pdf} ({os.path.getsize(output_pdf)} bytes)")
    else:
        print(f"Error generating PDF: {res.stderr}")
        
    if os.path.exists(temp_html):
        try: os.remove(temp_html)
        except: pass

if __name__ == "__main__":
    generate_pdf()
