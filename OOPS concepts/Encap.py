class Display:
    def __init__(self,x=10,y):
        self.a=x
        self.b=y
    def geta(self,x):
        self.a=x
    def getab(self,x,y):
        self.a=x
        self.b=y
    def seta(self):
        return self.a