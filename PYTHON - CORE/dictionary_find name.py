name=input('enter the name:')
marks={'ram':70,'raj':80,'siva':65}
for x in marks:
    print(x)
    if name==x:
        print(marks[x])
        break
else:
    print('no entry')