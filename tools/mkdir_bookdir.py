import os, shutil,platform


def mkdir_bookdir(bookid, bookname):
    p = '0'
    bookid = str(bookid)
    if platform.system()=='Windows':
        bookdir = 'e:\\books\\' + p * (6 - len(bookid)) + bookid
#    if platform.system()=='Linux':
    else:
        bookdir = 'done/' + p * (6 - len(bookid)) + bookid
    bookdir = bookdir + bookname
    if os.path.exists(bookdir):
        shutil.rmtree(bookdir)
        os.mkdir(bookdir)
    else:
        os.mkdir(bookdir)
    return bookdir
