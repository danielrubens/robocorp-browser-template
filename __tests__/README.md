# Test Files Overview

This folder contains test files designed to test functionalities related to HTML conversion and test execution.

## 1. `html_conversor.py`

### Description:
This file contains unit tests for the `HTMLConversor` class, which is responsible for converting HTML content to PDF format. The tests cover various methods of the `HTMLConversor` class, including opening the intranet website, logging in, and downloading an Excel file.

### Test Cases:
1. **test_open_the_intranet_website:**
   - Ensures that the `open_the_intranet_website` method navigates to the correct URL.
   
2. **test_log_in:**
   - Verifies that the `log_in` method fills in the login form with the correct credentials and clicks the login button.

3. **test_fill_and_submit_sales_form:**
   - Placeholder test case. Requires implementation.

4. **test_download_excel_file:**
   - Tests the functionality of downloading an Excel file.

## 2. `test_runner.py`

### Description:
This file contains a test runner class `TestRunner` and a task `run_test` to execute the tests defined in `html_conversor.py`.

### Test Runner:
- `TestRunner` class initializes the test suite and test runner.
- `test_html_conversor` method creates a test suite from `TestHTMLConversor` class and executes it using a text test runner.

### Task:
- `run_test` task creates an instance of `TestRunner` and executes the `test_html_conversor` method.
