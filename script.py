import requests
import json
import csv
import os
from datetime import datetime
import pytz

api_key = os.environ['AIRVISUAL_API_KEY']
pushbullet_api_key = os.environ['PUSHBULLET_API_KEY']
# Set Location - Change City, State, and Country based to match your desired location. 
# Keep in mind that the community API from IQair is limited to cities and cannot be used to retrieve specific stations. 
city = "New York City"
state = "New York"
country = "USA"

url = f"http://api.airvisual.com/v2/city?city={city}&state={state}&country={country}&key={api_key}"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
data = json.loads(response.text)
print(data)

city = data['data']['city']
state = data['data']['state']
country = data['data']['country']
aqius = data['data']['current']['pollution']['aqius']
temperature = data['data']['current']['weather']['tp']
pressure = data['data']['current']['weather']['pr']
humidity = data['data']['current']['weather']['hu']
wind_speed = data['data']['current']['weather']['ws']

# Get current date and time for New York City
# Adjust the timezone to fit the city you are retriving data about. 
tz = pytz.timezone('America/New_York')
now = datetime.now(tz)
date = now.strftime("%m/%d/%Y")
time = now.strftime("%H:%M:%S")

# Write header row to CSV file if it doesn't exist
if not os.path.exists('data.csv'):
    with open('data.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Time', 'City', 'State', 'Country', 'AQI (US)', 'Temperature (°C)', 'Pressure (hPa)', 'Humidity (%)', 'Wind Speed (m/s)'])

# Append data to CSV file
with open('data.csv', mode='a') as file:
    writer = csv.writer(file)
    writer.writerow([date, time, city, state, country, aqius, temperature, pressure, humidity, wind_speed])

# Send notification through Pushbullet if AQI is above certain thresholds
if aqius > 80:
    if aqius < 120:
        message = f"Current AQI (US) of {aqius} exceeds 80. Please be mindful about prolonged outdoor activities."
    elif aqius < 160:
        message = f"Current AQI (US) of {aqius} is above 120. Any outdoor activities should be reduced.Please remember to wear a mask."
    elif aqius < 190:
        message = f"Current AQI (US) of {aqius} is above 165. Please wear a mask and avoid outdoor activities."
    else:
        message = f"Current AQI (US) of {aqius} is above 190. Please avoid all outdoor activities in the area. Stay indoors and keep the windows shut. Make sure to keep the air purifier running. Shower after being outside for a prolonged period."

    notification_title = f"AQI Alert for {city}, {aqius} AQI!"
    notification_message = message

    # Send a notification to the specified device
    os.system(f'curl --header "Access-Token: {pushbullet_api_key}" --header "Content-Type: application/json" --data-binary "{{\\"body\\":\\"{notification_message}\\",\\"title\\":\\"{notification_title}\\",\\"type\\":\\"note\\"}}" --request POST https://api.pushbullet.com/v2/pushes')

