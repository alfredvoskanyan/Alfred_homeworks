def power(max):
    for i in range(max+1):
        yield 2**i

for i in power(10):
    print(i)