a=[]
n=int(input('enter the number:'))
for i in range(n):
    b=[]
    for j in range(n):
        c=int(input('enter the values'))
        b.append(c)
    a.append(b)
print(a)
i=0
while i<n:
    j=0
    while j<n:
        print(a[i][j],end=' ')
        j=j+1
    print('\n')
    i=i+1