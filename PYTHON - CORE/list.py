a=[]
n=int(input('enter the value:'))
i=0
while i<n:
    s=int(input('enter the list value:'))
    a.append(s)
    i=i+1
print(a)    
n=len(a)
i=-1
while i>=-n:
    print(a[i])
    i=i-1