d={'зима':[12,1,2], 'весна': [3,4,5], 'лето':[6,7,8],'осень':[9,10,11]}
a=int(input('введите месяц от 1 до 12:'))
while a<1 or a>12:
    print('Неверное число')
    a = int(input('введите месяц от 1 до 12:'))
for time, months in d.items():
    if a in months:
        print (time)