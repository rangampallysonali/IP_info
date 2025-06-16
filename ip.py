import requests
import json
from datetime import datetime

def fetch_and_display_ip_info():
    """Fetches IP information and displays it."""
    try:
        response = requests.get("https://ipinfo.io/json")
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        print("IP Information:")
        print(f"  IP Address: {data['ip']}")
        print(f"  City: {data.get('city', 'N/A')}")
        print(f"  Region: {data.get('region', 'N/A')}")
        print(f"  Country: {data['country']}")
        print(f"  Timezone: {data.get('timezone', 'N/A')}")
        
        current_time = datetime.now()
        print(f"  Current Time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")


    except requests.exceptions.RequestException as e:
        print(f"Error fetching IP information: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")

if __name__ == "__main__":
    fetch_and_display_ip_info()
