import glob
import os
import pandas as pd

firstNames=[] #List to store first names
lastNames=[] #List to store last names
emails=[] #List to store emails
titles=[] #List to store Job Titles

os.chdir("/Users/kennethcostichiii/Desktop/VSC-Directory/web-scraping/real estate - bosurban/vcfs")
for file in glob.glob("*.txt"):
    print(file)
    thisFile = open(file)
    for line in thisFile:
        if line.startswith('N:'):
            semiIndex = line.index(';')
            lastNameString = line[2:semiIndex]
            lastNames.append(lastNameString)
            firstNameString = line[semiIndex+1:-1]
            firstNames.append(firstNameString)
        elif line.startswith('TITLE:'):
            titleString = line[6:-1]
            titles.append(titleString)
        elif line.startswith('EMAIL'):
            emailString = line[20:-1]
            emails.append(emailString)
    thisFile.close()


df = pd.DataFrame({'First Name':firstNames,'Last Name':lastNames,'Email':emails,'Title':titles}) 
df.to_csv('cushmanDC.csv', index=False, encoding='utf-8')