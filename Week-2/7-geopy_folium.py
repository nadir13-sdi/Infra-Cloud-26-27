from geopy.geocoders import Nominatim
import folium

geolocator = Nominatim(user_agent="http://biasc.be")
city_country = "Kyiv, Ukraine"

location = geolocator.geocode(city_country)
print("Address:", location.address)
devnet_lat = location.latitude
devnet_lon = location.longitude
print("Coordinates:", (devnet_lat, devnet_lon))

coordinates = [devnet_lat, devnet_lon]
map_obj = folium.Map(location=coordinates, tiles='OpenStreetMap', zoom_start=12)
map_obj.save("geopy_location.html")
print("Map saved to geopy_location.html")
