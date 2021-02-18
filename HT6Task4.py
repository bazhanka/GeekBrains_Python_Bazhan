class Car:
    def __init__(self, speed, color,name):
        self.speed=speed
        self.color=color
        self.name=name
        self.is_police=False

    def go(self):
        print("Car is on its way")
    def stop(self):
        print('Car stopped')
    def turn(self,direction):
        print(f'Car turned to the {direction}')
    def show_speed(self):
        print(self.speed)
class TownCar(Car):
    def __init__(self, speed, color,name, places):
        Car.__init__(self, speed,color,name)
        self.places=places
    def show_speed(self):
        if int(self.speed)>60:
            print(f'Your speed {self.speed}km/h is over the limit!')
        else:
            print(self.speed)
class SportCar(Car):
    def __init__(self, speed, color,name):
        Car.__init__(self, speed,color,name)
        self.girlsmagnet=True

class WorkCar(Car):
    def __init__(self, speed, color,name, work):
        Car.__init__(self, speed,color,name)
        self.work=work
    def show_speed(self):
        if int(self.speed)>40:
            print(f'Your speed {self.speed}km/h is over the limit!')
        else:
            print(self.speed)
class PoliceCar(Car):
    def __init__(self, speed, color,name):
        Car.__init__(self, speed,color,name)
        self.is_police=True

volvo=TownCar(62,'blue','vv',7)
print(volvo.places)
print(volvo.name)
volvo.show_speed()
lamborgini=SportCar(180,'red','lambo')
print(lamborgini.girlsmagnet)
print(lamborgini.speed)
exi=WorkCar(90,'yellow','exi', 'dig')
print(exi.work)
print(exi.is_police)
exi.show_speed()
nine=PoliceCar(70,'white','911')
nine.go()
nine.turn('left')
nine.stop()
print(nine.is_police)