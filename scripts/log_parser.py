import re
import sys

patterns = {
    "basic": [
        r"Failed password for",
        r"Invalid user",
        r"Accepted password for root",
        r"sudo: .*authentication failure",
        r"Connection closed by .* port",
    ],
    "privilege": [
        r"User .* added to group .*sudo",
        r"Administrator privileges granted to",
        r"New user account created",
    ],
    "advanced": [
        r"reverse shell",
        r"powershell.exe",
        r"cmd.exe /c",
        r"wget .* http",
        r"curl .* http",
        r"EncodedCommand",
        r"Base64 decode",
        r"\\temp\\.*\\.exe",
    ]
}

def parse_logs(log_file, mode):
    selected_patterns = patterns.get(mode)
    if selected_patterns is None:
        print(f"Error: Unknown mode '{mode}'. Available modes: basic, privilege, advanced")
        return

    try:
        with open(log_file, 'r', errors='ignore') as file:
            for line_number, line in enumerate(file, 1):
                for pattern in selected_patterns:
                    if re.search(pattern, line, re.IGNORECASE):
                        print(f"[!] {mode.capitalize()} Suspicious Entry Found (Line {line_number}): {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{log_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] != "--mode":
        print("Usage: python log_parser.py --mode <basic|privilege|advanced> <log_file>")
    else:
        mode = sys.argv[2].lower()
        log_file = sys.argv[3]
        parse_logs(log_file, mode)
 
