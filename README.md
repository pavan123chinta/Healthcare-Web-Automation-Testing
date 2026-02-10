# Healthcare Automation Framework

A personal Selenium + Pytest automation framework built using Python, following Page Object Model (POM) design principles.

## Tech Stack
- Python
- Selenium WebDriver
- Pytest
- WebDriver Manager
- pytest-html

## Project Objective
To design a scalable and maintainable UI automation framework that demonstrates real-world automation practices such as reusable components, fixtures, reporting, and failure handling.

## Framework Structure
healthcare-automation-framework/
│
├── pages/
│ └── google_page.py # Page Object classes
│
├── tests/
│ └── test_google.py # Test cases
│
├── conftest.py # Pytest fixtures, browser setup, screenshots on failure
├── reports/ # HTML execution reports
├── screenshots/ # Screenshots captured on test failure
├── .gitignore


## Key Features
- Page Object Model for better code maintainability
- Centralized WebDriver management using Pytest fixtures
- Automatic browser setup using WebDriver Manager
- Screenshots captured automatically on test failure
- HTML test execution reports generation

## Sample Test Scenario
- Launch Chrome browser
- Navigate to Google homepage
- Validate page title
- Capture screenshot automatically if test fails

## How to Run Tests
```bash
pytest -v
Generate HTML Report
pytest -v --html=reports/report.html --self-contained-html
Notes
This framework is created as a personal project to showcase automation testing skills using industry-standard tools and best practices.
