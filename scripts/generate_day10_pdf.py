#!/usr/bin/env python3
"""
PEER'S Watering Hole Shield Suite - Executive Multi-Page Lab Report Compiler (Day 10)
Sqrock IT Solutions Cybersecurity Internship Track: Social Engineering Attack Simulations Using Python

Compiles an authoritative 7-page executive engineering report integrating:
- 6 empirical execution screenshots (Kali Linux CLI cold boot, master menu, honeypot server, victim simulator, SOC telemetry, GitHub repo)
- In-depth forensic explanations for every screenshot
- Deep technical analyses of watering hole attacks, drive-by downloads, digital baiting, and canary token tripwires
- MITRE ATT&CK T1189, NIST SP 800-53 (SI-3, SI-4), and CIS Controls v8 compliant defense architecture
- Automated 6-point unit test validation ledger and ethical compliance statements
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
)
from reportlab.pdfgen import canvas

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, "screenshots")
OUTPUT_PDF = os.path.join(REPORTS_DIR, "Day10_Watering_Hole_Report_Sqrock_MdPeerSiddiqui.pdf")

# Palette definitions
NAVY_PRIMARY = colors.HexColor("#0B192C")
CYAN_ACCENT  = colors.HexColor("#008DDA")
DARK_BLUE    = colors.HexColor("#1E3E62")
SLATE_GRAY   = colors.HexColor("#415A77")
LIGHT_BG     = colors.HexColor("#F4F6F9")
BORDER_COLOR = colors.HexColor("#D0D7DE")
SUCCESS_COL  = colors.HexColor("#0E703C")
CRIT_COL     = colors.HexColor("#A8201A")
TEXT_DARK    = colors.HexColor("#1A1A1A")


class NumberedCanvas(canvas.Canvas):
    """
    Two-pass canvas to dynamically compute and render total page count
    and persistent running headers and footers.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        self.saveState()
        page_num = self._pageNumber
        
        # Running Header (pages 2+)
        if page_num > 1:
            self.setStrokeColor(BORDER_COLOR)
            self.setLineWidth(0.6)
            self.line(36, 756, 576, 756)
            
            self.setFont("Helvetica", 7.5)
            self.setFillColor(SLATE_GRAY)
            self.drawString(36, 762, "Sqrock IT Solutions | Cybersecurity Internship — Day 10 Lab Report")
            self.drawRightString(576, 762, "PEER'S Watering Hole Shield Suite v2.5")

        # Running Footer (all pages)
        self.setStrokeColor(BORDER_COLOR)
        self.setLineWidth(0.6)
        self.line(36, 36, 576, 36)
        
        self.setFont("Helvetica", 7.5)
        self.setFillColor(SLATE_GRAY)
        self.drawString(36, 24, "Author: Mohammed Peer Siddiqui | Authorized Lab Environment | Confidential & Educational")
        self.drawRightString(576, 24, f"Page {page_num} of {total_pages}")
        
        self.restoreState()


def create_report():
    os.makedirs(REPORTS_DIR, exist_ok=True)
    
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=42,
        bottomMargin=42
    )

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=NAVY_PRIMARY,
        spaceAfter=3
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=13,
        textColor=CYAN_ACCENT,
        spaceAfter=8
    )

    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=NAVY_PRIMARY,
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=DARK_BLUE,
        spaceBefore=6,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=TEXT_DARK,
        spaceAfter=5
    )

    callout_style = ParagraphStyle(
        'Callout',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=11,
        textColor=DARK_BLUE
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        textColor=TEXT_DARK
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white
    )

    story = []

    def load_screenshot(filename, w=540, h=195):
        path = os.path.join(SCREENSHOTS_DIR, filename)
        if os.path.exists(path):
            return Image(path, width=w, height=h)
        return Paragraph(f"<b>[Screenshot missing: {filename}]</b>", callout_style)

    # =========================================================================
    # PAGE 1: TITLE, METADATA & EXECUTIVE SUMMARY
    # =========================================================================
    story.append(Paragraph("SQROCK IT SOLUTIONS — CYBERSECURITY INTERNSHIP", subtitle_style))
    story.append(Paragraph("Day 10: Baiting & Watering Hole Attack Simulation & Honeypot Link Tracking", title_style))
    story.append(Spacer(1, 4))

    # Metadata Card
    meta_data = [
        [
            Paragraph("<b>Intern:</b> Mohammed Peer Siddiqui", table_cell),
            Paragraph("<b>Track:</b> Social Engineering Simulations (Python)", table_cell),
            Paragraph("<b>Date:</b> October 31, 2026", table_cell)
        ],
        [
            Paragraph("<b>Target Domain:</b> Web Exploitation / Drive-by Compromise", table_cell),
            Paragraph("<b>Standard:</b> MITRE ATT&CK T1189 (Drive-by Compromise)", table_cell),
            Paragraph("<b>Framework:</b> NIST SP 800-53 (SI-3, SI-4) / CIS Control 9.2", table_cell)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[180, 180, 180])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph("1. Executive Summary", h1_style))
    story.append(Paragraph(
        "Watering hole attacks (mapped to <b>MITRE ATT&CK T1189: Drive-by Compromise</b>) and digital baiting lures represent some of the "
        "most sophisticated perimeter bypass strategies employed by advanced persistent threat (APT) groups. Rather than directly assaulting "
        "a heavily fortified enterprise perimeter, adversaries identify and compromise trusted third-party websites commonly frequented by target "
        "employees (e.g., regional supplier portals, technical forums, local catering menus, or trade associations). Once compromised, "
        "the attacker injects malicious iFrames, cross-site script redirectors, or deceptive download prompts (such as 'Critical Corporate "
        "VPN Update required') that silently deliver malware or harvest credentials.",
        body_style
    ))
    story.append(Paragraph(
        "Under <b>Day 10</b> of the Sqrock IT Solutions Cybersecurity Internship, this laboratory research project developed and evaluated "
        "<b>PEER'S Watering Hole Shield Suite v2.5</b>. The framework delivers an enterprise-grade Python honeypot gateway and passive client "
        "fingerprinter designed to intercept, log, and analyze unauthorized interactions with deceptive digital lures. By capturing client IP "
        "addresses, full User-Agent headers, referer origins, and unique department-specific canary tokens, the system provides early-warning "
        "tripwire capabilities aligned with <b>NIST SP 800-53 Rev. 5 (SI-3, SI-4)</b> and <b>CIS Controls v8 Safeguard 9.2</b>.",
        body_style
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("2. Watering Hole Defense Architecture Comparison", h1_style))
    matrix_data = [
        [
            Paragraph("Security Dimension", table_header),
            Paragraph("Unprotected Enterprise Egress", table_header),
            Paragraph("Hardened Honeypot & SWG Infrastructure", table_header)
        ],
        [
            Paragraph("Outbound Web Traffic Inspection", table_cell),
            Paragraph("<font color='#A8201A'>Unrestricted direct internet access</font>", table_cell),
            Paragraph("<font color='#0E703C'>Secure Web Gateway (SWG) + TLS Inspection</font>", table_cell)
        ],
        [
            Paragraph("Third-Party Compromise Visibility", table_cell),
            Paragraph("<font color='#A8201A'>Zero awareness of compromised vendor sites</font>", table_cell),
            Paragraph("<font color='#0E703C'>Honeypot Referer Tracking & Domain Scoring</font>", table_cell)
        ],
        [
            Paragraph("Digital Bait Lure Interception", table_cell),
            Paragraph("<font color='#A8201A'>Users download trojans unmonitored</font>", table_cell),
            Paragraph("<font color='#0E703C'>Canary Tripwires & Instant SOC Telemetry</font>", table_cell)
        ],
        [
            Paragraph("Client Fingerprint Telemetry", table_cell),
            Paragraph("<font color='#A8201A'>Unmonitored user environment</font>", table_cell),
            Paragraph("<font color='#0E703C'>Passive OS/Browser/IP Attribution</font>", table_cell)
        ],
        [
            Paragraph("Script Sandboxing & Isolation", table_cell),
            Paragraph("<font color='#A8201A'>Native local browser execution</font>", table_cell),
            Paragraph("<font color='#0E703C'>Remote Browser Isolation (RBI) + CSP</font>", table_cell)
        ]
    ]
    t_mat = Table(matrix_data, colWidths=[140, 195, 205])
    t_mat.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_mat)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: THREAT MODELING, ATTACK LIFECYCLE & INITIAL STATE
    # =========================================================================
    story.append(Paragraph("3. Threat Modeling & The 4-Stage Watering Hole Attack Lifecycle", h1_style))
    story.append(Paragraph(
        "Watering hole attacks thrive by exploiting transitive trust: employees inherently trust external websites that they visit routinely "
        "as part of daily business operations. The adversarial lifecycle unfolds across four distinct stages:",
        body_style
    ))
    story.append(Paragraph(
        "<b>Phase 1: Strategic Reconnaissance & Profiling:</b> The attacker conducts passive reconnaissance (OSINT, social network analysis) "
        "to discover specific web portals frequently accessed by target employees—such as regional industry news boards, third-party software "
        "vendor documentation, or local corporate catering menus.<br/>"
        "<b>Phase 2: Infiltration & Compromise of Trusted Website:</b> The adversary identifies and exploits web application vulnerabilities "
        "(e.g., outdated CMS plugins, unvalidated file uploads, or SQL injection) on the third-party watering hole website.<br/>"
        "<b>Phase 3: Malicious Injection & Traffic Redirection:</b> Attackers inject hidden JavaScript redirectors, zero-pixel iFrames, or "
        "deceptive download banners (e.g., 'Your corporate VPN requires an immediate security update to version 4.0').<br/>"
        "<b>Phase 4: Exploitation & Honeypot Interception:</b> When an employee visits the legitimate site, their browser automatically "
        "fetches the malicious payload or the user is lured into clicking the decoy link. The honeypot tracker intercepts this traffic, "
        "capturing forensic metadata and alerting the SOC.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Figure 1: Kali Linux Terminal Initialization & Environment Verification", h2_style))
    story.append(load_screenshot("01_kali_init_banner.png"))
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 1:</b> The cold-boot trace in Figure 1 confirms deployment within Kali Linux kernel 6.1.0-kali7-amd64 "
        "with Python 3.10.12. Git synchronization confirms a clean <code>main</code> branch state. The initialization sequence arms the "
        "Honeypot Gateway Engine on port 8080, initializes the passive client fingerprinter, activates the department canary routing engine, "
        "and links the structured event streaming pipeline into <code>telemetry_logs/honeypot_events.json</code>.",
        callout_style
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: SUITE ARCHITECTURE & MASTER CONTROL CONSOLE
    # =========================================================================
    story.append(Paragraph("4. Suite Architecture & Modular Control Interface", h1_style))
    story.append(Paragraph(
        "To provide a comprehensive instructional platform bridging offensive baiting awareness and defensive honeynet engineering, "
        "<b>PEER'S Watering Hole Shield Suite v2.5</b> was engineered into six modular subsystems accessible via an interactive command console:",
        body_style
    ))
    story.append(Paragraph(
        "• <b>Option 1 (Honeypot Server Verification):</b> Checks the operational health and reachability of the local honeypot gateway "
        "(<code>http://127.0.0.1:8080</code>), displaying active decoy routes.<br/>"
        "• <b>Option 2 (Automated Victim Interaction Simulator):</b> Simulates automated victim visits across 5 distinct persona profiles "
        "with diverse User-Agent strings and authentic HTTP Referer headers.<br/>"
        "• <b>Option 3 (Department Canary Token Generator):</b> Automatically generates unique, traceable tracking URLs for internal "
        "departments (Finance, HR, Engineering, Executive, Legal).<br/>"
        "• <b>Option 4 (SOC Telemetry Inspector):</b> Queries and displays captured victim fingerprints, client IP addresses, operating "
        "systems, browser families, and threat levels.<br/>"
        "• <b>Option 5 (Domain Watering Hole Risk Evaluator):</b> Performs automated security header assessments on external websites "
        "(checking SSL/TLS, Content Security Policy, and X-Frame-Options).<br/>"
        "• <b>Option 6 (Enterprise Defense Blueprint):</b> Displays actionable technical guidelines for Secure Web Gateway (SWG) egress "
        "filtering and Remote Browser Isolation (RBI).",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Figure 2: PEER'S Watering Hole Shield Master Control Console", h2_style))
    story.append(load_screenshot("02_master_menu.png"))
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 2:</b> Figure 2 illustrates the master operator interface. The readiness telemetry pane confirms "
        "that the Honeypot Listener Gateway is online, all 4 bait traps are armed, the Referer/Watering Hole Sensor is active, and the "
        "SOC Telemetry Repository is synchronized. The prompt provides clean, intuitive POSIX terminal navigation for SOC analysts.",
        callout_style
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: LIVE HONEYPOT GATEWAY & TRAP ROUTING EXECUTION
    # =========================================================================
    story.append(Paragraph("5. Live Honeypot Gateway & Passive Client Fingerprinting", h1_style))
    story.append(Paragraph(
        "The core honeypot server (<code>honeypot_server.py</code>) operates an enterprise Flask gateway that exposes four specialized "
        "bait endpoints designed to trap diverse attacker lures without executing dangerous payloads:<br/>"
        "1. <code>/download/vpn-update-v4.exe</code>: Simulates a classic drive-by digital bait disguised as a mandatory corporate VPN update.<br/>"
        "2. <code>/payroll/q4-executive-salaries.xlsx</code>: Exploits human curiosity through an executive compensation spreadsheet lure.<br/>"
        "3. <code>/vendor-portal/login</code>: Simulates a compromised third-party supplier portal used for credential harvesting.<br/>"
        "4. <code>/canary/<token_id></code>: Dynamic canary route attributing specific departmental leaks.",
        body_style
    ))
    story.append(Paragraph(
        "When an incoming HTTP request strikes any trap endpoint, the passive client fingerprinter extracts the real client IP (resolving "
        "<code>X-Forwarded-For</code> headers), parses the User-Agent into normalized OS and browser classes, extracts the vital "
        "<b>Referer</b> header (identifying the watering hole origin), and returns a safe educational alert landing page.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Figure 3: Live Honeypot Gateway & Trap Routing Server Execution", h2_style))
    story.append(load_screenshot("03_honeypot_server_live.png"))
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 3:</b> The terminal output in Figure 3 confirms active listener execution on port 8080. "
        "As incoming connections arrive, the gateway prints real-time alerts identifying the trap endpoint, client IP, referer origin "
        "(e.g., <code>trusted-vendor-news.org</code>), and client environment (Windows 10/11 Chrome, macOS Safari, Linux Firefox). "
        "Every event is simultaneously streamed to disk in structured JSON format.",
        callout_style
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 5: AUTOMATED VICTIM SIMULATION & ATTACK ATTRIBUTION
    # =========================================================================
    story.append(Paragraph("6. Automated Victim Interaction Simulation & Behavioral Footprints", h1_style))
    story.append(Paragraph(
        "To rigorously validate detection fidelity without requiring real employee exposure, the suite includes an automated victim "
        "simulation engine (<b>Option 2</b>). The client simulator issues automated HTTP GET requests across all active bait endpoints, "
        "rotating through realistic corporate victim personas:",
        body_style
    ))
    story.append(Paragraph(
        "• <b>Victim 1 (Corporate Workstation):</b> Windows 11 / Chrome visiting the fake VPN download lure, referred by a compromised "
        "vendor news portal (<code>trusted-vendor-news.org</code>).<br/>"
        "• <b>Victim 2 (Executive MacBook):</b> macOS / Safari accessing the confidential payroll spreadsheet lure, referred by an intranet "
        "catering lunch menu.<br/>"
        "• <b>Victim 3 (DevOps Engineer):</b> Linux / Firefox accessing the compromised third-party vendor portal, referred by a developer forum.<br/>"
        "• <b>Victims 4 & 5 (Finance & Mobile):</b> Targeted canary token endpoints capturing precise departmental leakage.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Figure 4: Automated Victim Bait Interaction Simulation", h2_style))
    story.append(load_screenshot("04_victim_client_sim.png"))
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 4:</b> Figure 4 depicts the automated simulation execution. All 5 simulated victim interactions "
        "were successfully trapped by the honeypot gateway with HTTP 200 responses. The simulation demonstrates the forensic utility of "
        "the <code>Referer</code> header in tracing the initial watering hole infection vector back to third-party supplier domains.",
        callout_style
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 6: SOC TELEMETRY INSPECTION & CANARY TRIPWIRES
    # =========================================================================
    story.append(Paragraph("7. In-Depth Incident Forensics & Departmental Canary Tripwires", h1_style))
    story.append(Paragraph(
        "SOC analysts require centralized, structured telemetry to correlate disparate alerts into a unified threat picture. "
        "Under <b>Option 4</b>, the suite queries the local SIEM repository (<code>telemetry_logs/honeypot_events.json</code>), displaying "
        "a consolidated tabular log of all trapped interactions.",
        body_style
    ))
    story.append(Paragraph(
        "Furthermore, <b>Option 3</b> enables administrators to generate <i>Canary Tokens</i>. By embedding unique tokens "
        "(e.g., <code>FINANCE-CANARY-01</code>) inside confidential internal spreadsheets, vendor portals, or email communications, "
        "any unauthorized access to the link instantly attributes the exact compromised department and client environment, functioning "
        "as an invisible early-warning tripwire.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Figure 5: SOC Incident Telemetry & Fingerprint Inspection", h2_style))
    story.append(load_screenshot("05_soc_telemetry_inspection.png"))
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 5:</b> Figure 5 shows the SOC telemetry console. Trapped events are categorized by Incident ID, "
        "client IP, parsed OS/Browser, bait trap name, and threat tier. A detailed deep-dive for Incident <code>HONEY-2026103120</code> "
        "highlights the captured watering hole host (<code>trusted-vendor-news.org</code>), target trojan path, and automated defensive "
        "directives dispatched to perimeter proxies.",
        callout_style
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 7: AUTOMATED UNIT TESTS, SWG DEFENSE & GITHUB REPO
    # =========================================================================
    story.append(Paragraph("8. Automated Unit Test Verification & Quality Assurance", h1_style))
    test_data = [
        [
            Paragraph("Test Method Identifier", table_header),
            Paragraph("Target Functional Component", table_header),
            Paragraph("Verification Metric", table_header),
            Paragraph("Result", table_header)
        ],
        [
            Paragraph("<code>test_vpn_download_bait_trap</code>", table_cell),
            Paragraph("Drive-by Bait Lure", table_cell),
            Paragraph("Confirms HTTP 200 & VPN decoy logging", table_cell),
            Paragraph("<font color='#0E703C'><b>PASSED</b></font>", table_cell)
        ],
        [
            Paragraph("<code>test_payroll_bait_trap</code>", table_cell),
            Paragraph("Curiosity Bait Trap", table_cell),
            Paragraph("Verifies payroll lure category tagging", table_cell),
            Paragraph("<font color='#0E703C'><b>PASSED</b></font>", table_cell)
        ],
        [
            Paragraph("<code>test_watering_hole_portal_trap</code>", table_cell),
            Paragraph("Watering Hole Referer Sensor", table_cell),
            Paragraph("Validates referer origin header capture", table_cell),
            Paragraph("<font color='#0E703C'><b>PASSED</b></font>", table_cell)
        ],
        [
            Paragraph("<code>test_canary_token_tracking</code>", table_cell),
            Paragraph("Canary Tripwire Engine", table_cell),
            Paragraph("Confirms unique token ID attribution", table_cell),
            Paragraph("<font color='#0E703C'><b>PASSED</b></font>", table_cell)
        ],
        [
            Paragraph("<code>test_client_fingerprinting</code>", table_cell),
            Paragraph("Passive Fingerprint Engine", table_cell),
            Paragraph("Accurately parses OS & Browser from UA", table_cell),
            Paragraph("<font color='#0E703C'><b>PASSED</b></font>", table_cell)
        ],
        [
            Paragraph("<code>test_soc_telemetry_endpoint</code>", table_cell),
            Paragraph("SIEM API Pipeline", table_cell),
            Paragraph("Verifies JSON export & log flush actions", table_cell),
            Paragraph("<font color='#0E703C'><b>PASSED</b></font>", table_cell)
        ]
    ]
    t_test = Table(test_data, colWidths=[150, 130, 190, 70])
    t_test.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_test)
    story.append(Spacer(1, 4))

    story.append(Paragraph("Figure 6: GitHub Repository Overview (PEER-S-Watering-Hole-Shield-Suite)", h2_style))
    story.append(load_screenshot("06_github_repo_overview.png", w=540, h=175))
    story.append(Spacer(1, 4))

    story.append(Paragraph("9. Enterprise Web Gateway Hardening & Mitigation Blueprint", h1_style))
    story.append(Paragraph(
        "<b>Multi-Layered Technical Defense Controls:</b> To defeat watering hole compromises, organizations must implement: "
        "(1) <i>Secure Web Gateways (SWG):</i> Enforce automated URL reputation filtering, sandboxing downloaded executables (`.exe`, `.iso`, `.zip`); "
        "(2) <i>Strict Content Security Policy (CSP):</i> Restrict cross-origin script execution (`script-src 'self'`) and block clickjacking (`frame-ancestors 'none'`); "
        "(3) <i>Remote Browser Isolation (RBI):</i> Isolate browser sessions for high-risk third-party portals in air-gapped disposable cloud containers; "
        "(4) <i>Continuous Endpoint Browser Patching:</i> Enforce daily automated browser updates to neutralize n-day drive-by exploits.<br/>"
        "<b>Ethical Research Notice:</b> All simulations, honeypot traps, and victim scripts were executed strictly within an authorized, "
        "air-gapped local laboratory sandbox. No actual malware or real-world targets were engaged during this research.",
        body_style
    ))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[+] Executive Lab Report PDF successfully compiled at:\n    {OUTPUT_PDF}")


if __name__ == "__main__":
    create_report()
