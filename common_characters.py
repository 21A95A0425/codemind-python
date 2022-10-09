z1=input()
z2=input()
s1=z1.lower()
s2=z2.lower()
a=[]
for i in s1:
    if i.isalpha():
        if i in s2 and i not in a:
            a.append(i)
a.sort()
if len(a)==0:
    print(-1)
else:
    print(''.join(a))