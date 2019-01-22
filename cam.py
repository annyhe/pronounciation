import urllib.request as urllib2
import sys
import os
from bs4 import BeautifulSoup

# run with 'python cam.py terrible'
os.makedirs('cambridge', exist_ok=True) 
WORD = sys.argv[1]
url = 'https://dictionary.cambridge.org/dictionary/english/' + WORD
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
# Take out the <div> of name and get its value
def my_function(str):
    title = str if str == 'British English' else 'American'
    suffix = '-br' if str == 'British English' else '-us'
    name_box = soup.select('[title*=": listen to ' + title + ' pronunciation"]')
    if name_box == []:
        print('Could not find dictionary word with' + suffix)
    else:
        # if title contains American pronounciation, then it is American, else it is British
        # filename = ('-us') if 'American' in title else ('-br')
        filename = WORD + suffix + '.mp3'
        comicUrl = 'https://dictionary.cambridge.org' + name_box[0].get('data-src-mp3')
        # print(comicUrl)
        # Download the image.
        # print('Downloading image %s...' % (comicUrl))
        print(os.path.basename(comicUrl))
        res = urllib2.urlopen(comicUrl)
        # print(res)

        #open the file for writing
        fh = open(os.path.join('cambridge', filename), 'wb')

        # read from request while writing to file
        fh.write(res.read())
        fh.close()

my_function('British English')
my_function('American')