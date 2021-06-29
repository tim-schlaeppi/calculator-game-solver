import unittest

import operations
from calculate import calculate


class TestCaseBasic(unittest.TestCase):
    def test_add_operation(self):
        config = {
            "start": 0,
            "end": 3,
            "moves": 3,
            "operations": [
                operations.Add(1),
            ]
        }
        self.assertEqual(['x + 1', 'x + 1', 'x + 1'], calculate(config))

    def test_subtract_operation(self):
        config = {
            "start": 0,
            "end": -3,
            "moves": 3,
            "operations": [
                operations.Subtract(1),
            ]
        }
        self.assertEqual(['x - 1', 'x - 1', 'x - 1'], calculate(config))

    def test_multiply_operation(self):
        config = {
            "start": 1,
            "end": 8,
            "moves": 3,
            "operations": [
                operations.MultiplyBy(2),
            ]
        }
        self.assertEqual(['x * 2', 'x * 2', 'x * 2'], calculate(config))


class TestCaseMetaOperations(unittest.TestCase):
    def test_addtobutton_operation(self):
        config = {
            "start": 0,
            "end": 123,
            "moves": 5,
            "operations": [
                operations.Append(1),
                operations.AddToButton(1)
            ]
        }
        self.assertEqual(['x || 1', '[+] 1', 'x || 2', '[+] 1', 'x || 3'], calculate(config))


class TestCaseSaveRestore(unittest.TestCase):
    def test_basic_funtions(self):
        config = {
            "start": 0,
            "end": 121,
            "moves": 5,
            "operations": [
                operations.Add(1),
                *operations.save()
            ]
        }
        self.assertEqual(['x + 1', 'save', 'restore', 'x + 1', 'restore'], calculate(config))


if __name__ == '__main__':
    unittest.main()
