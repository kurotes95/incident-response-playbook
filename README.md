# Incident Response Playbook

## 📌 Project Overview
This project is a structured **Incident Response Playbook** designed to help security analysts detect, investigate, and respond to cybersecurity threats efficiently. It includes:

- **Step-by-step response guides** for phishing, malware, and unauthorized access incidents.
- **Automated Python scripts** to analyze security logs and detect threats.
- **Sample cases** to practice and improve incident response skills.

## 📂 Folder Structure
```
incident-response-playbook/
│── README.md                   # Project documentation
│── playbooks/                   # Incident response guides
│   │── phishing-response.md     # Phishing attack response
│   │── malware-response.md      # Malware incident response
│   │── unauthorized-access.md   # Unauthorized access response
│── scripts/                     # Security automation scripts
│   │── log_parser.py            # Python script to analyze logs
│   │── email_header_parser.py   # Extract phishing indicators from emails
│── samples/                     # Example logs and phishing emails
│   │── phishing-email.eml       # Sample phishing email (sanitized)
│   │── malware_log_sample.log   # Sample malware-related log
│── requirements.txt             # Dependencies for Python scripts
│── .gitignore                   # Ignore unnecessary files
```

## ⚙️ Setup & Installation

### **1. Clone the Repository**
```bash
git clone https://github.com/kurotes95/incident-response-playbook.git
cd incident-response-playbook
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

## 🛠️ Usage

### **1. Using the Playbooks**
- Open the relevant markdown file inside the `playbooks/` directory.
- Follow the step-by-step instructions for investigating and responding to incidents.

### **2. Running the Log Parser**

The `log_parser.py` script allows you to scan log files for suspicious patterns. It supports three modes:

- **basic**: Detects failed login attempts, invalid users, and other basic suspicious activities.
- **privilege**: Looks for privilege escalation attempts, such as users added to sudo or admin groups.
- **advanced**: Detects advanced attack techniques like reverse shells, obfuscated PowerShell, suspicious downloads, etc.

**Example Usage:**

```bash
# Basic mode
python scripts/log_parser.py --mode basic samples/sample_log.txt

# Privilege mode
python scripts/log_parser.py --mode privilege samples/sample_log.txt

# Advanced mode
python scripts/log_parser.py --mode advanced samples/sample_log.txt
```

You can customize the regex patterns in `log_parser.py` to fit your environment.

### **3. Phishing Email Analysis**
```bash
python scripts/email_header_parser.py samples/phishing-email.eml
```
- Extracts important metadata from phishing emails to identify spoofed senders and malicious links.

## 🔥 Future Plans
- Add **more playbooks** for additional incident types (e.g., DDoS, insider threats, credential stuffing attacks).
- Enhance scripts with **real-time alerting** (e.g., integrate with SIEM tools like Splunk or ELK Stack).
- Include **interactive simulations** to test and refine response skills.

## 🤝 Contributions
- Feel free to **fork** this repository and submit pull requests with improvements.
- Report issues or suggest new features in the **Issues** section.

## 📜 License
This project is licensed under the **MIT License**. See the LICENSE file for more details.

---

🚀 **Let's improve cybersecurity one playbook at a time!**
