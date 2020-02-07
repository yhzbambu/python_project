import requests
import json
from bs4 import BeautifulSoup

in_theaters_url="https://movies.yahoo.com.tw/movie_intheaters.html"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/77.0.3865.120 Safari/537.36'}

resp=requests.get(url=in_theaters_url,headers=headers)
soup=BeautifulSoup(resp.text,"html.parser")
pages=soup.find("div","page_numbox").find_all("li")[-3].text
print(pages)

all_movie=[]
for page in range(1,int(pages)+1):
    resp=requests.get(url=in_theaters_url+"?page="+str(page),headers=headers)
    soup=BeautifulSoup(resp.text,"html.parser")
    movies=soup.find_all('div', 'release_info_text')
    for movie in movies:
        chinese_name =movie.find('div', 'release_movie_name').find('a').text.strip()
        english_name =movie.find('div', 'release_movie_name').find('div', 'en').find('a').text.strip()
        expectation=movie.find('div', 'leveltext').find('span').text.strip()
        satisfaction=movie.find('span','count')['data-num']
        release_date=movie.find('div', 'release_movie_time').text.replace('上映日期 ：','').strip()
        introduction=movie.find('div', 'release_text').text.replace(u'詳全文', '').strip()
        all_movie.append({
            "chinese_name":chinese_name,
            "english_name":english_name,
            "expectation":expectation,
            "satisfaction":satisfaction,
            "release_date":release_date,
            "inroduction":introduction,
        })    
with open('yahoo_movie_in_theaters_json.csv', 'w', encoding='utf-8') as f:
    json.dump(all_movie, f, indent=2, sort_keys=False, ensure_ascii=False)