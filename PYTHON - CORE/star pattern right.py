a=1
n=int(input('enter the value:'))
for i in range(n,0,-1):
    for j in range(i):
        print('',end=" ")
    for k in range(a):
        print('*',end=' ')
    print('\n')
    a=a+1