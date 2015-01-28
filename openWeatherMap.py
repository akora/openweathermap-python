#!/usr/bin/python

# OpenWeatherMap service provides open weather data for more than 200,000
# cities and any geo location that is available on our website and through API.

import sys
import math
import requests

base_url = 'http://api.openweathermap.org/data/2.5/weather'
api_key = ''  # << Get your API key (APPID) here: http://openweathermap.org/appid
cities = ['Esztergom', 'London, UK']


def get_temperature(city):
  query = base_url + '?q=%s&units=metric&APPID=%s' % (city, api_key)
  try:
    response = requests.get(query)
    # print("[%s] %s" % (response.status_code, response.url))
    if response.status_code != 200:
      response = 'N/A'
      return response
    else:
      weather_data = response.json()
      return weather_data
  except requests.exceptions.RequestException as error:
    print error
    sys.exit(1)


def main():
  for city in cities:
    location = get_temperature(city)
    print location['name'] + ' ' + str(math.ceil(location['main']['temp'])) + ' C (' + str(location['main']['temp']) + ')'

if __name__ == '__main__':
  main()

# TODO: fix TypeError: string indices must be integers, not str if base_url is incorrect
