list=[6,5,4,2,1]
a=int(input('Введите значение рейтинга'))
list.append(a)
list.sort(reverse=True)
print(list)