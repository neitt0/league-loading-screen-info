import requests
from decouple import config
import os
from webscrape import getJgPathLink

api_key = config('RIOT_API_KEY')

# USER INFO
# CHANGE LATER
region = 'na1'
summonerName = 'Arcsecond'

# code works (i do kn how now)
# summoner V4
def getPlayerId(region, summonerName, api_key):
  playerURL = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?api_key={api_key}"
  response = requests.get(playerURL).json()

  print(response['puuid'])

  return response['puuid']

# spectator V5
def getActiveGame(region, summonerID, api_key):
  gameURL = f"https://{region}.api.riotgames.com/lol/spectator/v5/active-games/by-summoner/{summonerID}?api_key={api_key}"
  return requests.get(gameURL).json()['participants']



# Get Jungler in live game
playersInLiveGame = getActiveGame(region, getPlayerId(region, summonerName, api_key), api_key)

junglerList = []

for player in playersInLiveGame:
  if player['spell1Id'] == 11 or player['spell2Id'] == 11:
    junglerList.append(player)

# print(junglerList)


# Get Champion from jungler
championsDDragon = requests.get('https://ddragon.leagueoflegends.com/cdn/14.5.1/data/en_US/champion.json').json()['data']

jgChamList = []

for jungler in junglerList:
  championKey = jungler['championId']
  for champion in championsDDragon:
    if championKey == int(championsDDragon[champion]['key']):
      jgChamList.append(champion)

print(jgChamList)

getJgPathLink(jgChamList)