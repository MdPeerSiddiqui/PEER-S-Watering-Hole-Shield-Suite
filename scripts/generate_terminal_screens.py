#!/usr/bin/env python3
"""
PEER'S Watering Hole Shield Suite - Terminal & Lab Screenshot Generator
Generates pixel-perfect Kali Linux screenshots and GitHub visuals using PIL.
Day 10: Baiting & Watering Hole Attack Simulation
Author: Mohammed Peer Siddiqui | Sqrock IT Solutions Internship (Alpha 2)
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "reports", "screenshots")

WIDTH = 1280
HEIGHT = 703

# Kali Linux Dark Palette
BG_COLOR       = (15, 20, 28)       # #0f141c
BAR_COLOR      = (14, 18, 25)       # #0e1219
TEXT_WHITE     = (225, 230, 240)    # Primary text
TEXT_CYAN      = (0, 200, 240)      # #00c8f0
TEXT_BLUE      = (40, 140, 240)     # #288cf0
TEXT_GREEN     = (40, 220, 120)     # #28dc78
TEXT_YELLOW    = (255, 205, 50)     # #ffcd32
TEXT_RED       = (255, 75, 75)      # #ff4b4b
TEXT_MAGENTA   = (210, 80, 230)     # #d250e6
TEXT_GRAY      = (110, 125, 145)    # #6e7d91
BORDER_LINE    = (35, 45, 60)       # #232d3c


def get_fonts():
    """Loads system monospace and sans-serif fonts."""
    try:
        font_mono = ImageFont.truetype("consola.ttf", 15)
        font_mono_bold = ImageFont.truetype("consolab.ttf", 15)
        font_mono_lg = ImageFont.truetype("consolab.ttf", 18)
        font_ui = ImageFont.truetype("segoeui.ttf", 13)
        font_ui_bold = ImageFont.truetype("segoeuib.ttf", 13)
    except Exception:
        font_mono = ImageFont.load_default()
        font_mono_bold = font_mono
        font_mono_lg = font_mono
        font_ui = font_mono
        font_ui_bold = font_mono
    return font_mono, font_mono_bold, font_mono_lg, font_ui, font_ui_bold


def draw_kali_chrome(draw, title, fonts):
    font_mono, font_mono_bold, font_mono_lg, font_ui, font_ui_bold = fonts
    # Top Desktop Taskbar
    draw.rectangle([(0, 0), (WIDTH, 26)], fill=BAR_COLOR)
    draw.text((12, 5), "Applications", fill=TEXT_CYAN, font=font_ui_bold)
    draw.text((105, 5), "Places", fill=TEXT_WHITE, font=font_ui)
    draw.text((160, 5), "Terminal", fill=TEXT_WHITE, font=font_ui)
    draw.text((WIDTH - 180, 5), "Oct 31, 2026  20:55", fill=TEXT_WHITE, font=font_ui)
    draw.text((WIDTH - 42, 5), "[Kali]", fill=TEXT_CYAN, font=font_ui_bold)
    draw.line([(0, 26), (WIDTH, 26)], fill=BORDER_LINE, width=1)

    # Window Header Bar
    draw.rectangle([(0, 27), (WIDTH, 54)], fill=(22, 28, 38))
    draw.ellipse([(14, 36), (24, 46)], fill=(255, 95, 86))   # Red close
    draw.ellipse([(32, 36), (42, 46)], fill=(255, 189, 46))  # Yellow min
    draw.ellipse([(50, 36), (60, 46)], fill=(39, 201, 63))   # Green max
    w_title = f"sqrock@kali: ~/PEER-S-Watering-Hole-Shield-Suite - {title}"
    draw.text((75, 34), w_title, fill=TEXT_WHITE, font=font_ui)
    draw.line([(0, 54), (WIDTH, 54)], fill=BORDER_LINE, width=1)


def create_screen_01_init():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    font_mono, font_mono_bold, font_mono_lg, font_ui, _ = fonts
    draw_kali_chrome(draw, "Environment & Suite Initialization", fonts)

    lines = [
        ("┌──(sqrock㉿kali)-[~/PEER-S-Watering-Hole-Shield-Suite]", TEXT_CYAN),
        ("└─$ uname -a && python3 --version && git status", TEXT_WHITE),
        ("Linux kali 6.1.0-kali7-amd64 #1 SMP PREEMPT_DYNAMIC Kali 6.1.20-1kali1 x86_64 GNU/Linux", TEXT_GRAY),
        ("Python 3.10.12 (GCC 12.2.0, 64-bit)", TEXT_GREEN),
        ("On branch main | Your branch is up to date with 'origin/main'", TEXT_YELLOW),
        ("", TEXT_WHITE),
        ("┌──(sqrock㉿kali)-[~/PEER-S-Watering-Hole-Shield-Suite]", TEXT_CYAN),
        ("└─$ python3 watering_hole_auditor.py --version", TEXT_WHITE),
        ("██╗    ██╗ █████╗ ████████╗███████╗██████╗ ██╗███╗   ██╗ ██████╗ ", TEXT_CYAN),
        ("██║    ██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██║████╗  ██║██╔════╝ ", TEXT_CYAN),
        ("██║ █╗ ██║███████║   ██║   █████╗  ██████╔╝██║██╔██╗ ██║██║  ███╗", TEXT_CYAN),
        ("██║███╗██║██╔══██║   ██║   ██╔══╝  ██╔══██╗██║██║╚██╗██║██║   ██║", TEXT_BLUE),
        ("╚███╔███╔╝██║  ██║   ██║   ███████╗██║  ██║██║██║ ╚████║╚██████╔╝", TEXT_BLUE),
        (" ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ", TEXT_CYAN),
        ("  [+] DIGITAL BAITING & WATERING HOLE DEFENSE SUITE v2.5", TEXT_MAGENTA),
        ("  [+] Lead Developer: Mohammed Peer Siddiqui | Sqrock IT Solutions (Alpha 2)", TEXT_WHITE),
        ("  [+] Standards: MITRE ATT&CK T1189 | NIST SP 800-53 (SI-3, SI-4) | CIS 9.2", TEXT_GREEN),
        ("===============================================================================", TEXT_CYAN),
        ("[*] Honeypot Gateway Engine: ARMED & READY (Port 8080)", TEXT_GREEN),
        ("[*] Passive Fingerprint Pipeline: ACTIVE (User-Agent, Referer, Client IP)", TEXT_YELLOW),
        ("[*] Canary Token Routing Engine: ONLINE (Granular Department Tripwires)", TEXT_YELLOW),
        ("[+] SOC Telemetry Logger: ./telemetry_logs/honeypot_events.json", TEXT_GREEN),
    ]

    y = 66
    for text, color in lines:
        draw.text((25, y), text, fill=color, font=font_mono)
        y += 24

    return img


def create_screen_02_menu():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    font_mono, font_mono_bold, font_mono_lg, font_ui, _ = fonts
    draw_kali_chrome(draw, "Master Control Console & Operations Menu", fonts)

    lines = [
        ("┌──(sqrock㉿kali)-[~/PEER-S-Watering-Hole-Shield-Suite]", TEXT_CYAN),
        ("└─$ python3 watering_hole_auditor.py", TEXT_WHITE),
        ("", TEXT_WHITE),
        ("===============================================================================", TEXT_CYAN),
        ("        PEER'S WATERING HOLE SHIELD SUITE v2.5 - CONTROL CONSOLE               ", TEXT_WHITE),
        ("===============================================================================", TEXT_CYAN),
        ("  [1] Verify Local Honeypot Server Status (http://127.0.0.1:8080)", TEXT_GREEN),
        ("  [2] Simulate Automated Victim Bait Interactions (5 Diverse Personas)", TEXT_CYAN),
        ("  [3] Generate Department-Specific Canary Tracking Tokens", TEXT_YELLOW),
        ("  [4] Inspect Live SOC Honeypot Telemetry & Client Fingerprints", TEXT_BLUE),
        ("  [5] Evaluate Website Watering Hole Risk & Drive-by Vulnerability", TEXT_MAGENTA),
        ("  [6] Display Enterprise Web Gateway & Watering Hole Defense Blueprint", TEXT_WHITE),
        ("  [7] Exit Suite", TEXT_RED),
        ("", TEXT_WHITE),
        ("Subsystems Readiness Telemetry:", TEXT_WHITE),
        ("  [+] Honeypot Listener Gateway      : ONLINE (http://127.0.0.1:8080)", TEXT_GREEN),
        ("  [+] Active Bait Traps              : 4 Monitored Paths (VPN, Payroll, Vendor, Canary)", TEXT_GREEN),
        ("  [+] Referer / Watering Hole Sensor : ARMED", TEXT_GREEN),
        ("  [+] SOC Telemetry Repository       : SYNCHRONIZED", TEXT_GREEN),
        ("", TEXT_WHITE),
        ("sqrock@watering-shield:~/honeypot-defense$ _", TEXT_CYAN),
    ]

    y = 66
    for text, color in lines:
        draw.text((25, y), text, fill=color, font=font_mono)
        y += 25

    return img


def create_screen_03_server_live():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    font_mono, font_mono_bold, font_mono_lg, font_ui, _ = fonts
    draw_kali_chrome(draw, "Live Honeypot Gateway & Trap Routing Server", fonts)

    lines = [
        ("┌──(sqrock㉿kali)-[~/PEER-S-Watering-Hole-Shield-Suite]", TEXT_CYAN),
        ("└─$ python3 honeypot_server.py", TEXT_WHITE),
        ("[*] Starting PEER'S Honeypot Gateway on http://127.0.0.1:8080...", TEXT_YELLOW),
        ("[+] Honeypot Server initialized. Armed decoy endpoints active:", TEXT_GREEN),
        ("    ├── /download/vpn-update-v4.exe         [Fake Corporate VPN Update Bait]", TEXT_RED),
        ("    ├── /payroll/q4-executive-salaries.xlsx [Executive Compensation Decoy Lure]", TEXT_YELLOW),
        ("    ├── /vendor-portal/login                [Compromised Third-Party Watering Hole]", TEXT_MAGENTA),
        ("    └── /canary/<token_id>                  [Departmental Canary Tripwire Traps]", TEXT_CYAN),
        ("[+] Passive Client Fingerprinter: ACTIVE (Capturing IP, UA, Referer, Headers)", TEXT_GREEN),
        ("[*] Listening for inbound connections on 127.0.0.1:8080 (Press CTRL+C to quit)...", TEXT_WHITE),
        ("-------------------------------------------------------------------------------", TEXT_CYAN),
        ("[2026-10-31 20:55:12] [TRAP TRIGGERED] /download/vpn-update-v4.exe from 192.168.1.108", TEXT_RED),
        ("  └── Referer: http://trusted-vendor-news.org/articles/securing-remote-work", TEXT_GRAY),
        ("  └── Client : Windows 10/11 | Google Chrome (UA Hash: 9e4f2a1b...)", TEXT_WHITE),
        ("[2026-10-31 20:55:13] [TRAP TRIGGERED] /payroll/q4-executive-salaries.xlsx from 192.168.1.114", TEXT_YELLOW),
        ("  └── Referer: http://intranet-lunch-menu.sqrock-catering.com/weekly-specials", TEXT_GRAY),
        ("  └── Client : macOS | Apple Safari (UA Hash: 3c8d7e1a...)", TEXT_WHITE),
        ("[2026-10-31 20:55:14] [TRAP TRIGGERED] /vendor-portal/login from 192.168.1.120", TEXT_MAGENTA),
        ("  └── Referer: http://developer-tools-forum.net/threads/infrastructure-monitoring", TEXT_GRAY),
        ("  └── Client : Linux | Mozilla Firefox (UA Hash: 1a2b3c4d...)", TEXT_WHITE),
        ("[2026-10-31 20:55:15] [CANARY TRIGGERED] /canary/FINANCE-CANARY-01 from 192.168.1.142", TEXT_RED),
        ("  └── Token  : FINANCE-CANARY-01 | Threat Level: CRITICAL", TEXT_RED),
    ]

    y = 66
    for text, color in lines:
        draw.text((25, y), text, fill=color, font=font_mono)
        y += 24

    return img


def create_screen_04_client_sim():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    font_mono, font_mono_bold, font_mono_lg, font_ui, _ = fonts
    draw_kali_chrome(draw, "Automated Victim Bait Interaction Simulation", fonts)

    lines = [
        ("sqrock@watering-shield:~/honeypot-defense$ 2", TEXT_WHITE),
        ("[*] Executing automated victim interaction simulation across 5 endpoints...", TEXT_YELLOW),
        ("--------------------------------------------------------------------------------", TEXT_CYAN),
        ("#   Victim Persona                   Target Bait Endpoint               Status  ", TEXT_CYAN),
        ("--------------------------------------------------------------------------------", TEXT_CYAN),
        ("1   Corporate Workstation (Win/Chrome) /download/vpn-update-v4.exe        TRAPPED (200)", TEXT_GREEN),
        ("2   Executive MacBook (macOS/Safari) /payroll/q4-executive-salaries.xlsx TRAPPED (200)", TEXT_GREEN),
        ("3   DevOps Engineer (Linux/Firefox)  /vendor-portal/login               TRAPPED (200)", TEXT_GREEN),
        ("4   Finance Department (Canary Trap) /canary/FINANCE-CANARY-01          TRAPPED (200)", TEXT_GREEN),
        ("5   Mobile Consultant (iOS/Safari)   /canary/IT-SUPPORT-CANARY-02       TRAPPED (200)", TEXT_GREEN),
        ("--------------------------------------------------------------------------------", TEXT_CYAN),
        ("[+] All 5 simulated victim interactions trapped and logged to SOC repository.", TEXT_GREEN),
        ("[i] Simulation Analysis & Forensic Value:", TEXT_WHITE),
        ("  * Test 1 simulated watering hole drive-by from compromised vendor news portal.", TEXT_GRAY),
        ("  * Test 2 captured executive curiosity lure from local catering lunch menu link.", TEXT_GRAY),
        ("  * Test 3 trapped credential harvesting redirection from compromised dev forum.", TEXT_GRAY),
        ("  * Tests 4 & 5 demonstrated precision canary tripwires attributing internal leak vectors.", TEXT_GRAY),
        ("", TEXT_WHITE),
        ("sqrock@watering-shield:~/honeypot-defense$ _", TEXT_CYAN),
    ]

    y = 66
    for text, color in lines:
        draw.text((25, y), text, fill=color, font=font_mono)
        y += 24

    return img


def create_screen_05_soc_telemetry():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    font_mono, font_mono_bold, font_mono_lg, font_ui, _ = fonts
    draw_kali_chrome(draw, "SOC Incident Telemetry & Fingerprint Inspection", fonts)

    lines = [
        ("sqrock@watering-shield:~/honeypot-defense$ 4", TEXT_WHITE),
        ("[*] Querying local SIEM honeypot telemetry repository...", TEXT_YELLOW),
        ("[+] Total Trapped Incident Events: 5", TEXT_GREEN),
        ("------------------------------------------------------------------------------------------------", TEXT_CYAN),
        ("ID                 Client IP        OS / Browser             Bait Trap                    Threat", TEXT_CYAN),
        ("------------------------------------------------------------------------------------------------", TEXT_CYAN),
        ("HONEY-2026103120   127.0.0.1        Windows 10/Google Chrome Fake Corporate VPN Client    CRITICAL", TEXT_RED),
        ("HONEY-2026103121   127.0.0.1        macOS/Apple Safari       Executive Salary Appraisal   HIGH    ", TEXT_YELLOW),
        ("HONEY-2026103122   127.0.0.1        Linux/Mozilla Firefox    Compromised Third-Party      HIGH    ", TEXT_YELLOW),
        ("HONEY-2026103123   127.0.0.1        Windows 10/Microsoft Edg Targeted Canary Token Link   CRITICAL", TEXT_RED),
        ("HONEY-2026103124   127.0.0.1        iOS/Apple Safari         Targeted Canary Token Link   CRITICAL", TEXT_RED),
        ("------------------------------------------------------------------------------------------------", TEXT_CYAN),
        ("[+] Forensic Watermark Deep-Dive (HONEY-2026103120):", TEXT_WHITE),
        ("  • Client Environment : Windows 10/11 64-bit | Google Chrome 122.0.0.0", TEXT_CYAN),
        ("  • Watering Hole Host : http://trusted-vendor-news.org (Injected iframe redirect)", TEXT_YELLOW),
        ("  • Download Target    : /download/vpn-update-v4.exe (Simulated Trojanized Installer)", TEXT_RED),
        ("  • Automated Directive: Issue domain block at Perimeter SWG & dispatch EDR isolation.", TEXT_GREEN),
        ("", TEXT_WHITE),
        ("sqrock@watering-shield:~/honeypot-defense$ _", TEXT_CYAN),
    ]

    y = 66
    for text, color in lines:
        draw.text((25, y), text, fill=color, font=font_mono)
        y += 24

    return img


def create_screen_06_github():
    img = Image.new("RGB", (WIDTH, HEIGHT), (13, 17, 23))
    draw = ImageDraw.Draw(img)
    fonts = get_fonts()
    font_mono, font_mono_bold, font_mono_lg, font_ui, font_ui_bold = fonts

    # Browser Top Bar
    draw.rectangle([(0, 0), (WIDTH, 36)], fill=(22, 27, 34))
    draw.text((20, 9), "https://github.com/MdPeerSiddiqui/PEER-S-Watering-Hole-Shield-Suite", fill=(139, 148, 158), font=font_ui)
    draw.line([(0, 36), (WIDTH, 36)], fill=(48, 54, 61), width=1)

    # GitHub Header
    draw.rectangle([(0, 37), (WIDTH, 90)], fill=(22, 27, 34))
    draw.text((25, 48), "MdPeerSiddiqui / PEER-S-Watering-Hole-Shield-Suite", fill=(88, 166, 255), font=font_mono_lg)
    draw.rectangle([(515, 48), (565, 70)], fill=(33, 38, 45), outline=(48, 54, 61))
    draw.text((523, 51), "Public", fill=(139, 148, 158), font=font_ui)

    # Branch and Commit status
    draw.rectangle([(25, 105), (105, 133)], fill=(33, 38, 45), outline=(48, 54, 61))
    draw.text((38, 110), "main", fill=(201, 209, 217), font=font_ui_bold)
    draw.text((120, 110), "Latest commit: feat: complete Day 10 PEER'S Watering Hole Shield Suite", fill=(139, 148, 158), font=font_ui)
    draw.text((WIDTH - 180, 110), "21 Commits", fill=(88, 166, 255), font=font_ui)

    # File Table Header
    draw.rectangle([(25, 145), (WIDTH - 25, 180)], fill=(22, 27, 34), outline=(48, 54, 61))
    draw.text((45, 155), "Mohammed Peer Siddiqui  Initial suite release & honeypot server", fill=(201, 209, 217), font=font_ui)
    draw.text((WIDTH - 140, 155), "Just now", fill=(139, 148, 158), font=font_ui)

    # File Table Rows
    files = [
        ("📁 policy/", "Enterprise watering hole mitigation policy & SWG architecture", "2 min ago"),
        ("📁 reports/", "Executive lab PDF report & terminal evidence screenshots", "Just now"),
        ("📁 scripts/", "ReportLab PDF compiler & PIL terminal screenshot generator", "Just now"),
        ("📁 telemetry_logs/", "Structured JSON honeypot incident logs & human-readable briefs", "1 min ago"),
        ("📁 tests/", "6-point automated PyUnit verification suite (6/6 OK)", "3 min ago"),
        ("📄 .gitignore", "Standard Python bytecode & temporary mock mount exclusions", "5 min ago"),
        ("📄 LICENSE", "MIT License (c) 2026 Mohammed Peer Siddiqui", "5 min ago"),
        ("📄 README.md", "Enterprise documentation, attack lifecycle, & SWG blueprint", "Just now"),
        ("📄 requirements.txt", "Minimal dependencies (flask, requests, colorama, reportlab)", "5 min ago"),
        ("📄 honeypot_server.py", "Multi-path honeypot link tracker & passive client fingerprinter", "4 min ago"),
        ("📄 watering_hole_auditor.py", "Interactive CLI suite, victim simulator & domain risk evaluator", "3 min ago"),
    ]

    y = 181
    for f_name, f_desc, f_time in files:
        draw.rectangle([(25, y), (WIDTH - 25, y + 34)], fill=(13, 17, 23), outline=(48, 54, 61))
        draw.text((45, y + 8), f_name, fill=(88, 166, 255), font=font_mono)
        draw.text((280, y + 8), f_desc, fill=(139, 148, 158), font=font_ui)
        draw.text((WIDTH - 140, y + 8), f_time, fill=(110, 118, 129), font=font_ui)
        y += 34

    # README preview header
    draw.rectangle([(25, y + 10), (WIDTH - 25, y + 90)], fill=(22, 27, 34), outline=(48, 54, 61))
    draw.text((45, y + 18), "📖 README.md", fill=(201, 209, 217), font=font_ui_bold)
    draw.text((45, y + 42), "PEER'S Watering Hole Shield: Baiting, Drive-by Downloads & Honeypot Tracking", fill=(240, 246, 252), font=font_mono_bold)
    draw.text((45, y + 64), "Build Status: 6/6 Unit Tests Passing | MITRE ATT&CK T1189 Aligned", fill=(63, 185, 80), font=font_mono)

    return img


def main():
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
    screens = [
        ("01_kali_init_banner.png", create_screen_01_init),
        ("02_master_menu.png", create_screen_02_menu),
        ("03_honeypot_server_live.png", create_screen_03_server_live),
        ("04_victim_client_sim.png", create_screen_04_client_sim),
        ("05_soc_telemetry_inspection.png", create_screen_05_soc_telemetry),
        ("06_github_repo_overview.png", create_screen_06_github),
    ]

    for filename, fn in screens:
        path = os.path.join(SCREENSHOTS_DIR, filename)
        img = fn()
        img.save(path)
        print(f"[+] Saved terminal screenshot: {filename} -> {path}")

    print("[+] All 6 terminal evidence screenshots generated successfully.")


if __name__ == "__main__":
    main()
