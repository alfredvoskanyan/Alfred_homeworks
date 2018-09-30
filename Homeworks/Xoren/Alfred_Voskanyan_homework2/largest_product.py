import sys

def adjacentElementsProduct(inputArray: list):
    product = inputArray[0]*inputArray[1]
    for i in range(1,len(inputArray)-1):
        temp = inputArray[i]*inputArray[i+1]
        product = product if product > temp else temp
    return product

def inputToList(str):
    return str.split(sep=",")

myArray = inputToList(sys.argv[1])
myArray = list(map(int, myArray))
print(adjacentElementsProduct(myArray))


