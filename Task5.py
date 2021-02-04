#Task5
plus=int(input('Введите выручку:'))
minus=int(input('Введите издержки:'))
if plus>0 and minus>0:
    result = plus - minus
    if result>0:
        print('Поздравляем, ваша прибыль составила:',result)
        rentability=float(result/plus)
        print ('Ваша рентабельность:',rentability)
        employees=int(input('Введите количество сотрудников'))
        conversion=float(result/employees)
        print('Прибыль на одного сотрудника:', conversion)
    else:
        print('Упс, вы работаете в убыток. Убытки составили:',result)
