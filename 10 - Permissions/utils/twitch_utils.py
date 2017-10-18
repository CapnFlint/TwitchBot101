import logging
import urllib2
import urllib
import json

from config import config

#---[ API Connector ]----------

def call_api(path):
    try:
        req = urllib2.Request("https://api.twitch.tv/kraken" + path)
        req.add_header('Accept', 'application/vnd.twitchtv.v5+json')
        req.add_header('Client-ID', config['api']['client_id'])
        req.add_header('Authorization', 'OAuth ' + config['api']['access_token'])

        response = urllib2.urlopen(req)

        data = json.load(response)

        if 'error' in data.keys():
            logging.warning("API Error: Failed Request")
            return {}

        return data

    except urllib2.URLError:
        logging.error("API Error: urllib2")

#---[ API utils ]----------

def get_ids(names):
    path = "/users"
    params = "?login=" + ','.join(names)
    results = {}

    data = call_api(path + params)

    if data:
        for user in data['users']:
            results[user['name']] = user['_id']
    else:
        logging.warning("No ID's found")

    return results

def get_subscribers(offset=0, subs=[]):
    path = "/channels/{0}/subscriptions"\
                .format(config['twitch']['channel_id'])
    params = "?limit=100&direction=desc&offset={0}".format(offset)

    data = call_api(path + params)

    if data:
        for user in data['subscriptions']:
            subs.append(user['user']['name'])

        total = int(data['_total'])

        if len(subs) < total:
            subs = get_subscribers(offset=offset + 100, subs=subs)

    return subs

#---[ TMI functions ]----------

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
