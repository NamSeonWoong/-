import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)


num = '737963366'
url = f"https://cafe.naver.com/joonggonara?iframe_url=/ArticleRead.nhn%3Fclubid=10050146%26page=1%26userDisplay=50%26boardtype=L%26articleid={num}%26referrerAllArticles=true"
req = requests.get(url)
html = req.text

soup = BeautifulSoup(html, "html.parser")

title = soup.select_one(
    '#tbody > table > tbody > tr > td > div > p'
)
#로그인버튼: #gnb_login_button > span.gnb_txt
f = open("새파일.txt", 'w')
for line in soup:
    f.write(str(line))
f.close()