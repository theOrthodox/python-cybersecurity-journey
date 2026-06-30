# 🔐 Password Strength Checker

A beginner-friendly cybersecurity project built in Python that evaluates the strength of a user-provided password based on common security best practices.

This project is part of my **Python Cybersecurity Journey**, where I build practical security-focused Python applications while learning cybersecurity concepts.

---

## 📌 Features

* Accepts a password from the user.
* Checks whether the password contains:

  * At least **8 characters**
  * At least **one uppercase letter**
  * At least **one lowercase letter**
  * At least **one numeric digit**
  * At least **one special character**
* Displays whether the password is **Strong** or **Weak**.

---

## 🛠 Technologies Used

* Python 3
* String Methods
* Functions
* Loops
* Conditional Statements

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/theOrthodox/02-password-strength-checker.git
```

Navigate to the project directory:

```bash
cd password-strength-checker
```

Run the program:

```bash
python password_checker.py
```

---

## Example

### Input

```text
Please enter your password:
Cyber@2026
```

### Output

```text
The password entered is: Cyber@2026
Strong
```

---

## Password Validation Rules

A password is considered **Strong** only if it satisfies all of the following:

* Minimum length of 8 characters
* Contains at least one uppercase letter
* Contains at least one lowercase letter
* Contains at least one digit
* Contains at least one special character

Otherwise, it is considered **Weak**.

---

## Concepts Practiced

* Functions
* Boolean Flags
* String Processing
* Character Classification
* Basic Input Validation
* Python Built-in String Methods

---

## Future Improvements

* Display which specific requirements are missing.
* Calculate a password strength score.
* Estimate password entropy.
* Detect common passwords using a wordlist.
* Prevent repeated characters and predictable patterns.
* Build a GUI version using Tkinter.
* Develop a web version using Flask.

---

## Learning Outcome

This project helped reinforce Python fundamentals while introducing a practical cybersecurity concept—password policy validation. It demonstrates the use of loops, conditional logic, string methods, and modular programming to solve a real-world security problem.

---

**Author**

Vinit Singh

Part of my **Python Cybersecurity Journey**.
