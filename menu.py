from posting import link_sharing, text_sharing
from friends import view_friends, see_friends_posts


def menu(current_user):
    action = 0
    while action != 5:
        action = int(input('\nPlease choose what you want to do:\n1 - post an image (copy the URL)\n2 - post a text\n3 - view friends\n4 - view posts from friends\n5 - quit\n'))
    
        if action == 1:
            print('\nPOSTING AN IMAGE\n')
            link = input('Add the link: ')
            comment = input('Make a comment, if you would like to: ')
            link_sharing(current_user, link, comment)
            print('Successfully posted!')

        elif action == 2:
            print('\nPOSTING A TEXT\n')
            text = input('Type here to share your thoughts: ')
            text_sharing(current_user, text)
            print('Successfully posted!')

        elif action == 3:
            print("\nMY FRIENDS\n")
            view_friends()

        elif action == 4:
            print("\nFRIEND'S POSTS\n")
            see_friends_posts("posts.txt")

        elif action == 5:
            print("\nGoodbye!")

        else:
            print("\nNot acceptable answer, please try again!\n")