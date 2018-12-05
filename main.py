from bs4 import BeautifulSoup;
import urllib2;
import json;

lunchUrl = "https://www.elondining.com/locations/clohan-hall/?date=2018-12-05"
dinnerUrl = ""

content = urllib2.urlopen(lunchUrl).read()

soup = BeautifulSoup(content)

lunch = soup.find(id="menu-station-data-a1d0c6e83f027327d8461063f4ac58a6-d395771085aab05244a4fb8fd91bf4ee")

list = lunch.find_all('a')

items = {}

for idx, child in enumerate(list):
    items[idx] = (child.string+".")

print (json.dumps(items))

with open('lunch.json', 'w') as outfile:
    json.dump(items, outfile)

items.clear()

dinner = soup.find(id="menu-station-data-a1d0c6e83f027327d8461063f4ac58a6-e3796ae838835da0b6f6ea37bcf8bcb7")
list = dinner.find_all('a')

for idx, child in enumerate(list):
    items[idx] = (child.string+".")

print(json.dumps(items))

with open('dinner.json', 'w') as outfile:
    json.dump(items, outfile)
