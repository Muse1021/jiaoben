# -*- coding: utf-8 -*-
#from_addr = "806028120@qq.com"
#password = "agcltngytwlubdei"
#to_addr = "1551848581@qq.com"
#smtp_server = "smtp.qq.com"
import smtplib
from email.mime.text import MIMEText
_user = "806028120@qq.com"
_pwd  = "agcltngytwlubdei"
_to   = "1551848581@qq.com"

msg = MIMEText("Test")
msg["Subject"] = "don't panic"
msg["From"]    = _user
msg["To"]      = _to

try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    print "Success!"
except smtplib.SMTPException,e:
    print "Falied,%s"%e 

