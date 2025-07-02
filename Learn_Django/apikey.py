import os
import pandas as pd
import requests

# Coordinates for Kampala, Uganda
lat = 0.347596
lon = 32.582520 

API_KEY = 'f0492ea08895bb2f9520ae51a06712f3'

url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    df = pd.DataFrame([data])
    df.to_csv('weather_data.csv', index=False)
    print("Data saved to weather_data.csv")
else:
    print(f"Error: {response.status_code}")
    print(response.text)    