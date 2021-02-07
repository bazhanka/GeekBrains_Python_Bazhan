def dossier(**kwargs):
    """Функция принимает на вход неограниченное количество именованных аргументов
    Выводит в одну строку все пары ключ-значение"""
    for key,value in kwargs.items():
        print(f"{key} - {value}",end=' ')

personal_dict={'имя':"", 'фамилию':"", 'год рождения':"", 'город проживания':"", 'email':"", 'телефон':"" }
for d in personal_dict.keys():
    info = input(f'Введите {d} - ')
    personal_dict[d] = info
dossier(**personal_dict)