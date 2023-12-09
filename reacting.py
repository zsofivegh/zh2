def see_friends_posts(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        index = 0
        for line in lines:
            parts = line.strip().split(';')
            reaction = input(parts[0] + ' posted on ' + parts[1] + ':\n' + parts[2] + '\n' + '(' + parts[3] + ' content)' + '\n' + 'What do you think about this post? (L - like, D - dislike, press any other key to skip reacting )' + '\n')
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

see_friends_posts('posts.txt')