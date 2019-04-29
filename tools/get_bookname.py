import requests,sys
from lxml import etree

def get_bookname(bookid, baseurl, headers):
    bookid: str = str(bookid)
    url = baseurl + '/book/' + bookid
    r = requests.get(url, headers)
    r.encoding = "gbk"
    html = r.text
    s = etree.HTML(html)
    title = s.xpath('//*[@id="info"]/h1/text()')
    if len(title) < 1:
        print('书籍编号输入错误')
        sys.exit()
    return title[0]
