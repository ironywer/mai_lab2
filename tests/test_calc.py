import math
import pytest
from app import add, sub, mul, div, fibonacci, is_palindrome

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(0, 7) == -7

def test_mul():
    assert mul(4, 3) == 12
    assert mul(-2, 3) == -6

def test_div_ok():
    assert div(10, 2) == 5
    assert math.isclose(div(1, 3), 0.3333333333, rel_tol=1e-9)

def test_div_by_zero():
    import pytest
    with pytest.raises(ZeroDivisionError):
        div(1, 0)

@pytest.mark.parametrize("n, expected", [
    (0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (10, 55)
])
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected

def test_fibonacci_negative():
    import pytest
    with pytest.raises(ValueError):
        fibonacci(-1)

@pytest.mark.parametrize("s, expected", [
    ("А роза упала на лапу Азора", True),
    ("racecar", True),
    ("not a palindrome", False),
    ("", True),
    ("  ", True),
])
def test_is_palindrome(s, expected):
    assert is_palindrome(s) is expected
