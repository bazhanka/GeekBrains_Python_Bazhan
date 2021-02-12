numbers=list(input().split())
print(numbers)
new_numbers=[]
for num in numbers:
    if numbers.count(num)==1:
        new_numbers.append(num)
print(new_numbers)