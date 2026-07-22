import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, HRFlowable
from reportlab.lib import colors

def create_psa_pdf(filename="PSA_Master_Operating_Manual.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Cyber/Minimalist Styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Title'],
        fontName='Helvetica-Bold',
        fontSize=26,
        leading=32,
        textColor=colors.HexColor('#38bdf8'),
        alignment=1,
        spaceAfter=15
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=13,
        leading=18,
        textColor=colors.HexColor('#94a3b8'),
        alignment=1,
        spaceAfter=30
    )
    
    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#38bdf8'),
        spaceBefore=15,
        spaceAfter=10
    )
    
    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=10,
        leading=15,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=10
    )

    code_style = ParagraphStyle(
        'CodeBlock',
        parent=styles['Code'],
        fontName='Courier',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#10b981'),
        backColor=colors.HexColor('#07090e'),
        borderPadding=8,
        spaceAfter=12
    )

    story = []

    # COVER PAGE
    story.append(Spacer(1, 100))
    story.append(Paragraph("POCKET STATE ARCHITECTURE (PSA™)", title_style))
    story.append(Paragraph("The Complete 20-Page Master Operating Manual", subtitle_style))
    story.append(HRFlowable(width="80%", thickness=2, color=colors.HexColor('#38bdf8'), spaceAfter=30))
    story.append(Paragraph("<b>Author & Architect:</b> Rean Van Aswegen<br/><b>Version:</b> 5.0 Production Release", subtitle_style))
    story.append(PageBreak())

    # PAGES 1 TO 20 CONTENT
    pages_content = [
        ("PAGE 1: Title & Architectural Blueprint", "Pocket State Architecture (PSA™) proves that production-grade software, offline AI networks, and high-margin business pipelines can be built and operated directly inside a native mobile Unix workstation."),
        ("PAGE 2: The PSA™ Manifesto", "Modern web development is broken by bloated node_modules and fragile cloud dependencies. PSA™ replaces multi-megabyte frameworks with 18KB POSIX shell scripts."),
        ("PAGE 3: POSIX Core vs. Heavy Frameworks", "By eliminating virtual DOM overhead, PSA™ achieves sub-millisecond execution speeds, 100/100 Lighthouse performance, and near-zero infrastructure costs."),
        ("PAGE 4: Workstation Setup", "Setting up Termux:\npkg update && pkg upgrade -y\npkg install -y bash git curl jq python clang"),
        ("PAGE 5: In-Memory State Engine", "State management is handled via native environment variables and key-value shell arrays rather than heavy database daemons."),
        ("PAGE 6: Zero-Bloat Asset Compilation", "Single-script compilers inline dynamic templates, atomic styling, and DOM interactions into a single atomic payload."),
        ("PAGE 7: Practical Project - Dynamic Site Compiler", "Executing build scripts directly on-device generates high-conversion landing pages in under 50ms."),
        ("PAGE 8: Local AI Integration (Ollama)", "Connect shell tools to local quantized LLMs (Llama 3 8B) via REST endpoints on port 11434 for 100% offline, privacy-first inference."),
        ("PAGE 9: Shell Pipelines to AI Endpoints", "Stream local AI insights directly into JSON pipelines using curl and jq without cloud API tokens or recurring monthly fees."),
        ("PAGE 10: Autonomous Local AI Agents", "Combine POSIX loop controllers with local LLMs to construct self-correcting agents for lead scoring, code audits, and data extraction."),
        ("PAGE 11: Document & Report Compilers", "Automate PDF generation and invoice compilation directly from markdown files using background POSIX jobs."),
        ("PAGE 12: High-Performance Data Crons", "Schedule background cron workflows to execute continuous system telemetry and local data backups."),
        ("PAGE 13: The Agency Blueprint", "Leverage zero-overhead architecture to build high-margin software agencies operating at 95%+ gross profit margins."),
        ("PAGE 14: Monetization Pillar 1 - AI Agents", "Deploy private, air-gapped local AI agent workflows for local business clients on retainer."),
        ("PAGE 15: Monetization Pillar 2 - Ultra-Fast Funnels", "Replace slow, bloated client websites with 100/100 Lighthouse POSIX web shells."),
        ("PAGE 16: Monetization Pillar 3 - Business Automation", "Sell custom background script pipelines that handle dynamic invoice generation and CRM synchronization."),
        ("PAGE 17: Retainer Packaging & Scaling", "Scale recurring $1,000/mo retainer packages across clients with $0.00 infrastructure overhead."),
        ("PAGE 18: Enterprise Data Privacy & Security", "Maintain complete compliance with POPIA, GDPR, and HIPAA by keeping all data local and air-gapped."),
        ("PAGE 19: The Master Production Compiler", "Run unified master scripts to compile dynamic client dashboards instantly."),
        ("PAGE 20: Conclusion & Future Outlook", "Engineered and authored by Rean Van Aswegen. The future of software belongs to lightweight, autonomous, mobile-first systems.")
    ]

    for title, body in pages_content:
        story.append(Paragraph(title, h1_style))
        story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cbd5e1'), spaceAfter=10))
        story.append(Paragraph(body, body_style))
        story.append(Spacer(1, 15))
        story.append(Paragraph("<code># PSA-SYSTEM-NODE-ACTIVE // PORT: 11434</code>", code_style))
        story.append(PageBreak())

    doc.build(story)
    print("[✓] SUCCESS: eBook compiled to PSA_Master_Operating_Manual.pdf")

if __name__ == '__main__':
    create_psa_pdf()
