import re

re_login = re.compile(r"^[a-z].*\@gmail\.com$")

re_uppercase = re.compile(r"[A-Z]")
re_lowercase = re.compile(r"[a-z]")
re_digit = re.compile(r"[0-9]")
re_special = re.compile(r"[~`!@#\$%\^&\*\(\)\+=_\-\{\}\[\]\|:;\"\'\?/<>,\.]")


def check_login(login):
    if re_login.search(login):
        return True
    else:
        return False

def check_pass(password):
    if len(password) < 8:
        print("Password is too short")
        return False
    else:
        count = bool(re_uppercase.search(password)) + bool(re_lowercase.search(password)) + bool(re_digit.search(password)) + bool(re_special.search(password))
        if count < 3:
            print("Missing required character")
            return False
        print("Password is valid")
        return True

def is_valid(login, password):
    return check_login(login) and check_pass(password)



############  TESTING   ##############

login = [
    '2wwwww@gmail.com',
    'qwwe3fsfd.gmail.com',
    'asdasd@mail.ru',
    'asassdad23@gmail.com'
]

password = [
    'aaw34',
    'aa2ssssssss',
    'AA#$AAAAAAA',
    '22@@1111111',
    '34A#22222222',
    '4a@@@@@@@@@@',
    'AAaa#########'
]
print("\n******** Testing Login**********\n\n")
for l in login:
    print("login:", l,  "is valid" if check_login(l) else "is invalid", end="\n\n")

print("\n\n******** Testing Password********\n\n")
for p in password:
    print("Password:", p, "is valid" if check_pass(p) else "is invalid", end="\n\n")

