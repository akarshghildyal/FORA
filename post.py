import requests

# URL
url = "https://65637844-7657-4005-895b-782e640e1224-00-2otbdi0gavunf.pike.repl.co/device"

# data values
data = {
    "motor":"on",
    "object": "null"
}

# Send a PATCH request with the JSON data
response = requests.patch(url, json=data)

# Check the response status code
if response.status_code == 200:
    print("Data successfully updated in the API.")
else:
    print(f"Failed to update data in the API. Status code: {response.status_code}, Response: {response.text}")
