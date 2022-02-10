from base64 import decode
from pickle import FALSE, TRUE
import random


def encodeShortURL(longURL,urlDB):
    alphabet="0123456789abcdefghijklmnoprqstuvwxyzABCDEFGHIJKLMNOPRQSTUVWXYZ"
    short_str=""
    for i in range(6):
        short_str += alphabet[random.randint(0,len(alphabet))]
    urlDB.update({"s_URL":"http://tinyurl.com/"+short_str})
    return urlDB

def decodeLongURL(shortURL,urlDB):
    if urlDB.get('s_URL') == shortURL:
        return TRUE
    else:
        return FALSE
def printURLdb(urlDB,longURL):
    urlDB.update({"l_URL":longURL})
    urlDB = encodeShortURL(longURL,urlDB)
    print(urlDB)
    print("ShortURL:" + urlDB.get('s_URL'))
    if decodeLongURL(urlDB.get('s_URL'),urlDB):
        print("LongURL: " + urlDB.get('l_URL'))

urlDB={'l_URL':'','s_URL':''}

longURL = input("enter URL:")
if "," in longURL:
    URLlist = longURL.split(',')
    for url in URLlist:
        printURLdb(urlDB,url)
else:
    printURLdb(urlDB,longURL)
