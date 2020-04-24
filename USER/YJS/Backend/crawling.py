import requests
from bs4 import BeautifulSoup
from decouple import config
import urllib

def search(keyword, page):
    base_url = "https://cafe.naver.com/joonggonara"
    headers = { # 헤더를 넣지 않아도 작동하는 것을 확인했습니다.
    "cookie" : config("cookie"),
    'Content-Type': 'application/json; charset=utf-8',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
    def get_article_data():
        newKeyword = str(keyword.encode('ms949')).lstrip("b'").rstrip("'").replace("\\x","%")
        url = base_url + f"/ArticleSearchList.nhn?search.clubid=10050146&search.searchdate=all&search.page={page}&search.searchBy=0&search.query={newKeyword}&search.includeAll=&search.exclude=&search.include=&search.exact=&"
        html = requests.get(url, headers = headers)
        soup = BeautifulSoup(html.text, 'html.parser')
        soup = soup.select('#main-area > div.article-board > table > tbody> tr')
        return soup

    def get_text_data(url):
        html = requests.get(base_url+url, headers = headers)
        soup = BeautifulSoup(html.text, 'html.parser')
        data = soup.select_one('html>body>#basisElement>#content-area>#main-area>div.list-blog>div.inbox')
        if not data:
            data = soup
        try:
            title = data.select_one("div.tit-box>div.fl>table>tr>td>span").text
        except:
            title="error!"
        try:
            category = data.select_one("div.tit-box>div.fl>table>tr>td>a.m-tcol-c").text
        except:
            category = "error!"
        try:
            user = data.select_one("div.etc-box > div.fl > table > tr > td > table > tr > td.p-nick > a").text
        except:
            user= "error!"
        try:
            price = data.select_one("span.cost").text
        except:
            price="error!"
        try :
            content = data.select_one("#tbody > div.NHN_Writeform_Main")
            # print(data.select_one("#tbody > div.NHN_Writeform_Main"))
            content = list(map(lambda x : x.text, content))
            if "* 거래전 필독! 주의하세요!" in content[0]:
                content.pop(0)
        except:
            content = []
        try: 
            date = data.select_one("div.tit-box > div.fr > table > tbody > tr > td.m-tcol-c.date").text
        except:
            date="2020. 04. 24"
        one = {"title": title, "user": user, "category": category, "price": price, "content": content, "date": date, "url": base_url+url}
        return one

    # 저장되어있는 id 목록 불러오기
    # article_id_list = list(np.load("./article_id_list.npy", allow_pickle=True).tolist())
    # 저장되어있던 process된 data목록 불러오기
    process_datas = []
    data = get_article_data()
    for tr in data:
        process_datas.append(get_text_data(tr.select_one('a.article')['href']))

    return process_datas
