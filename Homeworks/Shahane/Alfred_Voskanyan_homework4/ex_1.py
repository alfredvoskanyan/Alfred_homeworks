l = [0]*5

try:
    print(l[7])
except IndexError:
    print("list index out of range")
except:
    print("Unknown Error")