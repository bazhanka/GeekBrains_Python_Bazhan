class Stock_of_Equipment:
    @classmethod
    def __init__(cls,places):
        cls.places=places
        cls.var={}


class Office_Equipment:
    def __init__(self, purpose, size, number):
        self.purpose=purpose
        self.size=size
        self.number=number

    def put_to_stock(self, cls):
        if self.number<cls.places:
            cls.var[self.name]=self.number
            cls.places-=self.number
            return "Object successfully placed"
        else:
            return 'Not enough space'


    def proceed(self,cls):
        if self.name in cls.var:
            cls.var.pop(self.name)
            cls.places+=self.number
            return "Object proceed to the Office"
        else:
            return "Object not in the Stock"

class Printer(Office_Equipment):
    def __init__(self, purpose, size, number,time, name='Printer'):
        super(Printer, self).__init__(purpose, size, number)
        self.time=time
        self.name=name

    def proceed(self,cls):
        if self.name in cls.var:
            cls.var.pop(self.name)
            cls.places+=self.number
            return "Object proceed to the Store"
        else:
            return "Object not in the Stock"

    def __str__(self):
        return f'Printing takes {self.time}sec'

class Scanner (Office_Equipment):
    def __init__(self, purpose, size, number,device,name='Scanner'):
        super(Scanner, self).__init__(purpose, size, number)
        self.device=device
        self.name = name

    def proceed(self,cls):
        if self.name in cls.var:
            cls.var.pop(self.name)
            cls.places+=self.number
            return "Object proceed to the Palace of Putin"
        else:
            return "Object not in the Stock"

    def __setattr__(self, key, value):
        if key=="device":
            if type(value)==str:
                self.__dict__[key]=value
                print(f'{self.device} is connected')
            else:
                print('Device is incorrect')
        else:
            self.__dict__[key] = value

class Copymachine(Office_Equipment):
    def __init__(self, purpose, size, number, color=True, name='Copymachine'):
        super(Copymachine, self).__init__(purpose, size, number)
        self.color=color
        self.name = name

a=Printer('to print',45,12,3)
b=Scanner('to scan', 23,1,"PC")
c=Copymachine('to copy',67,3)
d=Stock_of_Equipment(16)

print(b.put_to_stock(Stock_of_Equipment))
print(d.var, d.places)
print(a.put_to_stock(Stock_of_Equipment))
print(d.var, d.places)
print(b.proceed(Stock_of_Equipment))
print(d.var, d.places)
print(c.proceed(Stock_of_Equipment))
print(a.proceed(Stock_of_Equipment))
print (a)
b.device=89
