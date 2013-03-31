#!/usr/bin/env python

from temperature_utils import TemperatureUtils

class TemperatureSensor:
    def __init__(self):
        self.device_path = '/sys/bus/w1/devices/28-0000045f6925/w1_slave'
        self._util = TemperatureUtils()
 
    def _readTemperature(self):
        f = open(self.device_path)
        lines = f.read().splitlines()
        f.close()

        temperatureData = lines[1].split(' ')[-1]
        return float(temperatureData[2:]) / 1000

    def getTemperature(self):
        """Temperature as Fahrenheit"""
        sensorCelsiusTemp = self._readTemperature()
        return '{0:.1f}'.format(self._util.celsiusToFahrenheit(sensorCelsiusTemp))

    def getTemperatureCelsius(self):
        """Temperature in Celsius"""
        return '{0:.1f}'.format(self._readTemperature())

if __name__ == "__main__":
    s = TemperatureSensor()
    print("Fahrenheit: " + s.getTemperature())
    print("Celsius: " + s.getTemperatureCelsius())
