'''for x in "python":
    print(x)'''


'''numbers=[11,12,12,15,17,20,35,16,10]
sum=0
for val in numbers:
    sum=sum+val
print("sum of the numbers", sum)'''

name=input("enter the name :")
text=input("select the letter :")
count=0
for letter in name:
    if letter==text:
        count+=1
print("Total letters",count)