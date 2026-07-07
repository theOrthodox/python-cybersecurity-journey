# URL Health Checker

A Python-based URL Health Checker that reads a list of URLs from a text file, sends HTTP GET requests to each URL, and generates a report containing status codes, response times, and redirection information.

This project demonstrates the use of Python's `requests` library, exception handling, HTTP response analysis, and basic network diagnostics.

---

## Features

- Read URLs from a text file
- Perform HTTP GET requests
- Display:
  - URL
  - HTTP Status Code
  - Response Time (milliseconds)
  - Redirect Detection
- Handle:
  - Missing input file
  - Connection errors
  - Request timeouts
- Generate a summary including:
  - Total URLs checked
  - Successful (2xx)
  - Client Errors (4xx)
  - Server Errors (5xx)
  - Failed Requests

---

## Project Structure

```
URL-Health-Checker/
│
├── url_checker.py
├── urls.txt
└── README.md
```

---

## Requirements

- Python 3.9+
- requests

Install the dependency:

```bash
pip install requests
```

---

## Input File

Create a text file containing one URL per line.

Example:

```
https://google.com
https://github.com
https://httpbin.org/status/404
https://httpbin.org/status/500
https://example.com
```

---

## Usage

Run the program:

```bash
python url_checker.py
```

Enter the path to your URL list when prompted.

Example:

```
Please enter the file path of the URL list:
C:\Users\YourName\Documents\urls.txt
```

---

## Sample Output

```
===== Report =====

URL: https://google.com
Status Code: 200
Response Time: 132.48 ms
Redirected: False

===== Report =====

URL: http://github.com
Status Code: 200
Response Time: 189.20 ms
Redirected: True

Redirected From:
http://github.com

Redirected To:
https://github.com/
```

---

## Summary

```
===== TOTAL SUMMARY REPORT =====

Total Checked : 5
2xx Responses : 3
4xx Responses : 1
5xx Responses : 1
Failed Requests : 0
```

---

## Technologies Used

- Python
- Requests Library
- HTTP Protocol
- Exception Handling

---

## Learning Outcomes

This project demonstrates:

- HTTP request handling
- Network diagnostics
- Status code classification
- Response time measurement
- Redirect detection
- Exception handling
- File handling in Python

---

Author 
Vinit Kumar Singh
