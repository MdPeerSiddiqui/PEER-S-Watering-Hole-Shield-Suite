#!/usr/bin/env python3
"""
================================================================================
Automated Unit Verification Suite for PEER'S Watering Hole Shield Suite
Author      : Mohammed Peer Siddiqui
Organization: Sqrock IT Solutions — Cybersecurity Internship (Alpha 2 Cohort)
================================================================================
"""

import os
import sys
import json
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from honeypot_server import app, parse_user_agent, INCIDENT_LOGS


class TestWateringHoleShield(unittest.TestCase):
    """Test suite covering honeypot routes, canary tracking, and fingerprinting."""

    def setUp(self):
        """Set up Flask test client and reset in-memory logs."""
        self.client = app.test_client()
        self.client.post("/api/clear")

    def test_vpn_download_bait_trap(self):
        """Verify fake VPN download endpoint traps connection and logs event."""
        res = self.client.get("/download/vpn-update-v4.exe", headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/122.0.0.0",
            "Referer": "http://trusted-partner.com/downloads"
        })
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Security Honeypot Trap Triggered", res.data)

        # Verify incident logged
        api_res = self.client.get("/api/events")
        data = api_res.get_json()
        self.assertEqual(data["total_events"], 1)
        self.assertEqual(data["events"][0]["bait_name"], "Fake Corporate VPN Client Update")

    def test_payroll_bait_trap(self):
        """Verify payroll lure records social engineering trap interaction."""
        res = self.client.get("/payroll/q4-executive-salaries.xlsx", headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) Safari/605.1.15"
        })
        self.assertEqual(res.status_code, 200)
        
        api_res = self.client.get("/api/events")
        data = api_res.get_json()
        self.assertEqual(data["total_events"], 1)
        self.assertEqual(data["events"][0]["trap_category"], "SOCIAL_ENGINEERING_LURE")

    def test_watering_hole_portal_trap(self):
        """Verify simulated watering hole login portal traps referer header."""
        referer_url = "http://compromised-industry-forum.org/topics/security"
        res = self.client.get("/vendor-portal/login", headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Firefox/123.0",
            "Referer": referer_url
        })
        self.assertEqual(res.status_code, 200)
        
        api_res = self.client.get("/api/events")
        data = api_res.get_json()
        self.assertEqual(data["events"][0]["referer_origin"], referer_url)

    def test_canary_token_tracking(self):
        """Verify department-specific canary token is captured and attributed."""
        token_id = "FINANCE-CANARY-9988"
        res = self.client.get(f"/canary/{token_id}")
        self.assertEqual(res.status_code, 200)
        
        api_res = self.client.get("/api/events")
        data = api_res.get_json()
        self.assertEqual(data["events"][0]["canary_token"], token_id)
        self.assertEqual(data["events"][0]["trap_category"], "CANARY_TRIPWIRE")

    def test_client_fingerprinting(self):
        """Verify User-Agent parser correctly determines OS and Browser."""
        ua_win_chrome = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"
        parsed = parse_user_agent(ua_win_chrome)
        self.assertEqual(parsed["detected_os"], "Windows 10/11")
        self.assertEqual(parsed["detected_browser"], "Google Chrome")

        ua_mac_safari = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2) AppleWebKit/605.1.15 Safari/605.1.15"
        parsed_mac = parse_user_agent(ua_mac_safari)
        self.assertEqual(parsed_mac["detected_os"], "macOS")
        self.assertEqual(parsed_mac["detected_browser"], "Apple Safari")

    def test_soc_telemetry_endpoint(self):
        """Verify SIEM telemetry endpoint returns correct format and clear function works."""
        self.client.get("/download/vpn-update-v4.exe")
        self.client.get("/payroll/q4-executive-salaries.xlsx")
        
        api_res = self.client.get("/api/events")
        data = api_res.get_json()
        self.assertEqual(data["status"], "SUCCESS")
        self.assertEqual(data["total_events"], 2)

        # Clear logs
        clear_res = self.client.post("/api/clear")
        self.assertEqual(clear_res.get_json()["status"], "SUCCESS")
        
        api_res2 = self.client.get("/api/events")
        self.assertEqual(api_res2.get_json()["total_events"], 0)


if __name__ == "__main__":
    unittest.main()
