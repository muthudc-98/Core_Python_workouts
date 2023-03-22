a=int(input('enter a:'))
b=int(input('enter b:'))
if a>b:
    s=a
else:
    s=b
while(1):
    if s%a==0 and s%b==0:
        print('Lcm is:',s)
        break
    s=s+1
