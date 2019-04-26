import requests
from lxml import etree


def get_bookname(bookid, baseurl, headers):
    bookid: str = str(bookid)
    url = baseurl + '/book/' + bookid
    r = requests.get(url, headers)
    r.encoding = "gbk"
    html = r.text
    s = etree.HTML(html)
    title = s.xpath('//*[@id="info"]/h1/text()')
    return title[0]
