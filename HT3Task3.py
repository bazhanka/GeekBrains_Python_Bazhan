def my_func(arg1,arg2,arg3):
    """Принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов."""
    maximum=max(arg1,arg2)
    if arg3>=maximum:
        return arg3+maximum
    else:
        n=arg1+arg2-maximum
        maximum2=max(n,arg3)
        return maximum+maximum2

print(my_func(7,8,9))
print(my_func(1,4,21))
print(my_func(11,4,2))
print(my_func(121,9898,4))

