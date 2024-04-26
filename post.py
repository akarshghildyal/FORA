import requests

# Define the URL of the API endpoint
url = "https://fluffy-happiness-ggx49wr57xvfx74-8000.app.github.dev/device"

# Define the JSON data to send
data = {
    "connection": False,
    "motor": "off",
    "speed": 0.0
}

# Send a POST request with the JSON data
response = requests.post(url, json=data)

# Check the response status code
if response.status_code == 200:
    print("Data successfully written to the API.")
else:
    print(f"Failed to write data to the API. Status code: {response.status_code}")
