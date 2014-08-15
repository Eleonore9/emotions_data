# Simple HTML scraping from 
# http://docs.python-guide.org/en/latest/scenarios/scrape/
from lxml import html
import requests

page = requests.get('http://www.pinterest.com/eleonore9/photography/')
tree = html.fromstring(page.text) 
# The 'tree' variable contains the whole HTML for the page

# Use XPath to locate the info needed
pins = tree.xpath('//a[@class="pinImageWrapper"]/attribute::href')
urls = tree.xpath('//img[@class="pinImg"]/attribute::src')

count = 0
for p in pins:
    pin = 'http://www.pinterest.com' + p
    count += 1
    print 'PIN: ', pin
print count

index = 0
for u in urls:
    index += 1
    print 'URL: ', u
print index
