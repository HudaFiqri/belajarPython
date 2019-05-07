#modul
import os
import time

#pembuka
if __name__ == '__main__':

    while True:

        os.system('cls')
        print('welcome to github')
        print('please login')
        print('')

        use = input('username >>> ')
        pas = input('password >>> ')

        if('root' == use and 'root' == pas):
            print('')
            print('access granted')
            time.sleep(1.02);

        elif('linfiq' == use and '12345' == pas):
            print('')
            print('access granted')
            time.sleep(1.02);

        else:
            print('username or password wrong')

        back = input('back? (y/n) ')

        if('n' == back):
            break
        
        elif('no' == back):
            break
