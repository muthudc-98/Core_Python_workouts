class Class:
    def __init__(self,a):
        self.__a=a
    def seta(self,a):
        self.__a=a
    def geta(self):
        return self.__a
    def __add__(first,second):
        return Class(first.__a + second.__a)
x=int(input('Enter the first value:'))
y=int(input('Enter the second value:'))
c=Class(x)
print(c.geta())
d=Class(y)
print(d.geta())
e=c+d
print(e.geta())

    
        