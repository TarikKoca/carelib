# Carelib

Carelib is a Python library developed by Caresept for AI-related tasks. It provides a set of tools and utilities to help with various artificial intelligence and machine learning operations.

## Installation

You can install Carelib using pip:

```bash
pip install carelib
```

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/TarikKoca/carelib.git
cd carelib
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -e .
```

## Testing

Run the test suite using:
```bash
python -m unittest discover -s tests -p "*.py" -v
```

## Project Structure

```
carelib/
├── carelib/          # Main package directory
├── tests/            # Test files
├── setup.py          # Package configuration
└── README.md         # This file
```