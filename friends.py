def view_friends():
    with open("friends.txt", "r+") as friendlist:
        list_of_friends = friendlist.readlines()
        for i in list_of_friends:
            print(i.strip())


    shutdown = 1
    add_or_delete = input("\nPress A to add or D to delete users or press any button to leave: ").upper()
    while shutdown == 1:
        if add_or_delete == 'A':
            friends_name = input("Type your new friend's name: ")
            with open("friends.txt","a") as c:
                c.write(friends_name + '\n')
                print(f"{friends_name} successfully added to your friend list! \n")
            
        elif add_or_delete == "D":
            delete_user_name = input("Write the name of your friend whom you want to delete: ")
            with open("friends.txt", 'r') as file:
                lines = file.readlines()
            with open("friends.txt", 'w') as file:
                for line in lines:
                    if line.strip() != delete_user_name:
                        file.write(line)
            print(f"{delete_user_name} has been deleted from your friends list.\n")
        shutdown = 0    


def see_friends_posts(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        index = 0
        for line in lines:
            parts = line.strip().split(';')
            reaction = input('\n' + parts[0] + ' posted on ' + parts[1] + ':\n' + parts[2] + '\n' + '(' + parts[3] + ' content)' + '\n' + 'What do you think about this post? (L - like, D - dislike, press any other key to skip reacting )' + '\n')
            if reaction == 'L':
                lines[index] = line.strip() + ';like\n'
            elif reaction == 'D':
                lines[index] = line.strip() + ';dislike\n'
            else:
                lines[index] = line.strip() + ';no reaction\n'
            index +=1
        print('You have seen all posts.')        

    with open(filename, 'w') as file:
        file.writelines(lines)