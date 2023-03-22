class big:
    __a=None
    __b=None
    __c=None
    __d=None
    __e=None
    def __init__(self):
        self.__a=10
        self.__b=20
        self.__c=30
    def num(self):
        self.__d=self.__a if self.__a>self.__b and self.__a>self.__c else self.__b
        self.__e=self.__c if self.__c>self.__a and self.__c>self.__d else self.__d
        return self.__e
    def print(self):
        print(self.__e)
m=big()
m.num()
m.print()
        