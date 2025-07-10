from weather_api import get_weather
from visualizer import show_weather_chart

def main():
    print("=== Weather Dashboard ===")
    city = input("Enter city name: ").strip()

    weather_data = get_weather(city)

    if weather_data:
        print(f"\nCity: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Pressure: {weather_data['main']['pressure']} hPa")

        show_weather_chart(weather_data)
    else:
        print("Could not retrieve weather data.")

if __name__ == "__main__":
    main()
