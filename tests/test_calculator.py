from calculator import Calculator
import pytest

def test_sum():
    """ Check the sum operation between two float variables. """
    assert 14 == Calculator.sum(10, 4)

def test_substract():
    """ Check the substract operation between two float variables. """
    assert 6 == Calculator.substract(10, 4)

def test_multiplication():
    """ Check the multiplication operation between two float variables. """
    assert 40 == Calculator.multiplication(10, 4)

def test_division():
    """ Check the division operation between two float variables. """
    assert 2.5 == Calculator.division(10, 4)

def test_zero_division():
    """ Check the ZeroDivisionError exception handling. """

    # Check raising of ZeroDivisonError exception.
    with pytest.raises(ZeroDivisionError) as excinfo:
        Calculator.division(10, 0)

    # Check the custom message of the exception.
    assert "ERROR: Divisor must be different from 0." == str(excinfo.value)