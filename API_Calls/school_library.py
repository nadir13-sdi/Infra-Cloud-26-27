import json
import requests

BASIS = "http://library.demo.local/api/v1"

r = requests.post(f"{BASIS}/loginViaBasic", auth=("cisco", "Cisco123!"))
print("Login status:", r.status_code)
token = r.json()["token"]
headers = {"X-API-KEY": token, "Content-Type": "application/json"}

r = requests.get(f"{BASIS}/books", headers=headers)
print("GET status:", r.status_code)
boeken = r.json()
print("Aantal boeken:", len(boeken))
for boek in boeken[:5]:
    print(boek["id"], "-", boek["title"], "-", boek["author"])

nieuw = {"id": 101, "title": "Netwerkautomatisatie", "author": "Student", "isbn": "123-4-56-789012-3"}
r = requests.post(f"{BASIS}/books", headers=headers, json=nieuw)
print("POST status:", r.status_code)
print(json.dumps(r.json(), indent=2))
