class Clothes:
    def __init__(self,name):
        self.name=name
class Coat(Clothes):
    def __init__(self,name,size):
        super().__init__(name)
        self.size=size
    @property
    def cloth(self):
        return self.size *6.5+0.5
class Suit(Clothes):
    def __init__(self,name,height):
        super().__init__(name)
        self.height=height
    @property
    def cloth(self):
        return self.height * 2 + 0.3

a=Coat("palto",42)
b=Suit('Barney',172)
print(a.cloth, b.cloth)