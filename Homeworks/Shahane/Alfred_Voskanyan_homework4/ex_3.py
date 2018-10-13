for i in range(3):
    try:
        x = int(input())
        y = int(input())

        print(x, '/', y, '=', x/y)
    except ValueError:
        print("Please insert an integer")
    except ZeroDivisionError:
        print("It's impossible divide to 0")
    except:
        print("Unknown Error")