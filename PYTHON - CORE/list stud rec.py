stud=[]
n=int(input('enter the value :'))
i=0
while i<n:
    rollno=int(input('rollno:'))
    name=input('name:')
    age=int(input('age:'))
    city=input('city:')
    rec=[rollno,name,age,city]
    stud.append(rec)
    i=i+1
print(stud)
'''for i in stud:
    print(i)'''
a=[]
print('enter the new record')
rollno=int(input('rollno:'))
name=input('name:')
age=int(input('age:'))
city=input('city:')
a=[rollno,name,age,city]
stud.insert(2,a)
print('new record')
print(stud)

