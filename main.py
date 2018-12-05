from bs4 import BeautifulSoup;
import urllib2;
import json;
import io;

url = "https://www.elondining.com/locations/clohan-hall/?date=2018-12-05"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content)

content = soup.find(id="menu-station-data-a1d0c6e83f027327d8461063f4ac58a6-d395771085aab05244a4fb8fd91bf4ee")

list = content.find_all('a')

items = []

for child in list:
    items.append(child.string)

print (json.dumps(items))

with open('data.json', 'w') as outfile:
    json.dump(items, outfile)

