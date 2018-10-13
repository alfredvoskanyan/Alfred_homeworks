l = ['a', 0, 2]

for i in range(len(l)):
    try:
        l[i] = 1/l[i]
    except TypeError:
        l[i] = 'TE'
    except ZeroDivisionError:
        l[i] = 'ZDE'
    except:
        l[i] = '?'

print(l)