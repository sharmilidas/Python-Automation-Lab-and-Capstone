Assignment 15 - Robot Framework Custom Keywords and Libraries

Objective:
Create reusable custom keywords in a Robot Framework resource file and use them
from a test suite to automate a complete SauceDemo login/logout flow.

Concepts:
- Robot Framework custom keywords
- Resource files
- SeleniumLibrary
- Keyword reuse
- Suite teardown
- Web UI automation

Execution:
1. Install dependencies:
   python -m pip install -r requirements.txt

2. Run:
   python -m robot custom_keywords.robot

Expected:
   1 test, 1 passed, 0 failed

Files:
- custom_keywords.robot: main test suite
- resources/saucedemo_keywords.resource: reusable custom keywords
- output.xml, log.html, report.html: Robot execution reports
- Screenshots/: labelled execution evidence
