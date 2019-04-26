import requests
from lxml import etree


def get_chaptername(baseurl, headers, link):
    url = baseurl + link
    r = requests.get(url, headers)
    r.encoding = "gbk"
    html = r.text
    s = etree.HTML(html)
    chaptername1 = s.xpath('//div[@class="bookname"]/h1/text()')
    if len(chaptername1) > 0:
        chaptername = chaptername1[0]
    else:
        chaptername = ''
    return chaptername
