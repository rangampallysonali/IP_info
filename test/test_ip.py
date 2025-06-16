import sys
import os
# Add parent directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ip import fetch_and_display_ip_info

class TestIPInfo(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_and_display_ip_info_success(self, mock_get):
        # Simulated JSON response
        mock_response = {
            "ip": "123.123.123.123",
            "city": "Hyderabad",
            "region": "Telangana",
            "country": "IN",
            "timezone": "Asia/Kolkata"
        }

        # Configure the mock to return a response with our mock data
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        mock_get.return_value.raise_for_status = lambda: None

        # Capture the print output
        captured_output = StringIO()
        sys.stdout = captured_output

        fetch_and_display_ip_info()

        # Reset stdout
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("IP Address: 123.123.123.123", output)
        self.assertIn("City: Hyderabad", output)
        self.assertIn("Country: IN", output)

    @patch('requests.get')
    def test_fetch_and_display_ip_info_http_error(self, mock_get):
        mock_get.side_effect = Exception("HTTP Error")

        captured_output = StringIO()
        sys.stdout = captured_output

        fetch_and_display_ip_info()

        sys.stdout = sys.__stdout__

        self.assertIn("Error fetching IP information", captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()
