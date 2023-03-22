'''x=['+','-','*','/','%']
t=input('enter the symbol ')
c=0
for i in x:
    if i in t:
        c=c+1
if c:
    print('Arithematic')
else:
    print('not an arithematic')'''

#sum and average of the odd and even number
a=int(input('enter the number :'))
esum=0
osum=0
ec=1
oc=0
for i in range(a):
    if i%2==0:
        esum=esum+i
        ec=ec+1
    else:
        osum=osum+i
        oc=oc+1
eavg=esum/ec
oavg=osum/oc
print('Even sum',esum)
print('Odd sum',osum)
print('Even average',eavg)
print('Odd average',oavg)
        
