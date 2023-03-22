f=open('text.txt','r')
line=0
char=0
words=0
s=f.readline()
c=len(s)
while c>0:
    line=line+1
    char=char+c
    d=s.split()
    e=len(d)
    words=words+e
    s=f.readline()
    c=len(s)
print('Number of lines',line)
print('Number of character',char)
print('Number of words',words)