def upload(s):
    b=[]
    for i in range(s):
        c=int(input('enter the value:'))
        b.append(c)
    return b
a=[]
n=int(input('enter the n number:'))
a=upload(n)
print(a)