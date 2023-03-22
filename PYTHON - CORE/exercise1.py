n=int(input('enter the number:'))
i=0
while i<=n:
    a=int(input('enter the value:'))
    if a>0:
        print(a,'is a positive')
    elif a<0:
        print(a,'is a negative')
    else:
        print(a,'is a zero')
    i=i+1