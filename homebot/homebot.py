from jabberbot import JabberBot, botcmd
import datetime
import subprocess
from temperature_sensor import TemperatureSensor

class SystemInfoJabberBot(JabberBot):

    # fun
    @botcmd
    def greeting(self, mess, args):
        """Greets you"""
        return 'sup'

    # system information
    @botcmd
    def serverinfo( self, mess, args):
        """Displays information about the server"""
        version = open('/proc/version').read().strip()
        loadavg = open('/proc/loadavg').read().strip()

        return '%s\n\n%s' % ( version, loadavg, )

    @botcmd
    def uptime(self, mess, args):
        """Get current uptime information"""
        return subprocess.check_output('uptime')

    @botcmd
    def time( self, mess, args):
        """Displays current server time"""
        return str(datetime.datetime.now())

    @botcmd
    def whoami(self, mess, args):
        """Tells you your username"""
        return mess.getFrom().getStripped()

    # sensor information
    @botcmd
    def temperature(self, mess, args):
        """Get the temperature of the room where the Raspberry Pi is located in fahrenheit"""
        sensor = TemperatureSensor()
        return sensor.getTemperature()

    @botcmd
    def temperaturecelsius(self, mess, args):
        """Get the temperature of the room where the Raspberry Pi is located in celsius"""
        sensor = TemperatureSensor()
        return sensor.getTemperatureCelsius()

username = 'threefourfivepoplar@gmail.com'
password = '###'
bot = SystemInfoJabberBot(username,password)
bot.serve_forever()
