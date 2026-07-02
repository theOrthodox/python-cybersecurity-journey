#  Security Incident Analyzer + IOC Extractor

A beginner-friendly Blue Team project written in Python that analyzes security log files and generates a formatted security incident report.

The tool identifies common security events, calculates an overall threat level, extracts Indicators of Compromise (IOCs), and summarizes the findings.

---

## Features

- Detects Failed Login Attempts
- Detects Password Reset Requests
- Detects Account Lockout Events
- Detects Suspicious Activity
- Calculates Overall Threat Level
- Identifies the Most Frequent Security Event
- Extracts IP Addresses (IOCs)
- Counts Unique IP Addresses
- Handles Invalid File Paths
- Generates a Clean Security Report

---

## Threat Level Logic

| Total Security Events | Threat Level |
|-----------------------:|-------------|
| 0 – 2 | LOW |
| 3 – 5 | MEDIUM |
| 6+ | HIGH |

---

## Example Log File

```text
INFO: User login successful
WARNING: Failed login attempt from 192.168.1.25
WARNING: Failed login attempt from 192.168.1.25
INFO: Password reset requested
WARNING: Account locked due to multiple failures
WARNING: Suspicious activity detected from 10.0.0.5
ERROR: Authentication service unavailable
WARNING: Failed login attempt from 172.16.10.100
INFO: Password reset requested
WARNING: Suspicious activity detected from 10.0.0.5
WARNING: Failed login attempt from 192.168.1.25
```

---

## Sample Output

```text
===== SECURITY EVENT REPORT =====

Failed Login Attempts : 4
Password Resets       : 2
Account Lockouts      : 1
Suspicious Activity   : 2

Total Security Events : 9

Threat Level          : HIGH

Most Frequent Event   : Failed Login Attempts

===== IOCs FOUND =====

192.168.1.25
10.0.0.5
172.16.10.100

Unique IP Addresses Found : 3
```

---

## Project Structure

```
security-incident-analyzer/
│
├── security_incident_analyzer.py
├── sample_logs.txt
├── README.md
└── LICENSE
```

---

## How It Works

1. The user provides the path to a log file.
2. The program reads every log entry.
3. Security events are counted.
4. IP addresses are extracted.
5. Duplicate IP addresses are removed.
6. The overall threat level is calculated.
7. A complete incident report is displayed.

---

## Technologies Used

- Python 3
- File Handling
- Functions
- Lists
- Loops
- String Methods
- Exception Handling

---

## Learning Objectives

This project helped practice:

- File handling
- String processing
- Log analysis
- Indicator of Compromise (IOC) extraction
- Basic Security Operations Center (SOC) concepts
- Python functions
- Exception handling
- Data processing

---


## Author

**Vinit Singh**
