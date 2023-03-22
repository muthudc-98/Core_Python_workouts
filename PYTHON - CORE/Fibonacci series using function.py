'''def fibonacci(n):
    if n<0:
        print('Incoorect output')
    elif n==0:
        return (0)
    elif n==1:
        return (1)
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
s=int(input('Enter the number:'))
c=fibonacci(s)
print(c)'''

def fibo(n):
    if n<=1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))

num=int(input('enter the value:'))
if num<=0:
    print('enter the +value')
else:
    print('Fibonacci :....')
    for i in range(num):
        print(fibo(i))
        



