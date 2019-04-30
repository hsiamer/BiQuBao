import sys,platform
import time
from getpass import getpass

from tools.get_bookname import get_bookname
from tools.get_chaptername import get_chaptername
from tools.get_linklist import get_linklist
from tools.get_text import get_text
from tools.mkdir_bookdir import mkdir_bookdir
from tools.mkfile import mkfile
from tools.mksinglefile import mksinglefile
from tools.sendmail import sendmail
from tools.mknovelpage import  mknovelpage
from tools.fillchapterlist import filechapter


baseurl = 'https://www.biqubao.com'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 "
                  "Safari/537.36 Core/1.53.4033.400 QQBrowser/9.6.12624.400"}

bookid = input('输入书籍编号:\n')
if bookid == '':
    print('退出程序')
    sys.exit()
bookname = get_bookname(bookid, baseurl, headers)
links = get_linklist(bookid, baseurl, headers)
cpt = len(links)
print(bookname,'章节总数:',cpt)
foi = input('1: 单个文件;2:分章节存储;Enter:退出程序\n')
if foi == '':
    print('退出程序')
    sys.exit()
if foi != '1' and foi != '2':
    print('输入错误')
    sys.exit()
if foi == '1':
    passwd = getpass('发件箱密码:')
    mksinglefile(bookname,bookid,baseurl,headers,links)
    bookdir = '0' * (6 - len(bookid)) + bookid + ' - ' + bookname + '.txt'
    o = input('是否要将下载文件发送到邮箱(1:是;2:否):\n')
    if o=='1':
        passwd = getpass('发件箱密码:')
        sendmail(bookname,bookdir,passwd)
    if o!='1':
        sys.exit()
if foi == '2':
    bookdir = mkdir_bookdir(bookid,bookname)
    chapterpage = mknovelpage(bookid,bookname)
    for i in range(6): # 测试用例
#    for i in range(len(links)):
        title = get_chaptername(baseurl, headers, links[i])
        text = get_text(baseurl, headers, links[i])
        print(title)
        chapterdir = mkfile(i+1,bookdir,title,text)
        filechapter(bookname,chapterpage,title,bookid,i+1)
        time.sleep(1)
        print('\t\t\t\t\t(',i+1,'/',cpt,')')


