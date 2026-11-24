import json
from netmiko import ConnectHandler

v_device_type = "cisco_ios"
v_host = "10.250.0.1"
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

print("=== show ssh ===")
print(connection.send_command("show ssh"))

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

with open("router_inventory_cml.json", "w") as f:
    json.dump(info, f, indent=4)

connection.disconnect()
