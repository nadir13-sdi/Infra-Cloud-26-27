import requests

token = "PLAK_HIER_JE_TOKEN"
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
URL = "https://webexapis.com/v1"

space = requests.post(f"{URL}/rooms", headers=headers, json={"title": "Infra-Cloud test"}).json()
print("Space gemaakt:", space["title"], space["id"])

msg = requests.post(f"{URL}/messages", headers=headers,
                    json={"roomId": space["id"], "text": "Hallo vanuit Python!"})
print("Bericht status:", msg.status_code)

weg = requests.delete(f"{URL}/rooms/{space['id']}", headers=headers)
print("Verwijderd, status:", weg.status_code)
