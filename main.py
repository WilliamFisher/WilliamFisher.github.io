from bs4 import BeautifulSoup;
import urllib2;
import json;

lunchUrl = "https://www.elondining.com/locations/clohan-hall"

print('Getting Clohan lunch and dinner items....')

content = urllib2.urlopen(lunchUrl).read()

soup = BeautifulSoup(content, 'html.parser')

section = soup.select(".c-tab")

dinnerNum = len(section)

dinner = section[dinnerNum - 1].find_all('a')

items = {}

for idx, child in enumerate(dinner):
    items[idx] = (child.string+'.')

with open('dinner.json', 'w') as outfile:
    json.dump(items, outfile)


items.clear()

lunch = section[dinnerNum - 2].find_all('a')

for idx, child in enumerate(lunch):
    items[idx] = (child.string+'.')

with open('lunch.json', 'w') as outfile:
    json.dump(items, outfile)

print('Done.')
