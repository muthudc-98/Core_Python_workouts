value=lambda x:x**2
m=0
n=int(input('Enter the value:'))
for i in range(n):
    s=int(input('enter the value:'))
    d=value(s)
    m=m+d
print(m)