numbers=list(input().split())
new_numbers=[]
for i in range (0,len(numbers)-1):
    if numbers[i]<numbers[i+1]:
        new_numbers.append(numbers[i+1])
print(new_numbers)