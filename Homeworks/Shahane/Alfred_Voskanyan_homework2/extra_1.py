import re
while True:
    password = input("Password: ")
    if len(password) < 8:
        print("Password must contain at least 8 characters")
    elif not re.search(r"\d", password):
        print("Password must contain at least 1 number")
    elif not re.search(r"[A-Z]", password):
        print("Password must contain at least 1 capital letter")
    else:
        print("Password is valid")
        break
