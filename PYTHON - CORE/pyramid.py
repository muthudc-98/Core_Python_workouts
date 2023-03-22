n=int(input('enter the value'))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end='')
    print('\n')


a=1
n=int(input('enter the value'))
for i in range(n,0,-1):
    for j in range(i):
        print('',end=' ')
    print('*'*a)
    a=a+1