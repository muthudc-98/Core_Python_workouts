def update():
    b=[]
    n=int(input('enter the values:'))
    for i in range(n):
        c=int(input('enter the values:'))
        b.append(c)
    return b
def display(*num):
    for i in num:
        print(i)
a=update()
display(a)