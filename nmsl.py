import requests
from bs4 import BeautifulSoup

#甜甜
def get_tiantian():
    url = 'https://s.nmsl8.club/loveword?type=1'
    html = requests.get(url)
    get_text = BeautifulSoup(html.text,"html.parser")
    sentence = get_text.find_all('p')
    row = sentence[0].get_text()
    return row

#嘴臭
def get_chouchou():
    '''
    url = 'https://s.nmsl8.club/loveword?type=2'
    html = requests.get(url)
    get_text = BeautifulSoup(html.text,"html.parser")
    sentence = get_text.find_all('p')
    row = sentence[0].get_text()
    return row
    '''