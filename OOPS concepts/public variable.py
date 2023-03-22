class arithmetic:
    x=None
    y=None
    z=None
    def __init__(self,x=10,y=20):
        self.x=x
        self.y=y
    def add(self):
        self.z=self.x+self.y
        print(self.z)
m=arithmetic()
n=m.add()
#print(n)