# weather_app
A flask app that uses a geolocation API and a weather data API to return weather condition for a users current location based on their IP address

Instructions:
1. Install to linux enviornment on NGINX using uwsgi
2. Make a call on localhost:5000 and confirm you recieve weather data for the test IP (should be Abidjan, Lagos, Ibadan)
3. remove first "location" variable in app.py and hash marks to allow first location and "ip_address" variable
4. Push to production and call from outside your nextwork to confirm you get data for near your location