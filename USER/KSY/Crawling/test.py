def find(url):
    data = url.split("=")
    return data[4][:9]


a = find("https://cafe.naver.com/ArticleRead.nhn?clubid=10050146&page=1&boardtype=L&articleid=739347107&referrerAllArticles=true")

print(a)