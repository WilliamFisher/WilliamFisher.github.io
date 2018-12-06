from bs4 import BeautifulSoup;
import urllib2;
import json;

lunchUrl = "https://www.elondining.com/locations/clohan-hall/?date=2018-12-06"
dinnerUrl = ""

content = urllib2.urlopen(lunchUrl).read()

soup = BeautifulSoup(content)

lunch = soup.find(id="menu-station-data-a1d0c6e83f027327d8461063f4ac58a6-2dace78f80bc92e6d7493423d729448e")

list = lunch.find_all('a')

items = {}

for idx, child in enumerate(list):
    items[idx] = (child.string+".")

print (json.dumps(items))

with open('lunch.json', 'w') as outfile:
    json.dump(items, outfile)

items.clear()

dinner = soup.find(id="menu-station-data-a1d0c6e83f027327d8461063f4ac58a6-0f49c89d1e7298bb9930789c8ed59d48")

list = dinner.find_all('a')

for idx, child in enumerate(list):
    items[idx] = (child.string+".")

print(json.dumps(items))

with open('dinner.json', 'w') as outfile:
    json.dump(items, outfile)
