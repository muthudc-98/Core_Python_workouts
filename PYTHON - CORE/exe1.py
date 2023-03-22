
#Swaping in list
'''a=[4,2,1,3,8]
b=len(a)
print('List numbers ',a)
for i in range(0,b):
    for j in range(i+1,b):
        if a[i]>a[j]:
            t=a[i]
            a[i]=a[j]
            a[j]=t
print('ascending order' ,a)'''


#alphabets
'''import string
word=input('Enter the word: ')
sum=''
print('a-z Alphabets..\n')
for i in string.ascii_lowercase:
    for j in word:
        if i==j:
            sum=sum+j
        else:
            continue

for i in sum:
    if i in word:
        s=True
    else:
        s=False

if s:
    print('True...')
else:
    print('False..')'''
            
    


#factorial
'''value=int(input('Enter the factorial value: '))
fact=1
if value<0:
    print('Enter the correct number..')
else:
    for i in range(1,value+1):
        fact=fact*i
        print(fact)
print('The factorial value of {} = {}'.format(value,fact))'''


#for loop
'''value=[1,1,11,11]
for i in value:
    print(i)
else:
    print('Completed')'''

'''a=input('Enter one word: ')
if (a.islower()):
    print('The given word is lowercase')
else:
    print('The given word is uppercase..')'''

'''word=input('Enter the word: ')
sum1=0
wlen=len(word)
for i in word:
    if i=='a' or i=='e' or  i=='i' or i=='o'  or  i=='u'  or  i=='A'  or  i=='E'  or  i=='I'  or  i=='O'  or  i=='U' :
        sum1=sum1+1
    else:
        continue
    
if sum1== wlen:
    print("The given word ",word," is containing Vowel words..")
else:
    print("The given word ",word," is not full of Vowel words..")'''
    


'''word=input('Enter the name: ')
rev=reversed(word)
print('*************')
if list(word)== list(rev):
    print("It's a palindrome")
else:
    print("It's not a panlindrome")'''

'''print('a,b,c,d,e')
print(10,10,10,10,10,sep='*',end='***')'''
'''import math
a=int(input('Enter the square value: '))
b=int(input('Enter the factorial value: '))
c=int(input('Enter the power value: '))

d=math.sqrt(a)
e=math.factorial(b)
f=math.pow(c,2)
print('\n Square value: ',d)
print('Factorial value: ',e)
print('Power value: ',f)'''

'''import keyword
print(keyword.kwlist)'''

#calculate datetime
'''from datetime import *

a1=int(input('Enter the starting year: '))
b1=int(input('Enter the starting month: '))
c1=int(input('Enter the starting day: '))

a2=int(input('Enter the ending year: '))
b2=int(input('Enter the ending month: '))
c2=int(input('Enter the ending day: '))
start=date(year=a1,month=b1,day=c1)
end=date(year=a2,month=b2,day=c2)
ans=end-start
print('Total days: ',ans)'''


#importing calendar
''' import calendar
mon=int(input('Enter the Month: '))
yr=int(input('Enter the Year: '))
print(calendar.month(yr,mon)) '''

'''x="Welcome to this website...."
def hell():
    global x
    x="Language...."
    #print("Python is a "+ x)

hell()
print('Python is a '+x) '''

#importing datetime
'''from datetime import *
today=datetime.now()
yesterday=today-timedelta(1)
tomorrow=today+timedelta(1)
print('-------')
print("Yesterday: ",yesterday.strftime('%d-%m-%y'))
print("Today: ",today.strftime('%d-%m-%y'))
print("Tomorrow: ",tomorrow.strftime('%d-%m-%y'))
print('-------') '''

'''from camelcase import CamelCase
a=CamelCase()
c='welcome to shop...'
print('a.hump(c)') '''
