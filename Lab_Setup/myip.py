# myip.py - Week 1, opdracht 6
import datetime
import requests

print(datetime.datetime.now())
r = requests.get("https://api.ipify.org?format=json", timeout=10)
print("Status code:", r.status_code)
data = r.json()          # JSON -> Python dict
print(data)
print("Mijn publiek IP-adres:", data["ip"])
