with open('Task5.txt', "w") as f5:
    numbers=list(input().split(' '))
    for number in numbers:
        f5.write(number+" ")

with open ('Task5.txt',"r") as f5_read:
    for line in f5_read:
       nums=list(line.split(' '))
       summ = 0
       for num in nums:
           try:
               num=int(num)
               summ+=num
           except ValueError:
               pass
print(summ)