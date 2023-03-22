print('permutation')
from itertools import permutations
def allpermutations(s):
    b=permutations(s)
    for x in list(b):
        print(''.join(x))
a=input('enter the Words:...')
allpermutations(a)