1.
# test_logic.py

def test_math_operations():
    # Check multiplication
    assert 15 * 3 == 45

    # Check if "pytest" is present in the sentence
    assert "pytest" in "Learning pytest is fun"
  2.
import pytest


@pytest.fixture
def sample_dict():
    return {"name": "Alice", "role": "Dev"}


def test_dict_keys(sample_dict):
    # Check if "role" key exists
    assert "role" in sample_dict

    # Check value of "name"
    assert sample_dict["name"] == "Alice"
  3.
import pytest


def get_element(my_list, index):
    return my_list[index]


def test_index_error():
    with pytest.raises(IndexError):
        get_element([1, 2, 3], 10)
4.
import pytest


@pytest.mark.parametrize("number", [2, 10, 22])
def test_is_even(number):
    assert number % 2 == 0
5.
import pytest
import os


@pytest.fixture
def temp_file():
    # Setup phase
    filename = "test.txt"

    with open(filename, "w") as file:
        file.write("Hello World")

    # Provide filename to the test
    yield filename

    # Teardown phase
    os.remove(filename)


def test_file_content(temp_file):
    with open(temp_file, "r") as file:
        content = file.read()

    assert content == "Hello World"

  Before the test runs:
test.txt is created.
"Hello World" is written into it.
yield filename sends the filename to the test.
After the test finishes:
os.remove(filename) deletes the file automatically.
      
