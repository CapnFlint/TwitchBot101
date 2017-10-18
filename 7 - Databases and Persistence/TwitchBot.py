import logging

from core.ConnectionManager import ConnectionManager

class TwitchBot():

    def __init__(self, channel):
        logging.basicConfig(level=logging.DEBUG)

        self.connMgr = ConnectionManager("capn_flint")

    def run(self):
        logging.info("Starting up!!!")
        self.connMgr.connect()


def main():
    bot = TwitchBot("capn_flint")
    bot.run()

if __name__ == "__main__":
    main()
