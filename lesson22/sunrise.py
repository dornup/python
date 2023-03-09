import requests
from geopy.geocoders import Nominatim
from pprint import pprint

pupipu = Nominatim(user_agent = "Melanya")
locatia = pupipu.geocode("Russia, Novosibirsk").raw
pprint(locatia)
response = requests.get("https://api.sunrise-sunset.org/json?lat=locatia['lat']&lng=locatia['lon']& date = today")
print(response["sunrise"],response["sunset"])


