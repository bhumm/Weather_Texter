from noaa_sdk import NOAA
from datetime import datetime, date, timezone, timedelta
import requests as r
import json

# Instantiate NOAA object
noaa = NOAA()

# Query for your area
query = noaa.get_forecasts('your_zip', 'your_country')

# Collect today's info
today = date.today()
t_y, t_m, t_d = today.year, today.month, today.day

# Parse query for date and time info
for entry in query:
    dt = datetime.fromisoformat(entry['startTime'])
    y, m, d, h = dt.year, dt.month, dt.day, dt.hour

    # If it is today:
    if y == t_y and m == t_m and d == t_d:
        # Collect weather info for 7am
        if h == 7:
            morn_temp = str(entry['temperature']) + 'F'
            morn_precip = str(entry['probabilityOfPrecipitation']['value']) + '%'
            morn_speed =  entry['windSpeed']
            morn_fore = entry['shortForecast']
        
        # Collect weather info for 12pm
        if h == 12:
            aft_temp = str(entry['temperature']) + 'F'
            aft_precip = str(entry['probabilityOfPrecipitation']['value']) + '%'
            aft_speed =  entry['windSpeed']
            aft_fore = entry['shortForecast']
            
        # Collect weather info for 5pm
        if h == 17:
            eve_temp = str(entry['temperature']) + 'F'
            eve_precip = str(entry['probabilityOfPrecipitation']['value']) + '%'
            eve_speed =  entry['windSpeed']
            eve_fore = entry['shortForecast']
            
# sinch info
service_plan_id = 'sinch_service_plan_id'
API_token = 'sinch_API_token'

from_number = 'from_number'
to_number = 'your_number'

headers = {
    "Authorization": f"Bearer {API_token}",
    "Content-Type": "application/json"
}

# The payload (to, from, and the message)
payload = {
    "from": from_number,
    "to": [to_number],
    "body": f"Today's Forecast: ------------------------- \
    Morning: temp:{morn_temp}, precip:{morn_precip}, forecast:{morn_fore}, wind speed:{morn_speed} -------------------------\
    Afternoon: temp:{aft_temp}, precip:{aft_precip}, forecast:{aft_fore}, wind speed:{aft_speed} -------------------------\
    Evening: temp:{eve_temp}, precip:{eve_precip}, forecast:{eve_fore}, wind speed:{eve_speed}"
}
#    Morning: temp:{morn_temp}, precip:{morn_precip}, forecast:{morn_fore}, wind speed:{morn_speed} -------------------------\

# Send the text
r.post(
    "your_sinch_API_link",
    headers = headers,
    data = json.dumps(payload)
)
