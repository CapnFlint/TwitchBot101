import logging
import socket
import re

from config import config
from commands import commands

class ConnectionManager():

    def __init__(self, channel):
        self.CHAN = "#" + channel

        self.sock = None
        self.running = False

        self.db_file = "botDB.sqlite"

#---[ Public Functions ]-----

    def send_message(self, msg):
        self._send_message(msg)

#---[ Private Functions]-----

    def _connect(self):
        self.sock = socket.socket()
        self.sock.connect((config['irc']['HOST'], config['irc']['PORT']))
        self.sock.send('PASS %s\r\n' % config['irc']['PASS'])
        self.sock.send('NICK %s\r\n' % config['irc']['NICK'])
        self.sock.send('JOIN %s\r\n' % self.CHAN)

        logging.info("Connected!")

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

        self.running = True

        try:
            while self.running:
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
                                logging.debug("PING Received!")
                                self._send_pong(line[1])

                            elif line[2] == 'PRIVMSG':
                                msg = self._parse_message(line)
                                # Display the message received
                                print "{0}: {1}".format(msg['sender'], msg['text'])

                                if msg['text'].lower().startswith("!test"):
                                    commands.command_test(self, msg)

                                if msg['text'].lower().startswith("!grog"):
                                    commands.command_grog(self, msg)

                            elif line[1] == 'JOIN':
                                pass

                            elif line[1] == 'PART':
                                pass

                            elif line[1] == 'MODE':
                                pass

                            else:
                                print " ".join(["MSG:"] + line)

                except socket.error:
                    logging.error("ERROR: Socket died")
                    break

                except socket.timeout:
                    logging.error("ERROR: Socket timeout")
                    break

                except KeyboardInterrupt:
                    logging.debug("Ctrl-C Detected!")
                    break

        except Exception as e:
            logging.error("Unhandled Error: " + str(e))

        logging.info("Closing Connection!")
        self.sock.send('PART %s\r\n' % self.CHAN)
