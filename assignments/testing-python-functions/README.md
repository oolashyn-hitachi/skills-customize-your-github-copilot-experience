# 📘 Assignment: Testing Python Functions with pytest

## 🎯 Objective

Learn to write and run automated tests for Python functions using pytest. Use a failing test to find and fix a bug in a function.

## 📝 Tasks

### 🛠️ Run and Extend the Tests

#### Description
Install pytest, run the provided tests, and add a test case of your own to `test_functions.py`.

#### Requirements
Completed program should:

- Install the packages listed in `requirements.txt` with `python -m pip install -r requirements.txt`.
- Run the tests with `python -m pytest`.
- Include at least one additional test using a descriptive function name that starts with `test_`.
- Use `assert` to check the expected result of a function call.

### 🛠️ Find and Fix the Average Bug

#### Description
Add tests for `calculate_average()` in `test_functions.py`. Use a failing test to identify and fix the function's calculation in `functions.py`.

#### Requirements
Completed program should:

- Test the average of a non-empty list, including a case where the result is not a whole number (for example, `[2, 3]` should produce `2.5`).
- Correct `calculate_average()` so it returns the accurate average rather than a rounded-down integer.
- Run the full test suite and confirm all tests pass.
