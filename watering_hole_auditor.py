#!/usr/bin/env python3
"""
================================================================================
PEER'S WATERING HOLE SHIELD SUITE v2.5 — Interactive Auditor & Client Simulator
Author      : Mohammed Peer Siddiqui
Organization: Sqrock IT Solutions — Cybersecurity Internship (Alpha 2 Cohort)
Track       : Social Engineering Attack Simulations Using Python (Day 10)
Standard    : MITRE ATT&CK T1189 (Drive-by Compromise) | NIST SP 800-53 (SI-3, SI-4)
================================================================================
"""

import os
import sys
import time
import json
import threading
import requests
from colorama import Fore, Style, init

init(autoreset=True)

BANNER = f"""
{Fore.CYAN}██╗    ██╗ █████╗ ████████╗███████╗██████╗ ██╗███╗   ██╗ ██████╗ 
{Fore.CYAN}██║    ██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██║████╗  ██║██╔════╝ 
{Fore.CYAN}██║ █╗ ██║███████║   ██║   █████╗  ██████╔╝██║██╔██╗ ██║██║  ███╗
{Fore.BLUE}██║███╗██║██╔══██║   ██║   ██╔══╝  ██╔══██╗██║██║╚██╗██║██║   ██║
{Fore.BLUE}╚███╔███╔╝██║  ██║   ██║   ███████╗██║  ██║██║██║ ╚████║╚██████╔╝
{Fore.BLUE} ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
{Fore.MAGENTA}  [+] DIGITAL BAITING & WATERING HOLE DEFENSE SUITE v2.5
{Fore.LIGHTBLACK_EX}  [+] Author: Mohammed Peer Siddiqui | Sqrock IT Solutions Alpha 2
  [+] Standard: MITRE ATT&CK T1189 | NIST SP 800-53 (SI-3, SI-4) | CIS Control 9.2
==============================================================================={Style.RESET_ALL}"""

SERVER_URL = "http://127.0.0.1:8080"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "telemetry_logs", "honeypot_events.json")

# Predefined Simulated Victims with diverse User-Agents and Referer headers
VICTIM_PROFILES = [
    {
        "label": "Corporate Workstation (Windows 11 / Chrome)",
        "endpoint": "/download/vpn-update-v4.exe",
        "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "referer": "http://trusted-vendor-news.org/articles/securing-remote-work"
    },
    {
        "label": "Executive MacBook (macOS / Safari)",
        "endpoint": "/payroll/q4-executive-salaries.xlsx",
        "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15",
        "referer": "http://intranet-lunch-menu.sqrock-catering.com/weekly-specials"
    },
    {
        "label": "DevOps Engineer (Linux / Firefox)",
        "endpoint": "/vendor-portal/login",
        "ua": "Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
        "referer": "http://developer-tools-forum.net/threads/infrastructure-monitoring"
    },
    {
        "label": "Finance Department Lead (Canary Trap)",
        "endpoint": "/canary/FINANCE-CANARY-01",
        "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "referer": "http://partner-billing-gateway.com/invoices/october"
    },
    {
        "label": "Mobile Field Consultant (iOS / Safari)",
        "endpoint": "/canary/IT-SUPPORT-CANARY-02",
        "ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
        "referer": "http://airport-wifi-portal.net/guest-login"
    }
]


def check_server_status():
    """Checks if the local honeypot server is reachable."""
    try:
        r = requests.get(SERVER_URL, timeout=1.5)
        return r.status_code == 200
    except Exception:
        return False


def simulate_victim_interactions():
    """
    Simulates automated victim visits against honeypot traps.
    Demonstrates diverse User-Agents and HTTP Referer headers.
    """
    if not check_server_status():
        print(f"{Fore.RED}[-] Honeypot Server is offline at {SERVER_URL}. Start it first (Option 1 or 'python honeypot_server.py').{Style.RESET_ALL}")
        return

    print(f"\n{Fore.YELLOW}[*] Executing automated victim interaction simulation across 5 endpoints...{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'#':<3} {'Victim Persona':<32} {'Target Bait Endpoint':<34} {'Status':<8}{Style.RESET_ALL}")
    print("-" * 80)

    for idx, v in enumerate(VICTIM_PROFILES, 1):
        target = f"{SERVER_URL}{v['endpoint']}"
        headers = {
            "User-Agent": v["ua"],
            "Referer": v["referer"]
        }
        try:
            r = requests.get(target, headers=headers, timeout=2.0)
            status_str = f"{Fore.GREEN}TRAPPED ({r.status_code}){Style.RESET_ALL}"
            print(f"{idx:<3} {v['label']:<32} {v['endpoint']:<34} {status_str}")
        except Exception as e:
            print(f"{idx:<3} {v['label']:<32} {v['endpoint']:<34} {Fore.RED}ERROR ({e}){Style.RESET_ALL}")
        time.sleep(0.3)

    print("-" * 80)
    print(f"{Fore.GREEN}[+] All 5 simulated victim interactions trapped and logged to SOC repository.{Style.RESET_ALL}")


def generate_canary_tokens():
    """Generates department-specific canary tracking tokens."""
    departments = ["Finance & Payroll", "Engineering & DevOps", "Human Resources", "Executive C-Suite", "Legal & Compliance"]
    print(f"\n{Fore.YELLOW}[*] Generating Departmental Canary Tokens for Tripwire Monitoring:{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'Department':<26} {'Token ID':<24} {'Tracked Honeypot URL'}{Style.RESET_ALL}")
    print("-" * 80)
    
    tokens = []
    for dept in departments:
        clean_tag = dept.split()[0].upper()
        tok = f"{clean_tag}-CANARY-{int(time.time()) % 10000:04d}"
        url = f"{SERVER_URL}/canary/{tok}"
        tokens.append({"department": dept, "token": tok, "url": url})
        print(f"{dept:<26} {tok:<24} {Fore.GREEN}{url}{Style.RESET_ALL}")

    print("-" * 80)
    print(f"{Fore.LIGHTCYAN_EX}[i] Operational Note: Plant these canary URLs in sensitive internal wikis or vendor memos.{Style.RESET_ALL}")
    return tokens


def inspect_soc_telemetry():
    """Inspects and displays recorded honeypot telemetry events."""
    if not os.path.exists(LOG_FILE):
        print(f"{Fore.YELLOW}[i] No incident telemetry found in {LOG_FILE}. Run Option 2 first.{Style.RESET_ALL}")
        return

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            events = json.load(f)
    except Exception as e:
        print(f"{Fore.RED}[-] Failed to read telemetry logs: {e}{Style.RESET_ALL}")
        return

    if not events:
        print(f"{Fore.YELLOW}[i] Incident log is empty. Trigger some traps to populate events.{Style.RESET_ALL}")
        return

    print(f"\n{Fore.GREEN}[+] Total Trapped Incident Events: {len(events)}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'ID':<18} {'Client IP':<16} {'OS / Browser':<24} {'Bait Trap':<28} {'Threat'}{Style.RESET_ALL}")
    print("-" * 96)

    for ev in events:
        env_str = f"{ev.get('client_os', 'Unknown')[:10]}/{ev.get('client_browser', 'Unknown')[:11]}"
        threat_col = Fore.RED if ev.get("threat_level") == "CRITICAL" else Fore.YELLOW
        print(f"{ev.get('event_id', 'N/A'):<18} {ev.get('client_ip', 'N/A'):<16} {env_str:<24} {ev.get('bait_name', 'N/A')[:28]:<28} {threat_col}{ev.get('threat_level', 'HIGH')}{Style.RESET_ALL}")

    print("-" * 96)
    print(f"{Fore.LIGHTCYAN_EX}[i] Detailed referer origins and User-Agent telemetry persisted at: {LOG_FILE}{Style.RESET_ALL}")


def evaluate_domain_watering_hole_risk(url):
    """
    Evaluates a third-party website's susceptibility to being compromised
    as a watering hole target (checking HTTPS, CSP, and security headers).
    """
    print(f"\n{Fore.YELLOW}[*] Evaluating watering hole compromise risk for: {url}...{Style.RESET_ALL}")
    try:
        r = requests.get(url, timeout=3.0)
        headers = r.headers
        
        has_csp = "Content-Security-Policy" in headers
        has_hsts = "Strict-Transport-Security" in headers
        has_xframe = "X-Frame-Options" in headers or "frame-ancestors" in headers.get("Content-Security-Policy", "")
        
        score = 0
        issues = []
        
        if not url.startswith("https://"):
            score += 40
            issues.append("MISSING_ENCRYPTION: Unencrypted HTTP connection (Vulnerable to MITM injection)")
        if not has_csp:
            score += 30
            issues.append("MISSING_CSP: No Content Security Policy (Vulnerable to rogue script injection)")
        if not has_xframe:
            score += 20
            issues.append("MISSING_FRAME_PROTECTION: Vulnerable to clickjacking / invisible iFrame injection")
            
        score = min(score, 100)
        verdict = "HIGH_WATERING_HOLE_RISK" if score >= 50 else ("MODERATE_RISK" if score > 0 else "HARDENED_PORTAL")
        col = Fore.RED if score >= 50 else (Fore.YELLOW if score > 0 else Fore.GREEN)
        
        print(f"{Fore.GREEN}[+] Security Assessment Complete:{Style.RESET_ALL}")
        print(f"  • Domain Target   : {url}")
        print(f"  • Vulnerability   : {col}{score} / 100 ({verdict}){Style.RESET_ALL}")
        print(f"  • CSP Header      : {'Active' if has_csp else 'Missing'}")
        print(f"  • HSTS Status     : {'Active' if has_hsts else 'Missing'}")
        
        if issues:
            print(f"\n{Fore.RED}[!] Security Deficiencies Identified:{Style.RESET_ALL}")
            for iss in issues:
                print(f"    └── [x] {iss}")
    except Exception as e:
        print(f"{Fore.RED}[-] Assessment failed: {e}{Style.RESET_ALL}")


def print_menu():
    print(f"\n{Fore.LIGHTBLACK_EX}--- [ PEER'S WATERING HOLE SHIELD CONTROL CONSOLE ] ---{Style.RESET_ALL}")
    print(f"  {Fore.CYAN}[1]{Fore.WHITE} Verify Local Honeypot Server Status ({SERVER_URL})")
    print(f"  {Fore.CYAN}[2]{Fore.WHITE} Simulate Automated Victim Bait Interactions (5 Diverse Personas)")
    print(f"  {Fore.CYAN}[3]{Fore.WHITE} Generate Department-Specific Canary Tracking Tokens")
    print(f"  {Fore.CYAN}[4]{Fore.WHITE} Inspect Live SOC Honeypot Telemetry & Client Fingerprints")
    print(f"  {Fore.CYAN}[5]{Fore.WHITE} Evaluate Website Watering Hole Risk & Drive-by Vulnerability")
    print(f"  {Fore.CYAN}[6]{Fore.WHITE} Display Enterprise Web Gateway & Watering Hole Defense Blueprint")
    print(f"  {Fore.CYAN}[7]{Fore.RED} Exit Suite")


def interactive_cli():
    print(BANNER)
    while True:
        print_menu()
        choice = input(f"\n{Fore.GREEN}sqrock@watering-shield{Fore.WHITE}:{Fore.BLUE}~/honeypot-defense{Fore.WHITE}$ ").strip()

        if choice == "1":
            is_up = check_server_status()
            if is_up:
                print(f"\n{Fore.GREEN}[+] Honeypot Server is ONLINE and actively listening on {SERVER_URL}{Style.RESET_ALL}")
                print(f"    Available Decoys: /download/vpn-update-v4.exe, /payroll/q4-executive-salaries.xlsx, /vendor-portal/login")
            else:
                print(f"\n{Fore.RED}[-] Honeypot Server is OFFLINE.{Style.RESET_ALL}")
                print(f"    Run '{Fore.YELLOW}python honeypot_server.py{Fore.WHITE}' in a separate terminal to launch.")

        elif choice == "2":
            simulate_victim_interactions()

        elif choice == "3":
            generate_canary_tokens()

        elif choice == "4":
            inspect_soc_telemetry()

        elif choice == "5":
            target = input(f"{Fore.YELLOW}Enter URL to evaluate (e.g., http://testphp.vulnweb.com): {Style.RESET_ALL}").strip()
            if target:
                evaluate_domain_watering_hole_risk(target)

        elif choice == "6":
            print(f"\n{Fore.CYAN}==============================================================================={Style.RESET_ALL}")
            print(f"{Fore.GREEN}    ENTERPRISE WATERING HOLE & DRIVE-BY DOWNLOAD DEFENSE BLUEPRINT             {Style.RESET_ALL}")
            print(f"{Fore.CYAN}==============================================================================={Style.RESET_ALL}")
            print(f"""
{Fore.YELLOW}1. Secure Web Gateway (SWG) & Egress Filtering:{Fore.WHITE}
   - Inspect all outbound employee web traffic for malicious redirect chains.
   - Restrict direct executable downloads (.exe, .scr, .iso) from unclassified domains.

{Fore.YELLOW}2. Content Security Policy (CSP) & Script Sandboxing:{Fore.WHITE}
   - Enforce strict CSP headers preventing unauthorized cross-origin script execution.
   - Implement Remote Browser Isolation (RBI) for untrusted vendor portals.

{Fore.YELLOW}3. Canary Tokens as Early Warning Tripwires:{Fore.WHITE}
   - Seed department-unique canary URLs inside corporate documentation and vendor chats.
   - Instant SOC alert triggered upon the first unauthorized request.

{Fore.YELLOW}4. Rapid Browser & Endpoint Patch Management:{Fore.WHITE}
   - Drive-by downloads rely heavily on unpatched browser and plugin vulnerabilities.
   - Enforce automated daily browser updates (Chrome/Edge/Firefox) with zero deferral.
""")

        elif choice == "7":
            print(f"\n{Fore.CYAN}[+] Exiting PEER'S Watering Hole Shield Suite. Monitoring active.{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}[-] Invalid option. Please select 1 through 7.{Style.RESET_ALL}")


if __name__ == "__main__":
    interactive_cli()
