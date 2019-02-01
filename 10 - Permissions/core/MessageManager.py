import logging

import threading
import time

class MessageManager(threading.Thread):

    def __init__(self, bot):
        threading.Thread.__init__(self)
        self.connMgr = bot.connMgr
        self.setDaemon(True)

        self.messages = [
            "Hello World!",
            "YARRR!",
            "I like Cheese"
        ]

        logging.info("MessageManager initialized...")

    def run(self):
        cooldown = 10
        while 1:
            time.sleep(cooldown)
            message = self.messages.pop(0)
            self.connMgr.send_message(message)
            self.messages.append(message)
