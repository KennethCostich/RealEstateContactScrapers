#!/bin/bash

# Create an array files that contains list of filenames
#files=($(< file.txt))

# Read through the url.txt file and execute wget command for every filename
#while IFS='=| ' read -r param uri; do 
#    for file in "${files[@]}"; do 
#        curl "${uri}${file}"
#    done
#done < url.txt

i=0

while IFS="" read -r p || [ -n "$p" ]
do
  curl "${p}" --output "vcfs/${i}.txt"
  ((i=i+1))
done < vcardDownloadLinks.txt