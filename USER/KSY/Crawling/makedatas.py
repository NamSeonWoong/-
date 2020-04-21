import requests
from bs4 import BeautifulSoup
from decouple import config
import numpy as np

base_url = "https://cafe.naver.com/joonggonara"

def get_article_data(article_url):
    url = base_url + "/ArticleRead.nhn?clubid=10050146&page=1&boardtype=L&articleid=" + article_url + "&referrerAllArticles=true"
    headers = { # 헤더를 넣지 않아도 작동하는 것을 확인했습니다.
        "cookie" : config("cookie"),
        'Content-Type': 'application/json; charset=utf-8',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
    html = requests.get(url, headers = headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup, url

def get_text_data(data, article_id, url):
    title = data.select_one(f"#post_{article_id} > div > div.tit-box > div.fl > table > tr > td:nth-child(1) > span").text
    category = data.select_one(f"#post_{article_id} > div > div.tit-box > div.fl > table > tr > td:nth-child(3) > a").text
    price = data.select_one("#tbody > table > tr > td > div > div.prod_price > span").text
    content = data.select("#tbody > div:nth-child(n+8)")
    content = list(map(lambda x : x.text, content))
    if content[0] == "\n* 거래전 필독! 주의하세요!\r* 연락처가 없이 외부링크, 카카오톡, 댓글로만 거래할 때\r* 연락처 및 계좌번호를 사이버캅과 더치트로 꼭 조회해보기\r* 업체인 척 위장하여 신분증과 사업자등록증을 보내는 경우\r* 고가의 물품(휴대폰,전자기기)등만 판매하고 최근(1주일 내) 게시글만 있을 때\r* 해외직구로 면세받은 물품을 판매하는 행위는 불법입니다.\n":
        content.pop(0)
    date = data.select_one(f"#post_{article_id} > div > div.tit-box > div.fr > table > tbody > tr > td.m-tcol-c.date").text
    one = {"title": title, "category": category, "price": price, "content": content, "date": date, "url": url}
    return one

# 저장되어있는 id 목록 불러오기
article_id_list = list(np.load("./article_id_list.npy", allow_pickle=True).tolist())
# 저장되어있던 process된 data목록 불러오기
process_datas = []

for i in range(20000):
    data, url = get_article_data(article_id_list[i])
    try:
        one = get_text_data(data, article_id_list[i], url)
        process_datas.append(one)
    except:
        pass
    if i % 1000 == 0:
        np.save("./process_datas", process_datas)
        print(i)

np.save("./process_datas", process_datas)
print("data길이: ",len(process_datas))














# # 프린트로 확인이 안되서 txt로 확인
# f = open("새파일.txt", "w", encoding="utf-8")
# for line in data:
#     f.write(str(line))
