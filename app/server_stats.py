import a2s
import requests
import json
import os
import socket

# https://python-valve.readthedocs.io/en/latest/source.html    

def get_server_status(SERVER_ADDRESS):
    url = f"http://api.steampowered.com/ISteamApps/GetServersAtAddress/v0001?addr={SERVER_ADDRESS[0]}:{SERVER_ADDRESS[1]}&format=json"
    response = requests.get(url)
    data = response.json()['response']
    json.dumps(data, indent=2)

    success = data['success']
    servers = data['servers']

    if success is False:
        return 0

    if len(servers) >= 1:
        for server in servers:
            if server['gamedir'] == 'valheim':
                return 1
        
    return 0


def get_players(SERVER_ADDRESS):
    try:
        info = a2s.info(SERVER_ADDRESS)
        return info.player_count

    except:
        return 0
        