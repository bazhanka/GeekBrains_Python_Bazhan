class MyError(Exception):
    def __init__(self,text):
        self.text=text

a=input('Type number')
b=input('Type number')
try:
    a=int(a)
    b=int(b)
    if b==0:
       raise MyError('Zero Division is Impossible')
except ValueError:
    print ('Not a number')
except MyError as err:
    print(err)
else:
    print(a/b)
