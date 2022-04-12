import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
import urllib.request


driver = webdriver.Chrome("/Users/kennethcostichiii/chromeDriver/chromedriver")

_URL = 'https://www.hunnemanre.com/teams'

driver.get(_URL)


for x in range(10):
    print(10-x)
    time.sleep(1)

#driver.find_element_by_class_name('relative text-lg font-bold view-more-link').click()

content = driver.page_source
# functional
r = requests.get(_URL)
soup = bs(content)
urls = []
#names = []
aArray = []
num = 1




for link in soup.find_all('a'):
    #print('another:')
    #print(link)
    thisHref = link.get('href')
    _FULLURL = 'https://www.hunnemanre.com' + thisHref
    #print(_FULLURL)
    if thisHref.startswith('/employees/') or thisHref.startswith('/agents/'):
        print("HEREHEREHEREHEREHEREHERE")
        urls.append(_FULLURL)
        #urls.append(thisHref)
        #names.append(soup.select('a')[i].attrs['href'])

#names_urls = zip(names, urls)

for url in urls:
    print(url)
    #newURL = url.replace(' ', '%20')
    txt = open("/Users/kennethcostichiii/Desktop/VSC-Directory/web-scraping/real estate - bosurban/hunnPeopleLinks.txt", "a")
    txt.write(url)
    txt.write('\n')
    txt.close()