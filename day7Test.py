import pytest
from src.operations import add, to_upper, get_numbers, square, divide


# --------------------------------------
# 1. Basic Test Function
# --------------------------------------
def test_sum():
    assert add(3, 5) == 8


# --------------------------------------
# 2. Assertion Failure (Intentional)
# --------------------------------------
def test_upper_fail():
    assert to_upper("hello") == "hello"   # intentional fail


# --------------------------------------
# 3. Fixture Usage
# --------------------------------------
@pytest.fixture
def num_list():
    return get_numbers()

def test_list_length(num_list):
    assert len(num_list) == 3


# --------------------------------------
# 4. Parameterized Test
# --------------------------------------
@pytest.mark.parametrize("x, expected", [
    (2, 4),
    (3, 9),
    (4, 16)
])
def test_square(x, expected):
    assert square(x) == expected


# --------------------------------------
# 5. Exception Handling
# --------------------------------------
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
