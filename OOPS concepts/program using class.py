class Aoc:
    def set(self):
        self.r=10
    def area(self):
        self.area=3.14*self.r**2
    def print(self):
        print(self.area)
a=Aoc()
a.set()
a.area()
a.print()