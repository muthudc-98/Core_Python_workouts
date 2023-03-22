f=open('file.txt','wb+')
a=[]
n=int(input('enter the n:'))
for i in range(n):
    b=int(input('enter the value:..'))
    a.append(b)
s=len(a)
t=bytearray(a)
f.write(t)
f.seek(0)
r=list(f.read(s))
print(r)
f.close()