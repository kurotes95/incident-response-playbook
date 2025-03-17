# 🔓 Unauthorized Access Incident Response Playbook

## 🔍 1. Identification
- Monitor SIEM alerts, firewall logs, and access control systems for:
  - Unusual login times or locations.
  - Multiple failed login attempts.
  - Privilege escalation or unauthorized system changes.
- Check for unauthorized accounts or newly created user accounts.
- Review logs:
  ```bash
  python scripts/log_parser.py samples/malware_log_sample.log
  ```
  (Customize the script to detect unauthorized login patterns.)

## 🛑 2. Containment
- Disable compromised accounts immediately.
- Terminate suspicious sessions or connections.
- Block malicious IP addresses or geolocations on firewalls.
- Change passwords for affected users, especially privileged accounts.

## 🧹 3. Eradication
- Remove unauthorized accounts, SSH keys, or API tokens.
- Close any backdoors or vulnerabilities used for access (e.g., unpatched software, weak passwords).
- Audit and clean up permissions, ensuring the principle of least privilege.

## 🔄 4. Recovery
- Restore affected systems or services to known good state (if tampering detected).
- Implement MFA for all critical accounts if not already enabled.
- Strengthen network segmentation to limit lateral movement.
- Conduct a thorough audit to ensure no persistence mechanisms remain.

## 📊 5. Lessons Learned
- Document:
  - How unauthorized access occurred.
  - Accounts, systems, and data affected.
  - Timeline of detection, containment, and recovery.
- Improve access control policies (e.g., password policies, account lockout thresholds).
- Conduct user and administrator security training.
- Update detection rules and monitoring tools to prevent recurrence.

---

🚀 **Access control is your first line of defense—lock it down tight!**
 
