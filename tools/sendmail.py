import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendmail(title,afile,passwd,receiver):
    sender = 'mrxia20170404@163.com'
#    receiver = '815006096@qq.com'
    smtpserver = 'smtp.163.com'
    username = 'mrxia20170404'

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(title, 'utf-8')

    # 邮件正文内容
    text = '这里是邮件的正文\n' + '附件:' + afile
    message.attach(MIMEText(text, 'plain', 'utf-8'))

    # 构造附件
    files = '/root/git/hsiamer.github.io/novels/' + afile
    att1 = MIMEText(open(files, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
#    att1["Content-Disposition"] = 'attachment;filename=%s' % afile.encode('utf-8')
#    att1["Content-Disposition"] = 'attachment;filename=%s' % afile.encode('gbk')
    att1.add_header("Content-Disposition", "attachment", filename=("gbk", "", afile))
    message.attach(att1)
    smtpObj = smtplib.SMTP_SSL()  # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法
    print('连接到邮件服务器')
    smtpObj.connect(smtpserver)
    print('登录中...')
    smtpObj.login(username, passwd)
    print('发送中...')
    smtpObj.sendmail(sender, receiver, message.as_string())
    print("邮件发送成功")
    smtpObj.quit()

