def filechapter(bookd,chaptername,bookid,chapterno):
    bookid = '0'*(6-len(str(bookid))) + bookid
    chapterno = '0'*(6-len(str(chapterno))) + str(chapterno) + ' - '
    strs = '<a href="' + bookid + '/' + chapterno +  chaptername  + '.html" target="_blank">' + chaptername + '</a><br>\n'
    with open(bookd,'a+',encoding='utf-8') as f:
        f.write(strs)
        f.close()


