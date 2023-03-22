def avg(marks):
    assert len(marks) !=0
    return sum(marks)/len(marks)
value=[1,2,3,4]
print('Average of mark1:',avg(value))
print('\n')
value=[]
print('Average of mark1:',avg(value))