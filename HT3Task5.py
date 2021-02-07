from typing import List

my_summ=0
def summa(*args):
    """Функция суммирует неограниченное количество аргументов во всей программе, переводя их в int.
    С каждым новым запуском новая сумма прибавляется к старой"""
    for arg in args:
        global my_summ
        arg=int(arg)
        my_summ += arg
    return my_summ


while True:
    numbers = input('Введите q, чтобы закончить, или введите числа: ').split(' ')
    new_numbers=[]
    if "q" in numbers:
        l = len(numbers)
        i = 0
        while i < l:
            if numbers[i] == "q":
                break
            else:
                new_numbers.append(numbers[i])
                i += 1
        print(summa(*new_numbers))
        break
    print(summa(*numbers))




