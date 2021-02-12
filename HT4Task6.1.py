from itertools import count
from sys import argv
skript_name, start_num = argv
for el in count(int(start_num)):
    if el>100:
        break
        else:
        print (el)