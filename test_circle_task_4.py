import unittest
import sys
from io import StringIO
from circle import main

class TestMainFunction(unittest.TestCase):

    def setUp(self):
        self.held_stdout = StringIO()
        self.held_stdin = StringIO()
        sys.stdout = self.held_stdout
        sys.stdin = self.held_stdin

    def tearDown(self):
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

    def test_valid_input(self):
        test_input = "5\n"
        expected_output = "Enter the radius of the circle: The area of the circle with radius 5.0 is 78.54\n"

        self.held_stdin.write(test_input)
        self.held_stdin.seek(0)

        main()

        self.assertEqual(self.held_stdout.getvalue(), expected_output)

    def test_invalid_input(self):
        test_input = "invalid\n"
        expected_output = "Enter the radius of the circle: Invalid input. Please enter a valid number.\n"

        self.held_stdin.write(test_input)
        self.held_stdin.seek(0)

        main()

        self.assertEqual(self.held_stdout.getvalue(), expected_output)

    def test_negative_input(self):
        test_input = "-5\n"
        expected_output = "Enter the radius of the circle: Radius cannot be negative.\n"

        self.held_stdin.write(test_input)
        self.held_stdin.seek(0)

        main()

        self.assertEqual(self.held_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
