import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    return response.json()

st.title("🌤️ Weather Info App")

city = st.text_input("Enter city name", "Mumbai")

if st.button("Get Weather"):
    if city:
        data = get_weather(city)
        if data.get("cod") != 200:
            st.error(f"Error: {data.get('message')}")
        else:
            st.success(f"Weather in {city}")
            st.write(f"🌡️ Temperature: {data['main']['temp']} °C")
            st.write(f"💨 Wind Speed: {data['wind']['speed']} m/s")
            st.write(f"☁️ Condition: {data['weather'][0]['description'].title()}")
    else:
        st.warning("Please enter a valid city name.")
