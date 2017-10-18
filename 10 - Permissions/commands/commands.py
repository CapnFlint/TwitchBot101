import logging
import sqlite3 as db

import utils.twitch_utils as twitch

commands = {}

def _check_permission(self, perm, tags):
    if int(tags[perm]):
        return True
    else:
        return False

def command_test(self, msg):
    # only mods
    print msg['tags']
    if _check_permission(self, 'mod', msg['tags']):
        self.send_message("I am a BOT! :)")
    else:
        self.send_message("No permission!")

commands['test'] = command_test

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

commands['grog'] = command_grog
