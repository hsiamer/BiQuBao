import sys
import time

from tools.get_bookname import get_bookname
from tools.get_chaptername import get_chaptername
from tools.get_linklist import get_linklist
from tools.get_text import get_text
from tools.mkdir_bookdir import mkdir_bookdir
from tools.mkfile import mkfile

baseurl = 'https://www.biqubao.com'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 "
                  "Safari/537.36 Core/1.53.4033.400 QQBrowser/9.6.12624.400"}

bookid = input('输入书籍编号:\n')
if bookid == '':
    sys.exit()
bookname = get_bookname(bookid, baseurl, headers)
bookdir = mkdir_bookdir(bookid,bookname)
print(bookname)
links = get_linklist(bookid, baseurl, headers)
cpt = len(links)
print('章节总数:',cpt)
for i in range(len(links)):
    title = get_chaptername(baseurl, headers, links[i])
    text = get_text(baseurl, headers, links[i])
    print(title)
    mkfile(i+1,bookdir,title,text)
    time.sleep(1)
    print('\t\t\t\t\t(',i+1,'/',cpt,')')
