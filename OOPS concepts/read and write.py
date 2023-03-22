f=open('text.txt','r+')
n=int(input('Enter the N:'))
for i in range(n):
    s=int(input('enter the value:'))
    f.write(s)
    f.write('\n')
    