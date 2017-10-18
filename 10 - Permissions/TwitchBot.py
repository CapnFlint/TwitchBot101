import logging

import thread

from core.ConnectionManager import ConnectionManager
from core.MessageManager import MessageManager

class TwitchBot():

    def __init__(self, channel):
        logging.basicConfig(level=logging.DEBUG)

        self.connMgr = ConnectionManager("capn_flint")
        self.msgMgr = MessageManager(self)

    def run(self):
        #self.msgMgr.start()

        logging.info("Starting up!!!")
        self.connMgr.connect()


def main():
    bot = TwitchBot("capn_flint")
    bot.run()

if __name__ == "__main__":
    main()
