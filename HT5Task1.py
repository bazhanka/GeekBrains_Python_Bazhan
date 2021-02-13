lines=list(input().split(' '))
with open('newtext.txt','w') as f:
    for line in lines:
        f.write(line+'\n')