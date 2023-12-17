from menu import menu
from login_signin import login, signin


log_or_sign = input('Hello! This is SocialApp!\npress S to sign in\nor press L to log in, if you have an account registrated!\n(press any other key to leave)\n').upper()

if log_or_sign == 'S':
    registrated = False
    current_user = signin(registrated)
    menu(current_user)

elif log_or_sign == 'L':
    login_proc = True
    current_user = login(login_proc)
    menu(current_user)

else:
    print('Goodbye!')