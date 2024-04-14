import requests

endpoint = "http://localhost:8000/api/"

data = requests.post(endpoint, json= {'title': "Hello World"})

print(data.text)
print(data.status_code)
print(data.headers)
print(data.json())