import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
import urllib.request


driver = webdriver.Chrome("/Users/kennethcostichiii/chromeDriver/chromedriver")

_URL = 'https://www.cushmanwakefield.com/en/united-states/people/search#first=276&sort=relevancy&f:City=[Washington,Washington%2C%20D.C.,Arlington]'

driver.get(_URL)
content = driver.page_source

# functional
r = requests.get(_URL)
soup = bs(content)
urls = []
names = []
aArray = []
num = 1

for x in range(5):
    print(5-x)
    time.sleep(1)


for pdiv in soup.findAll('div', attrs={'class':'card mix_person'}):
    #print(num)
    num = num + 1
    for i, link in enumerate(pdiv.find_all('a')):
        #print('another:')
        #print(link)
        thisHref = link.get('href')
        _FULLURL = 'https://www.cushmanwakefield.com' + thisHref
        #print(_FULLURL)
        if thisHref.startswith('/api/GetVCard'):
            print("HEREHEREHEREHEREHEREHERE")
            urls.append(_FULLURL)
            names.append(soup.select('a')[i].attrs['href'])

names_urls = zip(names, urls)

for name, url in names_urls:
    print(url)
    newURL = url.replace(' ', '%20')
    txt = open("/Users/kennethcostichiii/Desktop/VSC-Directory/web-scraping/real estate - bosurban/vcardDownloadLinks.txt", "a")
    txt.write(newURL)
    txt.write('\n')
    txt.close()