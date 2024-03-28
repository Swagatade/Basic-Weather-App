import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        print(f"Weather in {location}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print("Error fetching weather data. Please check the location and try again.")

def main():
    api_key = "2c0f0bfedeee3835f6ba9c4d98a1c9ae"  # Replace with your OpenWeatherMap API key
    location = input("Enter a city name or ZIP code: ")
    get_weather(api_key, location)

if __name__ == "__main__":
    main()
