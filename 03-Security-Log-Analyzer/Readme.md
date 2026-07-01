# Security Log Analyzer

A command-line tool that reads a security log file and generates 
a categorized summary report.

## Usage

```bash
python log_analyzer.py
```

When prompted, enter the full path to your log file.

## What It Does

- Reads a plain text log file line by line
- Counts occurrences of INFO, WARNING, and ERROR messages
- Displays a formatted summary report

## Concepts Demonstrated

- File I/O with exception handling
- Dictionary-based counters
- String pattern matching

## Example Output
===== LOG ANALYSIS REPORT =====

INFO MESSAGES    : 3

WARNING MESSAGES : 2

ERROR MESSAGES   : 2

## Sample Log Format

INFO: User login successful

WARNING: Multiple failed login attempts

ERROR: Database connection failed
