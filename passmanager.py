pin_pwd = input("What's the pin? : ")
if pin_pwd != "2005":
    print("Invalid pin")
    quit()

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            print(line)

def change():
    name = input("Add the account name: ")
    passwd = input("Create a strong password!: ")
    print("The details have been edited!")
    with open('password.txt', 'a') as f:
        f.write(name + "|" + passwd + "\n")

while True:
    mode = input("Would you like to view account, edit details, or delete account (view, change, q)? Press 'q' to exit: ").lower()
    if mode == "q":
        quit()
    if mode == "view":
        view()
    elif mode == "change":
        change()
    else:
        print("Invalid input, please try again.")

