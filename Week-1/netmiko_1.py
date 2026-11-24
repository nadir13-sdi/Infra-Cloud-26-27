# netmiko_1.py - Week 1, opdracht 6 (eerste test met de CSR1000v)
import datetime
from netmiko import ConnectHandler

print(datetime.datetime.now())
device = {
    "device_type": "cisco_ios",
    "host": "192.168.30.10",
    "username": "cisco",
    "password": "cisco123!",
    "secret": "cisco123!",
}
connection = ConnectHandler(**device)
connection.enable()
print(connection.send_command("show ip interface brief"))
connection.disconnect()
