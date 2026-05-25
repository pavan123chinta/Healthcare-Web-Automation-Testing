# Healthcare Automation Framework

A Selenium and Pytest-based healthcare web automation framework built using Python and designed with the Page Object Model (POM) architecture for scalable and maintainable UI testing.

## Overview

This project automates healthcare web application workflows including:

- Login validation
- UI workflow testing
- Browser automation
- Screenshot capture on failure
- HTML report generation

The framework demonstrates real-world automation testing practices with a focus on modularity, maintainability, and reusable automation components.

---

## Features

### UI Automation

- Automated browser launch and teardown
- Healthcare web workflow validation
- Reusable Page Object classes
- Cross-browser compatible automation

### Reporting

- HTML execution reports
- Automatic screenshot capture on failure
- Independent test execution

### Framework Design

- Page Object Model (POM)
- Reusable Pytest fixtures
- Modular project structure
- Centralized browser management

---

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- WebDriver Manager
- Page Object Model (POM)
- pytest-html

---

## Project Structure

```bash
healthcare-automation-framework/
│
├── pages/              # Page Object classes
├── tests/              # Test cases
├── conftest.py         # Fixtures and screenshot hooks
├── reports/            # HTML reports
├── screenshots/        # Failure screenshots
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/pavan123chinta/Healthcare-Web-Automation-Testing.git
cd Healthcare-Web-Automation-Testing
```

### Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Tests

```bash
pytest -v
```

Generate HTML report:

```bash
pytest -v --html=reports/report.html --self-contained-html
```

---

## Sample Test Scenario

- Launch Chrome browser
- Navigate to Google homepage
- Validate page title
- Capture screenshot automatically on failure

---

## Key Concepts Demonstrated

- Selenium WebDriver automation
- Pytest framework integration
- Page Object Model implementation
- Reusable automation framework design
- Screenshot handling on failure
- Automated HTML reporting
- Modular test architecture

---

## Author

**Pavan Chinta**  
QA Automation Engineer | Selenium | Pytest | Python
