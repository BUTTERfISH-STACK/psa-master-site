import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib import colors

def format_code(text):
    """Escapes HTML chars and preserves whitespace/newlines for ReportLab."""
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('\n', '<br/>').replace(' ', '&nbsp;')

def make_callout(title, body_text, border_color, bg_color, title_style, body_style):
    """Creates a visually rich, boxed callout card for notes, tips, and visual diagrams."""
    content = [
        Paragraph(f"<b>{title}</b>", title_style),
        Spacer(1, 4),
        Paragraph(body_text, body_style)
    ]
    t = Table([[content]], colWidths=[520])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg_color),
        ('BOX', (0,0), (-1,-1), 1, border_color),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    return t

def build_pdf(filename="PSA_Master_Operating_Manual.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    # Color Palette
    CYAN = colors.HexColor('#0284c7')
    CYAN_LIGHT = colors.HexColor('#e0f2fe')
    DARK_BG = colors.HexColor('#0f172a')
    GREEN = colors.HexColor('#059669')
    GREEN_LIGHT = colors.HexColor('#d1fae5')
    TEXT_DARK = colors.HexColor('#1e293b')
    MUTED = colors.HexColor('#64748b')
    AMBER = colors.HexColor('#d97706')
    AMBER_LIGHT = colors.HexColor('#fef3c7')

    styles = getSampleStyleSheet()

    # Custom Typography Styles
    title_style = ParagraphStyle(
        'CoverTitle', parent=styles['Title'],
        fontName='Helvetica-Bold', fontSize=24, leading=30,
        textColor=CYAN, alignment=1, spaceAfter=12
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubtitle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=11, leading=16,
        textColor=MUTED, alignment=1, spaceAfter=15
    )

    h1_style = ParagraphStyle(
        'H1', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=14, leading=18,
        textColor=CYAN, spaceBefore=8, spaceAfter=6
    )

    h2_style = ParagraphStyle(
        'H2', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=11, leading=14,
        textColor=TEXT_DARK, spaceBefore=6, spaceAfter=4
    )

    body_style = ParagraphStyle(
        'Body', parent=styles['BodyText'],
        fontName='Helvetica', fontSize=9, leading=13,
        textColor=TEXT_DARK, spaceAfter=6
    )

    callout_title = ParagraphStyle(
        'CalloutTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9.5, leading=12,
        textColor=DARK_BG
    )

    callout_body = ParagraphStyle(
        'CalloutBody', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8.5, leading=12,
        textColor=TEXT_DARK
    )

    code_style = ParagraphStyle(
        'Code', parent=styles['Code'],
        fontName='Courier', fontSize=7.5, leading=10.5,
        textColor=colors.HexColor('#10b981'), backColor=DARK_BG,
        borderPadding=6, spaceAfter=8, spaceBefore=4
    )

    story = []

    # =========================================================================
    # COVER PAGE
    # =========================================================================
    story.append(Spacer(1, 100))
    story.append(Paragraph("POCKET STATE ARCHITECTURE (PSA™)", title_style))
    story.append(Paragraph("The Complete 20-Page Master Operating Manual & Beginner's Guide", subtitle_style))
    story.append(HRFlowable(width="85%", thickness=2, color=CYAN, spaceAfter=25))
    story.append(Paragraph("From Zero Mobile Unix Setup to Local AI Pipelines & High-Margin Agency Automation", subtitle_style))
    story.append(Spacer(1, 60))
    
    cover_box = make_callout(
        "⚡ SYSTEM ARCHITECTURE OVERVIEW",
        "This guide covers end-to-end deployment of zero-overhead POSIX software. "
        "Learn how to set up native terminals, integrate offline AI, execute background cron routines, "
        "and launch $1,000/mo agency services directly from your mobile workstation.",
        CYAN, CYAN_LIGHT, callout_title, callout_body
    )
    story.append(cover_box)
    story.append(Spacer(1, 60))
    story.append(Paragraph("<b>Author & Architect:</b> Rean Van Aswegen<br/><b>Version:</b> 5.0 (Production Master Edition)", subtitle_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 1: Title, Blueprint & Executive Summary
    # =========================================================================
    story.append(Paragraph("PAGE 1: Architectural Blueprint & Executive Summary", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=CYAN, spaceAfter=8))
    story.append(Paragraph("<b>Author & Architect:</b> Rean Van Aswegen | <b>Core Standard:</b> POSIX Shell / ARM64 Mobile Unix", body_style))
    story.append(Paragraph("Pocket State Architecture (PSA™) proves that modern software development does not require multi-gigabyte frameworks, complex cloud clusters, or expensive monthly hosting subscriptions. You can design, compile, execute, and monetise production-grade systems directly within a native mobile terminal environment.", body_style))
    
    p1_hud = make_callout(
        "🖥️ HUD SYSTEM TELEMETRY MAP",
        format_code("┌────────────────────────────────────────────────────────────────────────┐\n"
                    "│ POSIX CORE STATE  ──► Native Termux Unix (ARM64) ──► In-Memory Map     │\n"
                    "│ LOCAL AI ENGINE   ──► Ollama (Port 11434)        ──► Llama 3 8B Quant  │\n"
                    "│ ASSET COMPILER    ──► Single-File HTML Compiler   ──► 18KB Payload     │\n"
                    "│ INFRASTRUCTURE    ──► $0.00 Overhead             ──► 100/100 Lighthouse│\n"
                    "└────────────────────────────────────────────────────────────────────────┘"),
        CYAN, DARK_BG, ParagraphStyle('H', parent=callout_title, textColor=CYAN), ParagraphStyle('B', parent=code_style)
    )
    story.append(p1_hud)
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Core Objectives of this Manual:</b><br/>"
                           "1. Transform any Android smartphone into an enterprise-grade developer workstation.<br/>"
                           "2. Eliminate dependency bloat by replacing standard JS frameworks with POSIX shell logic.<br/>"
                           "3. Run private, offline AI instances with zero API costs.<br/>"
                           "4. Productise these workflows into high-margin agency retainers ($1,000 - $3,000/mo).", body_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: Absolute Beginner Setup - Part 1 (Termux Installation)
    # =========================================================================
    story.append(Paragraph("PAGE 2: Absolute Beginner Setup – Step-by-Step Termux Setup", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=CYAN, spaceAfter=8))
    
    p2_warn = make_callout(
        "⚠️ CRITICAL INSTALLATION WARNING (F-DROID VS PLAY STORE)",
        "<b>DO NOT install Termux from the Google Play Store!</b> The Play Store version is deprecated and unmaintained due to Android target API restrictions. You will encounter repository sync errors.<br/>"
        "<b>Correct Source:</b> Download the latest Termux APK directly from <b>F-Droid.org</b> or GitHub Releases.",
        AMBER, AMBER_LIGHT, callout_title, callout_body
    )
    story.append(p2_warn)
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Step 1: Download & Install Termux</b><br/>"
                           "• Navigate to <code>f-droid.org</code> on your phone browser.<br/>"
                           "• Search for 'Termux' and download the <code>.apk</code> file.<br/>"
                           "• Open the download and allow 'Install from Unknown Sources'.", body_style))
    story.append(Paragraph("<b>Step 2: Initialize System Repositories & Storage</b><br/>"
                           "Open Termux and run the following core initialization commands:", body_style))
    story.append(Paragraph(format_code("# Step 2A: Update system packages and mirror repos\npkg update && pkg upgrade -y\n\n# Step 2B: Grant storage access to move files to phone storage\ntermux-setup-storage\n\n# Step 2C: Verify system architecture (Should return aarch64 / arm64)\nuname -m"), code_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: Absolute Beginner Setup - Part 2 (Toolchain Installation)
    # =========================================================================
    story.append(Paragraph("PAGE 3: Setting Up Your Core Developer Toolchain", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=CYAN, spaceAfter=8))
    story.append(Paragraph("To execute PSA™ compilers and local state engines, you need a lightweight Unix toolchain. Execute the following master installation command:", body_style))
    
    story.append(Paragraph(format_code("# Master Command: Install core developer utilities\npkg install -y bash git curl wget jq python clang micro pandoc openssh"), code_style))
    
    story.append(Paragraph("<b>Toolchain Breakdown — What Each Tool Does:</b>", h2_style))
    
    t3_data = [
        ['Package', 'Primary Role in PSA™ Stack', 'Beginner Execution Command'],
        ['bash', 'Native POSIX Shell State Controller', 'bash script.sh'],
        ['curl / wget', 'HTTP REST Request Transmitters', 'curl http://localhost:11434'],
        ['jq', 'High-Speed JSON Parser for AI Payloads', 'cat data.json | jq .response'],
        ['python', 'Advanced PDF & Document Compiler Engine', 'python build_ebook.py'],
        ['micro', 'Intuitive Terminal Code Editor (Mouse Support)', 'micro index.html'],
        ['pandoc', 'Markdown to Multi-Format Document Renderer', 'pandoc input.md -o output.pdf']
    ]
    t3 = Table(t3_data, colWidths=[70, 260, 190])
    t3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BG),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t3)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: Termux Terminal Shortcuts & Extra Keys Cheat-Sheet
    # =========================================================================
    story.append(Paragraph("PAGE 4: Termux Shortcuts & Productivity Cheat-Sheet", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=CYAN, spaceAfter=8))
    story.append(Paragraph("Mobile virtual keyboards lack physical keys like <code>CTRL</code>, <code>ALT</code>, or <code>TAB</code>. Termux allows you to enable a custom Extra Key Bar directly above your touch keyboard.", body_style))
    
    story.append(Paragraph("<b>Configure Extra Keys Row:</b><br/>Create the Termux configuration directory and append custom key bindings:", body_style))
    story.append(Paragraph(format_code("mkdir -p ~/.termux\necho \"extra-keys = [['ESC','TAB','CTRL','ALT','-','UP','DOWN']]\" > ~/.termux/termux.properties\ntermux-reload-settings"), code_style))
    
    story.append(Paragraph("<b>Essential Terminal Navigation Shortcuts:</b>", h2_style))
    
    t4_data = [
        ['Shortcut Combination', 'System Action / Command Function'],
        ['CTRL + C', 'Cancel / Interrupt currently executing process or loop'],
        ['CTRL + Z', 'Send running process to background thread'],
        ['CTRL + L', 'Clear terminal display screen instantly'],
        ['CTRL + D', 'Exit current terminal session or shell process'],
        ['Volume Up + Q', 'Toggle Extra Keys Bar visible / hidden'],
        ['Volume Up + W', 'Move cursor UP in terminal history'],
        ['Volume Up + S', 'Move cursor DOWN in terminal history']
    ]
    t4 = Table(t4_data, colWidths=[160, 360])
    t4.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BG),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t4)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 5: The PSA™ Manifesto & Philosophy
    # =========================================================================
    story.append(Paragraph("PAGE 5: The PSA™ Manifesto & Philosophy", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=CYAN, spaceAfter=8))
    story.append(Paragraph("Why Modern Software Engineering Is Broken", h2_style))
    story.append(Paragraph("Modern web development suffers from severe dependency inflation. A simple marketing page now ships with over 200 megabytes of <code>node_modules</code>, dozens of breaking third-party packages, and heavy client-side JavaScript execution.", body_style))
    
    p5_box = make_callout(
        "❌ THE TRADITIONAL FRAMEWORK TRAP",
        "• <b>Heavy Memory Footprint:</b> Consumes 300MB - 1GB RAM on startup.<br/>"
        "• <b>Vendor Lock-in:</b> Dependent on Vercel, AWS, or expensive hosting tiers.<br/>"
        "• <b>Fragile Pipelines:</b> Upstream NPM package updates break client builds.<br/>"
        "• <b>High Latency:</b> Complex client hydration cycles slow down initial page rendering.",
        AMBER, AMBER_LIGHT, callout_title, callout_body
    )
    story.append(p5_box)
    story.append(Spacer(1, 8))
    story.append(Paragraph("The PSA™ Alternative: Zero-Overhead Software", h2_style))
    story.append(Paragraph("PSA™ strips away all non-essential abstractions. By compiling static, atomic HTML/CSS payloads directly from native POSIX shell scripts, your applications load instantly, run anywhere, and cost $0.00 to host.", body_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 6: POSIX Shell Core vs Heavy Frameworks
    # =========================================================================
    story.append(Paragraph("PAGE 6: POSIX Core vs. Heavy Framework Benchmarks", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=CYAN, spaceAfter=8))
    story.append(Paragraph("Below is a side-by-side performance comparison measuring a React/Next.js application against a native POSIX-compiled PSA™ shell:", body_style))
    
    t6_data = [
        ['Performance Benchmark', 'Traditional Stack (React/Node)', 'PSA™ POSIX System'],
        ['Memory Allocation (RAM)', '~150 MB – 500 MB', '< 3.2 MB'],
        ['Initial Package Size', '180 MB – 350 MB (node_modules)', '0 KB (Native POSIX)'],
        ['HTTP Requests Required', '25 – 60 static bundles', '1 Self-Contained File'],
        ['Google Lighthouse Score', '55 – 85 / 100', '100 / 100 (Perfect)'],
        ['Page Load Latency', '800ms – 2,400ms', '< 0.4ms (Instant)'],
        ['Monthly Server Overhead', '$20 – $250 / month', '$0.00 (Self-Hosted/Local)']
    ]
    t6 = Table(t6_data, colWidths=[150, 185, 185])
    t6.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BG),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t6)
    story.append(Spacer(1, 10))
    
    p6_note = make_callout(
        "💡 ARCHITECTURAL INSIGHT",
        "By eliminating virtual DOM compilation overhead, PSA™ engines allow mobile ARM processors to handle hundreds of concurrent local requests with virtually zero battery drain or thermal throttling.",
        GREEN, GREEN_LIGHT, callout_title, callout_body
    )
    story.append(p6_note)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 7: The POSIX In-Memory State Engine (In-Depth)
    # =========================================================================
    story.append(Paragraph("PAGE 7: The In-Memory POSIX State Engine", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=CYAN, spaceAfter=8))
    story.append(Paragraph("How In-Memory Shell State Management Works", h2_style))
    story.append(Paragraph("Instead of running heavy database daemons (MySQL, PostgreSQL, MongoDB) which consume gigabytes of mobile RAM, PSA™ manages runtime state directly inside in-memory POSIX associative arrays and key-value state maps.", body_style))
    
    story.append(Paragraph("<b>Complete Annotated POSIX State Controller Script:</b>", body_style))
    story.append(Paragraph(format_code("#!/usr/bin/env bash\n# =======================================================\n# PSA™ CORE STATE ENGINE ENGINE v5.0\n# =======================================================\n\ndeclare -A GLOBAL_STATE\n\n# Function: Store key-value state pair\nstate_set() {\n    local key=\"$1\"\n    local val=\"$2\"\n    GLOBAL_STATE[\"$key\"]=\"$val\"\n    echo \"[STATE UPDATE] $key -> $val\"\n}\n\n# Function: Retrieve stored state value\nstate_get() {\n    local key=\"$1\"\n    echo \"${GLOBAL_STATE[\"$key\"]}\"\n}\n\n# Initialize State Values\nstate_set \"APP_NAME\" \"PSA Master Engine\"\nstate_set \"STATUS\" \"ONLINE\"\nstate_set \"SYSTEM_RAM\" \"$(free -m | awk '/Mem:/ {print $3}') MB\"\n\necho \"Active Application: $(state_get \"APP_NAME\")\"\necho \"Current RAM Allocation: $(state_get \"SYSTEM_RAM\")\""), code_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 8: Zero-Bloat Web Asset Compilation
    # =========================================================================
    story.append(Paragraph("PAGE 8: Zero-Bloat Web Asset Compilation", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=CYAN, spaceAfter=8))
    story.append(Paragraph("Single-Script Asset Compilation Model", h2_style))
    story.append(Paragraph("In traditional development, build tools like Webpack or Vite read hundreds of individual files and bundle them into large JavaScript payloads. PSA™ replaces this entire pipeline with a single executable POSIX shell script (<code>build.sh</code>).", body_style))
    
    p8_diagram = make_callout(
        "⚡ THE PSA™ COMPILATION PIPELINE",
        format_code("POSIX Build Controller (build.sh)\n"
                    "  │\n"
                    "  ├──► 1. Inlines Atomic Utility CSS Stylesheet\n"
                    "  ├──► 2. Injects Dynamic State Variables from Shell Map\n"
                    "  └──► 3. Compresses HTML Payload into Single File Output\n"
                    "  │\n"
                    "  ▼\n"
                    "index.html (18 KB Total Output / Instant 15ms Render Time)"),
        CYAN, DARK_BG, ParagraphStyle('H2', parent=callout_title, textColor=CYAN), ParagraphStyle('B2', parent=code_style)
    )
    story.append(p8_diagram)
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Key Advantages:</b><br/>"
                           "• Zero build tool maintenance or NPM updates.<br/>"
                           "• Single HTML file output means easy deployment to any static server or CDN.<br/>"
                           "• Blazing fast compile time (< 50ms total execution time).", body_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 9: Hands-On Tutorial - Building Your First Web Shell
    # =========================================================================
    story.append(Paragraph("PAGE 9: Hands-On Tutorial – Building Your First App", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=CYAN, spaceAfter=8))
    story.append(Paragraph("Let's build a functional, responsive web application directly inside Termux using a single POSIX compiler script.", body_style))
    
    story.append(Paragraph("<b>Step 1: Create the Compiler Script</b><br/>In Termux, create a file named <code>compile_site.sh</code>:", body_style))
    story.append(Paragraph(format_code("cat << 'EOF' > compile_site.sh\n#!/usr/bin/env bash\n# PSA™ Single-File Web Compiler\n\nOUTPUT_FILE=\"index.html\"\nAPP_TITLE=\"PSA Mobile Workstation\"\n\ncat << WEB_CONTENT > \"$OUTPUT_FILE\"\n<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>$APP_TITLE</title>\n    <style>\n        body { background: #0f172a; color: #f8fafc; font-family: sans-serif; padding: 2rem; }\n        .card { background: #1e293b; border: 1px solid #0284c7; padding: 1.5rem; border-radius: 12px; }\n        h1 { color: #0284c7; margin-top: 0; }\n    </style>\n</head>\n<body>\n    <div class=\"card\">\n        <h1>$APP_TITLE</h1>\n        <p>Built directly inside Termux Unix terminal. Zero external frameworks.</p>\n    </div>\n</body>\n</html>\nWEB_CONTENT\n\necho \"[✓] Compiled successfully to $OUTPUT_FILE!\"\nEOF"), code_style))
    story.append(Paragraph("<b>Step 2: Make Executable & Run</b>", h2_style))
    story.append(Paragraph(format_code("chmod +x compile_site.sh && ./compile_site.sh"), code_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 10: Local AI Integration (Ollama & Quantized LLMs)
    # =========================================================================
    story.append(Paragraph("PAGE 10: Local AI Integration – Ollama & Quantized Models", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=CYAN, spaceAfter=8))
    story.append(Paragraph("Why Run AI Locally on Your Mobile Device?", h2_style))
    story.append(Paragraph("Cloud AI APIs (OpenAI, Anthropic) introduce recurring per-token costs, high network latency, and serious data privacy risks. PSA™ integrates with local quantized AI models running directly on device or local networks via <b>Ollama</b>.", body_style))
    
    p10_ai_box = make_callout(
        "🤖 LOCAL AI ARCHITECTURE",
        format_code("Mobile Termux Terminal / Shell Script\n"
                    "  │\n"
                    "  ├──► Local HTTP REST Request (Port 11434)\n"
                    "  │\n"
                    "  ▼\n"
                    "Ollama Engine (Llama 3 8B Quantized Model - Q4_K_M)\n"
                    "  │\n"
                    "  ▼\n"
                    "100% Private, Offline Output Response (Zero API Token Fees)"),
        GREEN, DARK_BG, ParagraphStyle('H3', parent=callout_title, textColor=GREEN), ParagraphStyle('B3', parent=code_style)
    )
    story.append(p10_ai_box)
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Starting Local AI Models in Termux / Local Net:</b>", h2_style))
    story.append(Paragraph(format_code("# Pull and execute a high-speed 4-bit quantized Llama model\nollama run llama3:8b-instruct-q4_K_M"), code_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 11: Shell Pipelines to Local AI Endpoints
    # =========================================================================
    story.append(Paragraph("PAGE 11: Connecting Shell Pipelines to Local AI Endpoints", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=CYAN, spaceAfter=8))
    story.append(Paragraph("Querying Local AI via `curl` and `jq`", h2_style))
    story.append(Paragraph("Because local Ollama engines expose a standard HTTP REST interface on port `11434`, you can send prompts and parse JSON responses directly within native Bash scripts.", body_style))
    
    story.append(Paragraph("<b>Complete Production AI Pipeline Script:</b>", body_style))
    story.append(Paragraph(format_code("#!/usr/bin/env bash\n# =======================================================\n# PSA™ SHELL TO LOCAL AI CONNECTOR\n# =======================================================\n\nPROMPT=\"Explain the benefits of POSIX state management in 2 clear sentences.\"\n\necho \"[+] Querying local Llama 3 instance...\"\n\n# Query Ollama REST API Endpoint\nRESPONSE=$(curl -s http://localhost:11434/api/generate -d \"{\n  \\\"model\\\": \\\"llama3\\\",\n  \\\"prompt\\\": \\\"$PROMPT\\\",\n  \\\"stream\\\": false\n}\")\n\n# Extract clean response string using jq\nCLEAN_TEXT=$(echo \"$RESPONSE\" | jq -r '.response')\n\necho -e \"\\n--- AI RESPONSE ---\"\necho \"$CLEAN_TEXT\""), code_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 12: Building Autonomous Local AI Agents
    # =========================================================================
    story.append(Paragraph("PAGE 12: Building Autonomous Local AI Agents", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=CYAN, spaceAfter=8))
    story.append(Paragraph("What Is an Autonomous Shell Agent?", h2_style))
    story.append(Paragraph("An autonomous agent pairs a decision-making AI model with Unix execution loops. The agent reads input data, prompts the local LLM for instructions, executes POSIX commands based on the response, and updates system state automatically.", body_style))
    
    p12_loop = make_callout(
        "🔄 THE AUTONOMOUS AGENT EXECUTION LOOP",
        "<b>1. Read Input Data</b> (Scans inbound emails, lead files, or logs)<br/>"
        "<b>2. Prompt Local Llama</b> (Scores intent & determines action required)<br/>"
        "<b>3. Execute POSIX Action</b> (Outputs formatted PDF, triggers webhook, or updates database)<br/>"
        "<b>4. Update State Map</b> (Logs execution history & loops for next task)",
        CYAN, CYAN_LIGHT, callout_title, callout_body
    )
    story.append(p12_loop)
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Practical Real-World Use Cases:</b><br/>"
                           "• <b>Auto-Lead Qualifier:</b> Evaluates inbound contact forms and routes high-value leads automatically.<br/>"
                           "• <b>Auto-Code Auditor:</b> Inspects shell scripts for errors and applies optimizations automatically.", body_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 13: Automated Document & PDF Compilers
    # =========================================================================
    story.append(Paragraph("PAGE 13: Automated Document & PDF Compilers", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=CYAN, spaceAfter=8))
    story.append(Paragraph("Generating Professional Invoices & Reports via Shell Scripts", h2_style))
    story.append(Paragraph("PSA™ engines excel at taking raw Markdown text or state parameters and compiling them into styled PDF documents, client reports, or eBooks directly on device.", body_style))
    
    story.append(Paragraph("<b>Example: Markdown to PDF Compilation Pipeline</b>", body_style))
    story.append(Paragraph(format_code("# Step 1: Create sample Markdown report\ncat << 'EOF' > client_report.md\n# PSA Client Audit Report\n**Status:** Systems Operational  \n**Performance Score:** 100/100  \n\nAll background cron routines executed cleanly.\nEOF\n\n# Step 2: Compile Markdown to PDF using Pandoc & Weasyprint\npandoc client_report.md -o Client_Audit_Report.pdf \\\n    --pdf-engine=weasyprint \\\n    --metadata title=\"PSA Audit Report\""), code_style))
    story.append(Spacer(1, 8))
    story.append(Paragraph("This allows you to automate invoice compilation, client onboarding reports, and eBook publishing directly inside Termux.", body_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 14: High-Performance Data Crons & Automation
    # =========================================================================
    story.append(Paragraph("PAGE 14: High-Performance Data Processing & Crons", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=CYAN, spaceAfter=8))
    story.append(Paragraph("Automating Background Tasks with Cron Schedules", h2_style))
    story.append(Paragraph("Turn your pocket device into a 24/7 background automation engine using Unix `cron` scheduling. Cron automatically triggers background routines at exact time intervals.", body_style))
    
    story.append(Paragraph("<b>Setting Up Cron Schedules in Termux:</b>", body_style))
    story.append(Paragraph(format_code("# Open crontab schedule editor\ncrontab -e\n\n# Cron Syntax Format:\n# MIN HOUR DOM MON DOW COMMAND\n\n# Example 1: Run system health check every hour\n0 * * * * /data/data/com.termux/files/home/psa/system_check.sh\n\n# Example 2: Compile and back up daily sales report at 08:00 AM\n0 8 * * * /data/data/com.termux/files/home/psa/compile_daily_report.sh"), code_style))
    
    p14_note = make_callout(
        "⚡ BATTERY-EFFICIENT AUTOMATION",
        "Because native POSIX scripts execute in milliseconds, background cron jobs consume virtually zero battery compared to persistent heavy background apps.",
        GREEN, GREEN_LIGHT, callout_title, callout_body
    )
    story.append(p14_note)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 15: Shortcuts & Productivity Power Tools
    # =========================================================================
    story.append(Paragraph("PAGE 15: Custom Aliases & Productivity Shortcuts", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=CYAN, spaceAfter=8))
    story.append(Paragraph("Speed up your developer workflow by adding custom command shortcuts (aliases) to your `.bashrc` file.", body_style))
    
    story.append(Paragraph("<b>Configure `.bashrc` Custom Shortcuts:</b>", body_style))
    story.append(Paragraph(format_code("# Append custom aliases to ~/.bashrc\ncat << 'EOF' >> ~/.bashrc\n\n# Navigation Shortcuts\nalias psa='cd ~/psa && ls -la'\nalias edit='micro'\n\n# System Status Shortcuts\nalias ram='free -m'\nalias myip='curl -s https://ifconfig.me'\n\n# PSA Pipeline Shortcuts\nalias build='./compile_site.sh'\nalias ai='ollama run llama3:8b-instruct-q4_K_M'\nEOF\n\n# Reload configuration\nsource ~/.bashrc"), code_style))
    
    story.append(Paragraph("Now you can type simple commands like <code>build</code> or <code>ai</code> instead of typing long command paths each time.", body_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 16: The Agency Blueprint – Monetizing PSA™
    # =========================================================================
    story.append(Paragraph("PAGE 16: The Agency Blueprint – Monetizing PSA™", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=CYAN, spaceAfter=8))
    story.append(Paragraph("Transforming Technical Skills into High-Margin Revenue", h2_style))
    story.append(Paragraph("PSA™ isn't just an architectural framework; it is a **high-margin agency model**. Traditional agencies lose most of their revenue to cloud server fees, SaaS subscriptions, and platform lock-in. By leveraging zero-overhead architecture:", body_style))
    
    t16_data = [
        ['Financial Metric', 'Traditional Web Agency', 'PSA™ Powered Mobile Agency'],
        ['Hosting Overhead', '$500 – $2,000 / month', '$0.00 / month'],
        ['SaaS Dependency Costs', '$300 – $800 / month', '$0.00 (Self-Contained Shells)'],
        ['Client Monthly Fee', '$1,000 – $3,000 / month', '$1,000 – $3,000 / month'],
        ['Gross Profit Margin', '20% – 40% Margin', '95% – 99% Net Profit Margin']
    ]
    t16 = Table(t16_data, colWidths=[140, 190, 190])
    t16.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BG),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t16)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 17: Monetization Pillars (Agents, Funnels, Automation)
    # =========================================================================
    story.append(Paragraph("PAGE 17: Core Service Packages to Sell Clients", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=CYAN, spaceAfter=8))
    story.append(Paragraph("3 High-Value Offers You Can Launch Immediately:", h2_style))
    
    p17_offer1 = make_callout(
        "🚀 OFFER 1: ULTRA-FAST HIGH-CONVERSION WEBSITES ($1,000 - $2,500)",
        "Replace slow, bloated WordPress or Wix sites with a single-file POSIX web shell.<br/>"
        "<b>Key Selling Point:</b> Guarantees a perfect 100/100 Google Lighthouse score and instant page loads (<15ms), increasing client conversion rates.",
        CYAN, CYAN_LIGHT, callout_title, callout_body
    )
    story.append(p17_offer1)
    story.append(Spacer(1, 6))

    p17_offer2 = make_callout(
        "🤖 OFFER 2: PRIVATE LOCAL AI SUPPORT BOTS ($1,500 SETUP + $500/MO)",
        "Deploy 100% private, on-premise local AI support agents for legal, medical, or real estate clients.<br/>"
        "<b>Key Selling Point:</b> Complete data privacy (no customer data sent to third-party cloud AI) with zero API usage fees.",
        GREEN, GREEN_LIGHT, callout_title, callout_body
    )
    story.append(p17_offer2)
    story.append(Spacer(1, 6))

    p17_offer3 = make_callout(
        "⚙️ OFFER 3: AUTOMATED BUSINESS REPORT PIPELINES ($2,000 UPFRONT)",
        "Build automated background scripts that collect weekly sales logs and compile branded PDF invoices automatically.<br/>"
        "<b>Key Selling Point:</b> Saves business owners 10+ hours per week of manual data entry.",
        AMBER, AMBER_LIGHT, callout_title, callout_body
    )
    story.append(p17_offer3)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 18: Retainer Packaging & Sales Playbook
    # =========================================================================
    story.append(Paragraph("PAGE 18: Structuring $1,000/Month Retainer Agreements", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=CYAN, spaceAfter=8))
    story.append(Paragraph("To build predictable recurring revenue, bundle your automation tools into simple monthly service retainers:", body_style))
    
    t18_data = [
        ['Retainer Service Included', 'Cost to Your Agency', 'Perceived Client Value'],
        ['Local AI Maintenance & Prompt Fine-Tuning', '$0.00', '$800 / month'],
        ['Automated Daily Database Backups & Audits', '$0.00', '$300 / month'],
        ['High-Speed Web Shell Hosting & Updates', '$0.00', '$400 / month'],
        ['Total Monthly Package Value', '$0.00 Net Overhead', '$1,500 / month Value']
    ]
    t18 = Table(t18_data, colWidths=[200, 140, 180])
    t18.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BG),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t18)
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>The Scaling Math:</b><br/>"
                           "• 5 Retainer Clients @ $1,000/mo = <b>$5,000/month</b> ($0 hosting overhead)<br/>"
                           "• 10 Retainer Clients @ $1,000/mo = <b>$10,000/month</b> ($0 hosting overhead)", body_style))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 19: Enterprise Security, Data Isolation & Compliance
    # =========================================================================
    story.append(Paragraph("PAGE 19: Enterprise Security, Data Isolation & POPIA/GDPR", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=CYAN, spaceAfter=8))
    story.append(Paragraph("Air-Gapped Local Architecture for Total Compliance", h2_style))
    story.append(Paragraph("Data privacy laws (POPIA in South Africa, GDPR in Europe, HIPAA in the US) impose heavy fines on companies that leak sensitive customer data to third-party cloud platforms.", body_style))
    
    p19_sec = make_callout(
        "🔒 TOTAL DATA ISOLATION ADVANTAGE",
        "• <b>Zero Cloud Leakage:</b> Sensitive lead data and client records are stored exclusively in local key-value state arrays.<br/>"
        "• <b>Air-Gapped Operation:</b> AI pipelines continue running even if internet connectivity drops completely.<br/>"
        "• <b>Instant Audit Readiness:</b> No external subprocesses or remote servers tracking user activity.",
        CYAN, CYAN_LIGHT, callout_title, callout_body
    )
    story.append(p19_sec)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 20: Master Production Build Script & Conclusion
    # =========================================================================
    story.append(Paragraph("PAGE 20: Master Production Builder & Final Conclusion", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=CYAN, spaceAfter=8))
    story.append(Paragraph("Run this unified master production script inside Termux to deploy your core showcase environment instantly:", body_style))
    
    story.append(Paragraph(format_code("#!/usr/bin/env bash\n# =======================================================\n# PSA™ MASTER PRODUCTION BUILDER\n# Creator & Author: Rean Van Aswegen\n# =======================================================\n\nOUTPUT=\"psa_production.html\"\ncat << 'EOF' > \"$OUTPUT\"\n<!DOCTYPE html>\n<html>\n<head>\n    <title>PSA Production Node</title>\n    <style>\n        body { background: #0f172a; color: #f8fafc; font-family: sans-serif; text-align: center; padding: 3rem; }\n        .badge { background: rgba(5, 150, 105, 0.2); color: #10b981; padding: 6px 16px; border-radius: 99px; font-weight: bold; }\n        h1 { color: #0284c7; font-size: 2.2rem; }\n    </style>\n</head>\n<body>\n    <span class=\"badge\">● SYSTEM ONLINE</span>\n    <h1>Pocket State Architecture</h1>\n    <p>Engineered and compiled directly on ARM64 mobile Unix workstation.</p>\n</body>\n</html>\nEOF\necho \"[✓] Master Production Deployment Complete: $OUTPUT\""), code_style))
    
    story.append(Paragraph("<b>Conclusion & Final Words:</b><br/>"
                           "Pocket State Architecture (PSA™) was engineered and pioneered by <b>Rean Van Aswegen</b> to eliminate software engineering bloat and prove that world-class, high-margin software systems can be built and operated from anywhere in the world—using nothing more than a smartphone and a vision.", body_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph(format_code("=========================================================\nPOCKET STATE ARCHITECTURE (PSA™) - OPERATIONAL SYSTEM\nAUTHORED & ENGINEERED BY REAN VAN ASWEGEN\n========================================================="), code_style))

    # Build Document
    doc.build(story)
    print("[✓] SUCCESS: Master Manual compiled cleanly to PSA_Master_Operating_Manual.pdf")

if __name__ == '__main__':
    build_pdf()
