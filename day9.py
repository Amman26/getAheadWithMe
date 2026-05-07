1.
# test_logic.py

def test_math_operations():
    # Check multiplication
    assert 15 * 3 == 45

    # Check if "pytest" is present in the sentence
    assert "pytest" in "Learning pytest is fun"
    PS C:\Wipro Training\Python\PythonCoding\Daily Assignments\Day 9> pytest -v
============================================================================= test session starts ==============================================================================
platform win32 -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Program Files\Python314\python.exe
cachedir: .pytest_cache
rootdir: C:\Wipro Training\Python\PythonCoding\Daily Assignments\Day 9
collected 1 item                                                                                                                                                                

test_logic.py::test_math_operations PASSED                                                                                                                                [100%]

============================================================================== 1 passed in 0.06s ===============================================================================
PS C:\Wipro Training\Python\PythonCoding\Daily Assignments\Day 9> 
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
    PS C:\Wipro Training\Python\PythonCoding\Daily Assignments\Day 9> pytest -v test_fixture.py        
============================================================================= test session starts ==============================================================================
platform win32 -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Program Files\Python314\python.exe
cachedir: .pytest_cache
rootdir: C:\Wipro Training\Python\PythonCoding\Daily Assignments\Day 9
collected 1 item                                                                                                                                                                

test_fixture.py::test_dict_keys PASSED                                                                                                                                    [100%]

============================================================================== 1 passed in 0.02s ===============================================================================
PS C:\Wipro Training\Python\PythonCoding\Daily Assignments\Day 9> 
  3.
import pytest


def get_element(my_list, index):
    return my_list[index]


def test_index_error():
    with pytest.raises(IndexError):
        get_element([1, 2, 3], 10)
        Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Wipro Training\Python\PythonCoding\Daily Assignments\Day 9> pytest -v test_exception.py
============================================================================= test session starts ==============================================================================
platform win32 -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Program Files\Python314\python.exe
cachedir: .pytest_cache
rootdir: C:\Wipro Training\Python\PythonCoding\Daily Assignments\Day 9
collected 1 item                                                                                                                                                                

test_exception.py::test_index_error PASSED                                                                                                                                [100%]

============================================================================== 1 passed in 0.03s ===============================================================================

4.
import pytest


@pytest.mark.parametrize("number", [2, 10, 22])
def test_is_even(number):
    assert number % 2 == 0
PS C:\Wipro Training\Python\PythonCoding\Daily Assignments\Day 9> pytest -v test_parametrize.py
============================================================================= test session starts ==============================================================================
platform win32 -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Program Files\Python314\python.exe
cachedir: .pytest_cache
rootdir: C:\Wipro Training\Python\PythonCoding\Daily Assignments\Day 9
collected 3 items                                                                                                                                                               

test_parametrize.py::test_is_even[2] PASSED                                                                                                                               [ 33%]
test_parametrize.py::test_is_even[10] PASSED                                                                                                                              [ 66%]
test_parametrize.py::test_is_even[22] PASSED                                                                                                                              [100%]

============================================================================== 3 passed in 0.02s ===============================================================================
PS C:\Wipro Training\Python\PythonCoding\Daily Assignments\Day 9> 
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

PS C:\Wipro Training\Python\PythonCoding\Daily Assignments\Day 9> pytest -v test_file.py
============================================================================= test session starts ==============================================================================
platform win32 -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Program Files\Python314\python.exe
cachedir: .pytest_cache
rootdir: C:\Wipro Training\Python\PythonCoding\Daily Assignments\Day 9
collected 1 item                                                                                                                                                                

test_file.py::test_file_content PASSED                                                                                                                                    [100%]

============================================================================== 1 passed in 0.03s ===============================================================================
PS C:\Wipro Training\Python\PythonCoding\Daily Assignments\Day 9> 

  Before the test runs:
test.txt is created.
"Hello World" is written into it.
yield filename sends the filename to the test.
After the test finishes:
os.remove(filename) deletes the file automatically.
      
