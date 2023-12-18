import requests
import pywhatkit

pywhatkit.sendwhatmsg(+918354898812,"testing")
apikey = '162d6356ccd1d556cffa732d068d6fb4'

City = 'Varanasi'

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={City}&units=metric&APPID={apikey}")

weather = (weather_data.json()['weather'][0]['main'])
temp = round(weather_data.json()['main']['temp'])

print(weather,temp)