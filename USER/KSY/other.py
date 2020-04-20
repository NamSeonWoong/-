import requests
from bs4 import BeautifulSoup
from decouple import config

base_url = "https://cafe.naver.com/joonggonara"

# def find_id(url):
#     data = url.split("=")
#     return data[4][:9]

# def bs(page):
#     url = base_url + f"/ArticleList.nhn?search.clubid=10050146&search.boardtype=L&search.totalCount=151&search.page={page}"
#     headers = { # 헤더를 넣지 않아도 작동하는 것을 확인했습니다.
#         "cookie" : config("cookie"),
#         'Content-Type': 'application/json; charset=utf-8',
#         'Accept-Language': 'ko-KR,ko;q=0.9,en-US',
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
#     }
#     html = requests.get(url, headers = headers)
#     soup = BeautifulSoup(html.text, 'html.parser')
#     return soup

# page = bs(1)

# article_id_list = set()
# for num in range(1, 16):
#     this = page.select_one(f"#main-area > div:nth-child(6) > table > tbody > tr:nth-child({num}) > td.td_article > div.board-list > div > a").get('href')
#     article_id_list.add(find_id(this))
# print(article_id_list)

# article_id_list = list(article_id_list)

def get_article_data(article_url):
    url = base_url + "/ArticleRead.nhn?clubid=10050146&page=1&boardtype=L&articleid=" + article_url + "&referrerAllArticles=true"
    print(url)
    headers = { # 헤더를 넣지 않아도 작동하는 것을 확인했습니다.
        "cookie" : config("cookie"),
        'Content-Type': 'application/json; charset=utf-8',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
    html = requests.get(url, headers = headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup


data = get_article_data(article_id_list[0])

f = open("새파일.txt", "w", encoding="utf-8")
for line in data:
    f.write(str(line))
f.close()


def get_text_data(data, article_id):
    print(article_id)
    title = data.select_one(f"#post_{article_id} > div > div.tit-box > div.fl > table > tbody > tr > td:nth-child(1) > span").text
    category = data.select_one(f"#post_{article_id} > div > div.tit-box > div.fl > table > tbody > tr > td:nth-child(3) > a").text
    price = data.select_one("#tbody > table > tbody > tr > td > div > div.prod_price > span").text
    content = data.select_one("#tbody").text
    data = data.select_one(f"#post_{article_id} > div > div.tit-box > div.fr > table > tbody > tr > td.m-tcol-c.date").text

    one = {"title": title, "category": category, "price": price, "content": content, "data": data}
    return one

print(get_text_data(data, article_id_list[0]))

