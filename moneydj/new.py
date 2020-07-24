import time, requests
from selenium import webdriver
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/77.0.3865.120 Safari/537.36'}

url = requests.get('https://udn.com/news/breaknews/1', headers = headers).url
# 下方路徑為個人chromedriver.exe的位置
driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver.exe')
driver.get(url)

for i in range(20): 
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(2)
