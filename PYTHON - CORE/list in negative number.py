'''list1=[11,-21,0,45,66,-93]
for num in list1:
    if num<0:
        print(num,end='')'''

a=[]
n=int(input('enter the number'))
for i in range(n):
    b=int(input('enter b:'))
    a.append(b)
    print('enter the posotion ',i)
x=int(input('enter the deleted position:'))
a.pop(x)
print(a)