#!/usr/bin/env python

# run with 'python python_script.py terrible'
import requests, os, bs4, sys

os.makedirs('dictionary', exist_ok=True) 
print(sys.argv[0]) # prints python_script.py
print(sys.argv[1]) # prints var1
WORD = sys.argv[1]
url = 'https://www.dictionary.com/browse/' + WORD

# Download the page.
print('Downloading page %s...' % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

# Find the spans with matching attributes
# for dictionary.com
comicElem = soup.select('audio source')
if comicElem == []:
    print('Could not find comic image.')
else:
    i = 0
    # limit to 2
    while i < 2: 
        print(comicElem[i])
        comicUrl = comicElem[i].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save the image to ./dictionary.
        imageFile = open(os.path.join('dictionary', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()    
        i += 1

