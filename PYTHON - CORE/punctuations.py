punctuations='''()-[]{};:"'\,<>.!?@#$%^&*_+='''
inp_str=input("Enter the string: ")
no_punc=""
for char in punctuations:
    if char in inp_str:
        no_punc=no_punc+char
print("punctuations",no_punc)