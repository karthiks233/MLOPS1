import pytest
from src import calculator 
import math

# Use pytest.approx() to handle floating-point precision issues.

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(5, 0) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(-1, -1) == -2
    assert calculator.add(2.5, 3.5) == 6.0

def test_sub():
    assert calculator.sub(2, 3) == -2
    assert calculator.sub(5, 0) == 5
    assert calculator.sub(-1, 1) == -2
    assert calculator.sub(-1, -1) == 0
    assert calculator.sub(4.5, 2.5) == 2.0

def test_mul():
    assert calculator.mul(2, 3) == 6
    assert calculator.mul(5, 0) == 0
    assert calculator.mul(-1, 1) == -1
    assert calculator.mul(2.5, 2) == 5.0

def test_div():
    assert calculator.div(10, 2) == 5.0
    assert calculator.div(5, 2) == 2.5
    assert calculator.div(-1, -1) == 1.0
    assert calculator.div(-1, 100) == -0.01

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.div(10, 0)
    with pytest.raises(ZeroDivisionError):
        calculator.div(0, 0)

def test_sin():
    # Correctly test the tuple return values with an absolute tolerance for precision.
    assert calculator.sin(90, 0)[0] == pytest.approx(1.0, abs=1e-3)
    assert calculator.sin(90, 0)[1] == pytest.approx(0.0, abs=1e-3)
    assert calculator.sin(30, 60)[0] == pytest.approx(0.5, abs=1e-3)
    assert calculator.sin(30, 60)[1] == pytest.approx(math.sqrt(3) / 2, abs=1e-3)
    assert calculator.sin(-90, -30)[0] == pytest.approx(-1.0, abs=1e-3)
    assert calculator.sin(-90, -30)[1] == pytest.approx(-0.5, abs=1e-3)

def test_cos():
    # Correctly test the tuple return values with an absolute tolerance for precision.
    assert calculator.cos(90, 0)[0] == pytest.approx(0.0, abs=1e-3)
    assert calculator.cos(90, 0)[1] == pytest.approx(1.0, abs=1e-3)
    assert calculator.cos(30, 60)[0] == pytest.approx(math.sqrt(3) / 2, abs=1e-3)
    assert calculator.cos(30, 60)[1] == pytest.approx(0.5, abs=1e-3)
    assert calculator.cos(-90, -30)[0] == pytest.approx(0.0, abs=1e-3)
    assert calculator.cos(-90, -30)[1] == pytest.approx(math.sqrt(3) / 2, abs=1e-3)

def test_tan():
    # Correctly test the tuple return values with an absolute tolerance for precision.
    assert calculator.tan(45, 0)[0] == pytest.approx(1.0, abs=1e-3)
    assert calculator.tan(45, 0)[1] == pytest.approx(0.0, abs=1e-3)
    assert calculator.tan(-45, -30)[0] == pytest.approx(-1.0, abs=1e-3)
    assert calculator.tan(-45, -30)[1] == pytest.approx(-math.sqrt(3)/3, abs=1e-3)

def test_log():
    assert calculator.log(8, 2) == pytest.approx(3.0)
    assert calculator.log(10, 10) == pytest.approx(1.0)
    assert calculator.log(100, 10) == pytest.approx(2.0)
    # Test for log of a negative number or a base of 0 or 1.
    with pytest.raises(ValueError):
        calculator.log(-1, 2)
    with pytest.raises(ZeroDivisionError):
        calculator.log(10, 1)
    with pytest.raises((ValueError, ZeroDivisionError)):
        calculator.log(10, 0)


def test_exp():
    assert calculator.exp(2, 3) == pytest.approx(8.0)
    assert calculator.exp(5, 2) == pytest.approx(25.0)
    assert calculator.exp(-1, 2) == pytest.approx(1.0)
    assert calculator.exp(-2, 3) == pytest.approx(-8.0)

def test_root():
    # Correctly test the tuple return values
    assert calculator.root(4, 9)[0] == pytest.approx(2.0)
    assert calculator.root(4, 9)[1] == pytest.approx(3.0)
    assert calculator.root(100, 25)[0] == pytest.approx(10.0)
    assert calculator.root(100, 25)[1] == pytest.approx(5.0)
    # Test for square root of a negative number
    with pytest.raises(ValueError):
        calculator.root(-1, 2)
