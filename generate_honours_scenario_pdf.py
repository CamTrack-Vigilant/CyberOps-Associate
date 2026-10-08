"""
Generate Honours-Level Scenario-Based Assessment PDF (10 Marks)
Course: Cisco Certified CyberOps Associate
Module 28: Digital Forensics and Incident Analysis and Response
Students:
- Thabang Nhlokoma Buthelezi (Student ID: 230011908)
- Simphiwe Mbatha (Student ID: 230000110)
"""

import os
import subprocess

MODULE_DIR = r"C:\Users\fanele\CyberOps Associate\CyberOps-Associate\Module 28 - Digital Forensics and Incident Analysis and Response"
TEMP_DIR = os.environ.get("TEMP", r"C:\Users\fanele\AppData\Local\Temp")

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

@page {
    size: A4;
    margin: 14mm 14mm 16mm 14mm;
    @top-left {
        content: "CISCO CYBEROPS ASSOCIATE | HONOURS DEGREE PROGRAMME";
        font-family: 'Inter', sans-serif;
        font-size: 7pt;
        font-weight: 700;
        color: #0284c7;
        letter-spacing: 0.5px;
    }
    @top-right {
        content: "MODULE 28: DIGITAL FORENSICS & INCIDENT RESPONSE";
        font-family: 'Inter', sans-serif;
        font-size: 7pt;
        color: #64748b;
        font-weight: 600;
    }
    @bottom-left {
        content: "CANDIDATES: T.N. BUTHELEZI (230011908) & S. MBATHA (230000110)";
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
    line-height: 1.5;
    color: #1e293b;
    background-color: #ffffff;
}

/* Institutional Header */
.institutional-banner {
    border-bottom: 2.5px solid #0f172a;
    padding-bottom: 10px;
    margin-bottom: 12px;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
}

.title-section h1 {
    font-size: 15pt;
    font-weight: 900;
    color: #0f172a;
    margin: 0 0 2px 0;
    letter-spacing: -0.02em;
    text-transform: uppercase;
}

.title-section h2 {
    font-size: 9.5pt;
    font-weight: 700;
    color: #0284c7;
    margin: 0 0 4px 0;
}

.title-section .doc-subtitle {
    font-size: 8pt;
    color: #475569;
    font-weight: 500;
}

.meta-box {
    text-align: right;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 8px 12px;
    min-width: 260px;
}

.student-roster {
    margin-top: 4px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.5pt;
    color: #0f172a;
    line-height: 1.4;
}

.badge-tag {
    display: inline-block;
    padding: 2px 7px;
    border-radius: 4px;
    font-weight: 700;
    text-transform: uppercase;
    font-size: 6.5pt;
    letter-spacing: 0.5px;
}

.badge-blue { background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; }
.badge-green { background: #dcfce7; color: #15803d; border: 1px solid #bbf7d0; }
.badge-red { background: #fee2e2; color: #b91c1c; border: 1px solid #fecaca; }
.badge-purple { background: #f3e8ff; color: #7e22ce; border: 1px solid #e9d5ff; }
.badge-dark { background: #0f172a; color: #ffffff; }

/* Scenario Callout */
.scenario-container {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 5px solid #0284c7;
    border-radius: 6px;
    padding: 10px 14px;
    margin-bottom: 12px;
}

.scenario-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 5px;
    margin-bottom: 8px;
}

.scenario-title {
    font-size: 10pt;
    font-weight: 800;
    color: #0f172a;
    display: flex;
    align-items: center;
    gap: 8px;
}

.telemetry-grid {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 12px;
    margin-top: 8px;
}

.telemetry-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 8px 10px;
}

.telemetry-card h4 {
    margin: 0 0 5px 0;
    font-size: 8pt;
    font-weight: 700;
    color: #0f172a;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    display: flex;
    align-items: center;
    gap: 5px;
}

.code-snippet {
    background: #0f172a;
    color: #e2e8f0;
    font-family: 'JetBrains Mono', monospace;
    font-size: 6.8pt;
    padding: 6px 8px;
    border-radius: 4px;
    line-height: 1.35;
    overflow-x: hidden;
}

/* Timeline Visual */
.visual-timeline {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 8px 12px;
    margin: 10px 0 12px 0;
}

.timeline-track {
    display: flex;
    justify-content: space-between;
    position: relative;
    margin-top: 6px;
}

.timeline-track::before {
    content: '';
    position: absolute;
    top: 12px;
    left: 4%;
    right: 4%;
    height: 2px;
    background: #cbd5e1;
    z-index: 1;
}

.timeline-node {
    position: relative;
    z-index: 2;
    text-align: center;
    width: 22%;
}

.node-dot {
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: #ffffff;
    border: 3px solid #0284c7;
    margin: 4px auto 4px auto;
}

.node-dot.danger { border-color: #ef4444; background: #fee2e2; }
.node-dot.warning { border-color: #f59e0b; background: #fef3c7; }
.node-dot.success { border-color: #10b981; background: #d1fae5; }

.node-time {
    font-family: 'JetBrains Mono', monospace;
    font-size: 6.8pt;
    font-weight: 700;
    color: #0f172a;
}

.node-desc {
    font-size: 6.5pt;
    color: #475569;
    line-height: 1.2;
    margin-top: 2px;
}

/* Question Sections */
.question-card {
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    margin-bottom: 11px;
    background: #ffffff;
    overflow: hidden;
}

.question-header {
    background: #f1f5f9;
    padding: 6px 10px;
    border-bottom: 1px solid #e2e8f0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.q-title {
    font-size: 8.5pt;
    font-weight: 800;
    color: #0f172a;
    display: flex;
    align-items: center;
    gap: 6px;
}

.q-marks {
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.5pt;
    font-weight: 800;
    background: #0f172a;
    color: #ffffff;
    padding: 2px 7px;
    border-radius: 4px;
}

.question-body {
    padding: 9px 12px;
}

.question-prompt {
    font-size: 8pt;
    font-weight: 600;
    color: #1e293b;
    margin-bottom: 6px;
    line-height: 1.4;
}

.solution-box {
    background: #f8fafc;
    border-left: 3px solid #10b981;
    padding: 7px 10px;
    margin-top: 6px;
    font-size: 7.8pt;
    color: #334155;
}

.solution-box h5 {
    margin: 0 0 4px 0;
    font-size: 7.5pt;
    font-weight: 800;
    color: #047857;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.rubric-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 6.5pt;
    color: #64748b;
    background: #f1f5f9;
    padding: 1px 5px;
    border-radius: 3px;
    border: 1px solid #e2e8f0;
}

table.marking-grid {
    width: 100%;
    border-collapse: collapse;
    font-size: 7.2pt;
    margin-top: 5px;
}

table.marking-grid th {
    background: #1e293b;
    color: #ffffff;
    padding: 4px 6px;
    text-align: left;
    font-weight: 600;
}

table.marking-grid td {
    border: 1px solid #e2e8f0;
    padding: 3.5px 6px;
}

.page-break {
    page-break-before: always;
}
"""

HONOURS_HTML = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>CyberOps Module 28 Honours Scenario Assessment</title>
<style>{CSS}</style>
</head>
<body>

<!-- Institutional Header -->
<div class="institutional-banner">
    <div class="title-section">
        <h1>Honours-Level Scenario Assessment (10 Marks)</h1>
        <h2>Module 28: Digital Forensics and Incident Analysis & Response</h2>
        <div class="doc-subtitle">Cisco Certified CyberOps Associate (CBROPS 200-201) • Capstone Examination</div>
    </div>
    <div class="meta-box">
        <span class="badge-tag badge-dark">ASSESSMENT SUBMISSION</span>
        <div class="student-roster">
            <strong>Candidate 1:</strong> Thabang Nhlokoma Buthelezi<br>
            <strong>Student No:</strong> 230011908<br>
            <strong>Candidate 2:</strong> Simphiwe Mbatha<br>
            <strong>Student No:</strong> 230000110<br>
            <strong>Assessment Weight:</strong> 10 Marks Total
        </div>
    </div>
</div>

<!-- Scenario Description Container -->
<div class="scenario-container">
    <div class="scenario-header">
        <div class="scenario-title">
            <span class="badge-tag badge-red">CRITICAL INCIDENT</span>
            Operation "Phantom Beacon" – Core Banking Database Exfiltration
        </div>
        <div>
            <span class="badge-tag badge-blue">APEX FINANCIAL INFRASTRUCTURE</span>
            <span class="badge-tag badge-purple">SEVERITY: TIER 1 / HIGH</span>
        </div>
    </div>

    <p style="margin: 0 0 6px 0; font-size: 8pt; line-height: 1.45;">
        <strong>Background Scenario:</strong> On Friday at <strong>23:42 SAST</strong>, the Security Operations Center (SOC) at Apex Financial Services triggered automated high-severity alerts. An internal enterprise database server (<strong>Host: <code class="inline">CORE-DB-01</code>, IP: <code class="inline">10.140.20.15</code></strong>), which houses sensitive customer identity records and cryptographic transaction ledgers, initiated periodic outbound HTTPS connections over <strong>port 8443</strong> to an unclassified bulletproof hosting IP (<strong><code class="inline">194.26.29.112</code></strong>) in Eastern Europe.
    </p>

    <div class="telemetry-grid">
        <div class="telemetry-card">
            <h4><span class="badge-tag badge-red">IOC EVIDENCE</span> EDR & Process Injection Artifacts</h4>
            <div class="code-snippet">
[23:38:12] SYSMON EVENT ID 1 (Process Create):
Image: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
Cmd: powershell.exe -NonI -W Hidden -Enc JABjAGwAaQBlAG4AdAA...
ParentImage: C:\Windows\System32\spoolsv.exe (Print Spooler)
[23:39:44] SYSMON EVENT ID 8 (CreateRemoteThread):
SourceImage: powershell.exe (PID: 4892)
TargetImage: C:\Windows\System32\lsass.exe (PID: 672)
[23:41:05] ZEUS / SURICATA IDS ALERT:
ET MALWARE Cobalt Strike Malleable C2 HTTPS Beaconing detected
Source: 10.140.20.15:49822 -> Dest: 194.26.29.112:8443 (Interval: 45s)
            </div>
        </div>
        <div class="telemetry-card">
            <h4><span class="badge-tag badge-blue">OPERATIONAL CONTEXT</span> Physical & Human Telemetry</h4>
            <ul style="margin: 0; padding-left: 14px; font-size: 7.2pt; line-height: 1.35; color: #334155;">
                <li><strong>Physical Security Log:</strong> Server room badge reader logged access by a third-party facilities technician at 22:15 SAST.</li>
                <li><strong>USB Event Log:</strong> USB Mass Storage device (<code class="inline">VID_0781 / PID_5583</code> SanDisk 64GB) mounted at 22:20 SAST.</li>
                <li><strong>Junior Admin Proposal:</strong> The on-duty junior sysadmin panicked upon seeing outbound traffic and grabbed the server's dual AC power cords to "pull the plug immediately".</li>
                <li><strong>Database State:</strong> Oracle Database is actively processing over 1,200 international financial settlement threads.</li>
            </ul>
        </div>
    </div>
</div>

<!-- Visual Timeline -->
<div class="visual-timeline">
    <div style="font-size: 7.5pt; font-weight: 800; color: #0f172a; text-transform: uppercase; letter-spacing: 0.5px;">
        Incident Chronology & Investigation Timeline (SAST)
    </div>
    <div class="timeline-track">
        <div class="timeline-node">
            <div class="node-time">22:15 SAST</div>
            <div class="node-dot warning"></div>
            <div class="node-desc">Physical server room badge entry; rogue USB inserted at 22:20.</div>
        </div>
        <div class="timeline-node">
            <div class="node-time">23:38 SAST</div>
            <div class="node-dot danger"></div>
            <div class="node-desc">Print Spooler exploit spawns hidden encoded PowerShell.</div>
        </div>
        <div class="timeline-node">
            <div class="node-time">23:39 SAST</div>
            <div class="node-dot danger"></div>
            <div class="node-desc">Memory injection into <code class="inline">lsass.exe</code>; credential dump & C2 beacon.</div>
        </div>
        <div class="timeline-node">
            <div class="node-time">23:42 SAST</div>
            <div class="node-dot success"></div>
            <div class="node-desc">Suricata IDS & SIEM alert; SOC Tier 2 intervention required.</div>
        </div>
    </div>
</div>

<!-- Question 1 -->
<div class="question-card">
    <div class="question-header">
        <div class="q-title">
            <span class="badge-tag badge-dark">QUESTION 1</span>
            Order of Volatility (RFC 3227) & Live vs. Dead Forensic Acquisition
        </div>
        <div class="q-marks">3.0 MARKS</div>
    </div>
    <div class="question-body">
        <div class="question-prompt">
            Critique the junior administrator's decision to immediately pull the physical power cords from <code class="inline">CORE-DB-01</code>. With strict reference to the <strong>RFC 3227 Order of Volatility</strong>:
            <ol style="margin: 3px 0 0 0; padding-left: 16px;">
                <li>Identify <strong>three specific volatile forensic artifacts</strong> that would be permanently destroyed by this action and explain their direct diagnostic value to the investigation. (1.5 Marks)</li>
                <li>Formulate the precise, scientifically sound technical procedure the SOC team must execute to isolate the host without terminating power or corrupting ongoing forensic extraction. (1.5 Marks)</li>
            </ol>
        </div>

        <div class="solution-box">
            <h5>Marking Guide & Honours-Level Model Solution</h5>
            <p><strong>1. Destruction of Volatile Artifacts (1.5 Marks - 0.5 per artifact):</strong></p>
            <ul>
                <li><strong>Physical RAM (Priority 2):</strong> Contains the unencrypted Cobalt Strike payload, decrypted symmetric session keys (AES/TLS), and plaintext passwords harvested from <code class="inline">lsass.exe</code>. Pulling power wipes RAM instantly.</li>
                <li><strong>Active Network Sockets & ARP/Routing Tables (Priority 2):</strong> Ephemeral socket connections (<code class="inline">ESTABLISHED</code> states to <code class="inline">194.26.29.112:8443</code>) proving actual data exfiltration endpoints and internal lateral scanning targets.</li>
                <li><strong>Running Process Tree & Injected Threads (Priority 2):</strong> The parent-child lineage (<code class="inline">spoolsv.exe</code> $\rightarrow$ <code class="inline">powershell.exe</code> $\rightarrow$ <code class="inline">lsass.exe</code>) residing in memory registers/tables, without which process-injection cannot be legally proven.</li>
            </ul>
            <p><strong>2. Proper Isolation & Live Acquisition Procedure (1.5 Marks):</strong></p>
            <ul>
                <li><strong>Network Isolation via EDR / Switch Port ACL:</strong> Isolate the host at Layer 2/3 (or EDR software quarantine) to sever C2 communications while keeping operating system power on.</li>
                <li><strong>Live Volatile Memory Capture First:</strong> Connect sterile write-blocked media or run an out-of-band RAM acquisition agent (e.g., WinPmem, DumpIt, FTK Imager CLI) to dump physical RAM to an external sanitized forensic destination.</li>
            </ul>
        </div>
    </div>
</div>

<div class="page-break"></div>

<!-- Page 2 Header -->
<div class="institutional-banner">
    <div class="title-section">
        <h1>Honours-Level Scenario Assessment (Continued)</h1>
        <h2>Module 28: Digital Forensics and Incident Analysis & Response</h2>
        <div class="doc-subtitle">Mark Breakdown: Part B (2.0 Marks), Part C (3.0 Marks), Part D (2.0 Marks) • Total: 10 Marks</div>
    </div>
    <div class="meta-box">
        <div class="student-roster">
            <strong>Group Candidates:</strong><br>
            T.N. Buthelezi (230011908) & S. Mbatha (230000110)
        </div>
    </div>
</div>

<!-- Question 2 -->
<div class="question-card">
    <div class="question-header">
        <div class="q-title">
            <span class="badge-tag badge-dark">QUESTION 2</span>
            Evidence Integrity, Chain of Custody & Judicial Admissibility
        </div>
        <div class="q-marks">2.0 MARKS</div>
    </div>
    <div class="question-body">
        <div class="question-prompt">
            During the investigation, a junior analyst performed a regular file copy (logical copy) of the Oracle database folder to a USB drive, left the drive on an open desk over the weekend, and computed its SHA-256 hash on Monday morning before handing it to legal counsel.
            <ul style="margin: 3px 0 0 0; padding-left: 16px;">
                <li>Evaluate whether this digital evidence complies with the <strong>Best Evidence Rule</strong> and whether it is admissible in a court of law. (1.0 Mark)</li>
                <li>Identify two critical breaches of the <strong>Chain of Custody</strong> and explain how a defense attorney would exploit these procedural flaws to suppress the evidence. (1.0 Mark)</li>
            </ul>
        </div>

        <div class="solution-box">
            <h5>Marking Guide & Honours-Level Model Solution</h5>
            <ul>
                <li><strong>Violation of Best Evidence Rule (1.0 Mark):</strong> The evidence is <strong>inadmissible</strong>. A logical file copy copies only indexed active files, altering the file system's Last Accessed ($MACB$) metadata timestamps. Under the Best Evidence Rule, the court requires the original physical drive or an exact, verified <strong>bit-stream forensic clone</strong> (e.g., `.E01` or `.dd` raw image) containing unallocated space, file slack, and master tables captured via a hardware write-blocker.</li>
                <li><strong>Chain of Custody Breaches (1.0 Mark):</strong> 
                    1) <em>Failure of Secure Physical Control:</em> Leaving the evidence unattended on an open desk over the weekend creates an unmonitored temporal gap where unauthorized tampering, malware contamination, or hardware swap cannot be refuted.
                    2) <em>Belated Hash Computation:</em> Generating the cryptographic hash 48 hours later rather than at the exact second of collection invalidates integrity verification. Opposing counsel can file a motion in limine to suppress the evidence due to lack of tamper-evidence.
                </li>
            </ul>
        </div>
    </div>
</div>

<!-- Question 3 -->
<div class="question-card">
    <div class="question-header">
        <div class="q-title">
            <span class="badge-tag badge-dark">QUESTION 3</span>
            NIST SP 800-61 Rev 2 Containment Strategy & Operational Trade-offs
        </div>
        <div class="q-marks">3.0 MARKS</div>
    </div>
    <div class="question-body">
        <div class="question-prompt">
            In <strong>Phase 3 (Containment, Eradication & Recovery)</strong> of the NIST SP 800-61 Rev 2 lifecycle:
            <ol style="margin: 3px 0 0 0; padding-left: 16px;">
                <li>Distinguish between <strong>Short-Term Containment</strong> and <strong>Long-Term Containment</strong> actions required for this banking database intrusion. (1.5 Marks)</li>
                <li>The Chief Operating Officer (COO) demands that the database remain online due to $50 million in pending transactions, while the Lead Security Analyst insists on immediate network isolation. Propose a balanced technical containment strategy that mitigates data exfiltration while satisfying institutional risk requirements. (1.5 Marks)</li>
            </ol>
        </div>

        <div class="solution-box">
            <h5>Marking Guide & Honours-Level Model Solution</h5>
            <ul>
                <li><strong>Short-Term vs. Long-Term Actions (1.5 Marks):</strong>
                    <ul>
                        <li><em>Short-Term:</em> Immediate egress filtering at the perimeter firewall dropping all traffic to destination IP <code class="inline">194.26.29.112</code>; revoking compromised Service Account credentials; suspending Print Spooler service on domain controllers.</li>
                        <li><em>Long-Term:</em> Full enterprise domain password reset for administrative accounts; applying zero-day patches for print spooler vulnerabilities; deploying strict internal micro-segmentation VLANs restricting database access solely to trusted app servers.</li>
                    </ul>
                </li>
                <li><strong>Balanced Operational Containment Strategy (1.5 Marks):</strong>
                    Implement <strong>Targeted Egress Blackholing and Lateral Micro-Segmentation</strong>. Rather than severing all network interfaces (which causes complete operational failure), defenders:
                    1) Null-route the specific external C2 IP/domain at the border firewall and border BGP/proxy level, stopping data exfiltration instantly.
                    2) Apply host-level firewall rules permitting only incoming SQL queries on port 1521 from the pre-authenticated Application Servers (<code class="inline">10.140.10.0/24</code>), while strictly denying all outbound connections and SMB/RPC lateral ports. This permits critical transaction processing while completely quarantining the threat actor.
                </li>
            </ul>
        </div>
    </div>
</div>

<!-- Question 4 -->
<div class="question-card">
    <div class="question-header">
        <div class="q-title">
            <span class="badge-tag badge-dark">QUESTION 4</span>
            Incident Classification (VERIS Model) & Post-Incident Continuous Improvement
        </div>
        <div class="q-marks">2.0 MARKS</div>
    </div>
    <div class="question-body">
        <div class="question-prompt">
            Apply the <strong>VERIS (Vocabulary for Event Recording and Incident Sharing) 4A Model</strong> to categorize this incident, and formulate two non-punitive, institutional remediation policies to be mandated during the 14-day <strong>Post-Incident Lessons Learned</strong> meeting. (2.0 Marks)
        </div>

        <div class="solution-box">
            <h5>Marking Guide & Honours-Level Model Solution</h5>
            <ul>
                <li><strong>VERIS 4A Categorization (1.0 Mark - 0.25 each):</strong>
                    <table class="marking-grid">
                        <tr>
                            <th style="width: 20%;">VERIS Dimension</th>
                            <th style="width: 40%;">Incident Mapping</th>
                            <th style="width: 40%;">Justification</th>
                        </tr>
                        <tr>
                            <td><strong>1. Actors</strong></td>
                            <td>External (State-Sponsored APT) + Physical Partner</td>
                            <td>External adversary leveraging physical supply chain / technician access.</td>
                        </tr>
                        <tr>
                            <td><strong>2. Actions</strong></td>
                            <td>Physical (USB) + Malware + Hacking</td>
                            <td>Unauthorized media insertion, memory injection, and C2 command execution.</td>
                        </tr>
                        <tr>
                            <td><strong>3. Assets</strong></td>
                            <td>Server (Database: <code class="inline">CORE-DB-01</code>)</td>
                            <td>Core banking database hosting critical transactional ledgers.</td>
                        </tr>
                        <tr>
                            <td><strong>4. Attributes</strong></td>
                            <td>Confidentiality (Loss) & Integrity (Altered)</td>
                            <td>Credential theft from <code class="inline">lsass.exe</code> and unauthorized exfiltration attempt.</td>
                        </tr>
                    </table>
                </li>
                <li><strong>Institutional Remediation Policies (1.0 Mark):</strong>
                    1) <em>Hardware Peripheral Lockdown (USB Device Control):</em> Enforce Group Policy / EDR agent rules globally blocking unauthorized USB mass storage devices across all Tier 1/2 infrastructure.
                    2) <em>Two-Person Integrity Rule for Data Center Physical Access:</em> Mandate dual-custody physical escort and continuous CCTV monitoring for all external maintenance personnel inside core server rooms.
                </li>
            </ul>
        </div>
    </div>
</div>

<!-- Summary Evaluation Matrix -->
<table class="marking-grid" style="margin-top: 8px;">
    <thead>
        <tr>
            <th>Assessment Component</th>
            <th>Cisco CyberOps Syllabus Link</th>
            <th>NIST / Legal Standard</th>
            <th>Weight</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Question 1: Volatility & Memory Acquisition</td>
            <td>Section 28.1 (Evidence Handling)</td>
            <td>RFC 3227 Volatility Hierarchy</td>
            <td><strong>3.0 Marks</strong></td>
        </tr>
        <tr>
            <td>Question 2: Chain of Custody & Integrity</td>
            <td>Section 28.1 (Evidence Integrity)</td>
            <td>Best Evidence Rule / Federal Rule 901</td>
            <td><strong>2.0 Marks</strong></td>
        </tr>
        <tr>
            <td>Question 3: Incident Containment Strategy</td>
            <td>Section 28.2 (Incident Handling Lifecycle)</td>
            <td>NIST SP 800-61 Rev 2 Phase 3</td>
            <td><strong>3.0 Marks</strong></td>
        </tr>
        <tr>
            <td>Question 4: VERIS & Lessons Learned</td>
            <td>Section 28.3 (Incident Reporting Models)</td>
            <td>VERIS 4A Framework / Post-Mortem</td>
            <td><strong>2.0 Marks</strong></td>
        </tr>
        <tr style="background: #f1f5f9; font-weight: bold;">
            <td colspan="3" style="text-align: right;">TOTAL ASSESSMENT ALLOCATION:</td>
            <td><strong>10.0 MARKS</strong></td>
        </tr>
    </tbody>
</table>

</body>
</html>
"""

def generate_pdf():
    print("Generating Honours Scenario Assessment PDF (10 Marks)...")
    output_pdf = os.path.join(MODULE_DIR, "Module-28-Honours-Scenario-Assessment-10Marks.pdf")
    temp_html = os.path.join(TEMP_DIR, "temp_mod28_honours_assessment.html")
    
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(HONOURS_HTML)
        
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    user_data_dir = os.path.join(TEMP_DIR, "edge-pdf-honours")
    
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
