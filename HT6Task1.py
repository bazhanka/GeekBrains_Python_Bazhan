import time
class Trafficlight():
    _color="red"
    def _running(self):
        self._color='red'
        print(self._color)
        time.sleep(7)
        self._color='yellow'
        print(self._color)
        time.sleep(2)
        self._color='green'
        print(self._color)
        time.sleep(5)
a=Trafficlight()
a._running()
print(a._color)
a._color='green'
a._running()