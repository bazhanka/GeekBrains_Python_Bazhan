#Task4
a=int(input())
if a>0:
    a=str(a)
    l=len(a)
    g=0
    n=9
    while g<l-1:
        if a[g]==n:
            break
        else:
            g+=1
            n-=1
    print (a[g])
