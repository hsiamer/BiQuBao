import requests
from lxml import etree


def get_linklist(id, baseurl, headers):
    bookid = str(id)
    url: object = baseurl + '/book/' + bookid
    r = requests.get(url, headers)
    r.encoding = "gbk"
    html = r.text
    s = etree.HTML(html)
    links = s.xpath('//*[@id="list"]/dl/dd/a/@href')
    return links
