import requests
import time
import json
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/77.0.3865.120 Safari/537.36'}

#請求電子書的首頁
resp=requests.get("https://www.books.com.tw/web/sys_hourstop/home?loc=P_0007_001",headers=headers)
soup=BeautifulSoup(resp.text,"html.parser")
all=soup.find_all("div","type02_bd-a")
print(len(all))
for book in all:
    title=book.find("a").text
    print(title)
    try:
        author=book.find("ul","msg").find("a").text
    except:
        author="none"
    print(author)
    price=book.find("li","price_a").find_all("strong")[-1].text
    print(price)