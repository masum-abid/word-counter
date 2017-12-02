import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list=[]
    source_code=requests.get(url).text
    soup=BeautifulSoup(source_code, "html.parser")
    for post_text in soup.findAll('a', {'class': "item-title h4"}):
        content=post_text.string
        words=content.lower().split()
        for each_word in words:
            print(each_word)
            word_list.append(each_word)
    create_dictionary(word_list)


def create_dictionary(word_list):
    word_count={}
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)

start('http://bikroy.com/bn/ads')