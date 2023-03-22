'''num=int(input('enter the number '))
exp=int(input('enter the exponent value '))
value=1
for i in range(1,exp+1):
        value=value*num
print('{0} power {1} = {2}'.format(num,exp,value))'''

a=[4,2,5,1,3]
a.sort()
print('ascending',a)
a.reverse()
print('descending',a)