class MyError(Exception):
    def __init__(self,text):
        self.text=text

numbers=[]
while True:
    el=input('Type a number or q to finish')
    if el=='q':
        print(numbers)
        break
    else:
        try:
            if el.isdigit==False:
                raise MyError('Not a number')
            else:
                numbers.append(el)
        except MyError as err:
            print(err)

