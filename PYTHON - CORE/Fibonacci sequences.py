#Fibonacci sequences
n=int(input('enter the number :'))
n1,n2=0,1
count=0
if n<=0:
    print('enter the +ve number: ')
elif n<=1:
    print('Fibonnacii:..',n,':')
    print(n1)
else:
    print('Fibonnacii:..')
    while count<n:
        print(n1)
        t=n1+n2
        n1=n2
        n2=t
        count+=1