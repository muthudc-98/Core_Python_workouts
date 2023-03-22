f=open('test2.txt','wb')
a=[]
n=int(input('enter the n value:'))
for i in range(n):
    b=int(input('enter the b value:'))
    a.append(b)
s=len(a)
t=bytearray(a)
f.write(t)
f.close
f=open('test2.txt','rb')
r=list(f.read(s))
print(r)
f.close