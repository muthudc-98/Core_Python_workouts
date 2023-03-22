start=int(input('enter the start no'))
end=int(input('enter the end no'))
i=0
for i in range(start,end+1):
    if i%2==0:
        print('even number',i)
    else:
        print('odd number',i)
