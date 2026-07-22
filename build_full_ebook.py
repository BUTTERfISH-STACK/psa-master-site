import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable
)
from reportlab.lib import colors

def format_code(text):
    """Escapes HTML chars and preserves formatting for ReportLab Paragraphs."""
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('\n', '<br/>').replace(' ', '&nbsp;')

def build_pdf(filename="PSA_Master_Operating_Manual.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Base Cyberpunk / Minimalist Palette
    COLOR_CYAN = colors.HexColor('#0284c7')
    COLOR_BG_DARK = colors.HexColor('#0f172a')
    COLOR_TEXT_DARK = colors.HexColor('#1e293b')
    COLOR_GREEN = colors.HexColor('#059669')
    COLOR_MUTED = colors.HexColor('#64748b')

    title_style = ParagraphStyle(
        'CoverTitle', parent=styles['Title'],
        fontName='Helvetica-Bold', fontSize=24, leading=30,
        textColor=COLOR_CYAN, alignment=1, spaceAfter=15
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubtitle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=12, leading=16,
        textColor=COLOR_MUTED, alignment=1, spaceAfter=20
    )

    h1_style = ParagraphStyle(
        'H1', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=15, leading=19,
        textColor=COLOR_CYAN, spaceBefore=10, spaceAfter=8
    )

    h2_style = ParagraphStyle(
        'H2', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=12, leading=15,
        textColor=COLOR_TEXT_DARK, spaceBefore=8, spaceAfter=6
    )

    body_style = ParagraphStyle(
        'Body', parent=styles['BodyText'],
        fontName='Helvetica', fontSize=9.5, leading=14,
        textColor=COLOR_TEXT_DARK, spaceAfter=8
    )

    visual_style = ParagraphStyle(
        'VisualNote', parent=styles['Normal'],
        fontName='Helvetica-Oblique', fontSize=8.5, leading=12,
        textColor=colors.HexColor('#475569'), backColor=colors.HexColor('#f1f5f9'),
        borderPadding=8, spaceAfter=10, spaceBefore=5
    )

    code_style = ParagraphStyle(
        'Code', parent=styles['Code'],
        fontName='Courier', fontSize=8, leading=11,
        textColor=COLOR_GREEN, backColor=COLOR_BG_DARK,
        borderPadding=8, spaceAfter=10, spaceBefore=5
    )

    story = []

    # =========================================================================
    # COVER PAGE
    # =========================================================================
    story.append(Spacer(1, 120))
    story.append(Paragraph("POCKET STATE ARCHITECTURE (PSA™)", title_style))
    story.append(Paragraph("The Complete 20-Page Master Operating Manual", subtitle_style))
    story.append(HRFlowable(width="80%", thickness=2, color=COLOR_CYAN, spaceAfter=30))
    story.append(Paragraph("From Zero Mobile Unix Setup to Autonomous Local AI Agents & High-Margin Business Automation", subtitle_style))
    story.append(Spacer(1, 80))
    story.append(Paragraph("<b>Author & Architect:</b> Rean Van Aswegen<br/><b>Version:</b> 5.0 (Production Release)", subtitle_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 1
    # =========================================================================
    story.append(Paragraph("PAGE 1: Title, Attribution & Blueprint Overview", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_CYAN, spaceAfter=10))
    story.append(Paragraph("<b>Author & Architect:</b> Rean Van Aswegen", body_style))
    story.append(Paragraph("<b>Target Audience:</b> Developers, Automation Engineers, Mobile Technicians, and Agency Founders.", body_style))
    story.append(Paragraph(format_code("🎨 VISUAL LAYOUT:\n• Header: HUD matrix banner showing system telemetry (RAM: 3.2MB | SPEED: 0.4ms | DEPS: 0).\n• Central Graphic: Structural diagram mapping POSIX Core -> Native Termux Unix -> Local LLM Inference -> Zero-Overhead Infrastructure."), visual_style))
    story.append(Paragraph("Pocket State Architecture (PSA™) proves that you do not need expensive workstations, bloated server clusters, or third-party cloud APIs to build, compile, and execute enterprise-grade software.", body_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 2
    # =========================================================================
    story.append(Paragraph("PAGE 2: The PSA™ Manifesto & Philosophy", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_CYAN, spaceAfter=10))
    story.append(Paragraph("Why Modern Software Engineering Is Broken", h2_style))
    story.append(Paragraph("Modern web development has lost its way. Simple landing pages now ship with 200 MB of node_modules, multi-megabyte JavaScript bundles, and dozens of third-party cloud API dependencies.", body_style))
    story.append(Paragraph("This bloat creates severe vendor lock-in, fragile dependencies, high latency, and expensive monthly recurring bills.", body_style))
    story.append(Paragraph("The PSA™ Alternative", h2_style))
    story.append(Paragraph("PSA™ reverses this paradigm. Everything can be authored, compiled, executed, and monetized directly within a native mobile Unix environment (Termux) on a device that fits in your pocket.", body_style))
    story.append(Paragraph(format_code("TRADITIONAL STACK:\nReact/Next.js + Node + Webpack + Vercel = 250MB + $$$/mo\n\nVS\n\nPSA™ STACK:\nPOSIX Shell + Native HTML/CSS + Local AI = 18KB + $0/mo"), code_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 3
    # =========================================================================
    story.append(Paragraph("PAGE 3: POSIX Shell Core vs. Heavy Frameworks", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_CYAN, spaceAfter=10))
    story.append(Paragraph("Strip the Bloat, Keep the Speed", h2_style))
    story.append(Paragraph("At the heart of PSA™ is the POSIX State Core. Instead of relying on client-side JS virtual DOMs, state is managed in-memory using ultra-lightweight Unix environment maps and shell variables.", body_style))
    
    # Table for Page 3
    t3_data = [
        ['Metric', 'Traditional Stack', 'PSA™ POSIX System'],
        ['Initial Memory', '~150 MB - 500 MB', '< 4.0 MB'],
        ['HTTP Requests', '25 - 60 files', '1 Self-Contained File'],
        ['Lighthouse Score', '60 - 85 / 100', '100 / 100'],
        ['Execution Latency', '250ms - 1,200ms', '< 0.4ms'],
        ['Monthly Hosting', '$20 - $500+/mo', '$0.00 (Local/Self-Hosted)']
    ]
    t3 = Table(t3_data, colWidths=[130, 180, 180])
    t3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_BG_DARK),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1'))
    ]))
    story.append(t3)
    story.append(Spacer(1, 10))
    story.append(Paragraph(format_code("🎨 VISUAL LAYOUT:\nSide-by-side comparison featuring a bloated 200MB 'Node Monster' vs a razor-sharp 18KB 'POSIX Blade'."), visual_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 4
    # =========================================================================
    story.append(Paragraph("PAGE 4: Setting Up Your Pocket Workstation", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_CYAN, spaceAfter=10))
    story.append(Paragraph("Preparing the Mobile Unix Environment", h2_style))
    story.append(Paragraph("To start building with PSA™, transform your mobile smartphone into a full terminal workstation using Termux.", body_style))
    story.append(Paragraph(format_code("# 1. Update core system packages\npkg update && pkg upgrade -y\n\n# 2. Install essential POSIX utilities & dev tools\npkg install -y bash git curl wget jq python clang micro\n\n# 3. Grant storage permissions for persistent local builds\ntermux-setup-storage\n\n# 4. Verify native build environment\nuname -m # Returns aarch64 / arm64"), code_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 5
    # =========================================================================
    story.append(Paragraph("PAGE 5: The POSIX In-Memory State Engine", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_CYAN, spaceAfter=10))
    story.append(Paragraph("Pure Shell State Management", h2_style))
    story.append(Paragraph("Below is a pure, zero-dependency POSIX state engine pattern used to manage dynamic application state without heavy database servers:", body_style))
    story.append(Paragraph(format_code("#!/usr/bin/env bash\n# PSA™ CORE STATE CONTROLLER\n\ndeclare -A GLOBAL_STATE\n\nstate_set() {\n    local key=\"$1\"\n    local val=\"$2\"\n    GLOBAL_STATE[\"$key\"]=\"$val\"\n    echo \"[STATE UPDATE] $key -> $val\"\n}\n\nstate_get() {\n    local key=\"$1\"\n    echo \"${GLOBAL_STATE[\"$key\"]}\"\n}\n\nstate_set \"APP_NAME\" \"PSA Master Engine\"\nstate_set \"STATUS\" \"ONLINE\"\necho \"Current System Name: $(state_get \"APP_NAME\")\""), code_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 6
    # =========================================================================
    story.append(Paragraph("PAGE 6: Zero-Bloat Web Asset Compilation", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_CYAN, spaceAfter=10))
    story.append(Paragraph("How to Build 100/100 Lighthouse Web Shells", h2_style))
    story.append(Paragraph("Instead of using complex bundlers (Vite, Webpack), PSA™ uses single-file shell compilers (build.sh) that inline dynamic templates, atomic CSS styling, and client interaction modules into one ultra-compressed HTML payload.", body_style))
    story.append(Paragraph(format_code("Shell Compiler (build.sh)\n   │\n   ├──► Inline Atomic CSS\n   ├──► Minimal JavaScript\n   └──► POSIX State Map\n   │\n   ▼\nindex.html (18 KB Output Payload)"), code_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 7
    # =========================================================================
    story.append(Paragraph("PAGE 7: Hands-On Tutorial – Building Your First App", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_CYAN, spaceAfter=10))
    story.append(Paragraph("Single-Script Dynamic Site Compiler", h2_style))
    story.append(Paragraph("Create an executable file named compile_site.sh to output complete web structures:", body_style))
    story.append(Paragraph(format_code("#!/usr/bin/env bash\n# Compile a complete, responsive landing page in < 50ms\n\ncat << 'EOF' > index.html\n<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <title>PSA Powered Site</title>\n    <style>\n        body { background: #07090e; color: #f8fafc; font-family: system-ui; padding: 2rem; }\n        .card { background: #0f172a; border: 1px solid #38bdf8; padding: 1.5rem; border-radius: 12px; }\n    </style>\n</head>\n<body>\n    <div class=\"card\">\n        <h1>Compiled via PSA™</h1>\n        <p>Built directly on a smartphone terminal. Zero dependencies.</p>\n    </div>\n</body>\n</html>\nEOF\necho \"[✓] Site compiled cleanly to index.html!\""), code_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 8
    # =========================================================================
    story.append(Paragraph("PAGE 8: Local AI Integration (Ollama & Llama 3)", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_CYAN, spaceAfter=10))
    story.append(Paragraph("Private, Offline Machine Intelligence", h2_style))
    story.append(Paragraph("PSA™ integrates directly with local quantized LLM backends running on device or local networks using Ollama.", body_style))
    story.append(Paragraph(format_code("Smartphone (Termux Terminal)\n  │\n  ├──► POSIX Bash Pipeline\n  │     │\n  │     ▼ (Local HTTP REST / Port 11434)\n  └──► Local Ollama Engine (Llama 3 8B Quantized)\n        │\n        ▼\n   100% Offline AI Responses (0 Cloud Token Costs)"), code_style))
    story.append(Paragraph(format_code("# Pull and test a lightweight quantized Llama model\nollama run llama3:8b-instruct-q4_K_M"), code_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 9
    # =========================================================================
    story.append(Paragraph("PAGE 9: Connecting Shell Pipelines to AI Endpoints", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_CYAN, spaceAfter=10))
    story.append(Paragraph("Streaming Local AI Insights with curl & jq", h2_style))
    story.append(Paragraph("Write automated shell scripts that query your local AI model without cloud API keys or external billing:", body_style))
    story.append(Paragraph(format_code("#!/usr/bin/env bash\n# Query Local Ollama LLM directly from Bash\n\nPROMPT=\"Summarize the key benefits of Pocket State Architecture in 3 points.\"\n\ncurl -s http://localhost:11434/api/generate -d \"{\n  \\\"model\\\": \\\"llama3\\\",\n  \\\"prompt\\\": \\\"$PROMPT\\\",\n  \\\"stream\\\": false\n}\" | jq -r '.response'"), code_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 10
    # =========================================================================
    story.append(Paragraph("PAGE 10: Building Autonomous Local AI Agents", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_CYAN, spaceAfter=10))
    story.append(Paragraph("Multi-Step Decision-Making Agents", h2_style))
    story.append(Paragraph("By pairing local LLM pipelines with Unix loop controllers, you can construct autonomous agents that complete multi-step tasks independently:", body_style))
    story.append(Paragraph(format_code("PSA™ AGENT LOOP:\n1. Read Inputs ──► 2. Prompt Local Llama\n       ▲                   │\n       │                   ▼\n4. Update State ◄── 3. Execute POSIX Command"), code_style))
    story.append(Paragraph("<b>Key Applications:</b><br/>• Auto-Lead Qualifier: Scans email text, scores intent via local LLM, and logs leads.<br/>• Auto-Code Auditor: Inspects local shell scripts and generates optimization patches.", body_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 11
    # =========================================================================
    story.append(Paragraph("PAGE 11: Automated Document & PDF Compilers", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_CYAN, spaceAfter=10))
    story.append(Paragraph("Volume eBook & Report Generation", h2_style))
    story.append(Paragraph("PSA™ shines at converting markdown files, state variables, and dynamic content into beautifully formatted PDF manuals, invoices, and eBooks.", body_style))
    story.append(Paragraph(format_code("# Automated PDF compilation pipeline\npkg install -y pandoc weasyprint\n\n# Compile markdown source into a styled master PDF document\npandoc manual_source.md -o PSA_Master_Guide.pdf \\\n    --pdf-engine=weasyprint \\\n    --metadata title=\"PSA™ Operating Guide\""), code_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 12
    # =========================================================================
    story.append(Paragraph("PAGE 12: High-Performance Data Processing & Crons", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_CYAN, spaceAfter=10))
    story.append(Paragraph("Background Workflows on Mobile Unix", h2_style))
    story.append(Paragraph("Turn your pocket device into an active automation server using crontab and background job management.", body_style))
    story.append(Paragraph(format_code("# Edit crontab schedules\ncrontab -e\n\n# Run automated system check & backup every morning at 08:00 AM\n0 8 * * * /data/data/com.termux/files/home/psa/compile_daily_report.sh"), code_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 13
    # =========================================================================
    story.append(Paragraph("PAGE 13: The Agency Blueprint – Monetizing PSA™", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_CYAN, spaceAfter=10))
    story.append(Paragraph("Turning Zero-Overhead Tech into Revenue", h2_style))
    story.append(Paragraph("PSA™ isn't just an architectural framework; it is a high-margin agency business engine.", body_style))
    story.append(Paragraph("Traditional agencies spend thousands on cloud hosting, serverless compute, and databases. With PSA™:<br/>• <b>Infrastructure Cost:</b> ~$0.00 / month.<br/>• <b>Client Retainer Fee:</b> $500 - $2,500 / month.<br/>• <b>Gross Profit Margin:</b> 95% - 99%.", body_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 14
    # =========================================================================
    story.append(Paragraph("PAGE 14: Monetization Pillar 1 – Autonomous AI Agents", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_CYAN, spaceAfter=10))
    story.append(Paragraph("Client Service: $1,500 Setup + $500/mo Retainer", h2_style))
    story.append(Paragraph("Build custom, offline AI support and lead capture bots for local businesses (contractors, clinics, real estate, law firms).", body_style))
    story.append(Paragraph(format_code("CLIENT AI AGENT BOT OFFER:\n• 100% Local Data Privacy (No customer data leaves the premises)\n• Zero external API token fees (Fixed hosting cost = $0)\n• Instant response latency with zero cloud dependency"), visual_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 15
    # =========================================================================
    story.append(Paragraph("PAGE 15: Monetization Pillar 2 – Ultra-Fast Client Funnels", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_CYAN, spaceAfter=10))
    story.append(Paragraph("Client Service: $1,000 – $3,000 per Site Build", h2_style))
    story.append(Paragraph("Small businesses lose leads because standard WordPress or React sites take 4–6 seconds to load.", body_style))
    story.append(Paragraph("Deliver single-script PSA™ web platforms that:<br/>1. Load in under <b>15ms</b>.<br/>2. Score <b>100/100</b> on Google Lighthouse Mobile benchmarks.<br/>3. Include built-in local lead logging and automated webhooks.", body_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 16
    # =========================================================================
    story.append(Paragraph("PAGE 16: Monetization Pillar 3 – Business Automation", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_CYAN, spaceAfter=10))
    story.append(Paragraph("Client Service: $2,000 Upfront + $750/mo Retainer", h2_style))
    story.append(Paragraph("Automate manual data entry, PDF invoice generation, and customer onboarding pipelines for business clients using background POSIX scripts.", body_style))
    story.append(Paragraph("<b>Deliverables:</b><br/>• Automated Invoice Generators: Outputs branded PDF invoices from weekly logs.<br/>• Local CRM Sync Engine: Consolidates lead inputs into unified dashboards.", body_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 17
    # =========================================================================
    story.append(Paragraph("PAGE 17: Packaging & Scaling Recurring Retainers", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_CYAN, spaceAfter=10))
    story.append(Paragraph("The $10,000/Month Pocket Agency Model", h2_style))
    story.append(Paragraph("By scaling retainers across multiple clients, you build predictable recurring revenue with virtually no software hosting expenses.", body_style))
    
    t17_data = [
        ['Deliverable Included in Retainer', 'Cost to Agency', 'Client Value'],
        ['Local AI Maintenance & Fine-Tuning', '$0.00', '$800 / mo'],
        ['Automated Backup & System Audit', '$0.00', '$300 / mo'],
        ['High-Speed Web Hosting & State Engine', '$0.00', '$400 / mo'],
        ['Total Monthly Package Value', '$0.00', '$1,500 / mo']
    ]
    t17 = Table(t17_data, colWidths=[200, 140, 150])
    t17.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_BG_DARK),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1'))
    ]))
    story.append(t17)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 18
    # =========================================================================
    story.append(Paragraph("PAGE 18: Security, Local Data Isolation, & Air-Gapping", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_CYAN, spaceAfter=10))
    story.append(Paragraph("Total Enterprise-Grade Data Privacy", h2_style))
    story.append(Paragraph("Because PSA™ operates completely offline and within localized Unix nodes, it satisfies strict data privacy requirements (GDPR, POPIA, HIPAA).", body_style))
    story.append(Paragraph("• <b>Zero Cloud Leakage:</b> Client telemetry stays locked inside private local storage.<br/>• <b>Air-Gapped Execution:</b> System executes full AI workflows even without an active internet connection.", body_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 19
    # =========================================================================
    story.append(Paragraph("PAGE 19: The Master PSA™ Executable Script", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_CYAN, spaceAfter=10))
    story.append(Paragraph("The Complete Production Builder Script", h2_style))
    story.append(Paragraph(format_code("#!/usr/bin/env bash\n# PSA™ MASTER PRODUCTION SYSTEM COMPILER\n# Creator: Rean Van Aswegen\n\nOUTPUT=\"psa_production.html\"\ncat << 'EOF' > \"$OUTPUT\"\n<!DOCTYPE html>\n<html>\n<head>\n    <title>PSA™ Master Engine</title>\n    <style>\n        body { background: #07090e; color: #f8fafc; font-family: sans-serif; text-align: center; }\n        .badge { background: rgba(16, 185, 129, 0.2); color: #10b981; padding: 4px 12px; border-radius: 99px; }\n    </style>\n</head>\n<body>\n    <span class=\"badge\">SYSTEM READY</span>\n    <h1>Pocket State Architecture</h1>\n</body>\n</html>\nEOF\necho \"[✓] Master Build Complete: $OUTPUT\""), code_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 20
    # =========================================================================
    story.append(Paragraph("PAGE 20: Conclusion & The Future of Mobile-First Systems", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_CYAN, spaceAfter=10))
    story.append(Paragraph("Who Makes It Possible & What Comes Next", h2_style))
    story.append(Paragraph("Pocket State Architecture (PSA™) was engineered and pioneered by <b>Rean Van Aswegen</b> to eliminate software engineering bloat and prove that world-class, high-margin software systems can be built and operated from anywhere in the world—using nothing more than a smartphone and a vision.", body_style))
    story.append(Paragraph("As AI models get smaller, faster, and more efficient, the future belongs to those who control lightweight, local, and autonomous systems. You now hold the complete blueprint.", body_style))
    story.append(Spacer(1, 20))
    story.append(Paragraph(format_code("=========================================================\nPOCKET STATE ARCHITECTURE (PSA™) - OPERATIONAL SYSTEM\nDESIGNED, ENGINEERED & AUTHORED BY REAN VAN ASWEGEN\n========================================================="), code_style))

    doc.build(story)
    print("[✓] SUCCESS: Full 20-Page Manual compiled cleanly to PSA_Master_Operating_Manual.pdf")

if __name__ == '__main__':
    build_pdf()
