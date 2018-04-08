import mail 
if __name__=='__main__':
    email=mail.Mymail()
    mails=email.receive()
    email.show(mails)