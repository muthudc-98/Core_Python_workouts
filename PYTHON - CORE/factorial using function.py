def fact(x):
    if x==1:
        return 1
    else:
        d=x*fact(x-1)
    return d
n=int(input('enter the value:'))
e=fact(n)
print(e)