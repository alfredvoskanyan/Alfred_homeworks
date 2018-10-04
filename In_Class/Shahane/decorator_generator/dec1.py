list1 = ['Anna', 'Edgar']
list2 = ["Eliza", "Ani", "Vardan"]

def decorator(func):
    def wrapper(list):
        print(list1)
        func(list)
        print(list1)
    return wrapper

@decorator
def add_value(list):
     list1.extend(list)

add_value(list2)


