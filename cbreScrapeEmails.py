from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re

driver = webdriver.Chrome("/Users/kennethcostichiii/chromeDriver/chromedriver")

firstNames=[] #List to store first names
lastNames=[] #List to store last names
emails=[] #List to store emails
titles=[] #List to store Job Titles
#driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq")
driver.get("https://www.cbre.us/people-and-offices-results?FirstName=&LastName=&City=3670-C&g-recaptcha-response=03AGdBq27k_5WZ5Y5GUaNFexycW5MWLBakZsnh5n01OPhCWjatAmKt_HRBewbWe24vL3uwgBXi0a2z-lDZbX70Cfz0yNozI3WCBi4mYS5kjjbbclCaPJ9ViXowFOCcMuLyirwvSX5eek4johk9OcJgXvzWSioWa4OZmil6U4qAJ3XTDDq6kMbKXfcKEVdgimQ8QAkqvmmw6uBS35lLNDv7Sh92fL9udAf5iqHFY-Uum5Doeszy8WhgAajECC9eGTxE41nuPBXh6KCTXiMewFLN_lBKVCfEsVYL8j_WhCGUbisZ5GsiMPsZkNChcIV2ys8pmpJ5uv8lsSOQg33kBVbE18hLZHnOcHdsp5EVuJrWxKBJ9t5d86t1O43YfG3IkS5lqlrFRHo3Zw1mSHyRmMLtPYUK2GFU3zsWDPFIExsCZabfnCdHhJmuye2XGAPlH7qKVRZpGIzDi2BlUfywVDAbdXHJ4AXGM6TDkAnKYZFwPmXI8KSf5SdTxDCCPQZlP4_zhDWpl8sDQBP_")

content = driver.page_source
soup = BeautifulSoup(content)

#for pdiv in soup.findAll('div',href=True, attrs={'class':'profile'}):
for pdiv in soup.findAll('div', attrs={'class':'profile'}):
    name=pdiv.find('span', attrs={'class':'name'})
    #lastName=pdiv.find('span', attrs={'class':'axnyouaodfs'})
    emailDiv=pdiv.find('li', attrs={'class':'email'})
    #email=emailDiv.findAll("a")[0]["href"][8:]
    title=pdiv.find('span', attrs={'class':'title'})
    commaIndex = name.text.index(',')
    lastName = name.text[1:commaIndex]
    firstName = name.text[commaIndex+2:len(name.text)-1]
    firstNames.append(firstName)
    lastNames.append(lastName)
    if (title is None):
        print("GOT HERE")
        titles.append('')
    else:
        titles.append(title.text)

#i = 1

for a in soup.find_all("a", href=re.compile(r"^mailto:")):
    emails.append(a.text)
    #if (i == 10):
    #    emails.append('')
    
    #i = i + 1


df = pd.DataFrame({'First Name':firstNames,'Last Name':lastNames,'Email':emails,'Title':titles}) 
df.to_csv('emailsNamesDC.csv', index=False, encoding='utf-8')
#df.to_excel("output.xlsx") 