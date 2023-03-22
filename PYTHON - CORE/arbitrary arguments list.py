'''def s(*h):
    for i in h:
        print(i)
a=int(input('enter a:'))
b=int(input('enter b:'))
c=int(input('enter c:'))
d=int(input('enter d:'))
s(a,b,c,d)'''

num=int(input('enter the number:'))
def sum(n):
    if n<=1:
        return n
    else:
        return n+sum(n-1)
print('the sum is',sum(num))