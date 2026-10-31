#!/usr/bin/env python3
"""
================================================================================
PEER'S WATERING HOLE SHIELD SUITE v2.5 — Honeypot Link Tracker & Gateway
Author      : Mohammed Peer Siddiqui
Organization: Sqrock IT Solutions — Cybersecurity Internship (Alpha 2 Cohort)
Track       : Social Engineering Attack Simulations Using Python (Day 10)
Standard    : MITRE ATT&CK T1189 (Drive-by Compromise) | NIST SP 800-53 (SI-3, SI-4)
================================================================================
"""

import os
import sys
import json
import datetime
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGS_DIR = os.path.join(BASE_DIR, "telemetry_logs")
JSON_LOG = os.path.join(LOGS_DIR, "honeypot_events.json")
TXT_LOG = os.path.join(LOGS_DIR, "honeypot_events.txt")

# In-memory incident buffer
INCIDENT_LOGS = []


def ensure_directories():
    """Ensure telemetry directory exists."""
    os.makedirs(LOGS_DIR, exist_ok=True)


def parse_user_agent(ua_string):
    """
    Parses client User-Agent string into normalized OS and Browser classifications.
    Identifies automated bots, curl/python scripts, and legitimate user agents.
    """
    ua = ua_string.lower()
    
    # Detect Operating System
    if "windows nt 10.0" in ua or "windows 10" in ua or "windows 11" in ua:
        os_type = "Windows 10/11"
    elif "windows" in ua:
        os_type = "Windows (Legacy)"
    elif "macintosh" in ua or "mac os x" in ua:
        os_type = "macOS"
    elif "linux" in ua:
        os_type = "Linux"
    elif "android" in ua:
        os_type = "Android"
    elif "iphone" in ua or "ipad" in ua:
        os_type = "iOS"
    else:
        os_type = "Unknown OS / Embedded Device"

    # Detect Browser or Tool
    if "curl" in ua:
        browser = "cURL Terminal Client"
    elif "python-requests" in ua or "python" in ua:
        browser = "Python Automation Script"
    elif "edg/" in ua:
        browser = "Microsoft Edge"
    elif "chrome/" in ua and "safari" in ua:
        browser = "Google Chrome"
    elif "firefox/" in ua:
        browser = "Mozilla Firefox"
    elif "safari/" in ua and "chrome" not in ua:
        browser = "Apple Safari"
    else:
        browser = "Generic HTTP Client"

    return {"detected_os": os_type, "detected_browser": browser, "raw_ua": ua_string}


def record_honeypot_interaction(trap_category, bait_name, canary_token=None):
    """
    Core Honeypot Telemetry Engine:
    Captures remote IP, client headers, referer (watering hole origin),
    timestamps, and saves structured JSON incident telemetry.
    """
    ensure_directories()
    
    # Resolve real client IP
    client_ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    if client_ip and "," in client_ip:
        client_ip = client_ip.split(",")[0].strip()

    ua_header = request.headers.get("User-Agent", "Unknown-Agent")
    ua_meta = parse_user_agent(ua_header)
    referer = request.headers.get("Referer", "Direct / Bookmark / Hidden Referrer")

    event = {
        "event_id": f"HONEY-{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[:17]}",
        "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "client_ip": client_ip,
        "requested_path": request.path,
        "http_method": request.method,
        "trap_category": trap_category,
        "bait_name": bait_name,
        "canary_token": canary_token or "N/A",
        "referer_origin": referer,
        "client_os": ua_meta["detected_os"],
        "client_browser": ua_meta["detected_browser"],
        "raw_user_agent": ua_meta["raw_ua"],
        "accept_language": request.headers.get("Accept-Language", "en-US"),
        "threat_level": "CRITICAL" if "exe" in request.path or "canary" in request.path else "HIGH"
    }

    INCIDENT_LOGS.append(event)

    # Persist to JSON
    with open(JSON_LOG, "w", encoding="utf-8") as jf:
        json.dump(INCIDENT_LOGS, jf, indent=2)

    # Persist to Human-Readable TXT
    with open(TXT_LOG, "a", encoding="utf-8") as tf:
        tf.write(f"[{event['timestamp_utc']}] [HONEYPOT ALERT] ID: {event['event_id']}\n")
        tf.write(f"  • Source IP   : {event['client_ip']} | Host: {request.host}\n")
        tf.write(f"  • Bait Trap   : {event['bait_name']} ({event['trap_category']})\n")
        tf.write(f"  • Path        : {event['requested_path']}\n")
        tf.write(f"  • Referer     : {event['referer_origin']}\n")
        tf.write(f"  • Client Env  : {event['client_os']} | {event['client_browser']}\n")
        tf.write(f"  • Canary Tag  : {event['canary_token']}\n")
        tf.write("-" * 80 + "\n")

    return event


HTML_BAIT_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Security Alert - Honeypot Triggered</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0f141c; color: #e1e6f0; margin: 0; padding: 40px; }
        .card { max-width: 680px; margin: 0 auto; background: #161c26; border: 1px solid #232d3c; border-radius: 8px; padding: 30px; box-shadow: 0 8px 24px rgba(0,0,0,0.5); }
        h1 { color: #ff4b4b; font-size: 24px; margin-top: 0; }
        .badge { display: inline-block; background: #28dc78; color: #0f141c; font-weight: bold; padding: 4px 10px; border-radius: 4px; font-size: 12px; }
        .meta-box { background: #0e1219; border: 1px solid #288cf0; border-radius: 4px; padding: 15px; margin: 20px 0; font-family: monospace; font-size: 13px; }
        p { line-height: 1.6; color: #a0aec0; }
    </style>
</head>
<body>
    <div class="card">
        <span class="badge">SQROCK CYBER DEFENSE LAB</span>
        <h1>⚠️ Security Honeypot Trap Triggered</h1>
        <p>You have accessed a monitored digital decoy deployed as part of an authorized social engineering awareness simulation.</p>
        <div class="meta-box">
            <div><b>Incident ID :</b> {{ event.event_id }}</div>
            <div><b>Timestamp   :</b> {{ event.timestamp_utc }}</div>
            <div><b>Client IP   :</b> {{ event.client_ip }}</div>
            <div><b>Trap Path   :</b> {{ event.requested_path }}</div>
            <div><b>Environment :</b> {{ event.client_os }} ({{ event.client_browser }})</div>
            <div><b>Referer     :</b> {{ event.referer_origin }}</div>
            <div><b>Canary Token:</b> {{ event.canary_token }}</div>
        </div>
        <p>Your connection metadata has been logged to the SOC telemetry repository. No malicious code was executed.</p>
    </div>
</body>
</html>
"""


# ==============================================================================
# HONEYPOT BAIT & CANARY ROUTES
# ==============================================================================

@app.route("/")
def index():
    return jsonify({
        "server": "PEER'S Honeypot Link Tracker v2.5",
        "status": "ARMED_AND_LOGGING",
        "organization": "Sqrock IT Solutions Cyber Defense Lab",
        "active_traps": [
            "/download/vpn-update-v4.exe",
            "/payroll/q4-executive-salaries.xlsx",
            "/vendor-portal/login",
            "/canary/<token_id>"
        ]
    })


@app.route("/download/vpn-update-v4.exe")
def trap_fake_vpn():
    """Simulated Digital Bait: Fake Corporate VPN update lure."""
    event = record_honeypot_interaction(
        trap_category="DIGITAL_BAIT_DRIVE_BY",
        bait_name="Fake Corporate VPN Client Update"
    )
    return render_template_string(HTML_BAIT_TEMPLATE, event=event)


@app.route("/payroll/q4-executive-salaries.xlsx")
def trap_payroll():
    """Simulated Digital Bait: Executive Compensation lure."""
    event = record_honeypot_interaction(
        trap_category="SOCIAL_ENGINEERING_LURE",
        bait_name="Executive Salary Appraisal Sheet"
    )
    return render_template_string(HTML_BAIT_TEMPLATE, event=event)


@app.route("/vendor-portal/login")
def trap_watering_hole():
    """Simulated Watering Hole Trap: Compromised vendor login portal."""
    event = record_honeypot_interaction(
        trap_category="WATERING_HOLE_PORTAL",
        bait_name="Compromised Third-Party Vendor Portal"
    )
    return render_template_string(HTML_BAIT_TEMPLATE, event=event)


@app.route("/canary/<token_id>")
def trap_canary_token(token_id):
    """Department-Specific Canary Token Tracking Trap."""
    event = record_honeypot_interaction(
        trap_category="CANARY_TRIPWIRE",
        bait_name="Targeted Canary Token Link",
        canary_token=token_id
    )
    return render_template_string(HTML_BAIT_TEMPLATE, event=event)


@app.route("/api/events", methods=["GET"])
def get_events():
    """SIEM Telemetry API: Returns all recorded honeypot events."""
    return jsonify({
        "status": "SUCCESS",
        "total_events": len(INCIDENT_LOGS),
        "events": INCIDENT_LOGS
    })


@app.route("/api/clear", methods=["POST"])
def clear_events():
    """Admin endpoint to flush incident logs for clean testing."""
    global INCIDENT_LOGS
    INCIDENT_LOGS = []
    ensure_directories()
    with open(JSON_LOG, "w", encoding="utf-8") as jf:
        json.dump([], jf)
    return jsonify({"status": "SUCCESS", "message": "Incident telemetry flushed."})


if __name__ == "__main__":
    ensure_directories()
    print("[*] Starting PEER'S Honeypot Gateway on http://127.0.0.1:8080...")
    app.run(host="127.0.0.1", port=8080, debug=False)
