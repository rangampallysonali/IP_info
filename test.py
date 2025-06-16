import unittest
from unittest.mock import patch
import io
import ip  # your ip.py file (make sure test_ip.py is in same directory or Python path)

class TestIPPrintOutput(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fetch_and_display_ip_info_prints_expected(self, mock_stdout):
        ip.fetch_and_display_ip_info()  # call the function which prints

        output = mock_stdout.getvalue()

        # Check if some expected strings are in the printed output
        self.assertIn("IP Information:", output)
        self.assertIn("IP Address:", output)
        self.assertIn("Country:", output)

        # Optional: check that current time is printed (basic check for the label)
        self.assertIn("Current Time:", output)

if __name__ == '__main__':
    unittest.main()
