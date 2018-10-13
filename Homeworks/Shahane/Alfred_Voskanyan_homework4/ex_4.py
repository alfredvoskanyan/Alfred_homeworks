a = 10
try:
    print(a.name)
except Exception as ex:
    print(type(ex).__name__)
print("*******************************")
try:
    print(a.name)
except AttributeError:
    print("Object 'a' has no attribute 'name'")
except:
    print("Unknown Error")