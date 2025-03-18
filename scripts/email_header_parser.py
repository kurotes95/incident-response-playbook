 import email
import sys
from email import policy

# Function to parse email headers and extract key fields
def parse_email_headers(email_file):
    try:
        with open(email_file, 'r', encoding='utf-8', errors='ignore') as f:
            msg = email.message_from_file(f, policy=policy.default)
            print("\n[+] Email Header Information:")
            print(f"From: {msg['From']}")
            print(f"To: {msg['To']}")
            print(f"Subject: {msg['Subject']}")
            print(f"Date: {msg['Date']}")
            print(f"Return-Path: {msg['Return-Path']}")
            print(f"Reply-To: {msg['Reply-To']}")
            print(f"Received: {msg.get_all('Received')}")
            print(f"Message-ID: {msg['Message-ID']}")

            print("\n[+] SPF/DKIM/DMARC Fields:")
            print(f"Authentication-Results: {msg['Authentication-Results']}")
            print(f"DKIM-Signature: {msg['DKIM-Signature']}")
            print(f"ARC-Authentication-Results: {msg['ARC-Authentication-Results']}")

    except FileNotFoundError:
        print(f"Error: File '{email_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python email_header_parser.py <email_file>")
    else:
        parse_email_headers(sys.argv[1])

