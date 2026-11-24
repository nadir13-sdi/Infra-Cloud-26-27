import json
import psutil
import platform
import socket
import datetime

def collect_system_info():
    data = {}

    # CPU info
    data["cpu"] = {
        "platform": platform.platform(),
        "processor": platform.processor(),
        "physical_cores": psutil.cpu_count(logical=False),
        "logical_processors": psutil.cpu_count(logical=True),
        "cpu_percent_total": psutil.cpu_percent(interval=0.1),
    }

    # Memory info
    data["memory"] = psutil.virtual_memory()._asdict()

    # Network hostname
    data["network"] = {
        "hostname": socket.gethostname(),
        "fqdn": socket.getfqdn(),
    }

    return data

if __name__ == "__main__":
    print("Execution time:", datetime.datetime.now())
    info = collect_system_info()
    print(json.dumps(info, indent=2))
