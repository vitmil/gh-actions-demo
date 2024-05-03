# file: test_math_functions.py
#
# syntax how to run test: pytest-3 test_math_functions.py -v


import pytest

from math_functions import add_numbers


def test_add_numbers_positive():
    """
    Testa la funzione add_numbers con numeri positivi.
    """
    assert add_numbers(1, 2) == 3
    assert add_numbers(5, 7) == 12


def test_add_numbers_negative():
    """
    Testa la funzione add_numbers con numeri negativi.
    """
    assert add_numbers(-1, -2) == -3
    assert add_numbers(-5, -7) == -12


def test_add_numbers_zero():
    """
    Testa la funzione add_numbers con lo zero.
    """
    assert add_numbers(0, 0) == 0
    assert add_numbers(1, 0) == 1
    assert add_numbers(0, -1) == -1

