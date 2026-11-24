import paramiko
import netmiko
from netmiko import ConnectHandler
import datetime

print("Current time:", datetime.datetime.now())
print("Paramiko version:", paramiko.__version__)
print("Netmiko version:", netmiko.__version__)

device = {
    "device_type": "cisco_ios",
    "host": "10.10.20.48",
    "username": "developer",
    "password": "C1sco12345",
    "secret": "C1sco12345",
}
