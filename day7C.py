import pytest

# --------------------------------------
# 1. Basic Test Function
# --------------------------------------
def test_sum():
    assert 3 + 5 == 8


# --------------------------------------
# 2. Assertion Failure (Intentional)
# --------------------------------------
def test_upper_fail():
    assert "hello".upper() == "hello"   # This will FAIL intentionally


# --------------------------------------
# 3. Fixture Usage
# --------------------------------------
@pytest.fixture
def num_list():
    return [1, 2, 3]

def test_list_length(num_list):
    assert len(num_list) == 3


# --------------------------------------
# 4. Parameterized Test
# --------------------------------------
def square(x):
    return x * x

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
        result = 10 / 0
