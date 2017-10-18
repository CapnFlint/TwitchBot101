import socket
import re

class ConnectionManager():

    def __init__(self, channel):
        self.HOST = "irc.chat.twitch.tv"
        self.PORT = 6667
        self.CHAN = "#" + channel
        self.NICK = "" # Your twitch name, all lowercase
        self.PASS = "" # From http://www.twitchapps.com/tmi/

        self.sock = None

    def connect(self):
        self.sock = socket.socket()
        self.sock.connect((self.HOST, self.PORT))

        # Send oauth token
        self.sock.send('PASS %s\r\n' % self.PASS)
        # Send twitch handle
        self.sock.send('NICK %s\r\n' % self.NICK)
        # Join the channel
        self.sock.send('JOIN %s\r\n' % self.CHAN)
        print "Connected!"

        # Send a hello world!
        self.sock.send('PRIVMSG %s :%s\r\n' % (self.CHAN, "Hello World!"))

        # Close Connection
        print "Closing Connection!"
        self.con.send('PART %s\r\n' % self.CHAN)

def main():
    conn = ConnectionManager("capn_flint")
    conn.connect()

if __name__ == "__main__":
    main()
