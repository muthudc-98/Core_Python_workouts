def mono(s):
    return(all(s[i] <= s[i+1] for i in range(len(s)-1)))
a=[]
n=int(input('enter the number:'))
for i in range(n):
    c=int(input('enter the value:..'))
    a.append(c)
print(mono(a))