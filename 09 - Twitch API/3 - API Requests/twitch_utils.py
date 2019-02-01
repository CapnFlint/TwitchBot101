import logging
import urllib2
import urllib
import json

from config import config

def get_ids(names):
    url = "https://api.twitch.tv/kraken/users?login=" + ','.join(names)

    try:
        req = urllib2.Request(url)
        req.add_header('Accept', 'application/vnd.twitchtv.v5+json')
        req.add_header('Client-ID', config['api']['client_id'])

        response = urllib2.urlopen(req)

        data = json.load(response)

        if 'error' in data.keys():
            logging.warning("Users not found!")
            return {}

        results = {}

        for user in data['users']:
            results[user['name']] = user['_id']

        return results
    except urllib2.URLError:
        logging.error("get_ids: urllib2 error")
        return {}

def get_viewers(include_mods = True):
    url = "http://tmi.twitch.tv/group/user/{0}/chatters?client_id={1}"\
                .format(config['twitch']['channel'], config['api']['client_id'])
    try:
        response = urllib2.urlopen(url)
        userlist = json.load(response)['chatters']
        users = userlist['viewers']
        if include_mods:
            users = (users + userlist['moderators'] +
                    userlist['global_mods'] +
                    userlist['admins'] +
                    userlist['staff'])
        return users
    except urllib2.URLError:
        logging.error("get_viewers: urllib2 error")
        return {}

#NOTE: if someone upgrades a sub, they will show in multiple lists
def get_subscribers(offset=0, subs=[]):
    url = "https://api.twitch.tv/kraken/channels/{0}/subscriptions?limit=100&direction=desc&offset={1}"\
            .format(config['twitch']['channel_id'], offset)

    print "Retrieving subs " + str(offset) + " to " + str(offset + 100)

    try:
        req = urllib2.Request(url)
        req.add_header('Accept', 'application/vnd.twitchtv.v5+json')
        req.add_header('Client-ID', config['api']['client_id'])
        req.add_header('Authorization', 'OAuth ' + config['api']['access_token'])

        response = urllib2.urlopen(req)

        data = json.load(response)
        subs = subs + data['subscriptions']
        print subs
        total = int(data['_total'])

        if len(subs) < total:
            subs = get_subscribers(offset=offset + 100, subs=subs)

        return subs

    except urllib2.URLError as e:
        logging.error("get_subscribers: urllib2 error")
        return []



print get_ids(["capn_flint"])
print get_viewers()
print get_subscribers()
