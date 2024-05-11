import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city, api_key, units='metric'):
    """
    Get weather data for a given city using the OpenWeatherMap API.

    Args:
    - city (str): Name of the city.
    - api_key (str): API key for accessing the OpenWeatherMap API.
    - units (str): Units for temperature measurement (default: 'metric').

    Returns:
    - dict: Weather data for the specified city.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather():
    """
    Display weather information for the specified city using the provided API key and units.
    """
    city = city_entry.get()
    api_key = api_key_entry.get()
    units = units_var.get()

    weather_data = get_weather(city, api_key, units)
    if weather_data['cod'] == 200:
        weather_info = (
            f"Weather in {weather_data['name']}:\n"
            f"Temperature: {weather_data['main']['temp']}°C\n"
            f"Humidity: {weather_data['main']['humidity']}%\n"
            f"Wind Speed: {weather_data['wind']['speed']} m/s\n"
            f"Weather Condition: {weather_data['weather'][0]['description']}"
        )
        messagebox.showinfo("Weather Information", weather_info)
    else:
        messagebox.showerror("Error", f"Error: {weather_data['message']}")

# Create main window
root = tk.Tk()
root.title("Weather App")

# Create and arrange widgets (code omitted for brevity)

# Run the application
root.mainloop()

# Developed by [Rishi R](https://github.com/RishiR123)
