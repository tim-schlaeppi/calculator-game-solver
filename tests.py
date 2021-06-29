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

    def test_inverse_operation(self):
        config = {
            "start": 0,
            "end": 99,
            "moves": 3,
            "operations": [
                operations.Append(1),
                operations.Inverse10(),
            ]
        }
        self.assertEqual(['x || 1', 'x || 1', 'inv10 x'], calculate(config))


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
    def test_save_restore(self):
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

    def test_save_restore_2(self):
        config = {
            "start": 10,
            "end": 17,
            "moves": 6,
            "operations": [
                operations.Add(2),
                operations.DivideBy(3),
                operations.Reverse(),
                *operations.save()
            ]
        }
        self.assertEqual(['x -><-', 'save', 'x + 2', 'x + 2', 'restore', 'x / 3'], calculate(config))


class TestCaseLevels(unittest.TestCase):
    def test_level_146(self):
        config = {
            "start": 23,
            "end": 1234,
            "moves": 5,
            "operations": [
                operations.MultiplyBy(2),
                operations.Subtract(5),
                operations.ShiftLeft(),
                *operations.save()
            ]
        }
        self.assertEqual(['save', 'x * 2', 'x - 5', 'restore', 'x <<'], calculate(config))

    def test_level_147(self):
        config = {
            "start": 125,
            "end": 1025,
            "moves": 7,
            "operations": [
                operations.MultiplyBy(2),
                operations.DeleteLast(),
                *operations.save()
            ]
        }
        self.assertEqual(['x * 2', 'x <-', 'save', 'x * 2', 'x * 2', 'x <-', 'restore'], calculate(config))

if __name__ == '__main__':
    unittest.main()
