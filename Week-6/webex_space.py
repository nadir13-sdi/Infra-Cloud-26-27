# webex_space.py - Week 6: space maken, bericht sturen, space verwijderen
import requests

token = "PLAK_HIER_JE_TOKEN"
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
URL = "https://webexapis.com/v1"

# Space maken
space = requests.post(f"{URL}/rooms", headers=headers, json={"title": "Infra-Cloud test"}).json()
print("Space gemaakt:", space["title"], space["id"])

# Bericht sturen
msg = requests.post(f"{URL}/messages", headers=headers,
                    json={"roomId": space["id"], "text": "Hallo vanuit Python!"})
print("Bericht status:", msg.status_code)

# Space terug verwijderen
weg = requests.delete(f"{URL}/rooms/{space['id']}", headers=headers)
print("Verwijderd, status:", weg.status_code)   # 204 = OK
