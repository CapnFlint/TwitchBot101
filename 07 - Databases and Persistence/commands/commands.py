import logging
import sqlite3 as db

def command_test(self, msg):
    self._send_message("I am a BOT! :)")

def command_grog(self, msg):
    conn = db.connect(self.db_file)
    c = conn.cursor()
    c.execute('SELECT value FROM persistent_data WHERE name="grog_count"')
    value = c.fetchone()
    if value:
        value = value[0] + 1
        self._send_emote(" hands {0} a mug of Grog! ({1} mugs served)".format(msg['sender'], value))
        c.execute("UPDATE persistent_data SET value=? WHERE name='grog_count'", (value,))
    else:
        print "Database Error :("
    conn.commit()
    conn.close()
