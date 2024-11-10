import requests
import time
from datetime import datetime

# API endpoint
url = "http://<Your-Flask-Server-IP>:5000/update_location"

while True:
    # Fetch GPS coordinates (replace with actual GPS coordinates from the device)
    # For Termux, GPS data can be accessed via `termux-location`
    latitude = 47.4979  # Example coordinates
    longitude = 19.0402
    
    # Send location data to server
    data = {
        "latitude": latitude,
        "longitude": longitude,
        "timestamp": str(datetime.now())
    }
    response = requests.post(url, json=data)
    print(response.json())

    # Sleep for a specified interval (e.g., 60 seconds)
    time.sleep(60)
