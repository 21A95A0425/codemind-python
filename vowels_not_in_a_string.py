z=input()
v=["a",'e','i','o','u']
u=['A','E','I','O','U']
a=[]
for i in z:
    if i in v:
        v.remove(i)
if len(v)==0:
    print(0)
else:
    print(*v)