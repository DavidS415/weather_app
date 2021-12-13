import requests
import json
from typing import Dict

location = requests.get("https://api.freegeoip.app/json/76.226.167.228?apikey=de269640-5adf-11ec-9d7c-599c15729565")

data = location.text
formated_data = json.loads(data)
l = formated_data['latitude']
latitude = str(l)
lo = formated_data['longitude']
longitutde = str(lo)

weather_locations = requests.get("https://www.metaweather.com/api/location/search/?lattlong=" + latitude + "," + longitutde)

data_locations = weather_locations.text
formated_locations = json.loads(data_locations)

y_l = formated_locations[0]['woeid']
your_location = str(y_l)

your_weather = requests.get('https://www.metaweather.com/api/location/' + your_location)
print(your_weather.status_code)
print(your_weather.json())

#print(location.status_code)
#print(location.json())

#weather = requests.get("https://www.metaweather.com/api/location/search/?lattlong=37.9834,-122.0312")

#print(weather.status_code)
#print(weather.json())


#{'ip': '76.226.167.228', 'country_code': 'US', 'country_name': 'United States', 'region_code': 'CA', 'region_name': 'California', 'city': 'Concord', 'zip_code': '94520', 'time_zone': 'America/Los_Angeles', 'latitude': 37.9834, 'longitude': -122.0312, 'metro_code': 807}