import glob
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re

firstNames=[] #List to store first names
lastNames=[] #List to store last names
emails=[] #List to store emails
titles=[] #List to store Job Titles

driver = webdriver.Chrome("/Users/kennethcostichiii/chromeDriver/chromedriver")
i=1
file = open('hunnPeopleLinks.txt')
for line in file:
    print("Scraping: %2d/50" % (i))
    i+=1
    link = line.strip()
    driver.get(link)
    content = driver.page_source
    soup = BeautifulSoup(content)

    #if link.startswith('')

    emailComponent = soup.find("a", href=re.compile(r"mailto:"))
    if (emailComponent is not None):
        nameBefore = soup.find('h1', attrs={'class':'body-title agent-show-name'}).text
        name = nameBefore.strip()

        spaceIndex = name.index(' ')
        firstName = name[:spaceIndex]
        lastName = name[spaceIndex+1:]
        firstNames.append(firstName)
        lastNames.append(lastName)

        emailBefore = soup.find_all("a", href=re.compile(r"mailto:"))[1].get('href')
        email = emailBefore.strip()[7:]
        emails.append(email)

        titleBefore = soup.find("div", attrs={'class':'big-text body-semi-title'}).text
        title = titleBefore.strip()
        titles.append(title)
    else:
        print("SKIPPED ^")

    


df = pd.DataFrame({'First Name':firstNames,'Last Name':lastNames,'Email':emails,'Title':titles}) 
df.to_csv('hunneman.csv', index=False, encoding='utf-8')