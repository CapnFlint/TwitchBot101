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
        self.running = False

    def _connect(self):
        self.sock = socket.socket()
        self.sock.connect((self.HOST, self.PORT))
        # Send oauth token
        self.sock.send('PASS %s\r\n' % self.PASS)
        # Send twitch handle
        self.sock.send('NICK %s\r\n' % self.NICK)
        # Join the channel
        self.sock.send('JOIN %s\r\n' % self.CHAN)

        print "Connected!"

    def _request_capabilities(self):
        # Request capabilities
        self.sock.send('CAP REQ :twitch.tv/membership\r\n')
        self.sock.send('CAP REQ :twitch.tv/tags\r\n')
        self.sock.send('CAP REQ :twitch.tv/commands\r\n')

    def _send_message(self, msg):
        self.sock.send('PRIVMSG %s :%s\r\n' % (self.CHAN, msg))

    def connect(self):
        self._connect()
        self._request_capabilities()

        # Send a hello world!
        self._send_message("Hello World!")

        data = ""

        try:
            while True:
                try:
                    data = data + self.sock.recv(1024)
                    data_lines = re.split("[\r\n]+", data)
                    data = data_lines.pop()

                    for line in data_lines:
                        line = line.split()

                        if len(line) >= 1:
                            # Display the message received
                            print " ".join(["MSG:"] + line)

                except socket.error:
                    print "ERROR: Socket died"
                    break

                except socket.timeout:
                    print "ERROR: Socket timeout"
                    break

        except Exception as e:
            print "Unhandled Error: " + str(e)

        print "Closing Connection!"
        self.con.send('PART %s\r\n' % self.CHAN)

def main():
    conn = ConnectionManager("capn_flint")
    conn.connect()

if __name__ == "__main__":
    main()
