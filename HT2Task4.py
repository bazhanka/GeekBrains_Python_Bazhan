line=list(input().split(' '))
j=0
l=len(line)
a=1
while j<=l-1:
    print (f"{a}.{line[j]:.10}")
    a+=1
    j+=1

