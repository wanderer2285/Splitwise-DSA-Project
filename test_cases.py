import unittest
from splitwise import find_path
from io import StringIO
import sys

class TestSplitwiseAdvanced(unittest.TestCase):

    def capture_output(self, balances):
        """Capture printed output from find_path()"""
        captured_output = StringIO()
        sys.stdout = captured_output
        find_path(balances)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue().strip().split('\n') if captured_output.getvalue().strip() else []

    def test_single_person(self):
        balances = {"A": 0.0}
        self.assertEqual(self.capture_output(balances.copy()), [])

    def test_three_way_cycle(self):
        # A owes B, B owes C, C owes A — net balances simplify
        balances = {
            "A": -10.0,
            "B": 5.0,
            "C": 5.0
        }
        expected = sorted([
            "A needs to pay B: 5.0",
            "A needs to pay C: 5.0"
        ])
        result = sorted(self.capture_output(balances.copy()))
        self.assertEqual(result, expected)

    def test_large_values(self):
        balances = {
            "Alice": -1000.0,
            "Bob": 500.0,
            "Charlie": 500.0
        }
        expected = sorted([
            "Alice needs to pay Bob: 500.0",
            "Alice needs to pay Charlie: 500.0"
        ])
        result = sorted(self.capture_output(balances.copy()))
        self.assertEqual(result, expected)

    def test_decimal_precision(self):
        balances = {
            "X": -33.33,
            "Y": 33.33
        }
        result = self.capture_output(balances.copy())
        self.assertEqual(result, ["X needs to pay Y: 33.3"])  # rounded to 1 decimal place then 2

    def test_multiple_creditors_and_debtors(self):
        balances = {
            "P1": -40.0,
            "P2": -20.0,
            "P3": 30.0,
            "P4": 30.0
        }
        expected = sorted([
            "P1 needs to pay P3: 30.0",
            "P2 needs to pay P4: 20.0",
            "P1 needs to pay P4: 10.0"
        ])
        result = sorted(self.capture_output(balances.copy()))
        self.assertEqual(result, expected)

    def test_zero_sum_but_nonzero_balances(self):
        balances = {
            "A": -10.0,
            "B": 10.0
        }
        self.assertEqual(self.capture_output(balances.copy()), ["A needs to pay B: 10.0"])

    def test_multiple_zeros_and_one_transaction(self):
        balances = {
            "A": 0.0,
            "B": -10.0,
            "C": 10.0
        }
        self.assertEqual(self.capture_output(balances.copy()), ["B needs to pay C: 10.0"])


if __name__ == "__main__":
    unittest.main()
