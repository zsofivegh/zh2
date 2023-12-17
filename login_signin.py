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
                    else:
                        print("Wrong password! Try login again!")
                        break
            
        if not found:
            print('This user does not exist!')


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