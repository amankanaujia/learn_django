import requests
from pprint import pprint

API = 'cb771e45ac79a4e8e2205c0ce66ff633'
city = input("Enter a city : ")
base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API+"&q="+ city
weather_data = requests.get(base_url).json()
print(weather_data)