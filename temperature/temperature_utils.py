#!/usr/bin/env python

class TemperatureUtils:
    def celsiusToFahrenheit(self, c):
        """ Convert Celsius temperature to Fahrenheit"""
        return c * 9/5 + 32

    def fahrenheitToCelsius(self, f):
        """ Convert Fahrenheit temperature to Celsius """
        return (f - 32) * 5/9

if __name__ == "__main__":
    u = TemperatureUtils()
    print(u.fahrenheitToCelsius(72)) 
