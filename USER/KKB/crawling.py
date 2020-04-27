import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from decouple import config
from selenium.webdriver.firefox.options import Options
import time

def find_id(url):
    data = url.split("=")
    return data[4][:9]

def find_content(content):
    data = content.split("\n")
    num = 15
    dummy = ['직접거래 시 아래 사항에 유의해주세요.',
    '불확실한 판매자(본인 미인증, 해외IP, 사기의심 전화번호)의 물건은 구매하지 말아주세요.',
    '판매자와 의 연락은 메신저보다는 전화, 메일 등을 이용하시고 개인정보 유출에 주의하세요.',
    '계좌이체 시 선입금을 유도할 경우 안전한 거래인지 다시 한 번 확인해주세요.',
    '네이버에 등록된 판매 물품과 내용은 개별 판매자가 등록한 것으로서,',
    '네이버카페는 등록을 위한 시스템만 제공하며 내용에 대하여 일체의 책임을 지지 않습니다.',
    '* 거래전 필독! 주의하세요!', '* 연락처가 없이 외부링크, 카카오톡, 댓글로만 거래할 때',
    '* 연락처 및 계좌번호를 사이버캅과 더치트로 꼭 조회해보기',
    '* 업체인 척 위장하여 신분증과 사업자등록증을 보내는 경우',
    '* 고가의 물품(휴대폰,전자기기)등만 판매하고 최근(1주일 내) 게시글만 있을 때',
    '* 해외직구로 면세받은 물품을 판매하는 행위는 불법입니다.']
    while data[num] in dummy:
        num += 1
    return '\n'.join(data[num:])

def article_element(article):
    article_title = article.text

    article_url = article.get_attribute("href")
    article_id = find_id(article_url)

    print(article_url, article_id)

    time.sleep(1)
    driver.get(article_url)
    driver.switch_to.frame('cafe_main')

    # 모바일
    if article_title[:5] == "[공식앱]":
        title = driver.find_element_by_xpath('//*[@id="post_739362855"]/div/div[1]/div[1]/table/tbody/tr/td[1]/span')
        price = driver.find_element_by_xpath('//*[@id="tbody"]/div[3]/div/b/span[2]/font/span')
        content = driver.find_element_by_xpath('//*[@id="tbody"]')
        # trade_style = driver.find_element_by_xpath('//*[@id="post_739362855"]/div/div[1]/div[1]/table/tbody/tr/td[3]/a')
        category = driver.find_element_by_xpath(f'//*[@id="post_{article_id}"]/div/div[1]/div[1]/table/tbody/tr/td[3]/a')

        element = {
            "title": title.text,
            "price": price.text,
            "content": find_content(content.text),
            "trade_style": "mobile",
            "category": category.text
        }

    else:
        title = driver.find_element_by_xpath('//*[@id="tbody"]/table/tbody/tr/td/div/p')
        price = driver.find_element_by_xpath('//*[@id="tbody"]/table/tbody/tr/td/div/div[1]/span')
        content = driver.find_element_by_xpath('//*[@id="tbody"]')
        trade_style = driver.find_element_by_xpath('//*[@id="tbody"]/table/tbody/tr/td/div/table/tbody/tr[2]/td/span[1]')
        category = driver.find_element_by_xpath(f'//*[@id="post_{article_id}"]/div/div[1]/div[1]/table/tbody/tr/td[3]/a')

        element = {
            "title": title.text,
            "price": price.text,
            "content": find_content(content.text),
            "trade_style": trade_style.text,
            "category": category.text
        }
    print(element)
    driver.back()
    return element



USER = config("USER")
PASS = config("PASS")

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")


driver = webdriver.Chrome('C:/Users/134340/s02p23c102/USER/KSY/chromedriver.exe', options=options)

#로그인 페이지 접근
url_login = "https://nid.naver.com/nidlogin.login"
driver.get(url_login)

#텍스트박스에 아이디, 비밀번호 입력하기
driver.execute_script("document.getElementsByName('id')[0].value=\'" + USER + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + PASS + "\'")
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()


# url = f"https://cafe.naver.com/joonggonara?iframe_url=/ArticleRead.nhn%3Fclubid=10050146%26page=1%26userDisplay=50%26boardtype=L%26articleid={num}%26referrerAllArticles=true"
base_url = f"https://cafe.naver.com/joonggonara/"

article_list = []

for page in range(1, 2):
    # 중고나라 전체글 들어가기
    time.sleep(1)
    all_board = f"ArticleList.nhn?search.clubid=10050146&search.boardtype=L&search.totalCount=151&search.page={page}"
    driver.get(base_url + all_board)
    driver.switch_to.frame('cafe_main')


    # 중고나라 게시글 한개 들어가기 (모바일 작성, pc작성 구분)
    for num in range(1, 16):
        article = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[4]/table/tbody/tr[{num}]/td[1]/div[2]/div/a')
        temp = article_element(article)
        article_list.append(temp)

import csv

# 파일 생성
f = open("새파일.csv", 'w', encoding="utf-8")
writer = csv.writer(f)
for article in article_list:
    writer.writerow([article["title"], article["price"], article["content"], article["trade_style"], article["category"]])
f.close()

driver.quit()