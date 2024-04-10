import requests
from decouple import config
from webscrape import getJgPathLink

# needs to restart terminal every time it is updated
api_key = config('RIOT_API_KEY')

# USER INFO
# CHANGE LATER
regionFull = 'europe'
regionShort = 'euw1'
summonerName = 'xolaanis%20daddy'
tag = '4353'

# code works (i do kn how now)
# summoner v1
def getPlayerId(regionF, summonerName, tag, api_key):
  playerURL = f"https://{regionF}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summonerName}/{tag}?api_key={api_key}"

  print(playerURL)

  response = requests.get(playerURL).json()

  print(response)

  return response['puuid']

# spectator V5
def getActiveGame(regionS, summonerID, api_key):
  # gameURL = f"https://{tag}.api.riotgames.com/lol/spectator/v5/active-games/by-summoner/{summonerID}?api_key={api_key}"

  gameURL = f'https://{regionS}.api.riotgames.com/lol/spectator/v5/active-games/by-summoner/{summonerID}?api_key={api_key}'

  return requests.get(gameURL).json()['participants']



# Get Jungler in live game
def getJgInGame():
  playerId = getPlayerId(regionFull, summonerName, tag, api_key)
  playersInLiveGame = getActiveGame(regionShort, playerId, api_key)

  junglerList = []

  # look for smite summoner
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
        jgChamList.append(champion.lower())

  print(jgChamList)

  return jgChamList

getJgPathLink(getJgInGame())