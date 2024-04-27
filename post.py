import requests

# URL of the API endpoint
url = "https://super-invention-px7jvqwgj6qcrgrp-8000.app.github.dev/device"

# Define the JSON data to send, only the field you want to update
data = {
    "motor":"on",
    "object": "banana"
}

# Send a PATCH request with the JSON data
response = requests.patch(url, json=data)

# Check the response status code
if response.status_code == 200:
    print("Data successfully updated in the API.")
else:
    print(f"Failed to update data in the API. Status code: {response.status_code}, Response: {response.text}")
