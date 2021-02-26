class ComplexNums:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def __add__(self, other):
        return f'{self.real+other.real}+{self.imag+other.imag}j'

    def __mul__(self, other):
        return f'{self.real*other.real-self.imag*other.imag}+{self.imag*other.real+self.real*other.imag}j'

a=ComplexNums(3,4)
b=ComplexNums(1,8)
print(a+b, a*b)