import json
from netmiko import ConnectHandler

# Opdracht 2 : variabelen
v_device_type = "cisco_xe"
v_host = "192.168.30.10"
v_ssh_port = 22
v_username = "cisco"
v_password = "CHANGE_ME"
v_secret = "CHANGE_ME"

device = {
    "device_type": v_device_type,
    "host": v_host,
    "port": v_ssh_port,
    "username": v_username,
    "password": v_password,
    "secret": v_secret,
}

connection = ConnectHandler(**device)
connection.enable()

# Opdracht 1 : show ssh
print("=== show ssh ===")
print(connection.send_command("show ssh"))

# Opdracht 3 : info verzamelen (TextFSM)
v = connection.send_command("show version", use_textfsm=True)[0]
info = {
    "hostname": v["hostname"],
    "model": v["hardware"][0],
    "serial": v["serial"][0],
    "ios_version": v["version"],
    "uptime": v["uptime"],
}
interfaces = connection.send_command("show ip interface brief")
cdp = connection.send_command("show cdp neighbors")
routes = connection.send_command("show ip route")

print("\nDevice Information")
print("------------------")
for k, val in info.items():
    print(f"{k}: {val}")
print("\nInterfaces\n----------")
print(interfaces)
print("\nCDP Neighbors\n-------------")
print(cdp)
print("\nRouting Table\n-------------")
print(routes)

# Opdracht 4 : JSON opslaan
with open("router_inventory.json", "w") as f:
    json.dump(info, f, indent=4)

connection.disconnect()
