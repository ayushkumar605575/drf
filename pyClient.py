import requests

endpoint = "http://localhost:8000/api/"

data = requests.post(endpoint, json= {'product_id': 123})

print(data.text)
print(data.status_code)
print(data.headers)
print(data.json())