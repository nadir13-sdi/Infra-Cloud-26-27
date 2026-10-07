import requests
import json
import sys
import datetime

# --- Subnet Mask Helper Functions ---
netmask_prefixes = {
    '255.255.255.255': '/32', '255.255.255.254': '/31', '255.255.255.252': '/30',
    '255.255.255.248': '/29', '255.255.255.240': '/28', '255.255.255.224': '/27',
    '255.255.255.192': '/26', '255.255.255.128': '/25', '255.255.255.0': '/24'
}

def get_net_prefix(p_subnet_mask):
    return netmask_prefixes.get(p_subnet_mask, "Wrong input")

def get_number_ip_hosts(p_prefix):
    pbits = 32 - int(p_prefix[1:])
    return (2 ** pbits) - 2

print("Subnet test /27:", get_number_ip_hosts('/27'), "hosts")

# --- Fetch My IP Address ---
now = datetime.datetime.now()
print("\nCurrent Time:", now)

try:
    r = requests.get("https://api.ipify.org?format=json", timeout=10)
    if r.status_code == 200:
        ip_json = r.json()
        print("JSON response:", json.dumps(ip_json))
        print("IP Address:", ip_json.get("ip"))
    else:
        print("Error fetching IP:", r.status_code)
except Exception as e:
    print("Request failed:", e)
