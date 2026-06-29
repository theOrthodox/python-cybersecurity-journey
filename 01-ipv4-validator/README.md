# IPv4 Validator

## Overview

The IPv4 Validator is a Python program that verifies whether a user-provided IPv4 address is valid according to standard IPv4 formatting rules.

This project is part of my **Python Cybersecurity Journey**, where I build practical security-focused tools while learning Python.

---

## Features

- Validates IPv4 addresses
- Ensures exactly four octets are present
- Verifies that each octet contains only numeric characters
- Checks that every octet is within the valid range (0–255)
- Handles invalid input gracefully

---

## Skills Practiced

- Python Functions
- Loops
- Lists
- String Manipulation
- Exception Handling
- Input Validation

---

## Project Structure

```text
01-ipv4-validator/
│
├── ipv4_validator.py
├── README.md
└── sample_inputs.txt
```

---

## Example

### Valid Input

```text
192.168.1.1
```

Output

```text
IP entered is valid
```

---

### Invalid Input

```text
256.100.50.25
```

Output

```text
IP entered is invalid
```

---

## Author

**Vinit Singh**

