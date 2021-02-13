import json
firms={}
income=[]
profit=0
count=0
av_profit={}
with open('Task7.txt','r') as f7:
    for line in f7:
        line=line.strip()
        firm=list(line.split(" "))
        income.append(int(firm[-2])-int(firm[-1]))
        firms[firm[0]]=int(firm[-2])-int(firm[-1])
    for el in income:
        if el>0:
            profit+=el
            count+=1
    av_profit["average_profit"]=profit/count
result=[firms, av_profit]
print(result)

with open("NewTask7.json", "w") as json_w:
    json.dump(result,json_w)