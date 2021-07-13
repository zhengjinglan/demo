# _*_encoding:'utf-8' _*_
#需要使用到smtplib库，来进行邮箱的连接
import smtplib
#用于处理邮件内容的库，email.mine
from email.mime.text import MIMEText
#处理邮件附件，需要导入mimemultipart，header，mimebase
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders

#邮箱属性的配置
mailserver = 'smtp.126.com' #邮箱服务端URL pop.126.com, smtp.126.com
userName_SendMail = 'zjl_lan@126.com' #发件人
userName_AuthCode = 'QJOOYSSAXLRWVHDE' #邮箱发件授权码
received_mail = ['zjl_lan@126.com'] #定义邮件的接收者,可以定义多个，中间以逗号隔开

#发送一封简单的邮件
# content = '这是一封纯粹的文本信息内容'
# email = MIMEText(content, 'plain', 'utf-8')#纯文本形式的邮件内容定义，通过MIMEText进行操作
# email['Subject'] = '邮件主题' #定义邮件主题
# email['From'] = userName_SendMail #发件人
# email['To'] = ','.join(received_mail) #收件人

#发送一封HTML内容邮件
# content = '''
# <p>这是一封HTML文本的邮件</p>
# <p><a href="http://www.baidu.com">点击这里就送小龙女</a></p>
# '''
# email = MIMEText(content, 'html', 'utf-8')#纯文本形式的邮件内容定义，通过MIMEText进行操作
# email['Subject'] = '邮件主题_HTML' #定义邮件主题
# email['From'] = userName_SendMail #发件人
# email['To'] = ','.join(received_mail) #收件人

#邮件中发送附件
#附件配置邮箱
email = MIMEMultipart()
email['Subject'] = '邮件主题' #定义邮件主题
email['From'] = userName_SendMail #发件人
email['To'] = ','.join(received_mail) #收件人
#非图片附件
att = MIMEBase('application', 'actet-stream')
att.set_payload(open('附件.txt', 'rb').read())
att.add_header('Content-Disposition', 'attachment', filename = Header('附件.txt', 'gbk').encode())
encoders.encode_base64(att)
email.attach(att)

#图片附件
att1 = MIMEBase('application', 'actet-stream')
att1.set_payload(open('thpop.jpg', 'rb').read())
att1.add_header('Content-Disposition', 'attachment', filename = Header('thpop.jpg', 'gbk').encode())
encoders.encode_base64(att1)
email.attach(att1)
#发送邮件
smtp = smtplib.SMTP(mailserver, port=25) #qq邮箱使用SMTP_SSL，非QQ邮箱使用SMTP
smtp.login(userName_SendMail, userName_AuthCode)
smtp.sendmail(userName_SendMail, ','.join(received_mail), email.as_string())

smtp.quit()
