a=1
n=int(input('enter the value'))
for i in range(n,0,-1):
    for j in range(i):
        print('',end=' ')
    for k in range(a):
        print('*',end=' ')
    print('\n')
    a=a+1
b=1
for i in range(n-1,0,-1):
    print(' ',end='')
    for j in range(b):
        print('',end=' ')
    for k in range(i):
        print('*',end=' ')
    print('\n')
    b=b+1
