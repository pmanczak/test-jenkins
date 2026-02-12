# test-jenkins

A simple Python calculator script designed for easy testing in Jenkins CI/CD pipelines.

## Features

- Simple Python calculator with basic arithmetic operations (add, subtract, multiply, divide)
- Comprehensive unit tests using pytest
- Jenkins pipeline configuration (Jenkinsfile)
- Easy-to-use test runner script
- Coverage reporting

## Files

- `calculator.py` - Main calculator module with arithmetic functions
- `test_calculator.py` - Unit tests for the calculator
- `requirements.txt` - Python dependencies (pytest, pytest-cov)
- `Jenkinsfile` - Jenkins pipeline configuration
- `run_tests.sh` - Shell script to run tests (can be used in Jenkins or locally)

## Local Testing

### Prerequisites

- Python 3.x
- pip3

### Install Dependencies

```bash
pip3 install -r requirements.txt
```

### Run Tests

```bash
# Using pytest directly
pytest test_calculator.py -v

# With coverage report
pytest test_calculator.py -v --cov=calculator --cov-report=term-missing

# Using the test runner script
./run_tests.sh
```

### Run the Application

```bash
python3 calculator.py
```

## Jenkins Integration

This project includes a `Jenkinsfile` that defines a complete CI/CD pipeline with the following stages:

1. **Checkout** - Checks out the code from the repository
2. **Setup Python Environment** - Verifies Python installation
3. **Install Dependencies** - Installs required Python packages
4. **Run Tests** - Executes unit tests with coverage reporting
5. **Run Application** - Runs the calculator application

### Setting up in Jenkins

1. Create a new Pipeline job in Jenkins
2. Configure the job to use "Pipeline script from SCM"
3. Set SCM to Git and provide the repository URL
4. Set the script path to `Jenkinsfile`
5. Save and run the job

Alternatively, you can use the `run_tests.sh` script in a Freestyle project:

1. Create a new Freestyle project
2. Add a build step: "Execute shell"
3. Enter: `./run_tests.sh`
4. Save and run the job

## Test Results

The test suite includes tests for:
- Addition, subtraction, multiplication, and division operations
- Edge cases (zero, negative numbers, decimals)
- Error handling (division by zero)

All functions return proper exit codes for Jenkins integration.
