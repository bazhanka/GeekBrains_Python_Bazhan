class Road:
    def __init__(self, length, width):
        self._length=int(length)
        self._width=int(width)
    def asfalt(self):
        mass=int(input('Введите массу асфальта для покрытия 1кв.м на 1 см толщины'))
        sm=int(input('Введите толщину полотна'))
        print(self._length*self._width*mass*sm)

d=Road(20,5000)
d.asfalt()