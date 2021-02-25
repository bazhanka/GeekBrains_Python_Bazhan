class Matrix:
        def __init__(self,line):
            self.line=line.split(';')
            self.newlines=[]
            for arg in self.line:
                line_arg=[]
                for el in arg:
                    try:
                        el=int(el)
                        line_arg.append(el)
                    except ValueError:
                        pass
                self.newlines.append(line_arg)
        def __str__(self):
            return "\n".join(map(str,self.newlines))
        def __add__(self, other):
            sum=[]
            lineindex = 0
            for newline in self.newlines:
                index=0
                element=[]
                for el in newline:
                    x=other.newlines[lineindex][index]
                    element.append(el+x)
                    if index<len(newline)-1:
                        index+=1
                lineindex+=1
                sum.append(element)
            return "\n".join(map(str,sum))
a=Matrix('1,2,3;3,4,6;5 6 7')
b=Matrix('3,2,1;4,5,6;1,2,3')
print(a)
print(a+b)