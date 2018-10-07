import sys
my_file = open(sys.argv[1], 'r')
my_str = my_file.read()

for i in range(97, 123):
    letter = chr(i)
    print("%s: %s" % (letter, my_str.lower().count(letter)))