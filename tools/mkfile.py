import platform


def mkfile(chapterno,bookdir,chaptername,text):
    p = '0'
    chapterno = str(chapterno)
    chaptername = p*(6-len(chapterno)) + chapterno + ' - ' + chaptername
    if platform.system()=='Windows':
        bookd = bookdir + '\\' + chaptername
    if platform.system()=='Linux':
        bookd = bookdir + '/' + chaptername + '.txt'
    with open(bookd,'w+',encoding = 'utf-8') as f:
        f.write(text)
        f.close()
