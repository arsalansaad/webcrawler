import urllib
import urllib.request
from bs4 import BeautifulSoup

url="http://www.hindustantimes.com/editorials/"
page=urllib.request.urlopen(url)
soup=BeautifulSoup(page,"html.parser")

#for link in soup.findAll('a'):
    #print(link.get('href'))

for link in soup.findAll("div",{"class":"media-heading headingfour"}):
  print(link.text)



"""
 for link in soup.findAll("div",{"class":"media-heading headingfour"}):
    print(link.get('href'))
for link in soup.findAll('a'):
    print(link.get('href'))"""

"""
for link in soup.find('div',{"class":"ES2-100x4-text1 hover-icon"}):
    print(link.find('span',{"class":"ES2-100x4-text1-content"}))"""


"""print(soup.title.text)
for link in soup.findAll('a'):
    print(link.get('href'))"""



