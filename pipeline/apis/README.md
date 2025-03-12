# Data Collection - APIs

This project focuses on **data collection using public APIs**. The goal is to learn how to **retrieve and manipulate data from external services**, laying the foundation for data processing, analysis, and machine learning tasks.

I'm working with **Python's requests library** to make API requests, handle **pagination**, deal with **rate limiting**, and process **JSON responses** into usable data.

## Learning Objectives

By the end of this project, I will be able to:

- Use the Python `requests` package to interact with APIs.
- Perform **HTTP GET requests** to retrieve resources.
- Handle **pagination** when APIs return data in multiple pages.
- Respect **API rate limits** and implement waiting/retries.
- Fetch and parse **JSON** data from an external service.
- Manipulate and process JSON data in Python.

## Technologies Used

- Python 3.5
- Requests Library
- Ubuntu 16.04 LTS
- pycodestyle 2.4 (for code formatting)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/eadewusic/alu-machine_learning.git
   cd pipeline/apis
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install requests
   ```

## How to Run

All files are executable:
```bash
chmod +x fetch_data.py
chmod +x paginate_api.py
chmod +x handle_rate_limit.py
chmod +x process_data.py
```

Run each script like this:
```bash
./fetch_data.py
./paginate_api.py
./handle_rate_limit.py
./process_data.py
```

## Requirements

- All scripts are written in Python 3.5 and follow `pycodestyle` 2.4.
- Each file starts with the shebang:
  ```python
  #!/usr/bin/env python3
  ```
- All modules, classes, and functions are documented with Python docstrings.
- All files are executable.

## Resources

- [Requests Package](https://docs.python-requests.org/en/latest/)
- [Swapi API](https://swapi-api.alx-tools.com/)
- [GitHub API](https://docs.github.com/en/rest/users?apiVersion=2022-11-28)
