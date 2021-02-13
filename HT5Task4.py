d={'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
numbers=['1','2','3','4','5','6','7','8','9','0']
with open ('Task4.txt',"r") as f4:
    newdict={}
    for line in f4:
        for key in d.keys():
            if key in line:
                for number in numbers:
                    if number in line:
                        newdict[d.get(key)]=number
with open("NewTask4.txt","w") as newf4:
    for key,value in newdict.items():
        print(f'{key} - {value}', file=newf4)