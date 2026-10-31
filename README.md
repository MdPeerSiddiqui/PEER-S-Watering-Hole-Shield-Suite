# PEER'S Watering Hole Shield Suite: Digital Baiting & Honeypot Link Tracking

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/MITRE%20ATT%26CK-T1189%20Drive--by-red.svg?style=for-the-badge&logo=mitre-attack)](https://attack.mitre.org/techniques/T1189/)
[![Security Standard](https://img.shields.io/badge/NIST-SP%20800--53%20SI--3%2FSI--4-orange.svg?style=for-the-badge)](https://csrc.nist.gov/)
[![CIS Controls](https://img.shields.io/badge/CIS%20Controls-v8%20Safeguard%209.2-blue.svg?style=for-the-badge)](https://www.cisecurity.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Unit Tests](https://img.shields.io/badge/Unit%20Tests-6%2F6%20Passed-brightgreen.svg?style=for-the-badge)](tests/test_watering_hole.py)
[![Platform](https://img.shields.io/badge/Platform-Kali%20Linux%20%7C%20Windows-black.svg?style=for-the-badge&logo=linux)](https://www.kali.org/)

> **Day 10 Cybersecurity Internship Deliverable**  
> **Company:** Sqrock IT Solutions  
> **Specialization:** Social Engineering & Authentication Security Simulations Using Python  
> **Developer:** Mohammed Peer Siddiqui  
> **Repository:** [https://github.com/MdPeerSiddiqui/PEER-S-Watering-Hole-Shield-Suite](https://github.com/MdPeerSiddiqui/PEER-S-Watering-Hole-Shield-Suite)

---

## 📌 Executive Overview

Watering hole attacks (mapped to **MITRE ATT&CK T1189: Drive-by Compromise**) and digital baiting lures represent some of the most sophisticated perimeter bypass strategies employed by advanced persistent threat (APT) groups. Rather than directly assaulting a heavily defended corporate network, adversaries compromise trusted third-party websites commonly frequented by target employees (e.g., regional supplier portals, technical forums, local corporate catering menus). Once compromised, attackers inject invisible iFrames, cross-site script redirectors, or deceptive download banners that silently deliver trojanized installers or harvest employee credentials.

**PEER'S Watering Hole Shield Suite v2.5** is an enterprise-grade honeypot gateway, passive client fingerprinter, and watering hole defense framework developed for **Day 10** of the Sqrock IT Solutions Cybersecurity Internship. It delivers a dual-perspective platform:
1. **Honeypot Trap Gateway:** Runs multi-path decoy traps (`/download/vpn-update-v4.exe`, `/payroll/q4-executive-salaries.xlsx`, `/vendor-portal/login`, and `/canary/<token_id>`) that silently intercept, log, and neutralize unauthorized link interactions without executing weaponized code.
2. **Passive Client Fingerprinter & Tripwire Engine:** Captures remote IP addresses, parses client User-Agent strings into normalized OS and browser classes, records the critical `Referer` header to trace third-party watering hole origins, and correlates granular department-specific canary tokens for SOC alerting.

```
+========================================================================+
|             PEER'S WATERING HOLE SHIELD v2.5 - ARCHITECTURE            |
+========================================================================+
|                                                                        |
|  [Compromised Third-Party Watering Hole / Digital Bait Lure]           |
|          |                                                             |
|          v                                                             |
|  [Victim Clicks Link / Drive-by Redirect Initiated]                    |
|          |                                                             |
|   +------+----------------------------------------------------------+  |
|   | Dual-Perspective Assessment Framework                           |  |
|   |                                                                 |  |
|   |  MULTI-PATH HONEYPOT GATEWAY (Flask Listener Port 8080)         |  |
|   |   * Bait 1: /download/vpn-update-v4.exe (Fake VPN Installer)   |  |
|   |   * Bait 2: /payroll/q4-executive-salaries.xlsx (Salary Lure)   |  |
|   |   * Bait 3: /vendor-portal/login (Compromised Vendor Trap)      |  |
|   |   * Bait 4: /canary/<token_id> (Departmental Tripwire)          |  |
|   |                                                                 |  |
|   |  PASSIVE CLIENT FINGERPRINTING & SOC TELEMETRY PIPELINE         |  |
|   |   1. Real Client IP Resolution (X-Forwarded-For & Socket)       |  |
|   |   2. User-Agent Normalization (OS & Browser Attribution)        |  |
|   |   3. Watering Hole Origin Attribution via HTTP Referer          |  |
|   |   4. Granular Canary Attribution (Finance, HR, Engineering)     |  |
|   |   5. Structured SIEM Logging (JSON & Human-Readable Briefs)     |  |
|   +-----------------------------------------------------------------+  |
+========================================================================+
```

---

## 🛡️ Core Capabilities

1. **Multi-Path Honeypot Gateway (`honeypot_server.py`)**
   - Implements realistic enterprise digital decoys that trap inbound connections without serving weaponized malware.
   - Returns a stylized educational landing page alerting the visitor that they encountered an authorized corporate awareness honeypot.
   - Provides administrative SIEM endpoints (`GET /api/events` and `POST /api/clear`) for SOC log ingestion and testing.

2. **Passive Client Fingerprinter**
   - Automatically decomposes inbound request headers into structured intelligence:
     - **Client IP Address:** Evaluates proxy headers and direct sockets.
     - **Operating System:** Classifies Windows 10/11, macOS, Linux, iOS, and Android.
     - **Browser & Automation Engine:** Detects Chrome, Edge, Firefox, Safari, cURL, and Python automation tools.
     - **HTTP Referer Header:** Captures the referring third-party webpage, identifying which external site was compromised as the watering hole.

3. **Granular Departmental Canary Tokens**
   - Generates unique tracking tokens per organizational department (e.g., `FINANCE-CANARY-01`, `HR-CANARY-02`, `EXEC-CANARY-03`).
   - Seeding these URLs in internal wikis or vendor memos immediately identifies data leaks or unauthorized employee forwarding.

4. **Automated Victim Interaction Simulator (`watering_hole_auditor.py`)**
   - Includes a built-in automated test client that issues requests across all decoy endpoints rotating through five realistic corporate victim personas.

---

## 📂 Repository Structure

```
PEER-S-Watering-Hole-Shield-Suite/
├── honeypot_server.py            # Multi-path honeypot link tracker & passive client fingerprinter
├── watering_hole_auditor.py      # Interactive CLI suite, victim simulator & domain risk evaluator
├── requirements.txt              # Core project dependencies (flask, requests, colorama, reportlab)
├── LICENSE                       # MIT License
├── README.md                     # Technical documentation & usage guide
├── policy/
│   └── watering_hole_mitigation.md # Formal enterprise watering hole & SWG defense policy
├── telemetry_logs/
│   ├── honeypot_events.json      # Structured JSON honeypot incident logs
│   └── honeypot_events.txt       # Human-readable executive SOC incident briefings
├── tests/
│   └── test_watering_hole.py     # 6-point automated PyUnit verification suite
├── scripts/
│   ├── generate_terminal_screens.py # Headless PIL terminal screenshot generator
│   └── generate_day10_pdf.py     # ReportLab multi-page executive report compiler
└── reports/
    ├── Day10_Watering_Hole_Report_Sqrock_MdPeerSiddiqui.pdf # 7-page executive lab report
    └── screenshots/              # High-fidelity terminal evidence
        ├── 01_kali_init_banner.png
        ├── 02_master_menu.png
        ├── 03_honeypot_server_live.png
        ├── 04_victim_client_sim.png
        ├── 05_soc_telemetry_inspection.png
        └── 06_github_repo_overview.png
```

---

## 🚀 Installation & Setup

### 1. Prerequisites
- Python 3.10 or higher
- Git
- Kali Linux, Ubuntu, Debian, or Windows 10/11

### 2. Clone the Repository
```bash
git clone https://github.com/MdPeerSiddiqui/PEER-S-Watering-Hole-Shield-Suite.git
cd PEER-S-Watering-Hole-Shield-Suite
```

### 3. Create and Activate Virtual Environment
```bash
# On Linux / macOS / Kali:
python3 -m venv .venv
source .venv/bin/activate

# On Windows PowerShell:
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 💻 Execution & Usage Guide

### Terminal 1: Launch Honeypot Server
```bash
python honeypot_server.py
```
*Initializes the listener at `http://127.0.0.1:8080` with active traps for VPN updates, payroll lures, vendor portals, and canary tokens.*

### Terminal 2: Run Auditor & Victim Simulator
```bash
python watering_hole_auditor.py
```
*Provides an interactive control console offering:*
- **`[1] Verify Local Honeypot Server Status`** — Tests connectivity to port 8080.
- **`[2] Simulate Automated Victim Bait Interactions`** — Fires 5 diverse personas with realistic User-Agents and Referer headers.
- **`[3] Generate Department-Specific Canary Tracking Tokens`** — Creates targeted tripwires for Finance, HR, Engineering, etc.
- **`[4] Inspect Live SOC Honeypot Telemetry`** — Displays structured client fingerprints and threat tiers.
- **`[5] Evaluate Website Watering Hole Risk`** — Assesses external third-party domains for SSL, CSP, and clickjacking vulnerabilities.
- **`[6] Display Enterprise Web Gateway Blueprint`** — Details SWG egress filtering, CSP sandboxing, and browser patching.

---

## 🧪 Automated Unit Verification

A comprehensive 6-point test suite is included in `tests/test_watering_hole.py` utilizing the Flask test client:

```bash
python -m unittest tests/test_watering_hole.py -v
```

### Test Suite Results:
| Test Method | Target Component | Status |
| :--- | :--- | :---: |
| `test_vpn_download_bait_trap` | Digital Bait Lure (`/download/`) | `PASSED` |
| `test_payroll_bait_trap` | Social Engineering Lure (`/payroll/`) | `PASSED` |
| `test_watering_hole_portal_trap` | Watering Hole Referer Sensor (`/vendor-portal/`) | `PASSED` |
| `test_canary_token_tracking` | Canary Tripwire Engine (`/canary/<id>`) | `PASSED` |
| `test_client_fingerprinting` | Passive OS/Browser Fingerprinting | `PASSED` |
| `test_soc_telemetry_endpoint` | SIEM Telemetry & Log Clear API | `PASSED` |

**Verification Result: 6/6 Tests Passed (100% OK).**

---

## 📊 Security Architecture Comparison

| Feature Metric | Unprotected Enterprise Egress | Hardened Honeypot & SWG Infrastructure |
| :--- | :--- | :--- |
| **Outbound Web Traffic Inspection** | Unrestricted direct internet access | Secure Web Gateway (SWG) + TLS Inspection |
| **Third-Party Compromise Visibility** | Zero awareness of compromised vendor sites | Honeypot Referer Tracking & Domain Scoring |
| **Digital Bait Lure Interception** | Users download trojans unmonitored | Canary Tripwires & Instant SOC Telemetry |
| **Client Fingerprint Telemetry** | Unmonitored user environment | Passive OS/Browser/IP Attribution |
| **Script Sandboxing & Isolation** | Native local browser execution | Remote Browser Isolation (RBI) + CSP |

---

## 📜 Compliance & Industry Standards

- **MITRE ATT&CK T1189:** Drive-by Compromise.
- **NIST SP 800-53 Rev. 5 (SI-3):** Malicious Code Protection.
- **NIST SP 800-53 Rev. 5 (SI-4):** Information System Monitoring.
- **CIS Controls v8 (Safeguard 9.2):** Ensure Only Fully Supported Browsers and Email Clients Are Handled.

---

## 👤 Author & Acknowledgments

- **Lead Developer:** Mohammed Peer Siddiqui
- **Internship Organization:** Sqrock IT Solutions
- **Track:** Social Engineering Attack Simulations Using Python (Alpha 2 Cohort)
- **LinkedIn:** [Mohammed Peer Siddiqui](https://www.linkedin.com)
- **GitHub:** [@MdPeerSiddiqui](https://github.com/MdPeerSiddiqui)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for full details.
