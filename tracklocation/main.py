import phonenumbers
import opencage
import folium
from number import number

from phonenumbers import geocoder
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier 
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "Ben"))

from opencage.geocoder import OpenCageGeocode

key = "ae715da9dcdb4d4aa584872150a284b4"
geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
# print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")