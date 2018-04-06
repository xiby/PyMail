import os
import configparser
import getpass

def checkpsw(user,psw):
    return True

def login():
    '''
    @function: finish the login function 
    @return: True login successful; False login failed
    '''
    cfg=configparser.ConfigParser()
    cfg.read('user.ini')
    if(cfg.items('detial')==[]):
        '''
            当用户文件中未保存用户信息时，让用户输入信息
        '''
        user=input('输入用户帐号：')
        psw=getpass.getpass('输入用户密码：')
        if checkpsw(user,psw):
            return True,{'usr':user,'psw':psw}
        else:
            return False,{}
    else:
        return True
