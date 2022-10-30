z=(input())
c=''
for i in z:
    if '.' in i:
        c=c+'[.]'
    else:
        c=c+i
print(c)