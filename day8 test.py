import unittest
from src.operations import add, subtract, get_list, to_upper, is_upper, divide


# --------------------------------------
# 1. Basic Test Case
# --------------------------------------
class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)


# --------------------------------------
# 2. Setup and Teardown
# --------------------------------------
class TestList(unittest.TestCase):

    def setUp(self):
        self.data = get_list()

    def tearDown(self):
        print("Test completed")

    def test_length(self):
        self.assertEqual(len(self.data), 3)


# --------------------------------------
# 3. Multiple Assertions
# --------------------------------------
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(to_upper("hello"), "HELLO")

    def test_isupper(self):
        self.assertFalse(is_upper("hello"))


# --------------------------------------
# 4. Exception Testing
# --------------------------------------
class TestException(unittest.TestCase):

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


# --------------------------------------
# 5. Test Suite Execution
# --------------------------------------
class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)


class TestSubtract(unittest.TestCase):

    def test_sub(self):
        self.assertEqual(subtract(10, 5), 5)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAdd))
    suite.addTest(unittest.makeSuite(TestSubtract))

    runner = unittest.TextTestRunner()
    runner.run(suite)
