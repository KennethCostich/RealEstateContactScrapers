import os
import glob
import pandas as pd

# https://www.freecodecamp.org/news/how-to-combine-multiple-csv-files-with-8-lines-of-code-265183e0854/

# Import packages and set the working directory
os.chdir("/Users/kennethcostichiii/Desktop/VSC-Directory/web-scraping/real estate - bosurban/CBRENYC")

# Use glob to match the pattern 'csv' (using regular expressions)
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# Combine all files in the list and export as CSV

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_cbrenyc.csv", index=False, encoding='utf-8-sig')