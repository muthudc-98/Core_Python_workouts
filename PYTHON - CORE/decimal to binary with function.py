def decimaltobinary(num):
    if num>1:
        decimaltobinary(num//2)
    print(num%2,end='')
    
n=int(input('enter the n:'))
decimaltobinary(n)