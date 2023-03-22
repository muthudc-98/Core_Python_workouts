numb=int(input('enter the value :'))
for i in range(numb,0,-1):
    for j in range(i):
        print('*',end='')
    print('\n')


num=int(input('enter the value :'))
for i in range(num):
    for j in range(num):
        print('*',end='')
    print('')
    



n=int(input("enter the value "))
a=num
for i in range(n):
    for j in range(i):
        print(" ",end="")
    print("*"*a)
    a=a-1