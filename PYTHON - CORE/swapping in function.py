def swap(num1,num2):
    temp=num1
    num1=num2
    num2=temp
    return num1,num2
num1=int(input('enter num1:'))
num2=int(input('enter num2:'))
print(num1,num2)
print('SWAP:')
num1,num2=swap(num1,num2)
print(num1,num2)