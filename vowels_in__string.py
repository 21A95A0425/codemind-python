z=input()
v=["a",'e','i','o','u']
u=['A','E','I','O','U']
a=[]
for i in z:
    if i in v:
        if i not in a:
            a.append(i)
    if i in u:
        if i not in a:
            a.append(i)
if len(a)==0:
    print(-1)
else:
    print(*a)