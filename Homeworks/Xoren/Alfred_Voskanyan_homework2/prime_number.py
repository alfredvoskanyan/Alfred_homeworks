import sys

def divisors(n):
    l = []
    for i in range(2, n//2+1):
        if  not n%i:
            l.append(i)
    return l

def is_prime(n):
    if len(divisors(n)):
        return False
    return True

number = sys.argv[1]
print(number, "is a" if is_prime(number) else "is not a","prme number")