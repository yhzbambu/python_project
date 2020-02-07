import requests
from bs4 import BeautifulSoup
import json
import re
import time
from lxml import etree
hot_url="https://kma.kkbox.com/charts/hourly?terr=tw&lang=tc#"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/77.0.3865.120 Safari/537.36'}
today = time.strftime("%m/%d").replace("/","-")
localtime = time.asctime( time.localtime(time.time()) )
print(localtime)
html=requests.get(url=hot_url,headers=headers).content
selector = etree.HTML(html)

response=selector.xpath('/html/body/script[12]/text()')
top=0
for match in re.finditer('"song_url":"(.*?)"',response[0]):
    
    key=match.group().replace('\\','')
    song_url=key.replace('"song_url":"','').replace('"','')
    print(song_url)
    resp=requests.get(url=song_url,headers=headers)
    soup=BeautifulSoup(resp.text,'html.parser')
    top+=1
    print('%s Top%s' %(today,top))
    song_name=soup.find('h1','section-title').text
    print(song_name)
    performer=soup.find('dd','creator-nick').text.strip()
    print(performer)
    release=soup.find('time').text
    print(release)
    