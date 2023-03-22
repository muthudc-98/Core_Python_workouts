def upload(s):
    b=[]
    for i in range(s):
        c=int(input('enter the values:'))
        b.append(c)
    return b
a=[]
n=int(input('enter the n values:'))
a=upload(n)
print(a)