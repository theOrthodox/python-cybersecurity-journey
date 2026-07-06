# 🔎 TCP Port Scanner

A simple TCP Port Scanner built using Python's built-in `socket` module. This tool scans a user-specified range of TCP ports on a target IP address and reports whether each port is **OPEN** or **CLOSED**.

This project is part of my **Python Cybersecurity Journey**, where I build practical security-focused tools to strengthen my Python programming and cybersecurity fundamentals.

---

## 📌 Features

* Scan any valid IPv4 address.
* Specify a custom start and end port.
* Detect whether a TCP port is **OPEN** or **CLOSED**.
* Configurable timeout (1 second per port).
* Handles invalid IP addresses gracefully.
* Displays a scan summary including:

  * Total ports scanned
  * Number of open ports
  * Number of closed ports

---

## 🛠 Technologies Used

* Python 3
* Socket Programming
* TCP Networking
* Exception Handling

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/theOrthodox/port-scanner.git
```

Navigate to the project folder:

```bash
cd port-scanner
```

Run the program:

```bash
python port_scanner.py
```

---

## Example

### Input

```text
===== PORT SCANNER =====

ENTER THE IP ADDRESS:
127.0.0.1

Enter the start range:
20

Enter the end range:
30
```

### Output

```text
Port 22 is OPEN
Port 23 is CLOSED
Port 24 is CLOSED
...

==============================
Total Ports Scanned : 11
Open Ports          : 1
Closed Ports        : 10
==============================
```

---

## Validation

The scanner validates:

* Valid TCP port range (0–65535)
* Start port must not be greater than the end port
* Invalid IP addresses
* Connection timeout to prevent hanging

---

## Concepts Practiced

* Socket Programming
* TCP Client Connections
* Port Scanning Fundamentals
* Network Timeouts
* Exception Handling
* Loops and Functions
* User Input Validation

---

## Learning Outcome

This project helped me understand how TCP connections work at a low level using Python's `socket` module. It reinforced networking fundamentals, error handling, and how security professionals identify exposed network services during reconnaissance.

---

## Limitations

* Scans TCP ports only.
* Performs sequential scanning (single-threaded).
* Does not identify the service running on open ports.
* Does not perform banner grabbing.
* Intended for educational purposes and systems you own or are authorized to test.

---

## Disclaimer

This tool is intended for educational purposes and authorized security testing only. Scan only systems that you own or have explicit permission to assess.

---

## Author

**Vinit Singh**

Part of my **Python Cybersecurity Journey**.
