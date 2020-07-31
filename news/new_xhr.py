import json, requests
from selenium import webdriver
from bs4 import BeautifulSoup

for page in range(1,5):
    page=str(page)
    url="https://udn.com/api/more?page="+page+"&id=&channelId=1&cate_id=0&type=breaknews&totalRecNo=6657"
    resp=requests.get(url=url)
    data=json.loads(resp.text)
    articles=data['lists']

    for article in articles:
        title=article['title']
        link=article['titleLink']
        print(title,link)
        
