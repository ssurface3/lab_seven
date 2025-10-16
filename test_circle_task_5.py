import unittest
from unittest.mock import patch
from io import StringIO
from circle import main

class TestMainFunctionWithMock(unittest.TestCase):

    @patch('builtins.input', side_effect=['5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_input(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Enter the radius of the circle:", output)
        self.assertIn("The area of the circle with radius 5.0 is 78.54", output)

    @patch('builtins.input', side_effect=['invalid'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_input(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Enter the radius of the circle:", output)
        self.assertIn("Invalid input. Please enter a valid number.", output)

    @patch('builtins.input', side_effect=['-5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_negative_input(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Enter the radius of the circle:", output)
        self.assertIn("Radius cannot be negative.", output)

if __name__ == '__main__':
    unittest.main()
