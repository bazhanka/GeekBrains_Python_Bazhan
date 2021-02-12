from itertools import cycle
from sys import argv
skript_name, cycle_elements = argv
count=0
for el in cycle(cycle_elements):
    if count>6:
        break
    else:
        print(el)
        count+=1