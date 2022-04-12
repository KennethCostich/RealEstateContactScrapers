from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

driver = webdriver.Chrome("/Users/kennethcostichiii/chromeDriver/chromedriver")

firstNames=[] #List to store first names
lastNames=[] #List to store last names
emails=[] #List to store emails
titles=[] #List to store Job Titles
#driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq")

lastPageNumber = 8

#####################

link = 'https://www.us.jll.com/en/people?&locationFilter=District%20of%20Columbia'
driver.get(link)

for x in range(10):
    print(10-x)
    time.sleep(1)

content = driver.page_source
soup = BeautifulSoup(content)
#for pdiv in soup.findAll('div',href=True, attrs={'class':'profile'}):
for person in soup.findAll('li', attrs={'class':'search-results__people-list__item'}):
    name=person.find('h4', attrs={'class':'search-results__people-list__item__title'}).text.strip()
    title=person.find('h5', attrs={'class':'search-results__people-list__item__designation'}).text.strip()
    spaceIndex = name.index(' ')
    firstName = name[:spaceIndex]
    lastName = name[spaceIndex+1:]
    firstNames.append(firstName)
    lastNames.append(lastName)
    if (title is None):
        print("GOT HERE")
        titles.append('')
    else:
        titles.append(title)
#i = 1
for a in soup.find_all("a", href=re.compile(r"mailTo:")):

    emails.append(a.get('href')[7:])
    #if (i == 10):
    #    emails.append('')
    
    #i = i + 1



for i in range(2,lastPageNumber+1):
    newlink = 'https://www.us.jll.com/en/people?locationFilter=New+York&page={}'.format(i)
    print(newlink)
    #driver.get(newlink)
    #driver.find_element_by_class_name("pagination-button prev jll-icon-arrow-right ").click()
    driver.find_elements_by_tag_name('button')[11].click()

    for x in range(3):
        print(3-x)
        time.sleep(1)

    content = driver.page_source
    soup = BeautifulSoup(content)

    j=0
    #for pdiv in soup.findAll('div',href=True, attrs={'class':'profile'}):
    for person in soup.findAll('li', attrs={'class':'search-results__people-list__item'}):
        print(j)
        j+=1
        name=person.find('h4', attrs={'class':'search-results__people-list__item__title'}).text#.strip()
        title=person.find('h5', attrs={'class':'search-results__people-list__item__designation'}).text.strip()
        print('.'+ name + '.')
        if (name.startswith('Gabrielle') and name.endswith('Dame')):
            firstName = 'Gabrielle'
            lastName = 'Dame'
        elif (name.startswith('Seth') and name.endswith('Hecht')):
            firstName = 'Seth'
            lastName = 'Hecht'
        elif (name.startswith('Paul') and name.endswith('Smadbeck')):
            firstName = 'Paul'
            lastName = 'Smadbeck'
        elif (name.startswith('Bob') and name.endswith('Knakal')):
            firstName = 'Bob'
            lastName = 'Knakal'
        elif (name.startswith('Kenia') and name.endswith('Fuertes')):
            firstName = 'Kenia'
            lastName = 'Fuertes'
        else:
            spaceIndex = name.index(' ')
            firstName = name[:spaceIndex]
            lastName = name[spaceIndex+1:]

        firstNames.append(firstName)
        lastNames.append(lastName)
        if (title is None):
            print("GOT HERE")
            titles.append('')
        else:
            titles.append(title)
    #i = 1

    seen = False
    seenOnce = False
    seenTwice = False
    for a in soup.find_all("a", href=re.compile(r"mailTo:")):
        
        if ((not seen) and not (seenOnce and seenTwice)):
            emails.append(a.get('href')[7:])

        if (seen):
            seen = False
        elif (seenOnce and seenTwice):
            seenOnce = False
            seenTwice = False
        elif (a.get('href')[7:] == 'gabrielle.dame@am.jll.com'):
            seen = True
        elif (a.get('href')[7:] == 'cpeck@hfflp.com'):
            seen = True
        elif (a.get('href')[7:] == 'bethanie.derose@am.jll.com' and seenOnce):
            seenTwice = True
        elif (a.get('href')[7:] == 'bethanie.derose@am.jll.com'):
            seenOnce = True
        #if (i == 10):
        #    emails.append('')
        
        #i = i + 1

print("firstNames: {}".format(len(firstNames)))
print("lastNames: {}".format(len(lastNames)))
print("emails: {}".format(len(emails)))
print("titles: {}".format(len(titles)))

df = pd.DataFrame({'First Name':firstNames,'Last Name':lastNames,'Email':emails,'Title':titles}) 
df.to_csv('jllDC.csv', index=False, encoding='utf-8')
#df.to_excel("output.xlsx") 