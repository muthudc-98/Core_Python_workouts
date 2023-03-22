print('Generator')
def my():
    for i in range(5):
        yield i**2
d=my()
for i in d:
    print(i)