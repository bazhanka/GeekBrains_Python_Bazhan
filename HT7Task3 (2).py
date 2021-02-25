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
        lines=self.number//self.length
        rest=self.number-self.length*lines
        return "\n".join(['*' * self.length for _ in range(lines)]) + '\n' + '*' * (rest)
a=Cell(7)
b=Cell(10)
print(a+b,a-b,a*b,a/b)
print(a.make_order(3))
print(b.make_order(5))