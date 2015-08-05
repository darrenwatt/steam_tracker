import os
import requests
import time
import config

key = config.key
steamids = config.steamids
game = config.game
output_file = config.filename

def get_player_status():
    base_url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/'
    payload = {
        'key': key,
        'steamids': steamids
    }
    r = requests.get(base_url, payload)
    data = r.json()
    return data


def is_player_playing_game(data):
    try: gameextrainfo = data['response']['players'][0]['gameextrainfo']
    except KeyError:
        gameextrainfo = "None"
    if gameextrainfo == game:
        return 1
    else:
        return 0


def update_log(status):
    timestamp = time.strftime('%x %H:%M:%S')
    write_status = "{0}, {1}\n".format(timestamp, status)
    with open(os.path.normpath(output_file), "a") as f:
        f.write(write_status)

status = get_player_status()
exile = is_player_playing_game(status)
update_log(exile)