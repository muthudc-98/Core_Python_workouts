a=['a','e','i','o','u','A','E','I','O','U']
text=input('enter any character :')
c=0
for i in a:
    if i==text:
        c=c+1
if c:
    print('vowel',text)
else:
    print('not vowel',text)