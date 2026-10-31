# Enterprise Watering Hole & Digital Baiting Defense Policy

**Document ID:** SEC-POL-WATERHOLE-2026-V1  
**Organization:** Sqrock IT Solutions / Cyber Defense & Security Operations  
**Standard Compliance:** NIST SP 800-53 Rev. 5 (SI-3, SI-4, SC-7), MITRE ATT&CK T1189 (Drive-by Compromise), CIS Controls v8 (Safeguard 9.2, 9.3)  
**Author:** Mohammed Peer Siddiqui, Lead Security Intern  
**Approved By:** Chief Information Security Officer (CISO)  
**Effective Date:** October 2026  

---

## 1. Executive Overview & Threat Definition

A **Watering Hole Attack** (MITRE ATT&CK T1189: Drive-by Compromise) is an advanced social engineering and targeted intrusion strategy where adversaries, rather than attacking a heavily defended corporate network directly, identify and compromise trusted third-party websites frequently visited by target personnel.

```
+--------------------------------------------------------------------------+
|                  WATERING HOLE & BAITING ATTACK LIFECYCLE                |
+--------------------------------------------------------------------------+
|  1. Target Profiling & Strategic Reconnaissance                          |
|     * Attacker profiles victim enterprise (contractors, industry news,   |
|       regional vendor portals, local catering/services).                 |
|                                                                          |
|  2. Third-Party Site Infiltration & Compromise                           |
|     * Adversary exploits CMS vulnerabilities (e.g., WordPress plugin,    |
|       SQLi, XSS) on the watering hole website.                           |
|                                                                          |
|  3. Malicious Redirection & Drive-by Ingestion                           |
|     * Injects invisible iFrames, malicious JavaScript redirectors, or    |
|       fake software update prompts (e.g., "Critical VPN Update").        |
|                                                                          |
|  4. Victim Interaction & Honeypot Interception                           |
|     * Employee visits trusted site -> silently redirected or clicks lure.|
|     * SOC Honeypot tracker intercepts and logs IP, User-Agent, referer.  |
+--------------------------------------------------------------------------+
```

---

## 2. Mandatory Technical Countermeasures

### 2.1. Secure Web Gateways (SWG) & URL Reputation Filtering
* All egress corporate HTTP/HTTPS traffic must route through an enterprise Secure Web Gateway (e.g., Zscaler, Cloudflare Gateway, Palo Alto Networks).
* The gateway must perform real-time domain categorization, block newly registered domains (< 30 days old), and enforce dynamic sandboxing on downloaded binaries (`.exe`, `.msi`, `.iso`, `.zip`).

### 2.2. Content Security Policy (CSP) & Script Execution Controls
* Corporate websites and managed portals must implement strict Content Security Policy (CSP) headers:
  ```http
  Content-Security-Policy: default-src 'self'; script-src 'self' https://trusted-cdn.com; object-src 'none'; frame-ancestors 'none';
  ```
* Enforce endpoint browser isolation (RBI) or script restrictions preventing unauthorized cross-origin iFrames and unknown JavaScript execution.

### 2.3. Browser & Endpoint Patch Management
* Modern watering hole drive-by exploits rely on unpatched browser vulnerabilities (zero-days or n-days). Enterprise endpoints must maintain automated, centralized browser updating (Google Chrome, Microsoft Edge, Mozilla Firefox) with zero user deferral.

### 2.4. Canary Tokens & Honeypot Tripwires
* The security team deploys honey-links across strategic corporate documentation, vendor directories, and social profiles. Any outbound connection to these unique canary URLs immediately alerts the SOC, pinpointing compromised sites or leaked credentials.

---

## 3. Operational Response & Incident Playbook

1. **Detection & Triage:** When a honeypot trigger fires, the SOC extracts client IP, User-Agent, and the HTTP Referer header to identify the compromised watering hole origin.
2. **Perimeter Containment:** The SOC immediately adds the compromised external domain to the enterprise perimeter firewall/proxy blocklist.
3. **Endpoint Isolation:** The visiting workstation is queried via EDR; all temporary browser caches and download folders are analyzed in a malware sandbox.
4. **Third-Party Notification:** Formal notification is transmitted to the administrators of the compromised watering hole website detailing the injected malicious scripts.
