import requests

class WorkWithWeather:
    def answer(city, token):
        weatherInfo = {}
        res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&units=metric&appid={token}")
        data = res.json()

        try:
            weatherInfo['temp'] = data['main']['temp']
            weatherInfo['description'] = data['weather'][0]['description']
            weatherInfo['humidity'] = data["main"]["humidity"]
            weatherInfo['pressure'] = data["main"]["pressure"]
            weatherInfo['speed'] = data["wind"]["speed"]
        except:
            return 'Incorrect city'

        return weatherInfo