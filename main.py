from bs4 import BeautifulSoup;
import urllib2;
import json;

lunchUrl = "https://www.elondining.com/locations/clohan-hall"

print('Getting dinner menu....')

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

print('Done.')
