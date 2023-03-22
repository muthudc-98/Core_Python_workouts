class arithmetic:
    _x=None
    _y=None
    _z=None
    def __init__(self,x=5,y=10):
        self._x=x
        self._y=y
    def add(self):
        self._z=self._x+self._y
        return self._z
    def sub(self):
        self._z=self._x-self._y
        return self._z
    def multiply(self):
        self._z=self._x*self._y
        return self._z
    def divide(self):
        self._z=self._x/self._y
        return (self._z)
    def print(self):
        print(int(self._z))
