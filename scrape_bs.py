#Try to scrape using beautiful soup

from bs4 import BeautifulSoup 
import requests

print 1
page = requests.get('http://www.pinterest.com/eleonore9/photography/')
if page.status_code == 200:
    print 2
    #print page.text[:100]
    soup = BeautifulSoup(page.text)
    print type(soup.a)
