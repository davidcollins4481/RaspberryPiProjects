#!/usr/bin/env python

import pywapi
from temperature_logger import TemperatureLogger
from temperature_sensor import TemperatureSensor

# get area temperature
sensor = TemperatureSensor()
tempF = sensor.getTemperature()

# get outside temperature
noaaData = pywapi.get_weather_from_noaa('KCAK')
airportTempF = noaaData['temp_f']

# log temperature
logger = TemperatureLogger('garage')
logger.log(tempF, airportTempF)

