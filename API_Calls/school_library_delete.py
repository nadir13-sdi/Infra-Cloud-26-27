import requests

APIHOST = "http://library.demo.local"

r = requests.post(f"{APIHOST}/api/v1/loginViaBasic", auth=("cisco", "Cisco123!"))
apiKey = r.json()["token"]

for i in range(90, 100):
    r = requests.delete(f"{APIHOST}/api/v1/books/{i}", headers={"X-API-Key": apiKey})
    print(f"DELETE boek {i}: status {r.status_code}")
