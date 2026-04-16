# File Integrity Monitoring System (FIM)

## Description
This project monitors files for unauthorized changes by creating a baseline of file hashes and comparing them over time.

## Features
- SHA256 hashing for file integrity
- Detects file modification, deletion, and addition
- Generates alert reports
- Simulates real-world FIM tools

## Technologies
- Python
- Cybersecurity (Blue Team)
- Hashing Algorithms
- File Monitoring

## How to Use
Step 1: Create baseline
python monitor.py → select option 1

Step 2: Modify any file

Step 3: Run integrity check
python monitor.py → select option 2

## Output
Alerts saved in alerts.txt