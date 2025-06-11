# alumathpeer11

Pure Python matrix operations library without external dependencies.

## Features

- Matrix multiplication for different dimensions
- Efficient loop-based implementation
- No external dependencies
- Simple and intuitive API

## Installation

```bash
pip install alumathpeer11

```

## Usage

Visit pip repository: [library url](https://pypi.org/project/alumathpeer11/) and search for alumathpeer11

```python
from alumathpeer11 import Matrix, create_matrix
```

## Create matrices

m1 = create_matrix([[1, 2], [3, 4]])
m2 = create_matrix([[5, 6], [7, 8]])

## Matrix multiplication

result = m1 \* m2
print(result)


## Link to Library
[alumathpeer11 on PyPI](https://pypi.org/project/alumathpeer11/)

# Running Locally and Contributing

## Getting Started

Follow these steps to run the project locally and start contributing:

### 1. Clone Repository

```bash
git clone https://github.com/Mugisha-isaac/ALU_Formative_2
```

### 2. Change Directory

```bash
cd ALU_Formative_2
```

### 3. Install Required Tools

```bash
pip install setuptools wheel twine
```

## Next Steps

After completing the initial setup, you may want to:

### 4. Set Up Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 5. Install Project Dependencies

```bash
# Install the project in development mode
pip install -e .

# Or if there's a requirements file:
pip install -r requirements.txt
```

## Contributing Guidelines

### Code Style

- Follow PEP 8 guidelines for Python code
- Add docstrings to functions and classes
- Include tests for new functionality
- Update documentation as needed

### Building and Testing

Before submitting your contribution:

```bash
# Build the package
python -m build

# Run any linting tools
flake8 src/
# or
pylint src/

# Ensure tests pass
python -m pytest
```

cd alumathpeer11
python setup.py sdist bdist_wheel

```

```
