import requests
from datetime import datetime

# ISS code
# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
#
# print(longitude,latitude)

# Sunset Code
MY_LAT = 1.372580
MY_LONG = 103.893646

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split("+")[0]
sunset = data['results']['sunset'].split('T')[1].split("+")[0]


time_now = datetime.now()
print(sunset)
print(sunrise)
print(time_now)