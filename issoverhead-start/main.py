import requests
from datetime import datetime
from time import sleep
import smtplib

# MY_LAT = 51.507351 # Your latitude
# MY_LONG = -0.127758 # Your longitude
MY_LAT = 1.372580
MY_LONG = 103.893646


def is_iss_overhead(latitude, longitude):
    """
    Check if iss is overhead with 5 degrees +-, returns boolean on whether it is overhead
    :param latitude: float
    :param longitude: float
    :return: True/False
    """

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (iss_latitude < latitude + 5 or iss_longitude > latitude - 5) and \
            (iss_longitude < longitude + 5 or iss_longitude > longitude - 5):
        return True
    else:
        return False


# Your position is within +5 or -5 degrees of the ISS position.

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour < sunrise or time_now.hour > sunset:
        return True
    else:
        return False


while True:
    if is_dark() and is_iss_overhead(latitude=MY_LAT, longitude=MY_LONG):
        # Email send code
        # connection = smtplib.SMTP('SMTP.GMAIL.COM')
        # connection.starttls()
        # connection.login(user='',
        #                  password='')
        # connection.sendmail(from_addr='',to_addrs='',
        #                     msg='Subject: ISS is overhead \n\n Look above, the ISS is overhead now.')
        print('sent email, please look up now')
    else:
        break
    sleep(60)
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
