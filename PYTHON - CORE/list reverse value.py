def reverse(b):
    b.reverse()
    return b
a=[]
n=int(input('enter n:'))
for i in range(n):
    c=int(input('enter the value:'))
    a.append(c)
print(a)
print(reverse(a))