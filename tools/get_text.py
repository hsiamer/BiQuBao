import requests
from lxml import etree
def get_text(baseurl: object, headers: object, link: object) -> object:
    url = baseurl + link
    r = requests.get(url,headers)
    r.encoding="gbk"
    html = r.text
    fulltext = ''
    s = etree.HTML(html)
    texts = s.xpath('//*[@id="content"]/text()')
    for text in texts:
        fulltext = fulltext + text.strip() + '\n'
    fulltext = fulltext + '\n'
    return fulltext
