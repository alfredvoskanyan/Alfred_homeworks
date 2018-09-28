from getpass import getpass

while True:
    username = input("Username:")
    password = getpass()
    if username == "Batman" and password == "I am Batman":
        print("Welcome")
        break
    else:
        print("Incorrect username or password\nPleas try again")

