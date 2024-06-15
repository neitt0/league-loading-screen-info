from bs4 import BeautifulSoup
import requests

def getJgPathLink(arr):
  container = {}

  for champion in arr:
    jgDict = {}

    jgPathUrl = f"https://jungler.gg/champions/{champion}/"
    print(jgPathUrl)

    req = requests.get(jgPathUrl)
    soup = BeautifulSoup(req.text, 'html.parser')
    images = soup.find_all('img')

    # loop through {images} and assign {i} as key and link as value
    i = 0
    for image in images:
      if image['src'][-4] == 'w':
        # append to jgDict
        jgDict[ f"link #{i}" ] = image['src']
        i+=1
    i = 0

    # append jgDict to main container
    container[champion] = jgDict
  
  print(container)
  return container