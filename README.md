# Web Application Security Scanner

Educational defensive scanner for systems you own or are explicitly authorized to test.

Features: same-origin crawling, URL/form discovery, security-header checks, cookie checks, safe reflected-input detection, OWASP-oriented categories, severity classification, SQLite history, Flask dashboard and JSON API.

Run with Python 3.11+:
py -3.11 -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python app.py

Open http://127.0.0.1:5000

Use only authorized targets. For practice, use OWASP Juice Shop or DVWA locally. This project deliberately avoids credential attacks, destructive payloads, WAF bypasses and arbitrary third-party scanning.
