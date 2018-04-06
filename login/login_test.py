import login

if __name__=='__main__':
    print('开始测试...')
    while True:
        if login.login():
            print('登录成功')
            break
        else:
            print('登录失败')
            # print('是否继续测试？若是，请输入y,否则输入n')
            while True:
                ch=input('是否继续测试？若是，请输入y,否则输入n: ')
                flag=False
                if ch=='y':
                    flag=True
                    break
                elif ch=='n':
                    break
                else:
                    print('bad input!')
                    continue
            if flag:
                break 
            else:
                continue
