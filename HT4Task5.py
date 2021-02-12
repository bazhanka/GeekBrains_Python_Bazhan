from functools import reduce
newlist=[el for el in range (100,1001,2)]
def comp(prevel,el):
    return prevel*el
print(reduce(comp,newlist))
