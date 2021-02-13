with open('Task2.txt','r') as f2:
    countlines=0
    count=0
    for line in f2:
        countlines+=1
        count+=1
        words=line.split(' ')
        countwords=len(words)
        print(f"Количество слов в {count} строке:",countwords)
print("Количество строк: ", countlines)