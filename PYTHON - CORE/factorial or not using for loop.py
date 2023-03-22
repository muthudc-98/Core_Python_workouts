num=int(input("enter the value"))
fact=1
if num<0:
    print('is not a prime number')
else:
    for i in range(1,num+1):
        fact*=i
print("factorial of {} is {}".format(num,fact))