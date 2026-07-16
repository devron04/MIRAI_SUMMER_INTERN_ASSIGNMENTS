import requests 
import json

response = requests.get('https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0')
for data in response.json()['dataseries']:
    print(data)
