def lower_case(func):
    def wrapper():
        return func().capitalize()
    return wrapper

def add_str(func):
    def wrapper():
        return func() + "!!! Welcome to the party"
    return wrapper

@add_str
@lower_case
def hi():
    return "HI EVERYONE"

print(hi())