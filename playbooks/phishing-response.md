 # 📧 Phishing Incident Response Playbook

## 🔍 1. Identification
- Review reported emails for suspicious indicators:
  - Mismatched "From" address and display name.
  - Unexpected attachments or links.
  - Generic greetings or urgent language.
- Inspect email headers:
  ```bash
  python scripts/email_header_parser.py samples/phishing-email.eml
  ```
  - Check for spoofed domains, unusual "Return-Path", and "Received" fields.
- Verify links by hovering without clicking, or use:
  - [VirusTotal](https://www.virustotal.com/)
  - [URLScan](https://urlscan.io/)

## 🛑 2. Containment
- Block sender domain/IP on mail server.
- Quarantine affected emails across the organization.
- Disable compromised accounts and reset credentials.
- Alert users to not interact with suspicious emails.

## 🧹 3. Eradication
- Remove phishing emails from all user mailboxes.
  - Use your organization's email admin tools (e.g., Microsoft Defender, Google Admin Console, Proofpoint) to purge emails.
- Update spam filters and blacklists.
- Check for possible malware activity in logs:
  ```bash
  python scripts/log_parser.py samples/malware_log_sample.log
  ```

## 🔄 4. Recovery
- Re-enable affected accounts after password reset.
- Ensure multi-factor authentication (MFA) is enabled.
- Apply email security enhancements:
  - **SPF**, **DKIM**, **DMARC** configuration.

## 📊 5. Lessons Learned
- Document:
  - Timeline of the incident.
  - Attack vector and scope.
  - Impact assessment.
- Conduct phishing awareness training if users were affected.
- Review and improve detection/prevention mechanisms.

---

🚀 **Stay vigilant. One phish can sink the whole ship!**

