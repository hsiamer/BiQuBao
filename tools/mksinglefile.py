import platform
from tools.get_text import get_text
from tools.get_chaptername import get_chaptername


def mksinglefile(bookname, bookid, baseurl, headers, links):
    p = '0'
    bookid = str(bookid)
    bookname = p * (6 - len(bookid)) + bookid + ' - ' + bookname
    cpt = len(links)
    if platform.system() == 'Windows':
        bookd = 'e:\\books\\' + bookname + '.txt'
    else:
        bookd = '/root/git/hsiamer.github.io/novels/' + bookname + '.txt'
    with open(bookd, 'w+', encoding='utf-8') as f:
        f.write('')
        f.close()
    for i in range(len(links)):
        text = get_text(baseurl, headers, links[i])
        chaptername = get_chaptername(baseurl,headers,links[i]) + '\n'
        print(chaptername)
        with open(bookd, 'a+', encoding='utf-8') as f:
            f.write(chaptername)
            f.write(text)
            f.close()
        print('\t\t\t\t\t (', i + 1,'/', cpt, ")")
