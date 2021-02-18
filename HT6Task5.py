class Stationery:
    def __init__(self,title):
        self.title=title
    def draw(self):
        print('Запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        print('Пиши лекцию, харош рисовать')
class Pencil(Stationery):
    def draw(self):
        print('Я художник, я так вижу')
class Handle(Stationery):
    def draw(self):
        print ('Это искусство!')

one=Stationery('plume')
love=Pen('pink pen')
koch=Pencil ('kochinore')
perm=Handle('permanent')
one.draw()
love.draw()
koch.draw()
perm.draw()