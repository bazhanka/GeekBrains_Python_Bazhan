def int_func(arg1):
    """Функция возвращает аргумент-строку, капитализируя первый символ"""
    return arg1.title()
print(int_func('hmmnnvfdfc'))

words=input().split(' ')
for word in words:
    print(int_func(word), end=" ")