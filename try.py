import requests
import pywhatkit
import time

apikey = '162d6356ccd1d556cffa732d068d6fb4'

City = 'Varanasi'

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={City}&units=metric&APPID={apikey}")

weather = (weather_data.json()['weather'][0]['main'])
temp = round(weather_data.json()['main']['temp'])

print(weather,temp)



if temp < 20:
    temp = str(temp)
    text = temp+"°C"+"--> Low temperature! Get a sweater..."
    
elif temp > 30:
    temp = str(temp)
    text = temp+"°C" +"--> High Temperature! Don't get affected by the https://open.spotify.com/track/3USxtqRwSYz57Ewm6wWRMp?si=c449d08d97ab490a"
    
else:
    temp = str(temp)
    text = temp+"°C" +"--> Just the right temperature, Enjoy!"
    
def check_n_send():
    
    if weather == 'Clear':
        pywhatkit.sendwhats_image ('+910123456789','images\\clear.png',text,15,True,3)
        time.sleep(2)
        pywhatkit.sendwhats_image ('+910123456789','images\\❤️.png','',15,True,3)
        
    elif (weather == "Clouds"):
        pywhatkit.sendwhats_image ('+910123456789','images\\cloudy.png',text,15,True,3)
        time.sleep(2)
        pywhatkit.sendwhats_image ('+910123456789','images\\❤️.png','',15,True,3)
         
    elif(weather == "Rain"):
        pywhatkit.sendwhats_image ('+910123456789','images\\rainy.png',text,15,True,3)
        time.sleep(2)
        pywhatkit.sendwhats_image ('+910123456789','images\\❤️.png','',15,True,3)
        
    elif(weather == "Snow"):
        pywhatkit.sendwhats_image ('+910123456789','images\\snowy.png',text,15,True,3)
        time.sleep(2)
        pywhatkit.sendwhats_image ('+910123456789','images\\❤️.png','',15,True,3)
        
    elif(weather == "Thunderstorm"):
        pywhatkit.sendwhats_image ('+910123456789','images\\thunderstorm.gif',text,15,True,3)
        time.sleep(2)
        pywhatkit.sendwhats_image ('+910123456789','images\\❤️.png','',15,True,3)
        
    elif(weather == "Drizzle"):
        pywhatkit.sendwhats_image ('+910123456789','images\\drizzle.png',text,15,True,3)
        time.sleep(2)
        pywhatkit.sendwhats_image ('+910123456789','images\\❤️.png','',15,True,3)
        
    elif(weather == "Mist"):
        pywhatkit.sendwhats_image ('+910123456789','images\\mist.png',text,15,True,3)
        time.sleep(2)
        pywhatkit.sendwhats_image ('+910123456789','images\\❤️.png','',15,True,3)
        
    elif(weather == "Haze"):
        pywhatkit.sendwhats_image ('+910123456789','images\\hazy.png',text,15,True,3)
        time.sleep(2)
        pywhatkit.sendwhats_image ('+910123456789','images\\❤️.png','',15,True,3)
        
    elif(weather == "Fog"):
        pywhatkit.sendwhats_image ('+910123456789','images\\fog.png',text,15,True,3)
        time.sleep(2)
        pywhatkit.sendwhats_image ('+910123456789','images\\❤️.png','',15,True,3)
        
    else:
        pywhatkit.sendwhats_image ('+910123456789','images\\unknown.png',text,15,True,3)
        time.sleep(2)
        pywhatkit.sendwhats_image ('+910123456789','images\\❤️.png','',15,True,3)
        
check_n_send()