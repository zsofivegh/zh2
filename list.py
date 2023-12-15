def list_my_friends(file_name):
    list=[]
    with open(file_name, "r") as friendlist:
        list = friendlist.readlines()
    for i in list:
        print(i.strip())
        

list_my_friends("friends.txt")
    