from zsofi import link_sharing


def signin(registrated):
    print('SIGNING IN')
    while not registrated:
        name = input('\nusername: ')
        found = False
        with open('users.txt', 'r') as file:
            for line in file:
                name_in_line = line.strip().split(';')[0]
                if name_in_line == name:
                    print('This username is taken, choose something else!')
                    found = True
                    break

        if not found:
            passwd = input('password: ')
            with open('users.txt', 'a') as file:
                file.write('\n' + name + ';' + passwd)
            print('You are successfully registrated!')
            registrated = True
            login(registrated)

def login(login_proc):
    print('LOGGING IN')
    while login_proc:
        name = input('\nusername: ')
        found = False
        with open('users.txt', 'r') as file:
            for line in file:
                name_in_line, password_in_line = line.strip().split(';')
                if name_in_line == name:
                    found = True
                    password = input('password: ')
                    if password_in_line == password:
                        print("Successful login!")
                        login_proc = False
                        return name_in_line
                        break
                    else:
                        print("Wrong password! Try login again!")
                        break
            
        if not found:
            print('This user does not exist!')

log_or_sign = input('Hello! This is SocialApp!\npress S to sign in\nor press L to log in, if you have an account registrated!\n(press any other key to leave)\n')

if log_or_sign == 'S':
    registrated = False
    signin(registrated)

elif log_or_sign == 'L':
    login_proc = True
    current_user = login(login_proc)

else:
    print('Goodbye!')

#info = 1
#kilepsz=True
#while(kilepsz):
#    info = int(input('# Hi Norbi! Please choose, what would you like to do: \n(1) - make a post\n(2) - view friends\n(3) - see friend's posts\n(4) - quit '# ))
#    if info == 1:
#        print('# most az 1 et valasztotasd'# )
#        kilepsz = False

#print('# program vege'# )
action = 0
while action != 5:
    action = int(input('Welcome ' + current_user + '! Please choose what you want to do:\n1 - post an image (copy the URL)\n2 - post a text\n3 - view friends\n4 - view posts from friends\n5 - quit\n'))
    if action == 1:
        link = input('link: ')
        comment = input('commmment: ')
        link_sharing(current_user,link, comment)