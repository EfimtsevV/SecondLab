import requests

city = "Moscow,RU"
app_id = "1b5f72cfce60f86fc11e3451069bf33b"
data= {
   	"q": city,
	"units": "metric",
	"lang": "ru",
	"APPID": app_id
}

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
             params=data).json()

wind_speed = res["wind"]["speed"] # getting wind speed from req_weather (-> json) in mps
visibility = res["visibility"] # getting visibility from req_weather (-> json) in grade from 0 to 10000

print("_______Сегодня_______")
print("Город:", city)
print("Скорость ветра:",wind_speed)
print("Видимость:", visibility) 

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': app_id}).json()
print("_______Неделя_______")
for  i in res["list"]:
	print("Дата:", i['dt_txt'] )
	print("Скорость ветра:", {i['wind']['speed']})
	print("Видимость: ", {i['visibility']})
	print("______________________________")