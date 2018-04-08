import smtplib
import poplib
from email.header import Header
from email.mime.text import MIMEText
from email.parser import Parser

import getpass
import base64

def decode_base64(s,charset='utf8'):
    return str(base64.decodebytes(s.encode(encoding=charset)),encoding=charset)

class MailInfo():
    '''
    save mail detials
    '''
    def __init__(self):
        self.title=''
        self.from_nickname=''
        self.from_account=''
        self.to_nickname=''
        self.to_account=''
        self.text_content=''
        self.html_content=''

class Mymail():
    def __init__(self):
        self.user=input('输入邮箱帐号：')
        self.psw=getpass.getpass('输入密码：')
    def login(self):
        pass
    def send(self,content,recvs,title):
        '''
        @function: send your email
        @param: content: the content of the mail you will send
                recvs: the list of receivers
                ttile: title of your sending mail
        '''
        mail_host="smtp.163.com"
        mail_user=self.user
        mail_pass=self.psw
        sender=self.user
        receivers=recvs

        #开始发送邮件
        message=MIMEText(content,'plain','utf-8')   #内容，格式，编码
        message['From']='{}'.format(sender)
        message['To']=','.join(receivers)
        message['Subject']=title
        try:
            #use SSL to send mails
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
        @return: all the parsed mails
        '''
        pop3_server='pop.163.com'
        server=poplib.POP3(pop3_server)
        server.set_debuglevel(1)
        print(server.getwelcome().decode('utf8'))

        server.user(self.user)
        server.pass_(self.psw)

        print('Mail counts: {0}, Storage Size: {0}'.format(server.stat()))
        resp,mails,octets=server.list()
        print('邮件总数为：{}'.format(len(mails)))
        total_mail_numbers=len(mails)
        response_status,mail_message_lines,octets=server.retr(total_mail_numbers)
        print('邮件获取状态：{}'.format(response_status))
        print('原始邮件数据：\n{}'.format(mail_message_lines))
        msg_content=b'\r\n'.join(mail_message_lines).decode('gbk')
        msg=Parser().parsestr(text=msg_content)
        print('解码后的邮件信息：\n{}'.format(msg))
        mails=[]
        mails.append(self.parseMail(msg))
        server.close()
        return mails
        # return msg
    def parseMail(self,msg):
        '''
        @function: parser one of your 
        '''
        
        mailinfo=MailInfo()

        #解析收发双方信息
        from_str=msg.get('From')
        from_nickname,from_account=self.getName(from_str)
        # print(from_nickname,from_account)
        to_str=msg.get("To")
        to_nickname,to_account=self.getName(to_str)
        # print(to_nickname,to_account)
        mailinfo.from_nickname=from_nickname
        mailinfo.from_account=from_account
        mailinfo.to_nickname=to_nickname
        mailinfo.to_account=to_account

        #解析主题信息
        subject_str=msg.get("Subject")
        mailinfo.title=subject_str

        #解析邮件内容
        parts=msg.get_payload()
        # print(parts)
        content_type=parts[0].get_content_type()
        # print(parts[0].as_string())
        content_charset=parts[0].get_content_charset()
        # print(content_charset)
        content=parts[0].as_string().split('base64')[-1]
        mailinfo.text_content=decode_base64(content,content_charset)
        return mailinfo

    def getName(self,s):
        '''
        @function: get nickname and account from string s
        '''
        nickname,account=s.split(" ")
        # print(nickname,account)
        sp=nickname.split('?')
        charset,nickname=sp[1],sp[3]
        nickname=decode_base64(nickname,charset)
        account=account.lstrip('<')
        account=account.rstrip('>')
        return nickname,account


    def show(self,emails):
        '''
        @function: show your emails
        '''
        for item in emails:
            print('title: %s'%(item.title))
            print('from %s  <%s>'%(item.from_nickname,item.from_account))
            print('to %s <%s>'%(item.to_nickname,item.to_account))
            print(item.text_content)

