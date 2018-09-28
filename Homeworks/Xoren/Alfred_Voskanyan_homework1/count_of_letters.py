#!/usr/bin/env python3
import sys
str = sys.argv[1].lower()


for i in range(97, 123):
    letter = chr(i)
    print("%s: %s" % (letter, str.count(letter)))
