#!/usr/bin/env python3
"""Convert markdown study guide to PDF using fpdf2"""
from fpdf import FPDF
import re
from pathlib import Path

# Read the markdown file
md_file = Path(__file__).parent / "STUDY_GUIDE.md"
pdf_file = Path(__file__).parent / "STUDY_GUIDE.pdf"

print(f"Reading: {md_file}")
with open(md_file, 'r', encoding='utf-8') as f:
    md_content = f.read()

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=11)

# Add title
pdf.set_font("Helvetica", "B", size=16)
pdf.cell(0, 10, "Module 5 - Network Protocols Study Guide", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.set_font("Helvetica", size=11)
pdf.ln(10)

# Process markdown content
lines = md_content.split('\n')
in_code = False
in_table = False
buffer = []

def flush_buffer():
    """Flush accumulated text"""
    global buffer
    if buffer:
        text = '\n'.join(buffer).strip()
        if text:
            # Clean up markdown syntax
            text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # Bold
            text = re.sub(r'\*(.*?)\*', r'\1', text)      # Italic
            text = re.sub(r'`(.*?)`', r'\1', text)        # Code
            text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)  # Links
            text = text.replace('•', '*')  # Replace bullet with asterisk
            pdf.multi_cell(0, 5, text)
        buffer = []

for line in lines:
    # Headers
    if line.startswith('# '):
        flush_buffer()
        pdf.set_font("Helvetica", "B", size=14)
        pdf.cell(0, 10, line[2:], new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", size=11)
        pdf.ln(2)
    elif line.startswith('## '):
        flush_buffer()
        pdf.set_font("Helvetica", "B", size=12)
        pdf.cell(0, 10, line[3:], new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", size=11)
        pdf.ln(1)
    elif line.startswith('### '):
        flush_buffer()
        pdf.set_font("Helvetica", "B", size=11)
        pdf.cell(0, 8, line[4:], new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", size=11)
    elif line.startswith('#### '):
        flush_buffer()
        pdf.set_font("Helvetica", "B", size=10)
        pdf.cell(0, 7, line[5:], new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", size=11)
    elif line.startswith('```'):
        flush_buffer()
        in_code = not in_code
    elif line.startswith('---'):
        flush_buffer()
        pdf.ln(2)
    elif line.startswith('- ') or line.startswith('* '):
        flush_buffer()
        pdf.cell(5, 5, "*")
        pdf.multi_cell(0, 5, line[2:])
    elif line.startswith('|'):
        in_table = True
        buffer.append(line)
    elif line.strip() == '':
        if buffer and not in_table:
            flush_buffer()
    else:
        if in_code:
            pdf.set_font("Courier", size=9)
            pdf.multi_cell(0, 4, line.replace('•', '*'))
            pdf.set_font("Helvetica", size=11)
        else:
            buffer.append(line)

flush_buffer()

# Save PDF
pdf.output(pdf_file)
print(f"✓ PDF created successfully: {pdf_file}")
