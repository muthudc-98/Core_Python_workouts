'''a=0
n=int(input('enter the value:'))
for i in range(n,0,-1):
    for j in range(i):
        print(' ',end="")
    print('*'*a)
    a=a+1'''


n=int(input('enter the value:'))
a=n
for i in range(n):
    for j in range(i):
        print(' ',end="")
    print('*'*a)
    a=a-1