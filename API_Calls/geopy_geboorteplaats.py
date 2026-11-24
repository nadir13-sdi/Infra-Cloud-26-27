import datetime
import sys

import folium
from geopy.geocoders import Nominatim

plaats = sys.argv[1] if len(sys.argv) > 1 else "Brussel, België"
bestand = "geboorteplaats.html"

print(datetime.datetime.now())
geolocator = Nominatim(user_agent="infra-cloud-26-27")
location = geolocator.geocode(plaats)
print(location.address)
print((location.latitude, location.longitude))

kaart = folium.Map(location=[location.latitude, location.longitude], tiles="OpenStreetMap", zoom_start=13)
folium.Marker([location.latitude, location.longitude], popup=plaats, tooltip="Mijn geboorteplaats").add_to(kaart)
kaart.save(bestand)
print("Webpagina gemaakt:", bestand)
