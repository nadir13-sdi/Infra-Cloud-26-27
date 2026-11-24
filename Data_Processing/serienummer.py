# serienummer.py - Week 3, opdracht 8
# Het serienummer zit niet in psutil, dus ik vraag het apart op.
# Deze functie voeg ik toe in de scripts 2 tot 7 en ik zet in de dict:
#     "serienummer": get_serienummer(),
import platform
import subprocess


def get_serienummer():
    try:
        if platform.system() == "Windows":
            cmd = ["powershell", "-NoProfile", "-Command",
                   "(Get-CimInstance Win32_BIOS).SerialNumber"]
            serie = subprocess.run(cmd, capture_output=True, text=True, timeout=15).stdout.strip()
        else:
            with open("/sys/class/dmi/id/product_serial") as f:   # soms sudo nodig
                serie = f.read().strip()
        return serie or "N/A"
    except Exception:
        return "N/A"


if __name__ == "__main__":
    print("Serienummer:", get_serienummer())
