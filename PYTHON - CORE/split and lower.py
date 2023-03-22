def low(s):
    w=s.split()
    print(w)
    for i in range(len(w)):
        w[i]=w[i].lower()
    w.sort()
    return w
x=input('enter the word:..')
print(low(x))