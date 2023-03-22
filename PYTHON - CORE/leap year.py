start=2000
end=2022
for i in range(start,end+1):
    if i%4==0:
        print('leap year',i)
    else:
        print('not a leap',i)