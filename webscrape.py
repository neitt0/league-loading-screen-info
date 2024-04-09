from bs4 import BeautifulSoup
import requests

def getJgPathLink(arr):
  for champion in arr:
    jgPathUrl = f"https://jungler.gg/champions/{champion}/"
    print(jgPathUrl)
    r = requests.get(jgPathUrl)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')

    for image in images:
      if image['src'][-4] == 'w':
        print(champion)
        print(image['src'])

def sayHI(str):
  print(str)