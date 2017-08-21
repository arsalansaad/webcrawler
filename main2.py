import requests
from bs4 import BeautifulSoup


url = "http://www.hindustantimes.com/editorials/"
sourcecode = requests.get(url).text
soup = BeautifulSoup(sourcecode, "html.parser")


for link in soup.findAll("div",{ "class": "media-heading headingfour"}):
    print(link.text)
    for item in link.findAll('a'):
        print(item.get('href'))

# for link in soup.findAll("div",class_="media-heading headingfour"):
#   print(link.get('href'))