import requests
from bs4 import BeautifulSoup
import time
import datetime


url = "http://www.hindustantimes.com/editorials/merkel-wants-to-look-beyond-the-united-states-modi-can-help/story-wjxLJNFchALl1NOkEDrnVL.html"
sourcecode = requests.get(url)
text = sourcecode.text
soup = BeautifulSoup(text, "html.parser")

for link in soup.findAll('div', {"class":"story-details"}):
  print(link.text)