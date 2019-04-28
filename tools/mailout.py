import smtplib
import getpass
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = 'mrxia20170404@163.com'
receiver = '815006096@qq.com'
smtpserver = 'smtp.163.com'
username = 'mrxia20170404'
print('下面输入发件箱密码')
password = getpass.getpass('邮箱密码:')
mail_title = 'Python3邮件测试'

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = Header(mail_title, 'utf-8')

# 邮件正文内容
message.attach(MIMEText('这是邮件的正文', 'plain', 'utf-8'))

# 构造附件1（附件为TXT格式的文本）
att1 = MIMEText(open('f:\\1.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="f:\\1.txt"'
message.attach(att1)

smtpObj = smtplib.SMTP_SSL()  # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法
smtpObj.connect(smtpserver)
smtpObj.login(username, password)
smtpObj.sendmail(sender, receiver, message.as_string())
print("邮件发送成功")
smtpObj.quit()