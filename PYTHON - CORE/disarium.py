n=input('enter the number')
s=len(n)
c=int(n)
x=c
result=0
i=s
while(c!=0):
    digits=c%10
    result=result+pow(digits,i)
    c=int(c/10)
    i=i-1
if (result==x):
    print('disarium no')
else:
    print('Not an disarium no')