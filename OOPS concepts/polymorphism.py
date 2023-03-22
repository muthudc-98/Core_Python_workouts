from poly import Display
class Child(Display):
    def __init__(self,x=1,y=0):
        self.a=x
        self.b=y
    def add(self,x,y):
        return x+y
n=Child(54)
m=n.add1(5)
print(m)
n=Child(10,2)
z=n.add(1,4)
print(z)    