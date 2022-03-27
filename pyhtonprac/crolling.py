import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
#크롤링에서 중요한것
# 1. 요청하는것 requests
# 2. 요청되어서 가지고온 html 중에서 내가 원하는 정보를 잘 솎아내는 것 beautifulsoup
# 코딩 시작

#print(soup)

trs = soup.select('#old_content > table > tbody > tr')

for tr in trs:
    a_tag = tr.select_one('td.title > div > a')
    point = tr.select_one('tr:nth-child(2) > td.point')

    if a_tag is not None:
        title = a_tag.text
        rank = tr.select_one('td:nth-child(1) > img ')['alt']
        point = tr.select_one('td.point').text
        print(rank , title , point)




#title =soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')

#print(title) # text만 가지고 오고싶다면 title.text 를 붙이면된다. #속성을 가지고 오고싶다하면 title['href']


