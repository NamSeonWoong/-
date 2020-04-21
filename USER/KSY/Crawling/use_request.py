import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

list_url = "https://m.cafe.naver.com/joonggonara/ArticleAllListAjax.nhn"

params = {
    'search.clubid': '10050146',
    'search.boardtype': 'L',
    'search.questionTab': 'A',
    'search.totalCount': '201',
    'search.page': 1,
}

html = requests.get(list_url, params = params).text
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

