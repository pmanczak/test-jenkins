#!/usr/bin/env python3
"""
Unit tests for the calculator module.
"""

import pytest
from calculator import add, subtract, multiply, divide


def test_add():
    """Test addition function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(100, 200) == 300


def test_subtract():
    """Test subtraction function."""
    assert subtract(5, 3) == 2
    assert subtract(10, 10) == 0
    assert subtract(0, 5) == -5
    assert subtract(100, 50) == 50


def test_multiply():
    """Test multiplication function."""
    assert multiply(3, 4) == 12
    assert multiply(0, 10) == 0
    assert multiply(-2, 5) == -10
    assert multiply(7, 7) == 49


def test_divide():
    """Test division function."""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(1, 1) == 1
    assert divide(100, 4) == 25


def test_divide_by_zero():
    """Test division by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_edge_cases():
    """Test edge cases."""
    assert add(1.5, 2.5) == 4.0
    assert multiply(0.5, 2) == 1.0
    assert divide(5, 2) == 2.5
