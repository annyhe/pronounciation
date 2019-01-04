import urllib.request as urllib2
import sys
import os
from bs4 import BeautifulSoup

os.makedirs('cambridge', exist_ok=True) 
WORD = sys.argv[1]
url = 'https://dictionary.cambridge.org/dictionary/english/' + WORD
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
# Take out the <div> of name and get its value
name_box = soup.select('span[title*=' + WORD + ']')
name_box.pop(2)
print(name_box)
if name_box == []:
    print('Could not find comic image.')
else:
    i = 0
    # limit to 2
    while i < 2: 
        print(name_box[i])
        # for each name_box
        title = name_box[i].get('title')
        # if title contains American pronounciation, then it is American, else it is British
        filename = ('-us') if 'American' in title else ('-br')
        filename = WORD + filename + '.mp3'
        comicUrl = 'https://dictionary.cambridge.org' + name_box[i].get('data-src-mp3')
        # Download the image.
        # print('Downloading image %s...' % (comicUrl))
        print(os.path.basename(comicUrl))
        res = urllib2.urlopen(comicUrl)
        print(res)
        i += 1

        #open the file for writing
        fh = open(os.path.join('cambridge', filename), 'wb')

        # read from request while writing to file
        fh.write(res.read())
        fh.close()