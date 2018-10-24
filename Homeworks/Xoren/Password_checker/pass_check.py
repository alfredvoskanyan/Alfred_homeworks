import re

re_pass = re.compile(r'[^A-Za-z0-9@#$%_]')
re_digit = re.compile(r'\d')
re_capital = re.compile(r'[A-Z]')
print("Password must contain at least 8 characters\n"
      "Password must contain at least 1 digit\n"
      "Password must contain at least 1 capital letter\n"
      "Password can contain this characters: '@', '#', '$', '%', '_'")
while True:
    password = input("Enter Password to check: ")
    if len(password) < 8:
        print("Password must contain at least 8 characters")
    elif not re_digit.search(password):
        print("Password must contain at least 1 digit")
    elif not re_capital.search(password):
        print("Password must contain at least 1 capital letter")
    elif re_pass.search(password):
        print("Password contains invalid character")
    else:
        print("Password is valid")
        break