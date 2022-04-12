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
file = open('nmrkPeopleLinks.txt')
for line in file:
    print("Scraping: %3d/298" % (i))
    i+=1
    link = line.strip()
    driver.get(link)
    content = driver.page_source
    soup = BeautifulSoup(content)

    emailComponent = soup.find("a", href=re.compile(r"^mailto:"))
    if (emailComponent is not None):
        nameBefore = soup.find('h1', attrs={'class':'text-4xl lg:text-5xl font-serif text-blue-brand leading-tight-plus mb-4 md:mb-8 mt-8 md:mt-18'}).text
        name = nameBefore.strip()

        spaceIndex = name.index(' ')
        firstName = name[:spaceIndex]
        lastName = name[spaceIndex+1:]
        firstNames.append(firstName)
        lastNames.append(lastName)

        emailBefore = soup.find("a", href=re.compile(r"^mailto:")).text
        email = emailBefore.strip()[4:]
        emails.append(email)

        titleBefore = soup.find("p", attrs={'class':'mb-2'}).text
        title = titleBefore.strip()
        titles.append(title)
    else:
        print("SKIPPED ^")

    


df = pd.DataFrame({'First Name':firstNames,'Last Name':lastNames,'Email':emails,'Title':titles}) 
df.to_csv('nmrkDC.csv', index=False, encoding='utf-8')