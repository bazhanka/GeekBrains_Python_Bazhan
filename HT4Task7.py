def fact(n):
    result=1
    for el in range(1,n+1):
        result*=el
    return result

def generator(num):
    for el in range (1,fact(num)):
        yield el

num=int(input())
for number in generator(num):
    print(fact(number))

