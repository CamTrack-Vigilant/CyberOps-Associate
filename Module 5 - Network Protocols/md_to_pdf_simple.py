#!/usr/bin/env python3
"""Convert markdown study guide to PDF using fpdf2"""
import sys
import traceback
import unicodedata

def clean_text(text):
    """Remove or replace non-ASCII characters with ASCII equivalents"""
    # Replace common special Unicode characters
    replacements = {
        '—': '-',      # em dash
        '–': '-',      # en dash
        ''': "'",      # right single quote
        ''': "'",      # left single quote
        '"': '"',      # left double quote
        '"': '"',      # right double quote
        '•': '*',      # bullet
        '…': '...',    # ellipsis
        '≠': '!=',     # not equal
        '≥': '>=',     # greater than or equal
        '≤': '<=',     # less than or equal
        '×': 'x',      # multiplication sign
        '÷': '/',      # division sign
        'é': 'e',
        'è': 'e',
        'ê': 'e',
        'ë': 'e',
        'á': 'a',
        'à': 'a',
        'â': 'a',
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    # Remove any remaining non-ASCII characters
    text = ''.join(c if ord(c) < 128 else '?' for c in text)
    return text

try:
    from fpdf import FPDF
    import re
    from pathlib import Path
    
    # Read the markdown file
    md_file = Path(__file__).parent / "STUDY_GUIDE.md"
    pdf_file = Path(__file__).parent / "STUDY_GUIDE.pdf"
    
    print(f"[1] Reading: {md_file}", flush=True)
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    print(f"[2] Loaded {len(md_content)} characters", flush=True)
    
    # Create PDF
    print("[3] Creating PDF object", flush=True)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=10)
    
    # Add title
    print("[4] Adding title", flush=True)
    pdf.set_font("Helvetica", "B", size=16)
    title = "Module 5 - Network Protocols Study Guide"
    pdf.multi_cell(0, 8, title, new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(5)
    
    # Process markdown content
    print("[5] Processing content", flush=True)
    lines = md_content.split('\n')
    line_count = 0
    
    for line in lines:
        line_stripped = line.strip()
        
        # Skip empty lines
        if not line_stripped:
            pdf.ln(2)
            continue
        
        line_count += 1
        
        # Headers - level 1
        if line_stripped.startswith('# '):
            pdf.set_font("Helvetica", "B", size=14)
            text = line_stripped[2:].strip()
            text = clean_text(text)
            pdf.multi_cell(0, 6, text, new_x="LMARGIN", new_y="NEXT")
            pdf.ln(2)
            pdf.set_font("Helvetica", size=10)
            
        # Headers - level 2
        elif line_stripped.startswith('## '):
            pdf.set_font("Helvetica", "B", size=12)
            text = line_stripped[3:].strip()
            text = clean_text(text)
            pdf.multi_cell(0, 6, text, new_x="LMARGIN", new_y="NEXT")
            pdf.ln(1)
            pdf.set_font("Helvetica", size=10)
            
        # Headers - level 3
        elif line_stripped.startswith('### '):
            pdf.set_font("Helvetica", "B", size=11)
            text = line_stripped[4:].strip()
            text = clean_text(text)
            pdf.multi_cell(0, 5, text, new_x="LMARGIN", new_y="NEXT")
            pdf.set_font("Helvetica", size=10)
            
        # Headers - level 4
        elif line_stripped.startswith('#### '):
            pdf.set_font("Helvetica", "B", size=10)
            text = line_stripped[5:].strip()
            text = clean_text(text)
            pdf.multi_cell(0, 5, text, new_x="LMARGIN", new_y="NEXT")
            pdf.set_font("Helvetica", size=10)
            
        # Horizontal lines
        elif line_stripped.startswith('---'):
            pdf.ln(1)
            
        # Bullet points
        elif line_stripped.startswith('- ') or line_stripped.startswith('* '):
            text = line_stripped[2:].strip()
            # Clean markdown syntax
            text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
            text = re.sub(r'`(.*?)`', r'\1', text)
            text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
            text = clean_text(text)
            
            pdf.multi_cell(0, 4, "- " + text, new_x="LMARGIN", new_y="NEXT")
            
        # Code blocks
        elif line_stripped.startswith('```'):
            continue
            
        # Tables (simplified - just show as text for now)
        elif line_stripped.startswith('|'):
            continue
            
        # Regular text
        else:
            # Clean markdown syntax
            text = line_stripped
            text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
            text = re.sub(r'_(.*?)_', r'\1', text)
            text = re.sub(r'`(.*?)`', r'\1', text)
            text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
            text = clean_text(text)
            
            if text:
                pdf.set_font("Helvetica", size=10)
                pdf.multi_cell(0, 4, text, new_x="LMARGIN", new_y="NEXT")
    
    print(f"[6] Processed {line_count} lines", flush=True)
    
    # Save PDF
    print(f"[7] Saving PDF", flush=True)
    pdf.output(str(pdf_file))
    
    file_size = Path(pdf_file).stat().st_size / 1024
    print(f"[SUCCESS] PDF created: {pdf_file}")
    print(f"[INFO] File size: {file_size:.1f} KB")
    sys.exit(0)
    
except Exception as e:
    print(f"[ERROR] {type(e).__name__}: {str(e)}", flush=True)
    traceback.print_exc()
    sys.exit(1)
