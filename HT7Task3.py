class Cell:
    def __init__(self,number):
        self.number=number
    def __add__(self, other):
        return self.number+other.number
    def __sub__(self, other):
        if self.number-other.number>0:
            return self.number-other.number
        else:
            return "Minus value"
    def __mul__(self, other):
        return self.number*other.number
    def __truediv__(self, other):
        return self.number//other.number
    def make_order(self, length):
        self.length=length
        while True:
            if self.number<self.length:
                print('*'*self.number)
                break
            else:
                print('*'*self.length)
                self.number-=self.length

a=Cell(7)
b=Cell(10)
print(a+b,a-b,a*b,a/b)
a.make_order(3)
b.make_order(5)