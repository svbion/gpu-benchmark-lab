#!/usr/bin/env python3
from pathlib import Path
import re
import sys

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

ROOT = Path(__file__).resolve().parents[1]
REPORTS = [
    ('docs/reports/EXECUTIVE_SUMMARY.md', 'docs/reports/pdf/EXECUTIVE_SUMMARY.pdf'),
    ('docs/reports/INFRASTRUCTURE_REPORT.md', 'docs/reports/pdf/INFRASTRUCTURE_REPORT.pdf'),
    ('docs/reports/GPU_INVENTORY_REPORT.md', 'docs/reports/pdf/GPU_INVENTORY_REPORT.pdf'),
    ('docs/reports/CUSTOMER_VALIDATION_REPORT.md', 'docs/reports/pdf/CUSTOMER_VALIDATION_REPORT.pdf'),
    ('docs/reports/MANAGEMENT_REPORT.md', 'docs/reports/pdf/MANAGEMENT_REPORT.pdf'),
]

def clean_inline(text: str) -> str:
    text = re.sub(r'`([^`]+)`', r'<font name="Courier">\1</font>', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1', text)
    text = text.replace('&', '&amp;').replace('<font name=&quot;', '<font name="')
    text = text.replace('&lt;font name="Courier"&gt;', '<font name="Courier">').replace('&lt;/font&gt;', '</font>')
    return text

def parse(md_text: str, styles):
    story = []
    in_code = False
    code_lines = []
    table_lines = []

    def flush_code():
        nonlocal code_lines
        if code_lines:
            story.append(Paragraph('<br/>'.join(line.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;') for line in code_lines), styles['CodeBlock']))
            story.append(Spacer(1, 0.12 * inch))
            code_lines = []

    def flush_table():
        nonlocal table_lines
        if table_lines:
            rows = []
            for line in table_lines:
                cells = [clean_inline(c.strip()) for c in line.strip().strip('|').split('|')]
                if cells and not all(set(c) <= set(':- ') for c in cells):
                    rows.append(cells)
            if rows:
                col_count = max(len(r) for r in rows)
                rows = [r + [''] * (col_count - len(r)) for r in rows]
                tbl = Table(rows, repeatRows=1)
                tbl.setStyle(TableStyle([
                    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0c1424')),
                    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
                    ('GRID', (0,0), (-1,-1), 0.25, colors.HexColor('#9fb0c5')),
                    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0,0), (-1,-1), 8),
                    ('VALIGN', (0,0), (-1,-1), 'TOP'),
                    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f4f7fb')]),
                ]))
                story.append(tbl)
                story.append(Spacer(1, 0.16 * inch))
            table_lines = []

    for raw in md_text.splitlines():
        line = raw.rstrip()
        if line.startswith('```'):
            if in_code:
                in_code = False
                flush_code()
            else:
                flush_table()
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue
        if line.startswith('|'):
            table_lines.append(line)
            continue
        flush_table()
        if not line.strip():
            story.append(Spacer(1, 0.10 * inch))
            continue
        if line.startswith('> '):
            story.append(Paragraph(clean_inline(line[2:]), styles['Quote']))
        elif line.startswith('# '):
            story.append(Paragraph(clean_inline(line[2:]), styles['Title']))
            story.append(Spacer(1, 0.18 * inch))
        elif line.startswith('## '):
            story.append(Paragraph(clean_inline(line[3:]), styles['Heading1']))
        elif line.startswith('### '):
            story.append(Paragraph(clean_inline(line[4:]), styles['Heading2']))
        elif line.startswith('- '):
            story.append(Paragraph('• ' + clean_inline(line[2:]), styles['Bullet']))
        elif re.match(r'\d+\. ', line):
            story.append(Paragraph(clean_inline(line), styles['Bullet']))
        else:
            story.append(Paragraph(clean_inline(line), styles['BodyText']))
    flush_code()
    flush_table()
    return story

def build_pdf(src: Path, dst: Path):
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Quote', parent=styles['BodyText'], textColor=colors.HexColor('#526173'), leftIndent=12, borderColor=colors.HexColor('#76ff03'), borderWidth=1, borderPadding=6, spaceAfter=8))
    styles.add(ParagraphStyle(name='CodeBlock', parent=styles['Code'], fontName='Courier', fontSize=8, leading=10, backColor=colors.HexColor('#f4f7fb'), borderPadding=6, spaceAfter=8))
    styles['Title'].fontName = 'Helvetica-Bold'
    styles['Title'].textColor = colors.HexColor('#0c1424')
    styles['Heading1'].textColor = colors.HexColor('#10233b')
    styles['Heading2'].textColor = colors.HexColor('#10233b')
    styles['BodyText'].leading = 12
    styles['Bullet'].leftIndent = 14
    styles['Bullet'].firstLineIndent = -8
    dst.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(dst), pagesize=letter, rightMargin=0.65*inch, leftMargin=0.65*inch, topMargin=0.65*inch, bottomMargin=0.65*inch, title=src.stem.replace('_',' ').title())
    story = parse(src.read_text(encoding='utf-8'), styles)
    doc.build(story)

for src_rel, dst_rel in REPORTS:
    src = ROOT / src_rel
    dst = ROOT / dst_rel
    build_pdf(src, dst)
    print(f'Regenerated {dst.relative_to(ROOT)} from {src.relative_to(ROOT)}')
