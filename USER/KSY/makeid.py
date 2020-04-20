import requests
from bs4 import BeautifulSoup
from decouple import config
import numpy as np

base_url = "https://cafe.naver.com/joonggonara"

def find_id(url):
    data = url.split("=")
    return data[4][:9]

def bs(page):
    url = base_url + f"/ArticleList.nhn?search.clubid=10050146&search.boardtype=L&search.totalCount=151&search.page={page}"
    headers = { # 헤더를 넣지 않아도 작동하는 것을 확인했습니다.
        "cookie" : config("cookie"),
        'Content-Type': 'application/json; charset=utf-8',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
    html = requests.get(url, headers = headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup

article_id_list = set(np.load("./article_id_list.npy", allow_pickle=True).tolist())
while len(article_id_list) < 20000:
    for where in range(1, 500):
        page = bs(where)
        for num in range(1, 16):
            try:
                this = page.select_one(f"#main-area > div:nth-child(6) > table > tbody > tr:nth-child({num}) > td.td_article > div.board-list > div > a").get('href')    
                article_id_list.add(find_id(this))
            except:
                pass

np.save("./article_id_list", article_id_list)