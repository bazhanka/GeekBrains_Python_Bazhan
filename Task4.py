#Task4
a=int(input())
if a>0:
    a=str(a)
    l=len(a)
    g=0
    c=[]
    n=9
    while g<=l-1:
        c.append(int(a[g]))
        g+=1
    while n not in c:
        n-=1
    print(n)
