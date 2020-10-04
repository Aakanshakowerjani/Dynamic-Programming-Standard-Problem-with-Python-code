"""
def noOfPaths(m,n,array):
    count=[[0 for i in range(m+1)] for y in range(n+1)]
    for i in range(m+1):
        if i<=n:
            count[0][i]=1
    for i in range(n+1):
        count[i][0]=1"""







        
# import string
# string1=input()
# string1=''.join(reversed(string1))
# print(string.capwords(string1))










def func(sentence):
    words=sentence.split()
    sting=""
    for word in words:
        new_word=''.join(reversed(word))
        string+=(new_word.capitalize())
    return string

sentence=input()
print(func(sentence))

"""
lst=list(reversed(string))
c=0
for i in range(len(lst)):
    if i==0:
        lst[i]=lst[i].upper()
    elif lst[i]==' ':
        c=1
    elif c==1:
        lst[i]=lst[i].upper()
        c=0
for i in lst:
    print(i,end="")
"""