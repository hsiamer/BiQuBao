import platform


def mkfile(bookdir,chaptername,text):
    if platform.system()=='Windows':
        bookd = bookdir + '\\' + chaptername
    if platform.system()=='Linux':
        bookd = bookdir + '/' + chaptername
    with open(bookd,'w+',encoding = 'utf-8') as f:
        f.write(text)
        f.close()
