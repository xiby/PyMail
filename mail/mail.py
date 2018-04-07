import smtplib
from email.header import Header
from email.mime.text import MIMEText

class Mymail():
    def __init__(self,user_dit):
        self.user=user_dit[0]
        self.psw=user_dit[1]
    def login(self):
        pass
    def send(self,content,recvs,t):
        '''
        @function: send your email
        '''
        mail_host="smtp.163.com"
        mail_user=self.user
        mail_pass=self.psw
        sender=self.user
        receivers=recvs
        content='这是一封用Python写的邮件'
        title=t

        #开始发送邮件
        message=MIMEText(content,'plain','utf-8')   #内容，格式，编码
        message['From']='{}'.format(sender)
        message['To']=','.join(receivers)
        message['Subject']=title
        try:
            smtpObj=smtplib.SMTP_SSL(mail_host,465)
            smtpObj.login(mail_user,mail_pass)
            smtpObj.sendmail(sender,receivers,message.as_string())
            print("发送成功")
            #发送成功
        except smtplib.SMTPException as e:
            print(e)
            #发送失败，打印异常信息

    def receive(self):
        '''
        @function: receive your emails
        '''
        pass

    def show(self,emails):
        '''
        @function: show your emails
        '''
        pass
