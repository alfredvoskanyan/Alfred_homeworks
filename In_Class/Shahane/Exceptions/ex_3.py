username = input("Username:")

class MyException(Exception):
    pass
try:
    if username == "Rembo":
        raise MyException
    else:
        print("Welcome,", username)
except MyException:
    print("Rambo is an invalid username")
