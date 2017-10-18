import logging

def command_test(self, msg):
    self._send_message("I am a BOT! :)")

def command_grog(self, msg):
    self.grog_count += 1
    self._send_emote(" hands {0} a mug of Grog! ({1} mugs served)".format(msg['sender'], self.grog_count))
