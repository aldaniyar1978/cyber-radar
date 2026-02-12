#!/usr/bin/env python3
import json
import os
from datetime import datetime

def build_feed():
    """Build feed.json from collected threat intelligence"""
    
    # Sample threat intelligence data
    # In production, this would aggregate from multiple sources
    feed_items = [
        {
            "id": "threat-001",
            "title": "Critical Zero-Day Vulnerability in Popular Web Framework",
            "description": "A critical remote code execution vulnerability has been discovered in a widely-used web framework. Immediate patching recommended.",
            "category": "vulnerabilities",
            "severity": "critical",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "source": "CVE Database",
            "tags": ["zero-day", "RCE", "web-security"]
        },
        {
            "id": "threat-002",
            "title": "New Ransomware Campaign Targeting Healthcare Sector",
            "description": "Security researchers have identified a sophisticated ransomware campaign specifically targeting healthcare organizations with improved encryption methods.",
            "category": "malware",
            "severity": "high",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "source": "Threat Intelligence Report",
            "tags": ["ransomware", "healthcare", "encryption"]
        },
        {
            "id": "threat-003",
            "title": "State-Sponsored APT Group Exploiting VPN Vulnerabilities",
            "description": "Advanced persistent threat actors have been observed exploiting known vulnerabilities in enterprise VPN solutions to gain initial access.",
            "category": "apt",
            "severity": "high",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "source": "Cybersecurity Agency",
            "tags": ["APT", "VPN", "state-sponsored"]
        },
        {
            "id": "threat-004",
            "title": "Phishing Campaign Impersonating Major Financial Institutions",
            "description": "A large-scale phishing operation has been detected targeting customers of major banks with sophisticated credential harvesting techniques.",
            "category": "phishing",
            "severity": "medium",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "source": "Anti-Phishing Working Group",
            "tags": ["phishing", "financial", "social-engineering"]
        },
        {
            "id": "threat-005",
            "title": "IoT Botnet Expanding with New Exploitation Techniques",
            "description": "Researchers have observed a significant botnet expansion targeting IoT devices using newly discovered exploitation methods.",
            "category": "botnet",
            "severity": "medium",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "source": "IoT Security Research",
            "tags": ["IoT", "botnet", "DDoS"]
        }
    ]
    
    # Create output directory if it doesn't exist
    output_dir = 'docs/data'
    os.makedirs(output_dir, exist_ok=True)
    
    # Write feed.json
    output_file = os.path.join(output_dir, 'feed.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            "updated": datetime.now().isoformat(),
            "items": feed_items
        }, f, indent=2, ensure_ascii=False)
    
    print(f"Feed generated successfully: {len(feed_items)} items")
    print(f"Output: {output_file}")

if __name__ == '__main__':
    build_feed()
