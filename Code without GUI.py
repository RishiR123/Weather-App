import requests

# Function to fetch weather data from OpenWeatherMap API
def get_weather(city, api_key, units='metric'):
    # Construct the URL for the API request
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"
    
    # Send the HTTP GET request and parse the JSON response
    response = requests.get(url)
    data = response.json()
    
    return data

# Function to display weather information to the user
def display_weather(data):
    # Check if the API request was successful
    if data['cod'] == 200:
        # Extract and display relevant weather data
        print(f"Weather in {data['name']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
        print(f"Weather Condition: {data['weather'][0]['description']}")
    else:
        # Print error message if API request was unsuccessful
        print(f"Error: {data['message']}")

if __name__ == "__main__":
    # Get user input for city name and preferred units
    city = input("Enter the city name: ")
    api_key = "27ed057118a76602b97e514338f0463a"  # Replace with your actual OpenWeatherMap API key
    units = input("Enter the preferred units (metric/imperial): ").lower()

    # Call the get_weather function to fetch weather data
    weather_data = get_weather(city, api_key, units)
    
    # Display the weather information to the user
    display_weather(weather_data)

# Developer credit
print("This weather application was developed by [Rishi R](https://github.com/RishiR123).")
