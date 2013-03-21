#!/usr/bin/env python

__all__ = ['celsiusToFahrenheit', 'temperature', 'temperatureCelsius']

def celsiusToFahrenheit(c):
    """ Convert Celsius temperature to Fahrenheit"""
    return c * 9/5 + 32

def _readTemperature():
    """Read the temperature from the sensor"""
    device_path = '/sys/bus/w1/devices/28-0000045f6925/w1_slave'
    f = open(device_path)
    lines = f.read().splitlines()
    f.close()

    temperatureData = lines[1].split(' ')[-1]
    return float(temperatureData[2:]) / 1000

def temperature():
    """Temperature as Fahrenheit"""
    tempInCelsius = celsiusToFahrenheit(_readTemperature())
    return '{0:.1f}F'.format(tempInCelsius)

def temperatureCelsius():
    """Temperature in celsius"""
    return celsiusToFahrenheit(_readTemperature())
