import platform


def mkfile(chapterno,bookdir,chaptername,text):
    p = '0'
    chapterno = str(chapterno)
    chaptername1 = p*(6-len(chapterno)) + chapterno  + ' - ' + chaptername
    if platform.system()=='Windows':
        bookd = bookdir + '\\' + chaptername1
    if platform.system()=='Linux':
        bookd = bookdir + '/' + chaptername1 + '.html'
    title = '<head><title>' + chaptername + '</title></head><br>\n'
    with open(bookd,'w+',encoding = 'utf-8') as f:
        f.write(title)
        f.write(text)
        f.close()
    return bookd
