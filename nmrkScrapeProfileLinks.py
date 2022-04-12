import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
import urllib.request


driver = webdriver.Chrome("/Users/kennethcostichiii/chromeDriver/chromedriver")

_URL = 'https://www.nmrk.com/offices/washington-dc/people#tabBarContent'

driver.get(_URL)


for x in range(20):
    print(20-x)
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


for pdiv in soup.findAll('div', attrs={'class':'w-full md:w-1/2 lg:w-1/3 px-3 mb-2 md:mb-6 list-item visible'}):
    #print(num)
    num = num + 1
    for i, link in enumerate(pdiv.find_all('a')):
        #print('another:')
        #print(link)
        thisHref = link.get('href')
        #_FULLURL = 'https://www.cushmanwakefield.com' + thisHref
        #print(_FULLURL)
        if thisHref.startswith('https://www.nmrk.com/people/'):
            print("HEREHEREHEREHEREHEREHERE")
            #urls.append(_FULLURL)
            urls.append(thisHref)
            #names.append(soup.select('a')[i].attrs['href'])

#names_urls = zip(names, urls)

for url in urls:
    print(url)
    #newURL = url.replace(' ', '%20')
    txt = open("/Users/kennethcostichiii/Desktop/VSC-Directory/web-scraping/real estate - bosurban/nmrkPeopleLinks.txt", "a")
    txt.write(url)
    txt.write('\n')
    txt.close()