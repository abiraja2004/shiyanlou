
from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
#设置发送人
msg['from'] = "*****@126.com"
#设置收件人
msg['to'] = "*****@qq.com"

# 输入Email地址和口令:
from_addr = "****@126.com"
#该密码为邮箱授权码
password = "****"
# 输入收件人地址:
to_addr = "*****@qq.com"
# 输入SMTP服务器地址:
smtp_server = "smtp.126.com"

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()