with open("Task3.txt",'r') as f3:
    salaries=0
    employees=0
    lowsal=[]
    for line in f3:
        employee=line.split(' ')
        salaries+=int(employee[1])
        employees+=1
        if int(employee[1])<20000:
            lowsal.append(employee[0])
print(f"Получают меньше 20тыс: {','.join(lowsal)}" '\n'
      f"Средняя величина дохода сотрудников: {salaries/employees}")