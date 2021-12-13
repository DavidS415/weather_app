import flask
import requests
import json
from flask import render_template

app = flask.Flask(__name__)

@app.route("/")
def index():
    #ip_address = flask.request.remote_addr
    #location = requests.get("https://api.freegeoip.app/json/" + ip_address + "?apikey=de269640-5adf-11ec-9d7c-599c15729565")
    
    location = requests.get("https://api.freegeoip.app/json/0.0.0.0?apikey=de269640-5adf-11ec-9d7c-599c15729565")

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

    y_l2 = formated_locations[1]['woeid']
    your_location2 = str(y_l2)

    y_l3 = formated_locations[2]['woeid']
    your_location3 = str(y_l3)

    your_weather = requests.get('https://www.metaweather.com/api/location/' + your_location)
    your_weather2 = requests.get('https://www.metaweather.com/api/location/' + your_location2)
    your_weather3 = requests.get('https://www.metaweather.com/api/location/' + your_location3)
    weather = your_weather.text
    weather2 = your_weather2.text
    weather3 = your_weather3.text
    
    return render_template('index.html', weather = weather, weather2 = weather2, weather3 = weather3)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)