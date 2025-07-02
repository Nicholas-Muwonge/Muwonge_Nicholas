# Creating an API key for the project
# This is used to authenticate the user and allow them to access the API
import os
import pandas as pd
import requests

# Coordinates for Kampala, Uganda
lat = 0.347596
lon = 32.582520 

# Your API key
API_KEY = 'f0492ea08895bb2f9520ae51a06712f3'

# URL with the defined variables
url = f"http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=a0f0aa5d298957f90a2283b6838600d2"

# GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # save the data to a CSV file
    df = pd.DataFrame([data])
    df.to_csv('weather_data.csv', index=False)
    print("Data saved to weather_data.csv")
else:
    print(f"Error: {response.status_code}")
    print(response.text)    