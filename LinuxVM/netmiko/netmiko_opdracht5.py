from netmiko import ConnectHandler

device = {
    "device_type": "cisco_xe",
    "host": "192.168.30.10",
    "username": "cisco",
    "password": "CHANGE_ME",
    "secret": "CHANGE_ME",
}

connection = ConnectHandler(**device)
connection.enable()

config_commands = [
    "service password-encryption",
    "banner motd #Unauthorized access is prohibited#",
]
print(connection.send_config_set(config_commands))
print(connection.save_config())

# Verificatie
running = connection.send_command("show running-config")
for expected in ["service password-encryption", "Unauthorized access is prohibited"]:
    print(f"{expected!r} ->", "OK" if expected in running else "ONTBREEKT")

connection.disconnect()
