import requests
from bs4 import BeautifulSoup

url = "http://www.netmeds.com/medicine/manufacturers/"
sourcecode = requests.get(url)
text = sourcecode.text
soup = BeautifulSoup(text,"html.parser")

for link in soup.findAll('div', {"class":"drug-list-col"}):
    print(link.text)
    for item in link.findAll('a'):
        print(item.get('href'))