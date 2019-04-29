def filechapter(bookd,chaptername,chapterdir):
    strs = '<a href="' + chapterdir + '" target="_blank">' + chaptername + '</a><br>'
    with open(bookd,'a+',encoding='utf-8') as f:
        f.write(strs)
        f.close()


