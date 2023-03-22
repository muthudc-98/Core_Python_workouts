'''try:
    print(x)
except:
    print('error')
finally:
    a=int(input('enter the value A:'))
    b=int(input('enter the value B:'))
    c=a+b
    print(c)'''

'''import sys
data=[1,2,3,4,'abc',6]
for i in data:
    try:
        d=i/2
        print(int(d))
    except:
        print('error',sys.exc_info()[0])'''

try:
    a=int(input('enter the value A:'))
    b=int(input('enter the value B:'))
    c=a/b
    print(int(c))
except Exception as e:
    print('cannot divide with zero')
    print(e)
else:
    print('Program completed')
    
    
    
    
    
    
    
    
    
    
    