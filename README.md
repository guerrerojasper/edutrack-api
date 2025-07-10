# 🎓 EduTrack API

A lightweight RESTful API for managing educational data. Built with Flask‑RESTX for interactive swagger-style documentation, sqlite3 for persistence, pytest for unit testing, and integrated logging.

[![Flask‑RESTX](https://img.shields.io/badge/API-Flask--RESTX-blue.svg)]()
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)]()
[![SQLite](https://img.shields.io/badge/db-sqlite3-orange.svg)]()
[![pytest](https://img.shields.io/badge/test-pytest-green.svg)]()
---

## 🚀 Table of Contents

- [Tech Stack](#tech-stack)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Testing](#testing)  
- [Logging](#logging)  

---

## 🧰 Tech Stack

| Component         | Technology           |
|------------------|---------------------|
| **Framework**     | Flask‑RESTX         |
| **Database**      | sqlite3             |
| **Testing**       | pytest              |
| **Logging**       | Python `logging`    |
| **Doc**           | Swagger (via RESTX) |

---

## ✅ Features
- Interactive API documentation with Swagger UI
- RESTful operations for Students, Courses & Enrollments
- Persistent storage using sqlite3 (local file)
- Structured logging for API calls and internal events
- Unit & integration tests with pytest

---

## 🛠️ Installation
```bash
# Clone the repo
git clone https://github.com/guerrerojasper/edutrack-api.git
cd edutrack-api

# Create virtual env & install dependencies
python3 -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt

# Initialize database
flask db init
flask db migrate
flask db upgrade

```

---

## 📌 Usage
```bash
python3 run.py
```
Visit `http://127.0.0.1:5000/swagger` to access Swagger UI and explore endpoints.

---

## 🧪 Testing
Run unit tests.
```bash
pytest --maxfail=1 --disable-warnings -q

```
---

## 📝 Logging
- Uses Python's standard logging module.
- Logs HTTP requests, responses (with statuses), and error tracebacks.
- Output to console and optionally to edutrack.log file `/logs` folder (configurable).

---


