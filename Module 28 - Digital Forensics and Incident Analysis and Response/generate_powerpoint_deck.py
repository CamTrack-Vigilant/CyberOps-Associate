import os
import re
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # Set 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # completely blank layout

    # Official UNIZULU Palette
    NAVY = RGBColor(0, 40, 85)         # #002855
    NAVY_DEEP = RGBColor(0, 24, 51)    # #001833
    ROYAL = RGBColor(29, 78, 216)      # #1D4ED8
    GOLD = RGBColor(245, 158, 11)      # #F59E0B
    GOLD_LIGHT = RGBColor(254, 243, 199) # #FEF3C7
    WHITE = RGBColor(255, 255, 255)    # #FFFFFF
    BG_CARD = RGBColor(248, 250, 252)  # #F8FAFC
    BORDER_CARD = RGBColor(203, 213, 225) # #CBD5E1
    BORDER_NAVY = RGBColor(0, 40, 85)
    TEXT_MAIN = RGBColor(15, 23, 42)   # #0F172A
    TEXT_BODY = RGBColor(30, 41, 59)   # #1E293B
    TEXT_MUTED = RGBColor(100, 116, 139) # #64748B
    GREEN = RGBColor(21, 128, 61)
    RED = RGBColor(185, 28, 28)

    LOGO_PATH = "unizulu_logo.png"
    WATERMARK_PATH = "unizulu_watermark.png"

    def add_base_decorations(slide, slide_num, total_slides, tag_text, title_text, is_hero=False):
        # 1. Slide Background (Crisp White)
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = WHITE
        bg.line.fill.background()

        # 2. Watermark Badge Background
        if os.path.exists(WATERMARK_PATH):
            wm = slide.shapes.add_picture(WATERMARK_PATH, Inches(4.6), Inches(1.3), width=Inches(4.2))

        if is_hero:
            # Full UNIZULU Navy Hero Header
            header = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.5))
            header.fill.solid()
            header.fill.fore_color.rgb = NAVY
            header.line.fill.background()

            # Gold trim line
            gold_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.5), Inches(13.333), Inches(0.08))
            gold_line.fill.solid()
            gold_line.fill.fore_color.rgb = GOLD
            gold_line.line.fill.background()

            # UNIZULU Crest in Hero
            if os.path.exists(LOGO_PATH):
                slide.shapes.add_picture(LOGO_PATH, Inches(0.6), Inches(0.2), height=Inches(1.1))

            # Hero Title text
            tb = slide.shapes.add_textbox(Inches(1.8), Inches(0.25), Inches(10.8), Inches(1.0))
            tf = tb.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = "UNIVERSITY OF ZULULAND • CISCO CYBEROPS ACADEMY"
            p.font.name = "Segoe UI"
            p.font.size = Pt(13)
            p.font.bold = True
            p.font.color.rgb = GOLD

            p2 = tf.add_paragraph()
            p2.text = title_text
            p2.font.name = "Segoe UI"
            p2.font.size = Pt(22)
            p2.font.bold = True
            p2.font.color.rgb = WHITE
        else:
            # Standard Header Banner
            header = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.15))
            header.fill.solid()
            header.fill.fore_color.rgb = NAVY
            header.line.fill.background()

            # Gold accent line
            gold_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.15), Inches(13.333), Inches(0.06))
            gold_line.fill.solid()
            gold_line.fill.fore_color.rgb = GOLD
            gold_line.line.fill.background()

            # Logo
            if os.path.exists(LOGO_PATH):
                slide.shapes.add_picture(LOGO_PATH, Inches(0.5), Inches(0.12), height=Inches(0.9))

            # Header Titles
            tb = slide.shapes.add_textbox(Inches(1.4), Inches(0.12), Inches(9.8), Inches(0.9))
            tf = tb.text_frame
            tf.word_wrap = True
            p1 = tf.paragraphs[0]
            p1.text = tag_text.upper()
            p1.font.name = "Segoe UI"
            p1.font.size = Pt(10)
            p1.font.bold = True
            p1.font.color.rgb = GOLD

            p2 = tf.add_paragraph()
            p2.text = title_text
            p2.font.name = "Segoe UI"
            p2.font.size = Pt(19)
            p2.font.bold = True
            p2.font.color.rgb = WHITE

            # Right badge on header
            rb = slide.shapes.add_textbox(Inches(10.5), Inches(0.2), Inches(2.3), Inches(0.7))
            rtf = rb.text_frame
            rp = rtf.paragraphs[0]
            rp.text = "UNIZULU CSIRT"
            rp.alignment = PP_ALIGN.RIGHT
            rp.font.name = "Segoe UI"
            rp.font.size = Pt(12)
            rp.font.bold = True
            rp.font.color.rgb = GOLD

            rp2 = rtf.add_paragraph()
            rp2.text = "Module 28 • CyberOps"
            rp2.alignment = PP_ALIGN.RIGHT
            rp2.font.name = "Segoe UI"
            rp2.font.size = Pt(10)
            rp2.font.color.rgb = WHITE

        # Footer Banner
        footer = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(7.05), Inches(13.333), Inches(0.45))
        footer.fill.solid()
        footer.fill.fore_color.rgb = NAVY_DEEP
        footer.line.fill.background()

        # Footer gold top line
        fline = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(7.03), Inches(13.333), Inches(0.02))
        fline.fill.solid()
        fline.fill.fore_color.rgb = GOLD
        fline.line.fill.background()

        # Footer Text
        ftb = slide.shapes.add_textbox(Inches(0.5), Inches(7.08), Inches(9.0), Inches(0.35))
        fp = ftb.text_frame.paragraphs[0]
        fp.text = "University of Zululand • Faculty of Science, Agriculture & Technology • Department of Computer Science"
        fp.font.name = "Segoe UI"
        fp.font.size = Pt(9.5)
        fp.font.color.rgb = GOLD_LIGHT

        # Slide Number
        sntb = slide.shapes.add_textbox(Inches(10.5), Inches(7.08), Inches(2.3), Inches(0.35))
        snp = sntb.text_frame.paragraphs[0]
        snp.alignment = PP_ALIGN.RIGHT
        snp.text = f"Slide {slide_num} of {total_slides}"
        snp.font.name = "Segoe UI"
        snp.font.size = Pt(10)
        snp.font.bold = True
        snp.font.color.rgb = WHITE

    def add_notes(slide, notes_text):
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = notes_text

    def add_card(slide, left, top, width, height, title, items, border_color=BORDER_NAVY, fill_color=BG_CARD):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = fill_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)

        tb = slide.shapes.add_textbox(left + Inches(0.18), top + Inches(0.15), width - Inches(0.36), height - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Segoe UI"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = NAVY

        for item in items:
            p_item = tf.add_paragraph()
            p_item.text = f"•  {item}"
            p_item.font.name = "Segoe UI"
            p_item.font.size = Pt(10.5)
            p_item.font.color.rgb = TEXT_BODY
            p_item.space_before = Pt(4)

    def add_diagram_slide(slide_num, total_slides, tag, title, diag_file, cards_data, notes_text):
        slide = prs.slides.add_slide(blank_layout)
        add_base_decorations(slide, slide_num, total_slides, tag, title)
        add_notes(slide, notes_text)

        # Left: Diagram Image Box
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.55), Inches(1.35), Inches(7.5), Inches(5.4))
        box.fill.solid()
        box.fill.fore_color.rgb = WHITE
        box.line.color.rgb = NAVY
        box.line.width = Pt(2)

        if os.path.exists(diag_file):
            slide.shapes.add_picture(diag_file, Inches(0.7), Inches(1.5), width=Inches(7.2))

        # Diagram Caption badge
        cap_box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.55), Inches(6.35), Inches(7.5), Inches(0.4))
        cap_box.fill.solid()
        cap_box.fill.fore_color.rgb = NAVY
        cap_box.line.fill.background()
        cp = cap_box.text_frame.paragraphs[0]
        cp.alignment = PP_ALIGN.CENTER
        cp.text = "Cisco CyberOps Associate • Module 28 Master Architecture Diagram"
        cp.font.name = "Segoe UI"
        cp.font.size = Pt(10)
        cp.font.bold = True
        cp.font.color.rgb = GOLD

        # Right: Architectural Takeaway Cards
        card_h = (Inches(5.4) - (len(cards_data) - 1) * Inches(0.18)) / len(cards_data)
        for i, (c_title, c_desc) in enumerate(cards_data):
            c_top = Inches(1.35) + i * (card_h + Inches(0.18))
            card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.25), c_top, Inches(4.55), card_h)
            card.fill.solid()
            card.fill.fore_color.rgb = BG_CARD
            card.line.color.rgb = BORDER_CARD
            card.line.width = Pt(1.5)

            tb = slide.shapes.add_textbox(Inches(8.4), c_top + Inches(0.08), Inches(4.25), card_h - Inches(0.16))
            tf = tb.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = c_title
            p.font.name = "Segoe UI"
            p.font.size = Pt(12)
            p.font.bold = True
            p.font.color.rgb = NAVY

            p2 = tf.add_paragraph()
            p2.text = c_desc
            p2.font.name = "Segoe UI"
            p2.font.size = Pt(10)
            p2.font.color.rgb = TEXT_BODY
            p2.space_before = Pt(3)

    TOTAL_SLIDES = 26

    # ==========================================
    # SLIDE 1: Title & Welcome
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s1, 1, TOTAL_SLIDES, "28.0 Introduction", "Incident Response Models & Digital Forensics", is_hero=True)
    add_notes(s1, """Welcome to Module 28: Incident Response Models and Digital Forensics, presented by the University of Zululand Department of Computer Science.
In this capstone module, we answer the ultimate question: What do you do when an attack actually happens?
We examine four essential pillars:
1. Evidence Handling & Attack Attribution (forensics, volatility order, chain of custody, legal standards).
2. The Lockheed Martin Cyber Kill Chain (7 stages, defensive breakpoints, active SOC countermeasures).
3. The Diamond Model of Intrusion Analysis (4 core features, 6 meta-features, pivoting across nodes).
4. Incident Response procedures under NIST SP 800-61r2 (preparation, detection, containment, and post-incident lessons learned).""")

    # Intro description
    intro_tb = s1.shapes.add_textbox(Inches(0.6), Inches(1.75), Inches(12.1), Inches(0.8))
    itf = intro_tb.text_frame
    itf.word_wrap = True
    ip = itf.paragraphs[0]
    ip.text = "You have learned all about attack vectors and defensive tools to protect systems. In this capstone module, you will learn what to do when an attack actually happens, mastering forensic evidence preservation, intrusion analysis models, and NIST handling lifecycles."
    ip.font.name = "Segoe UI"
    ip.font.size = Pt(12.5)
    ip.font.color.rgb = TEXT_BODY

    # 4 Cards for 4 Topics
    topics = [
        ("28.1 Evidence Handling", [
            "Digital forensics processes",
            "Best vs. circumstantial evidence",
            "RFC 3227 order of volatility",
            "Chain of custody & attribution"
        ]),
        ("28.2 Cyber Kill Chain", [
            "Lockheed Martin 7-stage model",
            "Adversary vertical progression",
            "Defensive breakpoints for SOC",
            "Stopping attack execution"
        ]),
        ("28.3 Diamond Model", [
            "4 Core features: Adversary, Capability, Infrastructure, Victim",
            "6 Meta-features characterization",
            "Multi-event pivoting pathways"
        ]),
        ("28.4 Incident Response", [
            "NIST SP 800-61r2 4-phase cycle",
            "CSIRC capability & jump kits",
            "Containment strategy criteria",
            "Post-incident 10 review questions"
        ])
    ]
    card_w = Inches(2.85)
    for i, (t_title, t_items) in enumerate(topics):
        add_card(s1, Inches(0.6) + i * Inches(3.08), Inches(2.7), card_w, Inches(4.0), t_title, t_items)

    # ==========================================
    # SLIDE 2: Master Architecture 1 (Roadmap)
    # ==========================================
    add_diagram_slide(
        slide_num=2,
        total_slides=TOTAL_SLIDES,
        tag="28.0 Introduction • Module Architecture Roadmap",
        title="CyberOps: Incident Response Models Roadmap",
        diag_file="ab65b04f-09de-471a-9a89-305270b0ea91.jfif",
        cards_data=[
            ("1. Evidence Handling & Attribution (28.1)", "Covers digital forensics sources, volatile memory acquisition order (RFC 3227), legal evidence classifications, unbroken chain of custody, and attribution."),
            ("2. The Cyber Kill Chain (28.2)", "Identifies the 7 sequential stages developed by Lockheed Martin; pinpoints defensive breakpoints where SOC controls break the intrusion."),
            ("3. The Diamond Model (28.3)", "Classifies intrusion events using 4 core vertices and 6 meta-features; maps complex multi-victim intrusions through horizontal pivoting."),
            ("4. Incident Response (28.4)", "Applies NIST SP 800-61r2 handling procedures, CSIRC capability governance, DoD CMMC maturity levels, and lessons-learned metrics.")
        ],
        notes_text="""Here is the master architectural roadmap for Cisco CyberOps Associate Module 28. It connects the 4 core learning pillars: Section 28.1 Evidence Handling & Attack Attribution; Section 28.2 The Cyber Kill Chain; Section 28.3 The Diamond Model of Intrusion Analysis; and Section 28.4 Incident Response under NIST SP 800-61r2. Each phase builds upon the previous, preparing the analyst from initial digital forensic collection to executive reporting."""
    )

    # ==========================================
    # SLIDE 3: 28.1.1 Digital Forensics & Legal Context
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s3, 3, TOTAL_SLIDES, "28.1 Evidence Handling • 28.1.1 Digital Forensics", "Digital Forensics: Evidence & Legal Context")
    add_notes(s3, """Digital forensics is the recovery and investigation of information on digital devices related to criminal activity. Indicators of compromise (IoCs) are the evidence of an incident found on storage, volatile RAM, or pcaps and logs. We distinguish between private (internal) investigations and public investigations involving law enforcement. Also remember regulatory mandates like HIPAA: if patient data of 500+ individuals is breached, media and victims must be notified immediately! Forensics certifies the numbers.""")
    add_card(s3, Inches(0.6), Inches(1.4), Inches(5.8), Inches(5.3), "What is Digital Forensics?", [
        "Definition: Recovery and investigation of information on digital devices related to criminal activity.",
        "Indicators of Compromise (IoC): Tangible evidence that an incident occurred (disk files, volatile RAM, pcaps, logs).",
        "Tier 1 Analyst Role: Tier 1 analysts are often the first to uncover wrongdoing and must handle evidence so it supports legal prosecution.",
        "Golden Mandate: All IoCs must be preserved in untampered condition for future analysis and attack attribution."
    ])
    add_card(s3, Inches(6.8), Inches(1.4), Inches(5.8), Inches(5.3), "Investigation Contexts & Regulations", [
        "Private (Internal) Investigations: Focus on internal policy violations. If criminal conduct or intellectual property theft occurs, it becomes public by notifying law enforcement.",
        "Public Investigations: Carried out by public officials when internal users or external attackers violate legal statutes.",
        "Regulatory Mandates (US HIPAA): Requires notification if patient records breach. If >500 individuals are impacted in a jurisdiction, both media and affected victims must be notified.",
        "Organization Under Investigation: The organization itself may be investigated. Analysts must preserve evidence; intentional destruction results in criminal penalties."
    ])

    # ==========================================
    # SLIDE 4: Master Architecture 2 (Forensics Infographic)
    # ==========================================
    add_diagram_slide(
        slide_num=4,
        total_slides=TOTAL_SLIDES,
        tag="28.1 Evidence Handling • Master Architectural Infographic",
        title="Digital Forensics: Evidence Handling & Attribution",
        diag_file="f404cbb5-ce19-412b-9313-f04529e11869.jfif",
        cards_data=[
            ("1. Digital Forensics (28.1.1)", "Recovers digital evidence across storage, volatile RAM, and network pcaps; handles internal vs. public investigations; certifies breach numbers for regulatory compliance (HIPAA)."),
            ("2. Process & Types of Evidence (28.1.2 - 28.1.6)", "NIST SP 800-86 four phases (Collection, Examination, Analysis, Reporting); Best vs. Corroborating evidence; strict RFC 3227 volatility ladder (Registers ➔ RAM ➔ Disk ➔ Logs ➔ Archives)."),
            ("3. Integrity & Attribution (28.1.7 - 28.1.9)", "Unbroken chain of custody logbooks; hardware write-blockers; verified bit-level master replicas; attributing attacks via location (IP/MAC), malware code features, and MITRE TTPs.")
        ],
        notes_text="""This master infographic summarizes Section 28.1 across three core pillars: First, Digital Forensics sources (storage, RAM, network pcaps) and regulatory mandates like HIPAA. Second, the 4-phase forensic process (Collection, Examination, Analysis, Reporting), classifications of legal evidence, and the RFC 3227 Order of Volatility. Third, Data Integrity, Chain of Custody, master volume preservation with write-blockers and bit-level copies, and Attack Attribution via location, malware features, and TTPs."""
    )

    # ==========================================
    # SLIDE 5: 28.1.2 The Forensic Process (NIST SP 800-86)
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s5, 5, TOTAL_SLIDES, "28.1 Evidence Handling • 28.1.2 The Forensic Process", "The NIST SP 800-86 Forensic Process")
    add_notes(s5, """NIST SP 800-86 defines the 4-phase forensic process: Collection, Examination, Analysis, and Reporting. In Collection, media is acquired using write-blockers. In Examination, data is extracted and filtered using known-good hash databases. In Analysis, artifacts are correlated to determine what happened. In Reporting, documentation is created for leadership and legal prosecution.""")
    phases = [
        ("1. Collection (Media)", [
            "Identification of potential data sources (disks, RAM, logs).",
            "Acquisition, handling, and secure storage of digital media.",
            "Crucial Rule: Special care taken never to alter, damage, or omit evidence.",
            "Hardware write-blockers and bit-stream disk images."
        ]),
        ("2. Examination (Data)", [
            "Processing collected data to extract relevant digital artifacts.",
            "De-NISTing: Filtering out routine OS noise using NSRL databases.",
            "Recovering hidden, deleted, or timestomped files.",
            "Extracting active network connections and memory strings."
        ]),
        ("3. Analysis (Information)", [
            "Correlating digital artifacts to deduce the incident chronology.",
            "Reconstructing the attack timeline from log files.",
            "Determining adversary entry point and lateral movement.",
            "Deriving actionable attribution conclusions."
        ]),
        ("4. Reporting (Evidence)", [
            "Documenting findings, techniques, and forensic conclusions.",
            "Writing executive summaries for organizational leadership.",
            "Preparing technical evidence suitable for legal court proceedings.",
            "Detailed chain-of-custody transfer logs."
        ])
    ]
    for i, (p_title, p_items) in enumerate(phases):
        add_card(s5, Inches(0.6) + i * Inches(3.08), Inches(1.45), card_w, Inches(5.2), p_title, p_items)

    # ==========================================
    # SLIDE 6: 28.1.4 Classifications of Legal Evidence
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s6, 6, TOTAL_SLIDES, "28.1 Evidence Handling • 28.1.4 Types of Evidence", "Classifications of Legal Evidence")
    add_notes(s6, """In legal proceedings, evidence is classified as Direct or Indirect (Circumstantial). Direct evidence indisputably ties the accused to the crime or involves eyewitnesses. Indirect evidence establishes a hypothesis in combination with other facts. Evidence is also classified as Best Evidence (unaltered original state, such as a verified bit-stream forensic image) or Corroborating Evidence (secondary server logs verifying an endpoint alert).""")
    add_card(s6, Inches(0.6), Inches(1.4), Inches(5.8), Inches(5.3), "Primary Legal Classifications", [
        "Direct Evidence: Evidence that was indisputably in possession of the accused, or eyewitness evidence from someone who directly observed criminal behavior.",
        "Example of Direct: Live network packet capture showing attacker keyboard input originating from the accused's authenticated account.",
        "Indirect Evidence (Circumstantial): Evidence that, in combination with other facts, establishes a hypothesis.",
        "Example of Indirect: Prior history of committing similar intrusions or owning malware compilation tools matching the attack payload."
    ])
    add_card(s6, Inches(6.8), Inches(1.4), Inches(5.8), Inches(5.3), "Forensic Evidence Categories", [
        "Best Evidence: Evidence that is preserved in its unaltered original state. Storage devices used by the accused or verified bit-stream disk images.",
        "Integrity Proof: Cryptographic hash comparison (SHA-256) proving the forensic clone is bit-for-bit identical to the suspect drive.",
        "Corroborating Evidence: Evidence that supports an assertion developed from best evidence.",
        "Example of Corroborating: Secondary proxy or firewall logs confirming an unauthorized outbound connection flagged on an endpoint disk."
    ])

    # ==========================================
    # SLIDE 7: 28.1.6 RFC 3227: Order of Volatility
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s7, 7, TOTAL_SLIDES, "28.1 Evidence Handling • 28.1.6 RFC 3227 Volatility", "RFC 3227: Order of Volatility")
    add_notes(s7, """IETF RFC 3227 provides the official sequence for collecting digital evidence based on volatility. Data in registers, caches, and RAM disappears instantly on reboot or power loss, and can be overwritten by running processes. Therefore, evidence must be collected strictly from most volatile to least volatile: Registers/Caches -> RAM/Routing/Process Table -> Temp Files -> Fixed Media -> Remote Logs -> Physical Topology -> Archival Media.""")
    add_card(s7, Inches(0.6), Inches(1.4), Inches(4.8), Inches(5.3), "Why Volatility Dictates Collection", [
        "Volatile Data Loss: Data in RAM, processor registers, and caches is wiped instantly when power is cut or the machine reboots.",
        "Routine Overwriting: Active machine processes continually overwrite memory buffers during normal operation.",
        "Golden Rule of Collection: Always acquire the most volatile data first before powering down or disconnecting hardware.",
        "Documentation Mandate: Record exact system time, timezone offsets, hardware model, OS version, logged-in users, and physical port connections."
    ])
    # Volatility ladder cards
    ladder = [
        ("1. Memory registers, caches", "Disappears in nanoseconds; CPU registers and cache buffers"),
        ("2. Routing table, ARP cache, process table, RAM", "Disappears on reboot; active sockets, injected DLLs, decryption keys"),
        ("3. Temporary file systems", "Disappears on reboot; /tmp, swap space, pagefile.sys"),
        ("4. Non-volatile media (Disks, SSDs, USB)", "Fixed hard drives, solid-state drives, USB flash drives"),
        ("5. Remote logging and monitoring data", "Syslog servers, SIEM data, NetFlow, firewall logs"),
        ("6. Physical interconnections & topology", "Cable layout, switch port maps, physical network topology"),
        ("7. Archival media and backup tapes", "Least volatile; optical discs, tape backups, offsite archives")
    ]
    ladder_w = Inches(6.8)
    for i, (l_title, l_desc) in enumerate(ladder):
        l_top = Inches(1.4) + i * Inches(0.72)
        l_box = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.8), l_top, ladder_w, Inches(0.65))
        l_box.fill.solid()
        l_box.fill.fore_color.rgb = GOLD_LIGHT if i < 2 else BG_CARD
        l_box.line.color.rgb = GOLD if i < 2 else NAVY
        l_box.line.width = Pt(1.5)

        tb = s7.shapes.add_textbox(Inches(5.95), l_top + Inches(0.05), ladder_w - Inches(0.3), Inches(0.55))
        tf = tb.text_frame
        p = tf.paragraphs[0]
        p.text = l_title
        p.font.name = "Segoe UI"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = RED if i < 2 else NAVY

        p2 = tf.add_paragraph()
        p2.text = l_desc
        p2.font.name = "Segoe UI"
        p2.font.size = Pt(9)
        p2.font.color.rgb = TEXT_BODY

    # ==========================================
    # SLIDE 8: 28.1.7 & 28.1.8 Chain of Custody & Preservation
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s8, 8, TOTAL_SLIDES, "28.1 Evidence Handling • 28.1.7 & 28.1.8 Integrity", "Chain of Custody & Data Preservation")
    add_notes(s8, """Chain of custody documents the entire lifecycle of evidence: Who discovered it, exact timestamps, custody transfers, and physical storage security. If the chain is broken, evidence is deemed contaminated and inadmissible. Data preservation requires never working on original evidence; always create a bit-stream replica using hardware write-blockers and record SHA-256 hashes before and after copying.""")
    add_card(s8, Inches(0.6), Inches(1.4), Inches(5.8), Inches(5.3), "Chain of Custody Requirements", [
        "Definition: Detailed, unbroken legal record documenting collection, transfer, and storage of evidence.",
        "Discovery Record: Who found the evidence, where, and under what circumstances.",
        "Detailed Handling: Dates, exact timestamps, and names of all personnel involved.",
        "Custody Transitions: Formal receipt logs whenever responsibility changes hands.",
        "Physical Security: Access restricted exclusively to essential personnel; stored in tamper-evident forensic safes.",
        "Legal Impact: A broken chain of custody invalidates evidence in court, allowing guilty actors to walk free."
    ])
    add_card(s8, Inches(6.8), Inches(1.4), Inches(5.8), Inches(5.3), "Data Preservation Best Practices", [
        "Golden Rule of Forensics: NEVER examine, analyze, or boot original master evidence drives.",
        "Hardware Write-Blockers: Physical devices that prevent OS write commands from altering suspect drive timestamps or sectors.",
        "Bit-Stream Disk Images: Create a bit-for-bit clone (including deleted space and slack space), not a standard logical file copy.",
        "Cryptographic Hashing: Calculate SHA-256 / SHA-512 hashes of the original drive BEFORE copying and of the image AFTER copying.",
        "Hash Verification: Identical hashes prove mathematically that zero bytes were altered during the acquisition process."
    ])

    # ==========================================
    # SLIDE 9: 28.1.9 & 28.1.10 Attack Attribution & MITRE ATT&CK
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s9, 9, TOTAL_SLIDES, "28.1 Attack Attribution • 28.1.9 & 28.1.10 MITRE ATT&CK", "Attack Attribution & MITRE ATT&CK")
    add_notes(s9, """Attack attribution identifies the threat actor responsible through IP geolocation, malware code artifacts, and behavioral TTPs. While attribution is challenging due to proxy networks, the MITRE ATT&CK framework provides an industry-standard knowledge base categorizing adversary behavior across Tactics (Goals/Why), Techniques (Means/How), and Procedures (Execution actions).""")
    add_card(s9, Inches(0.6), Inches(1.4), Inches(5.8), Inches(5.3), "Attack Attribution Elements", [
        "Definition: The process of identifying the threat actor, organization, or nation-state responsible for an intrusion.",
        "Source Geolocation: Tracing IP and MAC addresses, VPN exit nodes, and Autonomous System Numbers (ASNs).",
        "Malware Code Features: Unique compiler signatures, embedded language strings, encryption routines, and debugging artifacts.",
        "TTP Behavioral Matching: Tactics, Techniques, and Procedures consistent with known Advanced Persistent Threat (APT) groups.",
        "Attribution Challenges: Attackers use compromised third-party servers, Tor, fast-flux DNS, and false-flag artifacts to misdirect analysts."
    ])
    add_card(s9, Inches(6.8), Inches(1.4), Inches(5.8), Inches(5.3), "MITRE ATT&CK Framework", [
        "Globally-Accessible Knowledge Base: Comprehensive matrix of adversary tactics and techniques based on real-world observations.",
        "Tactics ('Why'): The adversary's tactical goal (e.g., Initial Access, Execution, Persistence, Privilege Escalation, Exfiltration).",
        "Techniques ('How'): The specific method used to achieve the tactical goal (e.g., Spearphishing Attachment, DLL Sideloading, Pass-the-Hash).",
        "Procedures ('What'): The exact implementation code, script, or command sequence used by a specific threat group.",
        "SOC Benefit: Enables SOC teams to map telemetry, identify detection gaps, and prioritize high-risk threat actor profiles."
    ])

    # ==========================================
    # SLIDE 10: 28.2 Cyber Kill Chain: Stages 1 - 3
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s10, 10, TOTAL_SLIDES, "28.2 The Cyber Kill Chain • Stages 1 - 3", "The Cyber Kill Chain: Stages 1 to 3")
    add_notes(s10, """Developed by Lockheed Martin, the Cyber Kill Chain defines the 7 sequential stages of an attack. Breaking any single link stops the entire campaign. In Stage 1 (Reconnaissance), the attacker harvests intel and scans targets. In Stage 2 (Weaponization), malware is paired with an exploit. In Stage 3 (Delivery), the payload is sent via email, web, or USB. SOC defenses at these stages focus on threat intel, email attachment sandboxing, and web filtering.""")
    kc_early = [
        ("1. Reconnaissance", [
            "Adversary: Harvests emails, scans open ports, searches social media (LinkedIn, Twitter), and queries WHOIS databases.",
            "Objective: Identify vulnerable systems and high-value employee targets.",
            "SOC Defenses: Monitor web server and firewall logs; analyze border router traffic; minimize publicly exposed employee directory information."
        ]),
        ("2. Weaponization", [
            "Adversary: Couples a backdoor payload with an exploit designed for an identified target vulnerability (e.g., PDF or Office macro).",
            "Objective: Create an automated weaponizer package ready for transmission.",
            "SOC Defenses: Threat intelligence feeds; updating IDS/IPS detection rules; analyzing malware artifacts in an isolated sandbox."
        ]),
        ("3. Delivery", [
            "Adversary: Transmits the weaponized payload to the victim via spearphishing email attachment, compromised web link, or infected USB drive.",
            "Objective: Place the weaponized file into the target organization's boundary.",
            "SOC Defenses: Email attachment filtering & sandboxing; proxy log inspection; endpoint USB port control policies."
        ])
    ]
    card_w3 = Inches(3.85)
    for i, (k_title, k_items) in enumerate(kc_early):
        add_card(s10, Inches(0.6) + i * Inches(4.15), Inches(1.45), card_w3, Inches(5.2), k_title, k_items)

    # ==========================================
    # SLIDE 11: Master Architecture 3 (Kill Chain Diagram)
    # ==========================================
    add_diagram_slide(
        slide_num=11,
        total_slides=TOTAL_SLIDES,
        tag="28.2 Cyber Kill Chain • Master Tactical Diagram",
        title="Lockheed Martin Kill Chain: Adversary vs. SOC Defenses",
        diag_file="01daa9c8-a4d3-43bc-832f-f1098f6cd5df.jfif",
        cards_data=[
            ("Sequential Attack Traversal", "Adversary traverses 7 linear phases from Reconnaissance to Actions on Objectives. Breaking any single link halts the campaign and prevents adversary objective completion."),
            ("The Defensive Breakpoint", "The window between Delivery, Exploit Execution, and Persistence represents the SOC's highest leverage point to neutralize threats before lateral movement occurs."),
            ("Defense-in-Depth Layering", "Aligns network sensors, endpoint HIPS, DNS sinkholing, email sandboxing, and rapid containment playbooks directly against corresponding attack phases.")
        ],
        notes_text="""This tactical architecture diagram details the Lockheed Martin Cyber Kill Chain and corresponding SOC defenses. On the left is the adversary campaign: Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command and Control, and Actions on Objectives. In the center is the critical Defensive Breakpoint: stopping an exploit or persistence breaks the entire attack chain. On the right are active SOC defensive controls: log monitoring, signature updates, email filtering, endpoint hardening, and DNS sinkholing."""
    )

    # ==========================================
    # SLIDE 12: 28.2 Cyber Kill Chain: Stages 4 - 7
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s12, 12, TOTAL_SLIDES, "28.2 The Cyber Kill Chain • Stages 4 - 7", "The Cyber Kill Chain: Stages 4 to 7")
    add_notes(s12, """Stages 4 to 7 represent the operational execution of the attack. Stage 4 is Exploitation (triggering the vulnerability). Stage 5 is Installation (establishing persistent backdoors and registry Run keys). Stage 6 is Command and Control (opening a bi-directional beaconing channel). Stage 7 is Actions on Objectives (data exfiltration, ransomware, or destruction). Defensive countermeasures include endpoint hardening, HIPS, DNS sinkholing, and automated containment playbooks.""")
    kc_late = [
        ("4. Exploitation", [
            "Adversary: Malicious code triggers software vulnerability to gain code execution.",
            "Defense Breakpoint: Software patching, DEP/ASLR, endpoint hardening, user awareness training."
        ]),
        ("5. Installation", [
            "Adversary: Installs persistent backdoor service, modifies registry Run keys or scheduled tasks.",
            "SOC Defenses: Host-based IPS (HIPS), endpoint detection & response (EDR), file integrity monitoring."
        ]),
        ("6. Command & Control (C2)", [
            "Adversary: Opens bi-directional communication beacon (HTTPS/DNS) to external remote server.",
            "SOC Defenses: Outbound traffic anomaly detection, DNS sinkholing, SSL/TLS proxy inspection."
        ]),
        ("7. Actions on Objectives", [
            "Adversary: Performs lateral movement, credentials dumping, data exfiltration, or ransomware extortion.",
            "SOC Defenses: Rapid triage, packet capture analysis, account revocation, network segmentation."
        ])
    ]
    for i, (k_title, k_items) in enumerate(kc_late):
        add_card(s12, Inches(0.6) + i * Inches(3.08), Inches(1.45), card_w, Inches(5.2), k_title, k_items)

    # ==========================================
    # SLIDE 13: 28.3.1 Diamond Model: Core & Meta-Features
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s13, 13, TOTAL_SLIDES, "28.3 Diamond Model • 28.3.1 Overview", "The Diamond Model: Core & Meta-Features")
    add_notes(s13, """The Diamond Model of Intrusion Analysis establishes relationships between 4 core features: Adversary, Capability, Infrastructure, and Victim. It emphasizes that an adversary uses infrastructure to deliver a capability against a victim. Each event is further classified by 6 meta-features: Timestamp, Phase, Result, Direction, Methodology, and Resources. This model excels at tracking campaigns across multiple hosts and organizations.""")
    add_card(s13, Inches(0.6), Inches(1.4), Inches(5.8), Inches(5.3), "4 Core Features of an Event", [
        "Adversary: The threat actor or organization responsible for the malicious activity.",
        "Capability: The specific malware tools, exploits, or techniques utilized by the adversary.",
        "Infrastructure: The physical and logical communication paths used to establish contact (C2 IPs, domains, botnets).",
        "Victim: The target host, user account, IP address, or organization being exploited.",
        "Fundamental Axiom: An Adversary develops Capabilities, uses Infrastructure to connect to the Victim, and deploys Capability against the Victim."
    ])
    add_card(s13, Inches(6.8), Inches(1.4), Inches(5.8), Inches(5.3), "6 Meta-Features for Enrichment", [
        "1. Timestamp: Date and exact start/end time of the malicious event.",
        "2. Phase: The corresponding stage within the Cyber Kill Chain.",
        "3. Result: Outcome of the attempt (Success, Partial, or Failed).",
        "4. Direction: Traffic flow orientation (Adversary-to-Victim, Victim-to-Infrastructure, Bidirectional).",
        "5. Methodology: Broad attack category (e.g., Spearphishing, Port Scan, Content Delivery, SYN Flood).",
        "6. Resources: Software and hardware elements consumed (compromised servers, tools, libraries)."
    ])

    # ==========================================
    # SLIDE 14: Master Architecture 4 (Diamond Model Diagram)
    # ==========================================
    add_diagram_slide(
        slide_num=14,
        total_slides=TOTAL_SLIDES,
        tag="28.3 Diamond Model • Master Analytical Infographic",
        title="The Diamond Model & Attack Pivoting Architecture",
        diag_file="c535d161-11cb-455b-8625-1b1a1d999ff3.jfif",
        cards_data=[
            ("1. Core & Meta-Features (28.3.1)", "Four vertex nodes: Adversary, Capability, Infrastructure, Victim. Enriched by 6 meta-features: Timestamp, Phase, Result, Direction, Methodology, Resources."),
            ("2. Analytical Pivoting (28.3.2)", "Pivoting leverages discovered artifacts in one node (e.g., malware hash or C2 IP) to uncover connected victims or identify the adversary."),
            ("3. Kill Chain Threading (28.3.3)", "Combines vertical Kill Chain execution with horizontal pivoting across organizations (Gadgets Inc. NA1 to Victim 2 CRO).")
        ],
        notes_text="""This master architecture diagram illustrates the Diamond Model of Intrusion Analysis and its relationship to the Cyber Kill Chain. Part 1 shows the 4 core features: Adversary, Capability, Infrastructure, and Victim, along with meta-features (Timestamp, Phase, Result, Direction, Methodology, Resources). Part 2 shows Analytical Pivoting: moving from Victim to Capability to Infrastructure to Adversary. Part 3 illustrates vertical Kill Chain traversal against Gadgets Inc. with horizontal pivoting to compromise Victim 2."""
    )

    # ==========================================
    # SLIDE 15: 28.3.2 Pivoting Across the Diamond Model
    # ==========================================
    s15 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s15, 15, TOTAL_SLIDES, "28.3 Diamond Model • 28.3.2 Pivoting", "Pivoting Across the Diamond Model")
    add_notes(s15, """Pivoting is the analytical practice of using an artifact discovered in one diamond vertex to uncover related features in another vertex. For example, discovering malware on a victim leads to a C2 IP; searching logs for that IP reveals a second victim; analyzing both victims reveals a common threat actor.""")
    add_card(s15, Inches(0.6), Inches(1.4), Inches(5.8), Inches(5.3), "The Concept of Analytical Pivoting", [
        "Definition: Leveraging known information from one node to discover previously unknown nodes in the attack graph.",
        "Expanding Scope: Transforms an isolated alert on a single workstation into a complete view of the adversary's broader campaign.",
        "Connecting Disparate Data: Connects network traffic, host file artifacts, threat intelligence hashes, and adversary identities.",
        "Proactive Threat Hunting: Once a C2 IP or malware signature is discovered, the SOC hunts across historical logs to find all other affected internal systems."
    ])
    add_card(s15, Inches(6.8), Inches(1.4), Inches(5.8), Inches(5.3), "Step-by-Step Pivoting Pathway", [
        "Step 1 (Victim ➔ Capability): Victim alerts SOC to anomalous host crash; forensic analysis uncovers novel malware sample.",
        "Step 2 (Capability ➔ Infrastructure): Reverse engineering the malware extracts hardcoded C2 IP addresses and backup DNS domains.",
        "Step 3 (Infrastructure ➔ Victim 2): Querying enterprise firewall and NetFlow logs for the C2 IP discovers connections from a second host.",
        "Step 4 (Infrastructure ➔ Adversary): WHOIS registrant details and SSL certificate fingerprints link the C2 domain to a known APT adversary."
    ])

    # ==========================================
    # SLIDE 16: 28.3.3 Attack Threading & Correlation
    # ==========================================
    s16 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s16, 16, TOTAL_SLIDES, "28.3 Diamond Model & Kill Chain • 28.3.3 Threading", "Attack Threading: Gadgets Inc. to Victim 2")
    add_notes(s16, """Attack threading correlates sequential Diamond Model events with the Cyber Kill Chain. In the Gadgets Inc. case study, the adversary vertically traverses the Kill Chain against Admin NA1. Once NA1 is compromised, the adversary pivots horizontally, using NA1's email contacts to spearphish the CRO of Victim 2 (Interesting Research Inc.) and configuring NA1 as a web proxy for data exfiltration.""")
    add_card(s16, Inches(0.6), Inches(1.4), Inches(5.8), Inches(5.3), "Vertical Kill Chain Traversal (Gadgets Inc.)", [
        "Phase 1: Adversary searches web for Gadgets Inc., discovering administrator email addresses from technical forums.",
        "Phase 2: Sends spearphishing email with malicious attachment to administrator NA1.",
        "Phase 3: NA1 opens the attachment, triggering exploit execution and backdoor installation.",
        "Phase 4: Compromised host sends outbound HTTP registration beacon to remote C2 server.",
        "Phase 5: Adversary establishes hands-on-keyboard persistence and access."
    ])
    add_card(s16, Inches(6.8), Inches(1.4), Inches(5.8), Inches(5.3), "Horizontal Pivoting to Victim 2", [
        "Contact Mining: Adversary mines NA1's Outlook contact list, discovering executive contacts at Interesting Research Inc.",
        "Secondary Campaign: Adversary sends spearphishing emails from NA1's trusted account to the Chief Risk Officer (CRO) of Victim 2.",
        "Compromising Victim 2: CRO opens the attachment; identical malware payload compromises Victim 2 host.",
        "Proxy Configuration: Adversary configures NA1's workstation as a web proxy to route and exfiltrate stolen research data from Victim 2.",
        "Simultaneous Compromise: Adversary successfully controls two separate organizations via a single initial intrusion."
    ])

    # ==========================================
    # SLIDE 17: 28.4.1 Establishing a CSIRC Capability
    # ==========================================
    s17 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s17, 17, TOTAL_SLIDES, "28.4 Incident Response • 28.4.1 CSIRC Capability", "Establishing a CSIRC: Policy, Plan, Procedures")
    add_notes(s17, """NIST SP 800-61r2 mandates three baseline governance documents to establish an Incident Response capability: Policy, Plan, and Procedures. Policy defines organizational authority and severity definitions. The Plan provides the roadmap and structure. Procedures define step-by-step technical standard operating procedures (SOPs).""")
    add_card(s17, Inches(0.6), Inches(1.4), Inches(3.85), Inches(5.3), "1. Policy Document", [
        "Defines organizational mission, authority, and executive sponsorship.",
        "Establishes incident severity definitions and mandatory reporting timelines.",
        "Grants CSIRC explicit authority to isolate hosts and seize equipment during a breach.",
        "Reviewed and approved by board leadership."
    ])
    add_card(s17, Inches(4.75), Inches(1.4), Inches(3.85), Inches(5.3), "2. Plan Document", [
        "High-level strategic roadmap for the organization's incident response capability.",
        "Defines team organizational structure, roles, and escalation hierarchy.",
        "Establishes performance metrics and executive communication protocols.",
        "Defines budget, training schedules, and technology architecture."
    ])
    add_card(s17, Inches(8.9), Inches(1.4), Inches(3.85), Inches(5.3), "3. Procedures (SOPs)", [
        "Detailed technical Standard Operating Procedures (SOPs).",
        "Step-by-step checklists for handling specific incident categories.",
        "Forensic acquisition guides, hashing protocols, and chain of custody forms.",
        "Updated regularly following post-incident lessons learned."
    ])

    # ==========================================
    # SLIDE 18: 28.4.3 Stakeholders & CMMC Maturity
    # ==========================================
    s18 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s18, 18, TOTAL_SLIDES, "28.4 Incident Response • 28.4.3 Stakeholders & CMMC", "IR Stakeholders & DoD CMMC Levels")
    add_notes(s18, """Incident response requires cross-functional coordination beyond technical staff: Management, IT Support, Legal, Public Relations, and Human Resources. The US Department of Defense Cybersecurity Maturity Model Certification (CMMC) defines 5 maturity levels: Level 2 requires establishing a plan; Level 3 requires testing capability; Level 4 incorporates threat intel and 24/7 SOC; Level 5 utilizes automated real-time response.""")
    add_card(s18, Inches(0.6), Inches(1.4), Inches(5.8), Inches(5.3), "Key Incident Response Stakeholders", [
        "Management: Ultimate financial and operational responsibility; approves business disruption decisions.",
        "IT Support: Implements technical containment, routes traffic, and re-images systems.",
        "Legal Department: Evaluates criminal prosecution options, regulatory reporting (HIPAA, GDPR), and liability.",
        "Public Relations (PR): Manages external press releases to protect organizational reputation.",
        "Human Resources: Handles disciplinary action if internal employees violate acceptable use policies."
    ])
    add_card(s18, Inches(6.8), Inches(1.4), Inches(5.8), Inches(5.3), "DoD CMMC IR Maturity Levels", [
        "Level 2: Establish a basic IR plan, track incidents, and respond using predefined standard procedures.",
        "Level 3: Test and validate capability via tabletop exercises; report incidents to required government stakeholders.",
        "Level 4: Leverage adversary TTP knowledge; operate a 24/7/365 Security Operations Center; track threat campaigns.",
        "Level 5: Utilize automated real-time response playbooks and advanced live memory forensic capabilities."
    ])

    # ==========================================
    # SLIDE 19: 28.4.4 NIST SP 800-61r2 Incident Life Cycle
    # ==========================================
    s19 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s19, 19, TOTAL_SLIDES, "28.4 Incident Response • 28.4.4 NIST Life Cycle", "NIST SP 800-61r2 Incident Life Cycle")
    add_notes(s19, """The NIST SP 800-61r2 Incident Response Life Cycle is a continuous 4-phase framework: 1. Preparation (tools, team, jump kits); 2. Detection & Analysis (attack vectors, validating alerts); 3. Containment, Eradication & Recovery (stopping damage, clean rebuilds); 4. Post-Incident Activity (lessons learned, evidence retention). Feedback loops between detection and preparation ensure defenses harden after every incident.""")
    add_card(s19, Inches(0.6), Inches(1.4), Inches(5.8), Inches(5.3), "The 4 Continuous Phases", [
        "Phase 1: Preparation - Building CSIRT team capability, assembling forensic jump kits, and hardening network defenses.",
        "Phase 2: Detection & Analysis - Monitoring attack vectors, evaluating precursors and IoCs, and assessing scope and severity.",
        "Phase 3: Containment, Eradication & Recovery - Limiting damage, removing adversary artifacts, and safely restoring systems.",
        "Phase 4: Post-Incident Activity - Conducting lessons learned meetings, retaining evidence, and updating policies.",
        "Continuous Feedback Loop: Post-incident findings feed directly back into Phase 1 to harden baseline defenses."
    ])
    add_card(s19, Inches(6.8), Inches(1.4), Inches(5.8), Inches(5.3), "Precursors vs. Indicators of Compromise", [
        "Precursors: Signs that an incident MAY occur in the future.",
        "Precursor Examples: Web server log showing port scanning; vulnerability announcements; phishing campaign targeting staff.",
        "Indicators (IoCs): Signs that an incident HAS OCCURRED or IS CURRENTLY occurring.",
        "Indicator Examples: Antivirus alert for ransomware; unusual outbound traffic to foreign IP; unexpected system reboot with modified system files.",
        "SOC Challenge: Analysts receive hundreds of false positives daily and must rapidly validate legitimate indicators."
    ])

    # ==========================================
    # SLIDE 20: Master Architecture 5 (NIST IR Diagram)
    # ==========================================
    add_diagram_slide(
        slide_num=20,
        total_slides=TOTAL_SLIDES,
        tag="28.4 Incident Response • Master Life Cycle Infographic",
        title="NIST SP 800-61r2: Incident Response Life Cycle",
        diag_file="1c0ca5b4-26dd-4eac-abb6-a4967573c9e2.jfif",
        cards_data=[
            ("Circular 4-Phase Life Cycle (28.4.4)", "Continuous loop: Preparation (team, jump kits) ➔ Detection & Analysis (vector matrix, validation) ➔ Containment, Eradication & Recovery (clean-up, restore) ➔ Post-Incident Activities (lessons learned)."),
            ("Capability & Stakeholders (28.4.1 - 28.4.3)", "Three baseline governance documents (Policy, Plan, Procedures); Cross-functional team (Management, IT, Legal, PR, HR); DoD CMMC maturity levels 2 to 5."),
            ("Operational Decision-Making (28.4.6 - 28.4.9)", "7 Attack vectors matrix; Containment dilemma (sudden disconnect vs. monitoring); Evidence retention determined by Prosecution, Data Type, and Cost.")
        ],
        notes_text="""This master architecture diagram represents NIST SP 800-61r2 Incident Response operations. In the center is the 4-phase circular life cycle: Preparation, Detection & Analysis, Containment/Eradication/Recovery, and Post-Incident Activities. Surrounding it are key operational requirements: Policy/Plan/Procedures (28.4.1), Stakeholders & CMMC maturity levels (28.4.3), Attack Vectors matrix (28.4.6), Containment strategy criteria (28.4.7), and Evidence retention factors (28.4.9)."""
    )

    # ==========================================
    # SLIDE 21: 28.4.5 & 28.4.6 Vectors & Jump Kits
    # ==========================================
    s21 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s21, 21, TOTAL_SLIDES, "28.4 Incident Response • 28.4.5 & 28.4.6 Vectors", "Preparation, Jump Kits & Attack Vectors")
    add_notes(s21, """Preparation includes maintaining forensic jump kits equipped with analysis laptops, packet sniffers, write-blockers, clean media, and documentation. NIST categorizes incidents across 7 primary attack vectors: Web, Email, Loss/Theft, Impersonation, Attrition (DDoS), Removable Media, and External Hardware.""")
    add_card(s21, Inches(0.6), Inches(1.4), Inches(5.8), Inches(5.3), "Forensic Jump Kit Hardware & Tools", [
        "Dedicated Laptop: Hardened machine pre-loaded with packet sniffers, memory acquisition tools, and forensic software suites.",
        "Hardware Write-Blockers: Forensic bridges preventing disk write operations during bit-level cloning.",
        "Clean Storage Media: Cryptographically wiped external SSDs and thumb drives for storing evidence images.",
        "Network Tap & Cables: Hardware taps, ethernet crossover cables, and patch cables for passive traffic sniffing.",
        "Documentation Supplies: Chain of custody forms, evidence tape, antistatic bags, and tamper-evident labels."
    ])
    add_card(s21, Inches(6.8), Inches(1.4), Inches(5.8), Inches(5.3), "7 NIST Common Attack Vectors", [
        "1. Web: Attacks launched from web applications, cross-site scripting (XSS), SQL injection, or drive-by downloads.",
        "2. Email: Phishing attacks, malicious attachments, or social engineering links.",
        "3. Loss or Theft: Stolen laptops, smartphones, or backup storage drives.",
        "4. Impersonation: Social engineering, spoofing, man-in-the-middle, or rogue access points.",
        "5. Attrition: Denial of Service (DoS/DDoS) exhausting network bandwidth or server resources.",
        "6. Removable Media: Malware executed from infected USB flash drives or external drives.",
        "7. External/Hardware: Exploiting hardware firmware or unauthorized physical network devices."
    ])

    # ==========================================
    # SLIDE 22: 28.4.7 Containment & Recovery
    # ==========================================
    s22 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s22, 22, TOTAL_SLIDES, "28.4 Incident Response • 28.4.7 Containment & Recovery", "Containment, Eradication & Recovery")
    add_notes(s22, """Containment limits the scope of an incident. Criteria include potential damage, evidence preservation, availability impact, and duration. Analysts face the Containment Dilemma: abruptly severing network access stops the bleeding, but alerts the attacker who may wipe files or destroy evidence. Subtle routing or DNS redirection maintains surveillance while mitigating risk. Eradication removes artifacts, while Recovery cleanly restores systems from verified backups.""")
    add_card(s22, Inches(0.6), Inches(1.4), Inches(5.8), Inches(5.3), "Containment Strategy & The Dilemma", [
        "Strategy Criteria: Potential damage, evidence preservation needs, service availability impact, time/resources required, and solution duration.",
        "The Containment Dilemma: Abruptly disconnecting an infected server halts immediate spread, but tips off the adversary.",
        "Adversary Counteraction: If alerted, an adversary may execute anti-forensic wiper scripts or detonate ransomware early.",
        "Subtle Containment: Redirecting C2 traffic to a honeynet sinkhole or restricting VLAN routing allows the SOC to monitor TTPs without alerting the intruder."
    ])
    add_card(s22, Inches(6.8), Inches(1.4), Inches(5.8), Inches(5.3), "Eradication & Recovery Operations", [
        "Eradication Tasks: Deleting malware binaries, disabling compromised user accounts, closing exploited vulnerabilities, and patching systems.",
        "Recovery Tasks: Restoring systems from clean, verified backups, rebuilding OS images, and changing all administrative passwords.",
        "Phased Restoration: Bringing critical business services online in controlled phases to verify integrity.",
        "Enhanced Monitoring: Operating high-frequency logging and continuous surveillance for 30+ days to ensure no dormant backdoors remain."
    ])

    # ==========================================
    # SLIDE 23: 28.4.8 Lessons Learned
    # ==========================================
    s23 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s23, 23, TOTAL_SLIDES, "28.4 Incident Response • 28.4.8 Lessons Learned", "Post-Incident: The 10 Review Questions")
    add_notes(s23, """A lessons learned meeting is held within two weeks of incident closure. It answers 10 fundamental questions: Exactly what happened and when? Did staff follow SOPs? Were procedures adequate? Was precursor information missed? What corrective actions prevent recurrence? What precursors/indicators should be monitored? What additional tools are needed? How to improve external sharing? What management support was required? What corrective steps will be taken?""")
    add_card(s23, Inches(0.6), Inches(1.4), Inches(5.8), Inches(5.3), "Post-Incident Meeting Purpose", [
        "Mandatory Review: Conducted within 2 weeks of major incident resolution while memories are fresh.",
        "Blameless Culture: Focuses on process improvement, tool effectiveness, and technical gaps rather than assigning personal blame.",
        "Documentation Outcome: Produces formal Incident Summary Report detailing chronological timeline and financial damage.",
        "Policy Evolution: Revisions made to SOPs, firewall rule baselines, and employee security training programs."
    ])
    add_card(s23, Inches(6.8), Inches(1.4), Inches(5.8), Inches(5.3), "The 10 NIST Review Questions", [
        "1. Exactly what happened, and at what times?",
        "2. How well did staff and management perform?",
        "3. Were documented procedures followed?",
        "4. Were procedures adequate to handle the attack?",
        "5. What information was needed sooner?",
        "6. Were any precursor indicators missed?",
        "7. What corrective actions prevent recurrence?",
        "8. What new indicators should be monitored?",
        "9. What additional tools or resources are needed?",
        "10. How can information sharing with external partners be improved?"
    ])

    # ==========================================
    # SLIDE 24: 28.4.9 Metrics & Evidence Retention
    # ==========================================
    s24 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s24, 24, TOTAL_SLIDES, "28.4 Incident Response • 28.4.9 Metrics & Retention", "Incident Data Metrics & Evidence Retention")
    add_notes(s24, """Incident data collection must be actionable. High incident counts can indicate flawed methodology or CSIRT incompetence, while low counts may mean improved defense or total absence of detection! Retention depends on 3 factors: Prosecution (retain until legal action concludes), Data Type (forensics kept 3+ years vs. routine logs for 90 days), and Cost (storage expenses and legacy hardware maintenance).""")
    add_card(s24, Inches(0.6), Inches(1.4), Inches(5.8), Inches(5.3), "Actionable Metrics & Assessment", [
        "Interpreting Counts: High incident counts may indicate flawed methodology or CSIRT incompetence; low counts may show great defense or lack of detection! Separate counts by incident category.",
        "Time Metrics: Total labor hours expended, duration of each phase, time to initial detection, and escalation speed.",
        "Objective Assessment (NIST): Checking adherence to SOPs, evaluating precursor logs, calculating financial damage, and comparing initial vs. final impact assessments.",
        "Subjective Assessment: Self-assessments, peer reviews, and resource owner satisfaction feedback."
    ])
    add_card(s24, Inches(6.8), Inches(1.4), Inches(5.8), Inches(5.3), "3 Determining Retention Factors", [
        "1. Prosecution: Retain all evidence until legal proceedings and appeals conclude (months or years). Evidence involved in ongoing litigation may never be destroyed.",
        "2. Data Type: Routine emails and transient files may be retained for 90 days, while incident response forensic images are typically retained for 3 years or longer.",
        "3. Cost: Long-term physical storage, secure warehouse facilities, and maintaining legacy hardware capable of reading outdated magnetic media become expensive over time."
    ])

    # ==========================================
    # SLIDE 25: 28.4.10 Information Sharing & VERIS
    # ==========================================
    s25 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s25, 25, TOTAL_SLIDES, "28.4 Incident Response • 28.4.10 Sharing & VERIS", "Reporting & NIST Sharing Rules")
    add_notes(s25, """Section 28.4.10 covers reporting and information sharing. NIST provides 5 critical recommendations: plan ahead, consult legal, share throughout the lifecycle, automate sharing, and balance benefits against sensitive disclosure risks. VERIS (Vocabulary for Event Recording and Incident Sharing) is an open framework categorizing incidents across 4 A's: Actors, Actions, Assets, and Attributes, powering the annual Verizon DBIR.""")
    add_card(s25, Inches(0.6), Inches(1.4), Inches(5.8), Inches(5.3), "NIST 5 Information Sharing Rules", [
        "1. Plan Coordination: Establish incident coordination relationships with external parties before incidents occur.",
        "2. Consult Legal: Consult with legal counsel before sharing data to protect proprietary rights and regulatory compliance.",
        "3. Share Throughout Life Cycle: Perform bi-directional information sharing across all 4 phases of incident handling.",
        "4. Automate Sharing: Automate threat indicator feeds (STIX/TAXII) to achieve machine-speed defensive updates.",
        "5. Balance Benefits vs. Risks: Balance the security benefits of sharing against the risk of disclosing sensitive corporate data."
    ])
    add_card(s25, Inches(6.8), Inches(1.4), Inches(5.8), Inches(5.3), "VERIS Framework & Community Threat Intel", [
        "VERIS Overview: Vocabulary for Event Recording and Incident Sharing — standardized schema for logging security incidents.",
        "Powers Verizon DBIR: Powers the annual Verizon Data Breach Investigations Report using anonymized incident contributions.",
        "The 4 A's of VERIS:",
        "  • Actors: Who was involved (Internal, External, Partner)?",
        "  • Actions: What did they do (Malware, Hacking, Social, Error)?",
        "  • Assets: What systems were affected (Server, User, Network)?",
        "  • Attributes: What security properties were compromised (C, I, A)?"
    ])

    # ==========================================
    # SLIDE 26: Summary & Exam Key Takeaways (Closing)
    # ==========================================
    s26 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s26, 26, TOTAL_SLIDES, "Module 28 • Summary & Review", "Summary: CyberOps Exam Takeaways", is_hero=True)
    add_notes(s26, """To summarize Module 28: Remember the RFC 3227 Volatility ladder, never examine original evidence without write-blockers and hashes, break the Cyber Kill Chain as early as possible, use the Diamond Model to pivot between adversary, capability, infrastructure, and victim, and follow the NIST 4-phase incident life cycle. Thank you from the University of Zululand Department of Computer Science!""")

    add_card(s26, Inches(0.6), Inches(1.75), Inches(5.8), Inches(4.2), "Forensics & Evidence Essentials", [
        "RFC 3227 Volatility: Registers ➔ RAM ➔ Temp ➔ Disks ➔ Logs ➔ Topology ➔ Archives.",
        "Golden Rule: Never examine original evidence; create verified bit-level copies with write-blockers.",
        "Chain of Custody: Complete chronological log; broken chains result in legal inadmissibility.",
        "MITRE ATT&CK: Tactics (Why/Goals) ➔ Techniques (How/Means) ➔ Procedures (Exact actions)."
    ])
    add_card(s26, Inches(6.8), Inches(1.75), Inches(5.8), Inches(4.2), "Kill Chain, Diamond & NIST IR", [
        "Cyber Kill Chain: 7 sequential stages; breaking any single link halts the campaign.",
        "Diamond Model: Adversary uses Capability over Infrastructure against Victim; enables pivoting.",
        "Attack Threading: Connecting vertical Kill Chain steps with horizontal multi-victim pivots.",
        "NIST 4-Phases: Preparation ➔ Detection & Analysis ➔ Containment/Recovery ➔ Post-Incident."
    ])

    # Closing banner box
    c_box = s26.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(6.1), Inches(12.1), Inches(0.75))
    c_box.fill.solid()
    c_box.fill.fore_color.rgb = NAVY
    c_box.line.color.rgb = GOLD
    c_box.line.width = Pt(1.5)
    ctf = c_box.text_frame
    cp = ctf.paragraphs[0]
    cp.alignment = PP_ALIGN.CENTER
    cp.text = "University of Zululand (UNIZULU) • Department of Computer Science • Cisco CyberOps Academy"
    cp.font.name = "Segoe UI"
    cp.font.size = Pt(13)
    cp.font.bold = True
    cp.font.color.rgb = GOLD_LIGHT

    out_file = "Module_28_Incident_Response_Models_UNIZULU.pptx"
    prs.save(out_file)
    print(f"PowerPoint Presentation generated successfully: {out_file} ({os.path.getsize(out_file)} bytes)")

if __name__ == '__main__':
    create_deck()
