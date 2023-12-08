newuser = "i"
print("Jó napot kívánok!")

while newuser == "i":
    name = input("Adja meg a felhasználónevét: ")
    found = False

    with open("users.txt", "r") as file:
        for line in file:
            name_in_line, password_in_line = line.strip().split(';')
            if name_in_line == name:
                print("Ez a név már foglalt!")
                found = True
                break

    if not found:
        passwd = input("Adja meg a jelszavát: ")
        with open("users.txt", "a") as file:
            file.write(name + ' ' + passwd + '\n')
            print("Sikeres regisztráció!")

    newuser = input("Szeretne új felhasználót regisztrálni? (i/n) ")