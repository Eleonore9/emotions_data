#Try to scrape using beautiful soup library

from bs4 import BeautifulSoup 
import requests
import sys

DEBUG = True

if DEBUG:
    print 1
page = requests.get('http://www.pinterest.com/eleonore9/photography/')
if page.status_code == 200:
    if DEBUG:
        print 2
    soup = BeautifulSoup(page.text)
    #for item in soup.find_all('a', attrs={"class": u"pinImageWrapper"}):
    sys.stdout = open('print.html', 'w')
    items = soup.find_all("a", class_="pinImageWrapper")
    print '* ', len(items)
    for item in items:
        if DEBUG:
            #sys.stdout = open('print.html', 'w')
            print item 
