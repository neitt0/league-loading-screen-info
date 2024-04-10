from bs4 import BeautifulSoup
import requests

def getJgPathLink(arr):
  dict = {}

  for champion in arr:
    jgDict = {}

    jgPathUrl = f"https://jungler.gg/champions/{champion}/"
    print(jgPathUrl)

    req = requests.get(jgPathUrl)
    soup = BeautifulSoup(req.text, 'html.parser')
    images = soup.find_all('img')

    i = 0
    for image in images:
      if image['src'][-4] == 'w':

        jgDict[ f'{i}' ] = image['src']
        i+=1
    i = 0

    dict[champion] = jgDict
  
  print(dict)
  return dict