#!/bin/bash
# Test runner script for Jenkins
# This script installs dependencies and runs tests

set -e  # Exit on error

echo "=========================================="
echo "Starting test execution..."
echo "=========================================="

# Check Python version
echo "Python version:"
python3 --version

# Install dependencies
echo ""
echo "Installing dependencies..."
pip3 install -r requirements.txt

# Run tests with coverage
echo ""
echo "Running tests..."
pytest test_calculator.py -v --cov=calculator --cov-report=term-missing --cov-report=html

# Run the application
echo ""
echo "Running application..."
python3 calculator.py

echo ""
echo "=========================================="
echo "All tests passed successfully!"
echo "=========================================="

exit 0
