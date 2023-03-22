a=[]
n=int(input('enter the value:'))
i=0
while i<n:
    b=int(input('enter the values'))
    a.append(b)
    i=i+1
c=tuple(a)
print(c)
value=int(input('enter the particular:'))
m=c.count(value)
print('the',value,'count is..',m)
add=int(input('enter the particular value..'))
s=c.index(add)
print('the',add,'index is..',s)