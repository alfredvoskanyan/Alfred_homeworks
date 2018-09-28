list1 = [3, 6, True, True, -1, "abc", (1, 2), [2, 3], 6]

for i in range(len(list1)):
    if isinstance(list1[i], tuple):
        print("Count of elements are ", i)
        print("Tuple's index in list is :", i)
        break
