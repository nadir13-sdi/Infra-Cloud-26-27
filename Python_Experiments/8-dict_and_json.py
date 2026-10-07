import json

if_dict = {
    "ietf-interfaces:interfaces": {
        "interface": [
            {
                "name": "GigabitEthernet1",
                "description": "VBox",
                "type": "iana-if-type:ethernetCsmacd",
                "enabled": True,
                "ietf-ip:ipv4": {"address": [{"ip": "192.168.56.101", "netmask": "255.255.255.0"}]},
                "ietf-ip:ipv6": {}
            },
            {
                "name": "Loopback9",
                "description": "999",
                "type": "iana-if-type:softwareLoopback",
                "enabled": True,
                "ietf-ip:ipv4": {"address": [
                    {"ip": "10.9.9.9", "netmask": "255.255.255.0"},
                    {"ip": "172.29.0.9", "netmask": "255.255.255.0"}
                ]},
                "ietf-ip:ipv6": {}
            }
        ]
    }
}

print("Type of if_dict:", type(if_dict))
print(if_dict)

# Convert Dict to JSON string
if_json = json.dumps(if_dict, indent=2)
print("\nFormatted JSON String:")
print(if_json)
print("Type of if_json:", type(if_json))
