a=list(input())
j=0
l=len(a)
if l/2!=0:
    while j<l-1:
        b = a[j]
        a[j] = a[j + 1]
        a[j + 1] = b
        j += 2
else:
    while j<l:
        b = a[j]
        a[j] = a[j + 1]
        a[j + 1] = b
        j += 2

print(a)