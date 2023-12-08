registrated = False
log_or_sign = input('Hello! This is SocialApp!\npress S to sign in\nor press L to log in, if you have an account registrated!\n(press any other key to leave)\n')

if log_or_sign == 'S':
    while not registrated:
        name = input('username: ')
        found = False
        with open('users.txt', 'r') as file:
            for line in file:
                name_in_line, password_in_line = line.strip().split(';')
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

elif log_or_sign == 'L':
    while not registrated:
        name = input('\nusername: ')
        with open('users.txt', 'r') as file:
            for line in file:
                name_in_line, password_in_line = line.strip().split(';')
                if name_in_line == name:
                    password = input('password: ')
                    if password_in_line == password:
                        print("Successful login!")
                        registrated = True
                        break
                    else:
                        print("Wrong password! Try login again!")
                        break
                else:
                    print('This user does not exist!')
                    break

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

