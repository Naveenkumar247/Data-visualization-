import matplotlib.pyplot as plt

def show_weather_chart(data):
    labels = ['Temperature (°C)', 'Humidity (%)', 'Pressure (hPa)']
    values = [
        data['main']['temp'],
        data['main']['humidity'],
        data['main']['pressure']
    ]

    plt.figure(figsize=(6,4))
    plt.bar(labels, values, color=['skyblue', 'lightgreen', 'salmon'])
    plt.title(f"Weather Data for {data['name']}")
    plt.tight_layout()
    plt.show()
