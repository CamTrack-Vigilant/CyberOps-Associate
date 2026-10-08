"""
Generate Lab 14.2.8 Solution PDF:
Module 14 - Common Threats and Attacks
Lab 14.2.8: Lab - Social Engineering
"""

import os
import subprocess

LABS_DIR = r"C:\Users\fanele\CyberOps Associate\CyberOps-Associate\Module 14 - Common Threats and Attacks\Labs"
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
        content: "Module 14: Common Threats and Attacks | Lab Solution";
        font-family: 'Inter', sans-serif;
        font-size: 7.5pt;
        color: #64748b;
        font-weight: 500;
    }
    @bottom-left {
        content: "SOCIAL ENGINEERING THREAT ANALYSIS & DEFENSE GUIDE";
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
.qa-card.warning .question-title { color: #b45309; }

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

code.inline {
    background-color: #f1f5f9;
    color: #0f172a;
    padding: 1px 4px;
    border-radius: 3px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 8pt;
    border: 1px solid #e2e8f0;
}
"""

LAB_14_2_8_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Lab 14.2.8 - Social Engineering Solution</title>
<style>
{CSS}
</style>
</head>
<body>

<div class="doc-header">
    <div class="badge">Cisco Certified CyberOps Associate (CBROPS 200-201)</div>
    <h1>Lab 14.2.8: Social Engineering</h1>
    <div class="subtitle">Threat Vector Taxonomy, Psychological Manipulation Vectors, OSINT Risks, and Enterprise Defense Frameworks</div>
</div>

<div class="meta-grid">
    <div class="meta-item">
        <div class="meta-label">Course Module</div>
        <div class="meta-value">Module 14: Common Threats and Attacks</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Core Focus</div>
        <div class="meta-value">Human-Centric Cyber Threats</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Primary Reference</div>
        <div class="meta-value">SANS Institute Research Library</div>
    </div>
    <div class="meta-item">
        <div class="meta-label">Target Audience</div>
        <div class="meta-value">SOC Analysts & Security Teams</div>
    </div>
</div>

<h2>Objectives</h2>
<ul>
    <li><strong>Research and Identify Social Engineering Attack Vectors</strong> &mdash; Examine the taxonomy of human-based, computer-based, and mobile/hybrid attack methods.</li>
    <li><strong>Analyze Psychological Exploitation Techniques</strong> &mdash; Understand how attackers leverage trust, urgency, fear, authority, and social proof to bypass security boundaries.</li>
    <li><strong>Evaluate Social Media OSINT Risks</strong> &mdash; Dissect how open-source reconnaissance fuels spear phishing, whaling, and Business Email Compromise (BEC).</li>
    <li><strong>Formulate Enterprise Defensive Controls</strong> &mdash; Construct a defense-in-depth framework incorporating security awareness training (SAT), phishing-resistant MFA, clean desk policies, and technical controls.</li>
    <li><strong>Examine SANS Institute Governance</strong> &mdash; Understand the institutional role of SANS in global cybersecurity training, threat telemetry (ISC), and research standards.</li>
</ul>

<h2>Background / Scenario</h2>
<p>
Social engineering is the art of manipulating individuals into performing actions or divulging confidential information. Unlike purely technical exploits that target software bugs or misconfigurations, social engineering exploits the "human element" &mdash; exploiting cognitive biases, institutional trust, helpfulness, or fear of negative consequences.
</p>
<p>
Whether executed via phishing emails, impersonation phone calls (vishing), physical tailgating, or weaponized social media profiles, social engineering remains the primary initial access vector for modern cybercrime syndicates and Advanced Persistent Threats (APTs).
</p>

<h2>Lab Questions & Comprehensive Analytical Solutions</h2>

<div class="qa-card">
    <div class="question-title">Question A &mdash; Social Engineering Attack Methodologies</div>
    <div class="question-text">What are the three methods used in social engineering to gain access to information?</div>
    <div class="answer-box">
        <div class="answer-label">Official SANS / CyberOps Solution:</div>
        <p>Based on the SANS Institute research framework, social engineering attacks are classified into three primary operational methods:</p>
        <ol>
            <li>
                <strong>Human-Based (In-Person / Direct Interpersonal Interaction):</strong>
                <br>Involves direct person-to-person engagement where the adversary physically interacts or speaks directly with the victim. The attacker exploits interpersonal trust, polite compliance, or perceived administrative authority to obtain physical access, credentials, or confidential documents.
            </li>
            <li>
                <strong>Computer-Based (Technology-Driven / Digital Interaction):</strong>
                <br>Utilizes computers, software applications, websites, emails, or internet services to deceive users. The attacker creates fraudulent digital interfaces, spoofed domains, or weaponized files to trick victims into entering passwords, installing malware, or authorizing fraudulent transactions.
            </li>
            <li>
                <strong>Mobile-Based / Multi-Channel (Telecommunication & Hybrid):</strong>
                <br>Leverages mobile devices, telecommunications networks, SMS text messaging, voice communication (VoIP), mobile applications, or QR codes to manipulate targets remotely while on mobile platforms.
            </li>
        </ol>
    </div>
</div>

<div class="qa-card">
    <div class="question-title">Question B &mdash; Attack Examples by Classification Category</div>
    <div class="question-text">What are three examples of social engineering attacks from the first two methods in step 2a?</div>
    <div class="answer-box">
        <div class="answer-label">Detailed Attack Examples & Mechanics:</div>

        <p><strong style="color: #0369a1;">1. Human-Based Social Engineering Examples:</strong></p>
        <ul>
            <li><strong>Pretexting & Impersonation:</strong> The attacker invents a fabricated scenario (pretext), posing as a trusted authority figure &mdash; such as an internal IT support technician, high-ranking corporate executive, building maintenance engineer, or external auditor &mdash; to coerce the victim into revealing access credentials or executing an urgent override.</li>
            <li><strong>Tailgating / Piggybacking:</strong> The adversary physically breaches a restricted facility by closely following an authorized employee through secure access doors, turnstiles, or mantraps, often relying on social courtesy (e.g., holding heavy boxes or pretending to have misplaced a badge).</li>
            <li><strong>Shoulder Surfing & Dumpster Diving:</strong> Directly viewing confidential information over a user's shoulder (PINs, passwords, encryption keys) or searching organizational waste receptacles for disposed hard-copy documents, password cheat sheets, network diagrams, and employee directories.</li>
        </ul>

        <p><strong style="color: #0369a1;">2. Computer-Based Social Engineering Examples:</strong></p>
        <ul>
            <li><strong>Phishing (Spear Phishing & Whaling):</strong> Deceptive, mass or highly targeted emails crafted to impersonate reputable organizations (banks, internal HR, Microsoft 365, cloud providers). These messages contain malicious links directing victims to credential-harvesting portals or weaponized attachments (macro-enabled Office files, ISO images).</li>
            <li><strong>Watering Hole Attack:</strong> Adversaries identify and compromise legitimate, third-party public websites frequently visited by employees of a targeted enterprise, injecting zero-day exploits or drive-by download scripts to silently compromise visiting company endpoints.</li>
            <li><strong>Rogue Pop-ups & Scareware:</strong> Browser-based pop-ups displaying alarming fake security warnings (e.g., <em>"Your Computer is Infected with 17 Viruses!"</em>) prompting the user to download a fake utility or call a bogus technical support hotline.</li>
        </ul>
    </div>
</div>

<div class="qa-card warning">
    <div class="question-title">Question C &mdash; Social Networking & OSINT Threat Analysis</div>
    <div class="question-text">Why is social networking a social engineering threat?</div>
    <div class="answer-box">
        <div class="answer-label">SOC Threat Intelligence Analysis:</div>
        <p>Social networking platforms (LinkedIn, Facebook, X/Twitter, Instagram, GitHub) present severe security threats due to four key factors:</p>
        <ol>
            <li>
                <strong>Mass Over-Sharing of Open-Source Intelligence (OSINT):</strong>
                <br>Employees routinely publish detailed job titles, project assignments, technology stacks used by their employers, organizational hierarchies, corporate email formats, colleague relationships, and personal details (birth dates, pets, alma maters &mdash; often used as password reset challenge answers).
            </li>
            <li>
                <strong>Enabler of Precision Spear Phishing & Business Email Compromise (BEC):</strong>
                <br>Threat actors harvest publicly shared travel itineraries or executive transitions to execute high-impact pretexting. For example, knowing a CEO is currently on a flight to a conference enables an attacker to send an urgent spoofed email to accounting requesting an emergency wire transfer.
            </li>
            <li>
                <strong>Implicit Trust & Lowered Vigilance:</strong>
                <br>Users naturally perceive social media messages and connection requests as informal and low-risk compared to direct corporate email. Attackers create convincing fake profiles (e.g., posing as industry recruiters or vendors) to deliver malicious links and malware through Direct Messages (DMs).
            </li>
            <li>
                <strong>Targeted Organization Reconnaissance:</strong>
                <br>Adversaries map entire corporate infrastructure layouts, identifying key IT administrators, HR managers, and finance personnel to construct targeted spear phishing campaigns.
            </li>
        </ol>
    </div>
</div>

<div class="qa-card security">
    <div class="question-title">Question D &mdash; Enterprise Defense-in-Depth Strategy</div>
    <div class="question-text">How can an organization defend itself from social engineering attacks?</div>
    <div class="answer-box">
        <div class="answer-label">Multi-Layered SOC Defense Architecture:</div>
        <ol>
            <li>
                <strong>Continuous Security Awareness Training (SAT) & Simulated Phishing:</strong>
                <br>Conduct mandatory, frequent training sessions combined with unannounced simulated phishing/vishing exercises. Train staff to recognize cognitive manipulation triggers (extreme urgency, fear, greed, authority, scarcity) and provide an intuitive, one-click <em>"Report Phishing"</em> button.
            </li>
            <li>
                <strong>Enforce Phishing-Resistant Multi-Factor Authentication (MFA):</strong>
                <br>Mandate hardware-backed FIDO2 / WebAuthn security keys or number-matching authenticator apps. Phishing-resistant MFA ensures that even if an employee enters their plaintext password into a fake phishing portal, the attacker cannot complete authentication without physical access to the hardware authenticator.
            </li>
            <li>
                <strong>Strict Verification Policies & Dual-Authorization Protocols:</strong>
                <br>Establish non-negotiable out-of-band verification procedures for all sensitive operations (wire transfers, vendor bank detail updates, password resets). Require two-person authorization and direct verbal confirmation via known internal phone directory numbers &mdash; never using phone numbers provided in an incoming email.
            </li>
            <li>
                <strong>Physical Security & Clean Desk Policy:</strong>
                <br>Enforce strict badge-access controls with zero-tolerance policies for tailgating, require visitor badges and escorts, mandate cross-cut shredding of paper documents, and require locking workstations when unattended.
            </li>
            <li>
                <strong>Technical Email & Network Filtering Controls:</strong>
                <br>Deploy Next-Gen Secure Email Gateways (SEG) enforcing <strong>DMARC, DKIM, and SPF</strong> to block domain spoofing, alongside AI-driven anomaly detection, URL sandboxing, DNS sinkholing, and automated endpoint isolation.
            </li>
        </ol>
    </div>
</div>

<div class="qa-card reflection">
    <div class="question-title">Question E &mdash; Institutional Overview of the SANS Institute</div>
    <div class="question-text">What is the SANS Institute, which authored this article?</div>
    <div class="answer-box">
        <div class="answer-label">Institutional & Industry Context:</div>
        <p>
        The <strong>SANS Institute</strong> (originally an acronym for <em>SysAdmin, Audit, Network, and Security</em>) is the world's premier cooperative research and education organization specializing in information security training and certification. Founded in 1989, SANS operates as a cornerstone of the global cybersecurity community.
        </p>
        <p><strong>Core Contributions & Pillars of SANS:</strong></p>
        <ul>
            <li><strong>SANS Information Security Reading Room:</strong> A globally accessible repository containing over 3,000 peer-reviewed research papers and whitepapers on cybersecurity analysis, forensics, penetration testing, and defense strategies.</li>
            <li><strong>GIAC Certifications (Global Information Assurance Certification):</strong> Administers gold-standard professional certifications (such as GSEC, GCIH, GPEN, GCFA, and CISSP-aligned credentials) validating technical hands-on competency.</li>
            <li><strong>Internet Storm Center (ISC):</strong> The SANS "Internet's Early Warning System", which continuously collects and analyzes real-time threat telemetry from millions of distributed intrusion sensors worldwide to publish daily threat bulletins and attack trend analyses.</li>
        </ul>
    </div>
</div>

<table class="data-table">
    <thead>
        <tr>
            <th>Social Engineering Vector</th>
            <th>Primary Psychological Trigger</th>
            <th>Typical Attack Medium</th>
            <th>Primary Defensive Countermeasure</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Spear Phishing</strong></td>
            <td>Urgency, Curiosity, Authority</td>
            <td>Targeted Email / Weaponized PDF</td>
            <td>DMARC, AI Email Filters, Security Awareness Training</td>
        </tr>
        <tr>
            <td><strong>Pretexting (Helpdesk)</strong></td>
            <td>Helpfulness, Technical Intimidation</td>
            <td>Voice Call (Vishing) / Direct Chat</td>
            <td>Strict Out-of-Band Identity Verification Process</td>
        </tr>
        <tr>
            <td><strong>Tailgating / Piggybacking</strong></td>
            <td>Politeness, Social Etiquette</td>
            <td>Physical Access Gates / Turnstiles</td>
            <td>Access Badging, Anti-Passback Gates, Visitor Escorts</td>
        </tr>
        <tr>
            <td><strong>Baiting / Rogue USB</strong></td>
            <td>Curiosity, Financial Incentive</td>
            <td>Infected USB Drives in Parking Lot</td>
            <td>Disabling USB Mass Storage via Endpoint GPO / EDR</td>
        </tr>
        <tr>
            <td><strong>Watering Hole Attack</strong></td>
            <td>Implicit Trust in Industry Portals</td>
            <td>Compromised Niche Industry Website</td>
            <td>Endpoint Web Filtering, Browser Isolation, EDR</td>
        </tr>
    </tbody>
</table>

<div class="key-takeaways">
    <h3>CyberOps Analyst Key Insights</h3>
    <ul>
        <li><span class="badge-tag badge-red">Human Vulnerability</span> Technology controls cannot fully protect an organization if personnel can be manipulated into bypassing security policies.</li>
        <li><span class="badge-tag badge-blue">OSINT Sanitization</span> Organizations must establish clear social media and public disclosure policies to minimize digital footprints.</li>
        <li><span class="badge-tag badge-green">FIDO2 MFA</span> Implementing phishing-resistant multi-factor authentication effectively neutralizes credential-harvesting phishing attacks.</li>
        <li><span class="badge-tag badge-purple">No-Blame Culture</span> Establishing an open, non-punitive reporting culture encourages rapid incident disclosure, minimizing dwell time during security breaches.</li>
    </ul>
</div>

</body>
</html>"""

def main():
    print("Generating Lab 14.2.8 Solution PDF...")
    output_pdf = os.path.join(LABS_DIR, "14.2.8-Lab-Social-Engineering-Solution.pdf")
    
    temp_html = os.path.join(TEMP_DIR, "temp_lab_14_2_8.html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(LAB_14_2_8_HTML)
    
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    user_data_dir = os.path.join(TEMP_DIR, "edge-pdf-lab-14-2-8")
    
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
