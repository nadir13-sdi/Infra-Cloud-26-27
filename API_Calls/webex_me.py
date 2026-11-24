import json

import requests

access_token = "PLAK_HIER_JE_TOKEN"
headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}

res = requests.get("https://webexapis.com/v1/people/me", headers=headers, timeout=10)
print("API Return Code:", res.status_code)
if res.ok:
    data = res.json()
    print("Naam:", data.get("displayName"))
    print("Status:", data.get("status"))
    print(json.dumps(data, indent=4))
else:
    print("Niet OK:", res.text)
