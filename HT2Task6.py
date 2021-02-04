shop=[]
names=[]
prices=[]
quantities=[]
measures=[]
dict_analytics={'название':names,'цена':prices,'количество':quantities,'ед':measures}
a=input('Есть товар?')
while a=='да':
    number=input("введите номер товара")
    name=input("введите название товара")
    names.append(name)
    price=input("введите цену товара")
    prices.append(price)
    quantity=input("введите количество товара")
    quantities.append(quantity)
    measure=input("введите единицу измерения товара")
    measures.append(measure)
    dict_items={'название':name,'цена':price,'количество':quantity,'ед':measure}
    item=(number, dict_items)
    shop.append(item)
    a = input('Есть товар?')
print(shop)
print(dict_analytics)