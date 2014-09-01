#Try to scrape using beautiful soup library

from bs4 import BeautifulSoup 
import requests

DEBUG = True

if DEBUG:
    print 1
page = requests.get('http://www.pinterest.com/eleonore9/photography/')
if page.status_code == 200:
    if DEBUG:
        print 2
    #print page.text[:100]
    soup = BeautifulSoup(page.text)
    links = soup.a
    if DEBUG:
        print links
