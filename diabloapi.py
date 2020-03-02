import requests


def request(url):
    response = requests.get(url)
    return response.json()


def get_token():
    url = 'https://eu.battle.net/oauth/token'
    client_id = None
    client_secret = None

    response = requests.post(url, data={'grant_type': 'client_credentials'}, auth=(client_id, client_secret))
    return '?access_token=' + response.json().get("access_token")


def season_leaderboard(token, season=19):
    url = "https://eu.api.blizzard.com/data/d3/season/{}{}".format(str(season), token)
    return url


def era_leaderboard(token, hero_class='barbarian', era=12):
    url = "https://eu.api.blizzard.com/data/d3/era/{}/leaderboard/rift-{}{}".format(str(era), hero_class, token)
    return url


def season_index(token):
    url = 'https://eu.api.blizzard.com/data/d3/season/{}'.format(token)
    return url


def era_index(token):
    url = 'https://us.api.blizzard.com/data/d3/era/{}'.format(token)
    return url


def get_battle_tag(battle_tag):
    index = battle_tag.find('#')
    battle_tag = battle_tag[0: index] + '-' + battle_tag[index + 1:]
    return battle_tag


def profile(token, battle_tag):
    battle_tag = get_battle_tag(battle_tag)
    url = 'https://eu.api.blizzard.com/d3/profile/{}/{}'.format(battle_tag, token)
    return url


def hero(token, battle_tag, hero_id):
    battle_tag = get_battle_tag(battle_tag)
    url = 'https://eu.api.blizzard.com/d3/profile/{}/hero/{}{}'.format(battle_tag, str(hero_id), token)
    return url


def get_act(token):
    url = 'https://eu.api.blizzard.com/d3/data/act{}'.format(token)
    return url
