from jabberbot import JabberBot, botcmd
import datetime
import temperature

class SystemInfoJabberBot(JabberBot):
    @botcmd
    def serverinfo( self, mess, args):
        """Displays information about the server"""
        version = open('/proc/version').read().strip()
        loadavg = open('/proc/loadavg').read().strip()

        return '%s\n\n%s' % ( version, loadavg, )
    
    @botcmd
    def time( self, mess, args):
        """Displays current server time"""
        return str(datetime.datetime.now())

    @botcmd
    def rot13( self, mess, args):
        """Returns passed arguments rot13'ed"""
        return args.encode('rot13')

    @botcmd
    def whoami(self, mess, args):
        """Tells you your username"""
        return mess.getFrom().getStripped()

    @botcmd
    def temperature(self, mess, args):
        """Get the temperature of the room where the Raspberry Pi is located"""
        return temperature.temperature()

username = 'threefourfivepoplar@gmail.com'
password = '###'
bot = SystemInfoJabberBot(username,password)
bot.serve_forever()
