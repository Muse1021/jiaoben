# -*- coding: utf-8 -*-
#from_addr = "806028120@qq.com"
#password = "sffnbxxdyflebgab"
#to_addr = "1551848581@qq.com"
#smtp_server = "smtp.qq.com"
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart       
from email.mime.image import MIMEImage   
_user = "806028120@qq.com"
_pwd  = "sffnbxxdyflebgab"
_to   = "1551848581@qq.com"

#msg = MIMEText("Test")
msg = MIMEMultipart('related')
msg["Subject"] = "don't panic"
msg["From"]    = _user
msg["To"]      = _to
att = MIMEText(open('d:\\1.jpg', 'rb').read(), 'base64', 'utf-8')    
att["Content-Type"] = 'application/octet-stream'    
att["Content-Disposition"] = 'attachment; filename="1.jpg"'    
msg.attach(att)
msg.body = "This is a first email"
#msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
#以文件形式
#msg.attach(MIMEText('send with file...'))
#以html形式发送
#msg.attach(MIMEText('<html><h1>你好</h1></html>','html','utf-8'))   
#with open('d:\\1.jpg', 'rb') as f:
#	mine = MIMEb
try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    print "Success!"
except smtplib.SMTPException,e:
    print "Falied,%s"%e 

