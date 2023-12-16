from zsofi import link_sharing
from zsofi import text_sharing

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

action = 0
while action != 5:
    action = int(input('Welcome ' + current_user + '! Please choose what you want to do:\n1 - post an image (copy the URL)\n2 - post a text\n3 - view friends\n4 - view posts from friends\n5 - quit\n'))
    if action == 1:
        link = input('link: ')
        comment = input('comment: ')
        link_sharing(current_user, link, comment)
    elif action == 3:
        print("\nThe list of my friends: ")
        with open("friends.txt", "r+") as friendlist:
                list_of_friends = friendlist.readlines()
                for i in list_of_friends:
                    print(i.strip())
        list_of_friends=[]
        shutdown = 1
        add_or_delete = input("\n(A)dd or (D)elete users or press any button to leave: ").upper()
        while shutdown == 1:
            if add_or_delete == 'A':
                friends_name = input("Type your new friend's name: ")
                with open("friends.txt","a") as c:
                    c.write(friends_name)
                    print(f"{friends_name} successfully added to your friend list! \n")
                shutdown = 0
            elif add_or_delete == "D":
                def delete_user(username, filename):
                    with open(filename, 'r') as file:
                        lines = file.readlines()
                            
                    with open(filename, 'w') as file:
                        for line in lines:
                            if line.strip() != username:
                                file.write(line)
                delete_user_name = input("Write the name of your friend whom you want to delete: ")
                delete_user(delete_user_name, 'friends.txt')
                print(f"{delete_user_name} has been deleted from your friends list.\n")
            shutdown = 0
            
                    

                            
                    
                
    elif action == 2:
        text_sharing(current_user,"IDENEMTUDOM")
        