number = int(input("Enter number: "))

factorial = 1
for i in range(2, number+1):
    factorial *= i
print("Factorial of %s is %s" % (number, factorial))