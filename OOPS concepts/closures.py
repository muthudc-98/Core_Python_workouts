print('closures')
def fun(strt):
    def dis(end):
        return strt+end
    return dis
x=fun(50)
y=fun(60)
print(x(2),y(3))