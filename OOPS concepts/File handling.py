'''f=open('test phy.txt','a')
print(f.write('\n'))
print(f.write('Started OOPS'))
f.close
f=open('test phy.txt','r')
print(f.read())
f.close()'''

f=open('test py.txt','w')
n=int(input('enter the no:'))
for i in range(n):
    b=int(input('b value:'))
    f.write(str(b))
    f.write('\n')
f.close()
f=open('test py.txt','r')
sum=0
for i in f:
    x=int(i)
    sum=sum+x
    print(sum)
f.close()
'''f=open('test py.txt','r')
f.read()
f.close()'''
f=open('test py.txt','w')
f.write('sum:')
f.write(str(sum))
f.close()




    
    