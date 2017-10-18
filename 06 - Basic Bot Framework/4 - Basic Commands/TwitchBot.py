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

        self.grog_count = 0

    def _connect(self):
        self.sock = socket.socket()
        self.sock.connect((self.HOST, self.PORT))
        self.sock.send('PASS %s\r\n' % self.PASS)
        self.sock.send('NICK %s\r\n' % self.NICK)
        self.sock.send('JOIN %s\r\n' % self.CHAN)

        print "Connected!"

    def _request_capabilities(self):
        # Request capabilities
        self.sock.send('CAP REQ :twitch.tv/membership\r\n')
        self.sock.send('CAP REQ :twitch.tv/tags\r\n')
        self.sock.send('CAP REQ :twitch.tv/commands\r\n')

    def _send_message(self, msg):
        self.sock.send('PRIVMSG %s :%s\r\n' % (self.CHAN, msg))

    def _send_emote(self, msg):
        emote = '\001ACTION ' + msg + '\001'
        self._send_message(emote)

    def _send_pong(self, nonce):
        self.sock.send('PONG %s\r\n' % msg)

    def _get_tags(self, data):
        data = data.split(';')
        tagmap = {}
        for d in data:
            (key, val) = d.split('=')
            tagmap[key] = val;
        return tagmap

    def _parse_message(self, message):
        msg = {}

        msg["sender"] = re.match(':(.*)!', message[1]).group(1).encode('utf-8')
        msg["text"] = " ".join(message[4:]).lstrip(":")
        msg["channel"] = message[3]
        msg["tags"] = self._get_tags(message[0])

        return msg


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
                        # :capn_flint!capn_flint@capn_flint.tmi.twitch.tv PRIVMSG #capn_flint :test
                        line = line.split()

                        # [':capn_flint!capn_flint@capn_flint.tmi.twitch.tv', 'PRIVMSG', '#capn_flint', ':test']
                        if len(line) >= 1:
                            if line[0] == 'PING':
                                print "PING!"
                                self._send_pong(line[1])

                            elif line[2] == 'PRIVMSG':
                                msg = self._parse_message(line)
                                # Display the message received
                                print "{0}: {1}".format(msg['sender'], msg['text'])

                                if msg['text'].lower().startswith("!test"):
                                    self._send_message("I am a BOT! :)")

                                if msg['text'].lower().startswith("!grog"):
                                    self.grog_count += 1
                                    self._send_emote(" hands {0} a mug of Grog! ({1} mugs served)".format(msg['sender'], self.grog_count))

                            elif line[1] == 'JOIN':
                                pass

                            elif line[1] == 'PART':
                                pass

                            elif line[1] == 'MODE':
                                pass

                            else:
                                print " ".join(["MSG:"] + line)

                except socket.error:
                    print "ERROR: Socket died"
                    break

                except socket.timeout:
                    print "ERROR: Socket timeout"
                    break

                except KeyboardInterrupt:
                    print "Ctrl-C Detected!"
                    break

        except Exception as e:
            print "Unhandled Error: " + str(e)

        print "Closing Connection!"
        self.sock.send('PART %s\r\n' % self.CHAN)

def main():
    conn = ConnectionManager("capn_flint")
    conn.connect()

if __name__ == "__main__":
    main()
