import time

def dec(func):
    def wrapper(*args):
        t1 = time.time()
        func(*args)
        t2 = time.time()
        print("Creating time is:", t2-t1)
    return wrapper

class Person:
    def __init__(self,
                 name = 'John',
                 last_name = 'Smith',
                 age = 20,
                 gender = 'male',
                 student = True):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student = student

    @dec
    def greeting(self, second_person):
        print("Welcome dear", second_person.name)

    def Goodbye(self):
        print("Bye everyone!")

    def Favorite_num(self, num1):
        print("My favourite number is", num1)

p1 = Person()
p2 = Person()
p2.greeting(p1)

p1.Goodbye()
p2.Goodbye()

p1.Favorite_num(4)
p1.Favorite_num(5)